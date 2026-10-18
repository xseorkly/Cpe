# -*- coding: utf-8 -*-
"""Pages d'atelier (stagiaire et formateur) et diaporamas de bilan."""
import html as H

esc = H.escape
ARIA = ' aria-current="page"'

TYPE_CLASS = {
    "Texte officiel": "t-off", "Établissement": "t-eta", "Messages": "t-msg", "Témoignages": "t-tem",
    "Données": "t-don", "Observation": "t-obs", "Écrits professionnels": "t-ecr", "Article": "t-art",
    "Ressource": "t-res", "Simulation": "t-sim", "Rebondissement": "t-reb", "Situation": "t-sit", "Outil": "t-out",
}


def fmt_min(m):
    h, mn = divmod(m, 60)
    return f"{h} h {mn:02d}" if h and mn else (f"{h} h" if h else f"{mn} min")


def doc_card(a, k, d, collapsible=False, open_=False):
    n = a["n"]
    tcls = TYPE_CLASS.get(d.get("type", ""), "")
    badge = f'<span class="doc-type {tcls}">{esc(d.get("type", "Document"))}</span>'
    body = f'<div class="doc-body">{d["html"].strip()}</div>'
    btn = f'<button class="btn ghost small" type="button" data-print-doc aria-label="Imprimer le document {k}">Imprimer</button>'
    if collapsible:
        g = d.get("groupe")
        return (f'<details class="doc doc-lib" id="a{n}-doc-{k}" data-groups="{g or ""}"{" open" if open_ else ""}>'
                f'<summary class="doc-head"><span class="doc-no">Document {k}</span><span class="doc-title">{esc(d["titre"])}</span>{badge}</summary>'
                f'{body}<div class="doc-foot">{btn}</div></details>')
    return (f'<article class="doc{" doc-reb" if d.get("type") == "Rebondissement" else ""}" id="a{n}-doc-{k}">'
            f'<header class="doc-head"><div><span class="doc-no">Document {k}</span><h4>{esc(d["titre"])}</h4></div>{badge}{btn}</header>'
            f'{body}</article>')


def inline_ids(a):
    s = set()
    for p in a["phases"]:
        s.update(p.get("docs", []))
    return s


def slides_dialogue(a):
    """Insère un temps de parole des groupes et trois questions à la salle."""
    base = list(a["slides"])
    q = list(a.get("cloture", []))
    out = []
    apports = [x for x in base[2:] if x["t"] != "cle"]
    cut1, cut2 = 2 + max(1, len(apports) // 3), 2 + max(2, (2 * len(apports)) // 3)
    for i, sl in enumerate(base):
        out.append(sl)
        if i == 1:
            out.append(dict(t="dialogue", titre="À vous d'abord", texte="Par groupe, 5 minutes : pour chacun de ces points, qu'avez-vous décidé, et sur quel document vous êtes-vous appuyés ? Un porte-parole par groupe répond en une minute."))
        if i == cut1 and q:
            out.append(dict(t="q", texte=q.pop(0)))
        if i == cut2 and q:
            out.append(dict(t="q", texte=q.pop(0)))
    for rest in q:
        out.append(dict(t="q", texte=rest))
    return out


def slides_html(a):
    out = []
    slides = slides_dialogue(a)
    total = len(slides)
    for i, s in enumerate(slides):
        t = s["t"]
        src = f'<p class="slide-src">{esc(s["source"])}</p>' if s.get("source") else ""
        if t == "titre":
            inner = f'<p class="slide-kicker">Atelier {a["n"]} · Bilan</p><h3 class="slide-big">{esc(s["titre"])}</h3><p class="slide-sous">Bilan de l&#39;atelier {a["n"]} · {esc(a["titre"])}</p><p class="slide-q">« {esc(a["problematique"])} »</p>'
        elif t == "points":
            inner = f'<h3>{esc(s["titre"])}</h3><ul class="slide-list">' + "".join(f"<li>{esc(p)}</li>" for p in s["points"]) + "</ul>"
        elif t == "deux":
            (ta, la), (tb, lb) = s["a"], s["b"]
            col = lambda tt, ll, c: f'<div class="slide-col {c}"><h4>{esc(tt)}</h4><ul>' + "".join(f"<li>{esc(x)}</li>" for x in ll) + "</ul></div>"
            inner = f'<h3>{esc(s["titre"])}</h3><div class="slide-cols">{col(ta, la, "ca")}{col(tb, lb, "cb")}</div>'
        elif t == "etapes":
            inner = f'<h3>{esc(s["titre"])}</h3><ol class="slide-steps">' + "".join(f'<li><strong>{esc(l)}</strong><span>{esc(x)}</span></li>' for l, x in s["etapes"]) + "</ol>"
        elif t == "def":
            inner = f'<h3>{esc(s["titre"])}</h3><div class="slide-def"><p class="slide-term">{esc(s["terme"])}</p><p>{esc(s["definition"])}</p></div>'
        elif t == "dialogue":
            inner = f'<p class="slide-kicker">Bilan dialogué · les groupes d\'abord</p><h3 class="slide-big">{esc(s["titre"])}</h3><p class="slide-q">{esc(s["texte"])}</p>'
        elif t == "q":
            inner = f'<p class="slide-kicker">Question à la salle</p><p class="slide-cle">{esc(s["texte"])}</p><p class="slide-src">Une minute de réflexion, puis trois réponses.</p>'
        elif t == "cle":
            inner = f'<p class="slide-kicker">À retenir</p><p class="slide-cle">{esc(s["texte"])}</p>'
        else:
            raise ValueError(t)
        out.append(f'<section class="slide slide--{t}{" active" if i == 0 else ""}" aria-label="Diapositive {i + 1} sur {total}">{inner}{src}</section>')
    return "".join(out)


MOT_DE_PASSE = "ZESE2027"  # saisi « ZESE2027 » ou « ZESE 2027 » (les espaces sont ignorés)


def chiffrer(texte, mot_de_passe=MOT_DE_PASSE):
    """AES-GCM 256, clé dérivée par PBKDF2-SHA256 (200 000 itérations)."""
    import base64, json, os
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    sel, iv = os.urandom(16), os.urandom(12)
    cle = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=sel, iterations=200000).derive(mot_de_passe.encode())
    ct = AESGCM(cle).encrypt(iv, texte.encode("utf-8"), None)
    b = lambda x: base64.b64encode(x).decode()
    return json.dumps({"s": b(sel), "iv": b(iv), "ct": b(ct)})


def bilan_dialog(a):
    data = chiffrer(slides_html(a))
    return f"""<dialog class="bilan" aria-label="Bilan de l'atelier {a['n']}">
  <div class="bilan-bar"><strong>Bilan · Atelier {a['n']}</strong><span class="slidecount" aria-live="polite"></span>
    <div class="bilan-btns"><button class="btn small ghost" data-prev type="button" aria-label="Diapositive précédente" hidden>←</button><button class="btn small ghost" data-next-slide type="button" aria-label="Diapositive suivante" hidden>→</button><button class="btn small ghost" data-full type="button" hidden>Plein écran</button><button class="btn small ghost" data-lock type="button" hidden>Verrouiller</button><button class="btn small" data-close type="button">Fermer</button></div></div>
  <form class="bilan-lock" data-unlock action="#" onsubmit="return false">
    <p class="slide-kicker">Espace formateur</p>
    <h3>Ce bilan est réservé au formateur</h3>
    <p class="muted">Saisissez le mot de passe de la formation pour projeter le diaporama. Il reste mémorisé sur cet appareil jusqu'à ce que vous cliquiez sur « Verrouiller ».</p>
    <label for="pwd-{a['n']}" class="sr">Mot de passe</label>
    <div class="lock-row"><input id="pwd-{a['n']}" type="password" autocomplete="current-password" placeholder="Mot de passe" required><button class="btn" type="submit" data-unlock-btn>Déverrouiller</button></div>
    <p class="lock-err" role="alert" hidden>Mot de passe incorrect.</p>
  </form>
  <div class="slides" hidden></div>
  <div class="bilan-progress" aria-hidden="true"><span></span></div>
  <script type="application/json" class="bilan-data">{data}</script>
</dialog>"""


def pistes_block(a):
    n = a["n"]
    f = a["formateur"]
    crit = "".join(f"<li>{esc(c)}</li>" for c in a["criteres"])
    obj = "".join(f"<li>{esc(r)}</li>" for r in f["relances"])
    vig = "".join(f"<li>{esc(v)}</li>" for v in f["vigilance"])
    contenu = (f'<p class="pistes-intro">Ces propositions sont des pistes argumentées, pas un corrigé unique : '
               f'd\'autres réponses sont recevables si elles s\'appuient sur les faits, les textes et le cadre de votre établissement.</p>'
               f'<div class="pistes-attendus">{f["attendus"]}</div>'
               f'<h4>Les objections qu\'on vous opposera, et auxquelles il faut savoir répondre</h4><ul>{obj}</ul>'
               f'<h4>Points de vigilance</h4><ul>{vig}</ul>'
               f'<h4>Votre production est réussie si…</h4><ul class="checks">{crit}</ul>')
    data = chiffrer(contenu)
    return f"""<dialog class="pistes-dlg" aria-label="Propositions de réponse de l'atelier {n}"><section class="pistes" data-pistes>
  <div class="pistes-head"><div><p class="label">Propositions de réponse · protégé</p><h3>Pistes pour l'atelier {n}</h3><p class="muted small">À consulter après votre propre travail : elles servent de référence au bilan et à la relecture.</p></div>
  <div class="pistes-btns"><button class="btn ghost small" type="button" data-pistes-lock hidden>Verrouiller</button><button class="btn small" type="button" data-pistes-close>Fermer</button></div></div>
  <form class="pistes-lock" data-pistes-form action="#" onsubmit="return false">
    <label for="ppwd-{n}" class="sr">Mot de passe</label>
    <div class="lock-row"><input id="ppwd-{n}" type="password" autocomplete="current-password" placeholder="Mot de passe de la formation" required><button class="btn" type="submit">Afficher les propositions</button></div>
    <p class="lock-err" role="alert" hidden>Mot de passe incorrect.</p>
  </form>
  <div class="pistes-body" hidden></div>
  <script type="application/json" class="pistes-data">{data}</script>
</section></dialog>"""


def kit_pages():
    import json, os
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kit_pages.json")
    try:
        return json.load(open(p, encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def kit_box(a, prefix=""):
    n = a["n"]
    pages = kit_pages().get(str(n), {})
    src = f"{prefix}ressources/kits/atelier-{n}-dossier.pdf"
    items = []
    for k, d in enumerate(a["docs"], 1):
        if d.get("type") == "Rebondissement":
            continue
        pg = pages.get(str(k), 1)
        items.append(f'<li><a href="{src}#page={pg}" data-kit-page="{pg}" target="_blank" rel="noopener"><span class="kit-no">{k}</span>{esc(d["titre"])}</a></li>')
    return f"""<details class="kit" data-kit data-src="{src}">
  <summary><span class="kit-ico" aria-hidden="true">PDF</span><span><strong>Le dossier de l'atelier, à l'écran ou sur papier</strong><span class="small muted"> · {len(items)} documents · les mêmes que ceux imprimés sur votre table</span></span></summary>
  <div class="kit-body">
    <ol class="kit-list">{"".join(items)}</ol>
    <div class="kit-view"><iframe title="Dossier imprimable de l'atelier {n}" loading="lazy"></iframe></div>
    <p class="small"><a href="{src}" target="_blank" rel="noopener">Ouvrir le PDF dans un nouvel onglet</a> · <a href="{src}" download>Télécharger</a> · Les rebondissements ne sont pas dans ce dossier : ils apparaissent à l'étape prévue.</p>
  </div>
</details>"""


def competences_list(C, a):
    return '<ul class="comp-list">' + "".join(f'<li><abbr title="{esc(C.C2013[k])}">{k}</abbr><span>{esc(C.C2013[k])}</span></li>' for k in a["competences"]) + "</ul>"


def atelier_page(C, a, MALLETTE_BY_ATELIER):
    n = a["n"]
    NB = len(C.ATELIERS)
    docs = a["docs"]
    inl = inline_ids(a)
    lib_ids = [k for k in range(1, len(docs) + 1) if k not in inl]
    for k in lib_ids:
        assert docs[k - 1].get("groupe"), f"Atelier {n} : document {k} ni affiché ni dans le dossier"
    steps = "".join(f'<li><a href="#a{n}-t{i}" data-step="{i}">{i} · {esc(p["titre"])}</a></li>' for i, p in enumerate(a["phases"], 1))
    steps += f'<li><a href="#a{n}-fin" data-step="fin">Bilan</a></li>'

    sections = []
    for i, p in enumerate(a["phases"], 1):
        parts = []
        if p.get("docs"):
            parts.append('<div class="docs">' + "".join(doc_card(a, k, docs[k - 1]) for k in p["docs"]) + "</div>")
        if p.get("sequence"):
            items = "".join(f'<li class="event" data-event hidden><span class="event-time">{h}</span><p>{esc(x)}</p></li>' for h, x in p["sequence"])
            parts.append(f'<div class="sequence" data-sequence><ol class="events">{items}</ol><button class="btn" type="button" data-next-event>Révéler l\'événement suivant</button><p class="small muted" data-seq-done hidden>Tous les événements sont révélés.</p></div>')
        if p.get("mission"):
            cards = []
            for gi, g in enumerate(a["groupes"], 1):
                links = "".join(f'<a class="chip-link" href="#a{n}-doc-{k}" data-open-doc>Doc. {k}</a>' for k in g["docs"])
                qs = "".join(f"<li>{esc(q)}</li>" for q in g["questions"])
                cards.append(f'<article class="mission"><header><span class="mission-no">Groupe {gi}</span><h4>{esc(g["nom"])}</h4><p class="mission-angle">{esc(g["angle"])}</p></header><ol>{qs}</ol><div class="mission-docs"><span class="label">Pistes dans le dossier</span>{links}</div></article>')
            mt = esc(p.get("mission_titre", "Les missions des groupes experts"))
            parts.append(f'<div class="missions"><h3 class="label">{mt}</h3><div class="mission-grid">{"".join(cards)}</div><p class="small muted">Les pistes ne suffisent pas : tout le dossier est à votre disposition, et certains documents doivent être lus avec méfiance.</p></div>')
        if p.get("dossier"):
            filt = '<button type="button" class="filter is-on" data-filter="">Tout le dossier</button>' + "".join(
                f'<button type="button" class="filter" data-filter="{gi}">Groupe {gi} · {esc(g["nom"])}</button>' for gi, g in enumerate(a["groupes"], 1))
            lib = "".join(doc_card(a, k, docs[k - 1], collapsible=True) for k in lib_ids)
            parts.append(f"""<div class="dossier" data-dossier>
  <div class="dossier-head"><h3>Le dossier documentaire</h3><p class="small muted">{len(lib_ids)} documents · ouvrez ceux dont vous avez besoin</p></div>
  <div class="dossier-tools"><div class="filters" role="group" aria-label="Filtrer par groupe">{filt}</div>
  <label class="search"><span class="sr">Rechercher dans le dossier</span><input type="search" data-doc-search placeholder="Rechercher un mot…"></label></div>
  <div class="dossier-list">{lib}</div>
  <p class="small muted" data-no-result hidden>Aucun document ne contient ce mot.</p>
</div>""")
        if p.get("affiche"):
            parts.append(f'<div class="affiche"><p class="label">Sur l\'affiche</p><p>{esc(p["affiche"])}</p></div>')
        if p.get("affirmations"):
            aff = "".join(f"<li>{esc(x)}</li>" for x in p["affirmations"])
            parts.append(f'<div class="affirmations"><p class="label">Les affirmations lues par le formateur</p><ol>{aff}</ol><p class="small muted">D\'accord ou pas d\'accord : pas de position médiane.</p></div>')
        if p.get("vote"):
            v = p["vote"]
            opts = "".join(f'<label class="vote-opt"><input type="radio" name="vote-a{n}-{v["id"]}" value="{esc(o)}" data-vote="a{n}:{v["id"]}" data-vote-q="{esc(v["question"])}"><span>{esc(o)}</span></label>' for o in v["options"])
            parts.append(f'<fieldset class="vote"><legend>{esc(v["question"])}</legend><div class="vote-opts">{opts}</div></fieldset>')
        if p.get("rappel_vote"):
            parts.append(f'<div class="recall"><p class="label">Votre premier choix</p><blockquote data-recall-vote="a{n}:{p["rappel_vote"]}"><span class="muted">Aucun vote enregistré sur cet appareil.</span></blockquote></div>')
        if p.get("roles"):
            parts.append(f'<p class="roles"><span class="label">Rôles dans le groupe, à faire tourner à chaque atelier</span>Animateur · gardien du temps · rapporteur · <strong>avocat du diable</strong> : il défend la position inverse de celle du groupe.</p>')
        if p.get("planner"):
            mois = ["Septembre", "Octobre", "Novembre", "Décembre", "Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Toute l'année"]
            doms = ["Démocratie scolaire", "Équipe AED", "Suivi des élèves", "Prévention et pilotage"]
            head = "".join(f"<th scope=\"col\">{esc(d)}</th>" for d in doms)
            rows = "".join(
                f'<tr><th scope="row">{esc(m)}</th>' + "".join(
                    f'<td><textarea rows="2" aria-label="{esc(m)} · {esc(d)}" data-note="a{n}:cal:{mi}:{di}" data-label="Atelier {n} · Calendrier · {esc(m)} · {esc(d)}"></textarea></td>'
                    for di, d in enumerate(doms, 1)) + "</tr>"
                for mi, m in enumerate(mois, 1))
            parts.append(f'<div class="planner"><p class="label">Mon calendrier annuel · enregistré au fur et à mesure</p><div class="tablewrap"><table class="planner-grid"><thead><tr><th></th>{head}</tr></thead><tbody>{rows}</tbody></table></div><p class="small muted">Pour chaque moment : quoi, qui pilote, avec qui, date au plus tard. Votre calendrier se retrouve dans « Mon carnet ».</p></div>')
        if p.get("positions"):
            pos = "".join(f'<div class="position pos-{j}"><h4>{esc(t)}</h4><p>{esc(x)}</p></div>' for j, (t, x) in enumerate(p["positions"], 1))
            parts.append(f'<div class="positions">{pos}</div>')
        if p.get("production"):
            crit = "".join(f'<li><label><input type="checkbox" data-check="a{n}:crit:{j}"> {esc(c)}</label></li>' for j, c in enumerate(a["criteres"], 1))
            parts.append(f'<div class="production-box"><p class="label">Production attendue</p><p class="production">{esc(a["production"])}</p><p class="label">Critères de réussite · cochez quand c\'est vérifié</p><ul class="criteria">{crit}</ul></div>')
        if p.get("rappel"):
            parts.append(f'<div class="recall"><p class="label">Ce que vous aviez écrit au début</p><blockquote data-recall="a{n}:t1"><span class="muted">Vous n\'aviez rien noté au temps 1 sur cet appareil.</span></blockquote></div>')
        last = i == len(a["phases"])
        nxt = (f'<button class="btn" type="button" data-next="fin">J\'ai terminé : passer au bilan</button>' if last
               else f'<button class="btn" type="button" data-next="{i + 1}">J\'ai terminé : passer à l\'étape {i + 1}</button>')
        sections.append(f"""<section class="temps" id="a{n}-t{i}" data-temps="{i}"{" hidden" if i > 1 else ""}>
  <header class="temps-head"><span class="temps-no">Étape {i}</span><h2>{esc(p['titre'])}</h2><span class="mod">{esc(p['modalite'])}</span></header>
  {f'<p class="fmt"><span>{esc(p["format"])}</span></p>' if p.get("format") else ""}
  <div class="consigne"><p>{esc(p['consigne'])}</p></div>
  {"".join(parts)}
  <div class="note-zone"><label for="note-a{n}-t{i}">Mes notes · étape {i}</label>
  <textarea id="note-a{n}-t{i}" data-note="a{n}:t{i}" data-label="Atelier {n} · Étape {i} · {esc(p['titre'])}" rows="4" placeholder="Vos réponses, vos arguments, vos doutes. Aucune donnée réelle."></textarea></div>
  <div class="temps-foot">{nxt}</div>
</section>""")

    clot = "".join(f"<li>{esc(q)}</li>" for q in a["cloture"])
    refs = "".join(f'<li><a href="{C.REF[k][1]}" target="_blank" rel="noopener">{esc(C.REF[k][0])}</a></li>' for k in a["refs"])
    ap = f'<a class="btn ghost" href="approfondir/{a["approfondir"]}.html">Approfondir : {esc(C.APPROFONDIR[a["approfondir"]])}</a>' if a.get("approfondir") else ""
    prev_l = f'<a class="btn ghost" href="atelier-{n - 1}.html">← Atelier {n - 1}</a>' if n > 1 else '<a class="btn ghost" href="index.html">← Le parcours</a>'
    next_l = f'<a class="btn" href="atelier-{n + 1}.html">Atelier {n + 1} →</a>' if n < NB else '<a class="btn" href="positionnement.html#fin">Mon positionnement final →</a>'
    pager = "".join(f'<a href="atelier-{k}.html"{ARIA if k == n else ""}>{k}</a>' for k in range(1, NB + 1))
    crit_plain = "".join(f"<li>{esc(c)}</li>" for c in a["criteres"])

    return f"""
<div class="atelier" data-atelier="{n}" data-steps="{len(a['phases'])}">
<section class="hero hero-atelier">
  <div class="wrap">
    <nav class="pager" aria-label="Ateliers">{pager}</nav>
    <p class="eyebrow">Atelier {n} sur {NB} · {esc(a['titre'])}</p>
    <h1 class="problem">{esc(a['problematique'])}</h1>
    <ul class="moteur" aria-label="Le déroulé de l'atelier">{"".join(f"<li>{esc(m)}</li>" for m in a.get("moteur", []))}</ul>
  </div>
</section>
<div class="wrap">
  {kit_box(a)}
  <section class="situation" aria-labelledby="sit-{n}">
    <p class="label" id="sit-{n}">La situation</p>
    <div class="situation-txt">{a['situation'].strip()}</div>
  </section>

  <section class="brief">
    <div class="brief-col"><h2 class="label">Ce que l'atelier vous fait travailler</h2><ul class="checks">{"".join(f"<li>{esc(o)}</li>" for o in a['objectifs'])}</ul></div>
    <div class="brief-col"><h2 class="label">Compétences du CPE</h2>{competences_list(C, a)}
      <p class="small muted">Référentiel de formation 2026 : {esc(a['blocs_detail'])}.</p>
      <h2 class="label">Vous devrez produire</h2><p class="production">{esc(a['production'])}</p>
      <details class="crit-preview"><summary>Voir les critères de réussite</summary><ul>{crit_plain}</ul></details></div>
  </section>

  <section class="howto">
    <p><strong>Comment avancer ?</strong> Cet atelier a son propre déroulé : {esc(", ".join(a.get("moteur", [])).lower())}. Chaque étape ne s'ouvre que lorsque la précédente est terminée. Dans le dossier, tout n'est pas fiable, et une information nouvelle viendra bousculer vos conclusions.</p>
    <div class="howto-actions"><button class="btn ghost small" type="button" data-reset>Recommencer l'atelier</button><button class="btn ghost small" type="button" data-print-revealed>Imprimer les documents ouverts</button><button class="btn ghost small" type="button" data-open-bilan>Bilan formateur 🔒</button><button class="btn ghost small" type="button" data-open-pistes>Propositions de réponse 🔒</button></div>
  </section>

  <ol class="stepper" aria-label="Étapes de l'atelier">{steps}</ol>
  {"".join(sections)}

  <section class="temps cloture" id="a{n}-fin" data-temps="fin" hidden>
    <header class="temps-head"><span class="temps-no">Bilan</span><h2>Mise en commun et apports</h2><span class="mod">Collectif · 15 min</span></header>
    <div class="bilan-launch">
      <div><p class="label">Diaporama du formateur · protégé</p><p>Bilan dialogué : les groupes répondent d'abord, puis le formateur fait les apports, avec trois questions à la salle.</p></div>
      <button class="btn big" type="button" data-open-bilan>Ouvrir le bilan ▸</button>
    </div>
    <h3 class="label">Pour conclure, chacun pour soi</h3>
    <ol class="questions">{clot}</ol>
    <div class="note-zone"><label for="note-a{n}-fin">Ce que je retiens de l'atelier {n}</label>
    <textarea id="note-a{n}-fin" data-note="a{n}:fin" data-label="Atelier {n} · Ce que je retiens" rows="5" placeholder="Le geste professionnel que je garde, l'idée qui m'a déplacé, ce que je vérifierai dans mon établissement."></textarea></div>
    <div class="pistes-launch"><div><p class="label">Propositions de réponse · protégé</p><p>Les pistes argumentées pour chaque étape, à relire après votre travail.</p></div><button class="btn" type="button" data-open-pistes>Voir les propositions de réponse 🔒</button></div>
    <div class="refs"><h3 class="label">Textes de référence</h3><ul>{refs}</ul></div>
    <div class="actions">{ap}<a class="btn ghost" href="mallette.html#fiche-{MALLETTE_BY_ATELIER.get(n, 1)}">Compléter ma fiche de mallette</a></div>
  </section>
  <nav class="next-prev" aria-label="Atelier précédent et suivant">{prev_l}{next_l}</nav>
</div>
</div>
{bilan_dialog(a)}
{pistes_block(a)}
<noscript><style>.temps[hidden],.event[hidden]{{display:block!important}}</style></noscript>
"""


def formateur_page(C, a):
    n = a["n"]
    NB = len(C.ATELIERS)
    f = a["formateur"]
    total = sum(p["duree"] for p in a["phases"]) + 15
    rows = "".join(
        f"<tr><td><strong>{i}. {esc(p['titre'])}</strong><br><span class=\"small muted\">{esc(p.get('format', ''))}</span></td><td>{p['duree']} min</td><td>{esc(p['modalite'])}</td><td>{esc(f['deroule'][i - 1])}</td></tr>"
        for i, p in enumerate(a["phases"], 1))
    rows += "<tr><td><strong>Bilan</strong></td><td>15 min</td><td>Collectif</td><td>Bilan dialogué : 5 minutes de retour des groupes sur la diapositive « À vous d'abord », puis 10 minutes d'apports ponctuées de trois questions à la salle.</td></tr>"
    pieges = []
    for k, d in enumerate(a["docs"], 1):
        if d.get("type") == "Rebondissement":
            pieges.append(f"<li>Document {k} · {esc(d['titre'])} : rebondissement, à révéler au temps prévu.</li>")
    groupes = "".join(
        f'<tr><td>Groupe {gi} · {esc(g["nom"])}</td><td>{esc(g["angle"])}</td><td>{", ".join(str(x) for x in g["docs"])}</td></tr>'
        for gi, g in enumerate(a["groupes"], 1))
    groupes = f'<section class="block"><h2>Missions des groupes</h2><div class="tablewrap"><table><thead><tr><th>Groupe</th><th>Question</th><th>Documents pistes</th></tr></thead><tbody>{groupes}</tbody></table></div></section>' if groupes else ""
    seq = ""
    for p in a["phases"]:
        if p.get("sequence"):
            seq = '<h3>Événements à révéler</h3><ol class="events plain">' + "".join(f'<li class="event"><span class="event-time">{h}</span><p>{esc(x)}</p></li>' for h, x in p["sequence"]) + "</ol>"
    docs = "".join(doc_card(a, k, d) for k, d in enumerate(a["docs"], 1))
    pager = "".join(f'<a href="atelier-{k}.html"{ARIA if k == n else ""}>{k}</a>' for k in range(1, NB + 1))
    outline = "".join(f"<li>{esc(s.get('titre') or s.get('texte', ''))}</li>" for s in a["slides"])
    return f"""
<section class="hero hero-formateur">
  <div class="wrap">
    <nav class="pager" aria-label="Fiches formateur">{pager}</nav>
    <p class="eyebrow">Fiche formateur · Atelier {n} · {fmt_min(total)}</p>
    <h1>{esc(a['titre'])}</h1>
    <p class="lead">{esc(a['problematique'])}</p>
    <ul class="moteur">{"".join(f"<li>{esc(m)}</li>" for m in a.get("moteur", []))}</ul>
    <div class="hero-actions"><button class="btn light" type="button" data-open-bilan>Projeter le bilan</button><a class="btn light ghost" href="../atelier-{n}.html">Page stagiaire</a><button class="btn light ghost" type="button" data-print-page>Imprimer la fiche</button></div>
  </div>
</section>
<div class="wrap">
  <section class="brief">
    <div class="brief-col"><h2 class="label">Objectifs</h2><ul class="checks">{"".join(f"<li>{esc(o)}</li>" for o in a['objectifs'])}</ul></div>
    <div class="brief-col"><h2 class="label">Compétences (arrêté 2013)</h2>{competences_list(C, a)}
      <p class="small muted">Référentiel de formation 2026 : {esc(a['blocs_detail'])}.</p>
      <h2 class="label">Matériel</h2><ul>{"".join(f"<li>{esc(m)}</li>" for m in f['materiel'])}</ul></div>
  </section>
  <section class="block"><h2>Déroulé</h2><div class="tablewrap"><table class="deroule"><thead><tr><th>Étape</th><th>Durée</th><th>Modalité</th><th>Conduite du formateur</th></tr></thead><tbody>{rows}</tbody><tfoot><tr><td>Total</td><td>{fmt_min(total)}</td><td colspan="2"></td></tr></tfoot></table></div>
  <ul class="small muted">{"".join(pieges)}</ul></section>
  {groupes}
  <section class="block relances"><h2>Questions pour mettre en difficulté</h2><p class="muted">À poser en circulant, sans donner la réponse. Le but est que le stagiaire argumente avec le dossier.</p><ul>{"".join(f"<li>{esc(r)}</li>" for r in f['relances'])}</ul></section>
  <section class="block corrige"><h2>Ce que l'on attend</h2>{f['attendus']}{seq}</section>
  <section class="block vigilance"><h2>Points de vigilance</h2><ul>{"".join(f"<li>{esc(v)}</li>" for v in f['vigilance'])}</ul></section>
  <section class="block"><h2>Le diaporama de bilan</h2><p class="muted">{len(a['slides'])} diapositives. Il s'ouvre aussi depuis la fin de la page stagiaire.</p><ol>{outline}</ol><button class="btn" type="button" data-open-bilan>Projeter le bilan</button></section>
  <section class="block"><h2>Le dossier complet (version imprimable)</h2>
  <p><a class="btn" href="../ressources/kits/atelier-{n}-complet.pdf" target="_blank" rel="noopener">PDF à imprimer pour la salle, rebondissements compris</a> <a class="btn ghost" href="../ressources/kits/atelier-{n}-dossier.pdf" target="_blank" rel="noopener">PDF vu par les stagiaires</a></p>
  <p class="small muted">Un document par page, pour l'imprimer en cartes-documents à poser sur les tables. Sur la page stagiaire, les documents de départ et les rebondissements n'apparaissent qu'à l'étape prévue.</p><div class="docs all">{docs}</div></section>
</div>
{bilan_dialog(a)}
"""
