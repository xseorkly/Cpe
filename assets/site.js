/* Entrer dans le métier de CPE — comportements du site.
   Toutes les données restent dans le navigateur (localStorage, préfixe cpe3:). */
(function () {
  "use strict";
  var P = "cpe3:";
  var D = window.CPE_DATA || { ateliers: [], mallette: [], approfondir: {}, echelle: [] };

  function get(k) { try { return localStorage.getItem(P + k); } catch (e) { return null; } }
  function set(k, v) { try { localStorage.setItem(P + k, v); return true; } catch (e) { return false; } }
  function del(k) { try { localStorage.removeItem(P + k); } catch (e) {} }
  function allKeys() {
    var out = [];
    try { for (var i = 0; i < localStorage.length; i++) { var k = localStorage.key(i); if (k && k.indexOf(P) === 0) out.push(k.slice(P.length)); } } catch (e) {}
    return out.sort();
  }
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function confirmTwice(btn, msg, action) {
    if (btn.dataset.armed === "1") { action(); return; }
    var orig = btn.textContent; btn.dataset.armed = "1"; btn.textContent = msg;
    setTimeout(function () { btn.dataset.armed = ""; btn.textContent = orig; }, 4000);
  }

  /* ---------- Notes (ateliers, mallette, approfondir) ---------- */
  $$("textarea[data-note]").forEach(function (t) {
    var key = "note:" + t.dataset.note;
    var v = get(key); if (v !== null) t.value = v;
    if (t.dataset.label) set("label:" + t.dataset.note, t.dataset.label);
    var timer, badge = document.createElement("span"); badge.className = "saved"; badge.setAttribute("aria-live", "polite");
    var lab = t.id ? $('label[for="' + t.id + '"]') : null; if (lab) lab.appendChild(badge);
    t.addEventListener("input", function () {
      var ok = t.value.trim() ? set(key, t.value) : (del(key), true);
      clearTimeout(timer); badge.textContent = ok ? "Enregistré sur cet appareil" : "Enregistrement impossible : exportez vos notes";
      timer = setTimeout(function () { badge.textContent = ""; }, 1800);
    });
  });

  /* ---------- Ateliers : révélation progressive ---------- */
  var at = $("[data-atelier]");
  if (at) {
    var n = at.dataset.atelier, steps = parseInt(at.dataset.steps, 10), pk = "prog:a" + n;
    var sections = $$(".temps[data-temps]", at);
    var level = function () { var v = get(pk); return v === "fin" ? steps + 1 : Math.max(1, Math.min(steps, parseInt(v || "1", 10) || 1)); };
    var apply = function (scrollTo) {
      var lv = level();
      sections.forEach(function (s) {
        var idx = s.dataset.temps === "fin" ? steps + 1 : parseInt(s.dataset.temps, 10);
        s.hidden = idx > lv;
        s.classList.toggle("is-done", idx < lv);
      });
      $$(".stepper a", at).forEach(function (a) {
        var st = a.dataset.step === "fin" ? steps + 1 : parseInt(a.dataset.step, 10);
        a.classList.toggle("open", st <= lv); a.classList.toggle("current", st === lv); a.classList.toggle("done", st < lv);
        if (st === lv) a.setAttribute("aria-current", "step"); else a.removeAttribute("aria-current");
      });
      if (scrollTo) { var target = sections.filter(function (s) { return !s.hidden; }).pop(); if (target) { target.scrollIntoView({ block: "start" }); var h = $("h2", target); if (h) { h.setAttribute("tabindex", "-1"); h.focus({ preventScroll: true }); } } }
    };
    $$("[data-next]", at).forEach(function (b) {
      b.addEventListener("click", function () { set(pk, b.dataset.next); $$("[data-recall]").forEach(function (r) { var v = get("note:" + r.dataset.recall); if (v) r.textContent = v; }); apply(true); });
    });
    var reset = $("[data-reset]"); if (reset) reset.addEventListener("click", function () {
      confirmTwice(reset, "Confirmer : revenir au temps 1 (notes conservées)", function () {
        del(pk); del("seq:a" + n); history.replaceState(null, "", location.pathname); location.reload();
      });
    });
    // Séquence d'événements (atelier 8)
    $$("[data-sequence]", at).forEach(function (sq) {
      var evs = $$("[data-event]", sq), btn = $("[data-next-event]", sq), done = $("[data-seq-done]", sq), sk = "seq:a" + n;
      var show = function () {
        var c = Math.min(evs.length, parseInt(get(sk) || "0", 10) || 0);
        evs.forEach(function (e, i) { e.hidden = i >= c; });
        btn.hidden = c >= evs.length; done.hidden = c < evs.length;
      };
      btn.addEventListener("click", function () { set(sk, String((parseInt(get(sk) || "0", 10) || 0) + 1)); show(); });
      show();
    });
    apply(false);
    // Un lien vers un document déjà révélé ouvre la bonne section
    if (location.hash) { var t = document.getElementById(location.hash.slice(1)); if (t && t.closest(".temps[hidden]")) location.hash = ""; }
  }

  /* ---------- Impression ---------- */
  $$("[data-print-doc]").forEach(function (b) {
    b.addEventListener("click", function () {
      var d = b.closest(".doc"); $$(".print-target").forEach(function (x) { x.classList.remove("print-target"); });
      d.classList.add("print-target"); document.body.classList.add("print-one"); window.print();
    });
  });
  $$("[data-print-revealed]").forEach(function (b) { b.addEventListener("click", function () { document.body.classList.add("print-revealed"); window.print(); }); });
  $$("[data-print-page]").forEach(function (b) { b.addEventListener("click", function () { window.print(); }); });
  window.addEventListener("afterprint", function () {
    document.body.classList.remove("print-one", "print-revealed");
    $$(".print-target").forEach(function (x) { x.classList.remove("print-target"); });
  });

  /* ---------- Bilan formateur (diaporama) ---------- */
  var dlg = $("dialog.bilan");
  if (dlg) {
    var slides = $$(".slide", dlg), pos = 0, counter = $(".slidecount", dlg);
    var show = function (i) {
      pos = Math.max(0, Math.min(slides.length - 1, i));
      slides.forEach(function (s, k) { s.classList.toggle("active", k === pos); });
      counter.textContent = (pos + 1) + " / " + slides.length;
      $("[data-prev]", dlg).disabled = pos === 0; $("[data-next-slide]", dlg).disabled = pos === slides.length - 1;
      var bar = $(".bilan-progress span", dlg); if (bar) bar.style.width = ((pos + 1) / slides.length * 100) + "%";
      var box = $(".slides", dlg); if (box) box.scrollTop = 0;
    };
    $$("[data-open-bilan]").forEach(function (b) { b.addEventListener("click", function () { dlg.showModal(); show(0); }); });
    $("[data-prev]", dlg).addEventListener("click", function () { show(pos - 1); });
    $("[data-next-slide]", dlg).addEventListener("click", function () { show(pos + 1); });
    $("[data-close]", dlg).addEventListener("click", function () { dlg.close(); });
    $("[data-full]", dlg).addEventListener("click", function (e) {
      dlg.classList.toggle("full"); e.currentTarget.textContent = dlg.classList.contains("full") ? "Réduire" : "Plein écran";
    });
    dlg.addEventListener("close", function () { dlg.classList.remove("full"); });
    document.addEventListener("keydown", function (e) {
      if (!dlg.open) return;
      if (e.key === "ArrowRight" || e.key === " ") { show(pos + 1); e.preventDefault(); }
      if (e.key === "ArrowLeft") { show(pos - 1); e.preventDefault(); }
    });
  }


  /* ---------- Dossier documentaire : filtres, recherche, liens ---------- */
  $$("[data-dossier]").forEach(function (dz) {
    var docs = $$(".doc-lib", dz), filters = $$("[data-filter]", dz), q = $("[data-doc-search]", dz), none = $("[data-no-result]", dz), cur = "";
    var run = function () {
      var term = (q && q.value || "").trim().toLowerCase(), shown = 0;
      docs.forEach(function (d) {
        var okG = !cur || (" " + d.dataset.groups + " ").indexOf(" " + cur + " ") > -1;
        var okT = !term || d.textContent.toLowerCase().indexOf(term) > -1;
        d.hidden = !(okG && okT); d.classList.toggle("is-hit", !!term && okT);
        if (!d.hidden) shown++;
      });
      if (none) none.hidden = shown > 0;
    };
    filters.forEach(function (f) { f.addEventListener("click", function () { cur = f.dataset.filter; filters.forEach(function (x) { x.classList.toggle("is-on", x === f); }); run(); }); });
    if (q) q.addEventListener("input", run);
  });
  $$("a[data-open-doc], .chip-link").forEach(function (l) {
    l.addEventListener("click", function () {
      var t = document.getElementById(l.getAttribute("href").slice(1)); if (!t) return;
      if (t.hidden) { t.hidden = false; }
      if (t.tagName === "DETAILS") t.open = true;
    });
  });

  /* ---------- Rappel de la première réaction ---------- */
  $$("[data-recall]").forEach(function (b) {
    var v = get("note:" + b.dataset.recall); if (v) b.textContent = v;
  });

  /* ---------- Critères de réussite ---------- */
  $$("input[data-check]").forEach(function (c) {
    c.checked = get("check:" + c.dataset.check) === "1";
    c.addEventListener("change", function () { if (c.checked) set("check:" + c.dataset.check, "1"); else del("check:" + c.dataset.check); });
  });

  /* ---------- Accueil : état d'avancement ---------- */
  $$("[data-state-for]").forEach(function (el) {
    var k = el.dataset.stateFor, p = get("prog:a" + k);
    if (p === "fin") el.textContent = "✓ Terminé";
    else if (p && p !== "1") el.textContent = "En cours · temps " + p;
  });

  /* ---------- Positionnement ---------- */
  var radios = $$("input[data-pos]");
  if (radios.length) {
    var refresh = function () {
      D.ateliers.forEach(function (a) {
        var d = parseInt(get("pos:debut:" + a.n) || "0", 10), f = parseInt(get("pos:fin:" + a.n) || "0", 10);
        var cell = $('[data-delta="' + a.n + '"]'); if (!cell) return;
        cell.textContent = d && f ? (f - d > 0 ? "+" : "") + (f - d) : "";
        cell.classList.toggle("up", d && f && f > d);
      });
    };
    radios.forEach(function (r) {
      if (get("pos:" + r.dataset.pos) === r.value) r.checked = true;
      r.addEventListener("change", function () { set("pos:" + r.dataset.pos, r.value); refresh(); });
    });
    refresh();
  }

  /* ---------- Carnet : rendu, export, import ---------- */
  function noteBlocks() {
    var groups = [];
    D.ateliers.forEach(function (a) {
      var items = [];
      a.temps.forEach(function (t, i) { var v = get("note:a" + a.n + ":t" + (i + 1)); if (v) items.push(["Étape " + (i + 1) + " · " + t, v]); });
      var b = get("note:a" + a.n + ":fin"); if (b) items.push(["Bilan personnel", b]);
      groups.push(["Atelier " + a.n + " · " + a.titre, items]);
    });
    var m = [];
    D.mallette.forEach(function (t, i) {
      [["methode", "Ma méthode"], ["contacts", "Mes interlocuteurs"], ["verifier", "À vérifier"]].forEach(function (f) {
        var v = get("note:mallette:" + (i + 1) + ":" + f[0]); if (v) m.push(["Fiche " + (i + 1) + " · " + t + " · " + f[1], v]);
      });
    });
    var plan = get("note:mallette:plan"); if (plan) m.push(["Plan des trente premiers jours", plan]);
    groups.push(["Ma mallette", m]);
    var ap = [];
    allKeys().forEach(function (k) { if (k.indexOf("note:appr:") === 0) ap.push([get("label:" + k.slice(5)) || k.slice(10), get(k)]); });
    groups.push(["Approfondissements", ap]);
    var pos = [];
    D.ateliers.forEach(function (a) {
      var d = get("pos:debut:" + a.n), f = get("pos:fin:" + a.n);
      if (d || f) pos.push(["Atelier " + a.n + " · " + a.but, "Début : " + (d ? d + " (" + D.echelle[d - 1] + ")" : "—") + " · Fin : " + (f ? f + " (" + D.echelle[f - 1] + ")" : "—")]);
    });
    groups.push(["Mon positionnement", pos]);
    return groups;
  }
  var list = $("#carnet-list");
  if (list) {
    var html = "", any = false;
    noteBlocks().forEach(function (g) {
      html += '<section class="carnet-at"><h2>' + esc(g[0]) + "</h2>";
      if (!g[1].length) html += '<p class="muted small">Rien de noté pour l\'instant.</p>';
      g[1].forEach(function (it) { any = true; html += '<div class="carnet-entry"><h4>' + esc(it[0]) + "</h4><p>" + esc(it[1]) + "</p></div>"; });
      html += "</section>";
    });
    list.innerHTML = (any ? "" : '<p class="muted">Votre carnet est vide. Vos notes apparaîtront ici dès que vous écrirez dans un atelier.</p>') + html;
  }
  function download(name, text, type) {
    var a = document.createElement("a"), u = URL.createObjectURL(new Blob([text], { type: type }));
    a.href = u; a.download = name; document.body.appendChild(a); a.click(); a.remove(); setTimeout(function () { URL.revokeObjectURL(u); }, 1000);
  }
  $$("[data-export]").forEach(function (b) {
    b.addEventListener("click", function () {
      var date = new Date().toISOString().slice(0, 10);
      if (b.dataset.export === "json") {
        var o = { format: "cpe3", exporte: date, donnees: {} };
        allKeys().forEach(function (k) { o.donnees[k] = get(k); });
        download("carnet-cpe-" + date + ".json", JSON.stringify(o, null, 2), "application/json");
        return;
      }
      var lines = ["# Mon carnet de formation CPE", "", "Exporté le " + date + ". Notes personnelles, fictives, sans donnée identifiante.", ""];
      noteBlocks().forEach(function (g) {
        if (!g[1].length) return;
        lines.push("## " + g[0], "");
        g[1].forEach(function (it) { lines.push("### " + it[0], "", it[1], ""); });
      });
      download("carnet-cpe-" + date + ".md", lines.join("\n"), "text/markdown;charset=utf-8");
    });
  });
  var imp = $("[data-import]");
  if (imp) imp.addEventListener("change", function () {
    var f = imp.files[0]; if (!f) return;
    var r = new FileReader();
    r.onload = function () {
      try {
        var o = JSON.parse(r.result); if (o.format !== "cpe3" || !o.donnees) throw new Error();
        Object.keys(o.donnees).forEach(function (k) { set(k, o.donnees[k]); });
        location.reload();
      } catch (e) { var msg = document.createElement("p"); msg.className = "small"; msg.style.color = "var(--danger)"; msg.textContent = "Ce fichier n'est pas une sauvegarde du carnet."; imp.closest(".actions").after(msg); }
    };
    r.readAsText(f);
  });
  var wipe = $("[data-wipe]");
  if (wipe) wipe.addEventListener("click", function () {
    confirmTwice(wipe, "Confirmer l'effacement définitif", function () { allKeys().forEach(del); location.reload(); });
  });
})();
