# -*- coding: utf-8 -*-
"""Génère le site « Entrer dans le métier de CPE » à partir de content.py.

Usage : python3 _build/build.py   (depuis la racine du dépôt)
"""
import html as H
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import content as C  # noqa: E402

esc = H.escape
ARIA = ' aria-current="page"'
FORM_CLS = ' class="is-formateur"'


# --------------------------------------------------------------------------
# Typographie française : espaces insécables devant : ; ? ! et dans « »
# --------------------------------------------------------------------------
def typo(doc):
    parts = re.split(r"(<[^>]+>|<script.*?</script>|<style.*?</style>)", doc, flags=re.S)
    out = []
    for p in parts:
        if p.startswith("<"):
            out.append(p)
            continue
        p = re.sub(r" ([:;?!»])", " \\1", p)
        p = re.sub(r"« ", "« ", p)
        out.append(p)
    return "".join(out)


def write(rel, doc):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(typo(doc))


def ref_link(key, cls=""):
    label, url = C.REF[key]
    c = f' class="{cls}"' if cls else ""
    return f'<a{c} href="{url}" target="_blank" rel="noopener">{esc(label)}</a>'


def fmt_min(m):
    h, mn = divmod(m, 60)
    if h and mn:
        return f"{h} h {mn:02d}"
    if h:
        return f"{h} h"
    return f"{mn} min"


# --------------------------------------------------------------------------
# Gabarit commun
# --------------------------------------------------------------------------
NAV = [
    ("index.html", "Le parcours"),
    ("positionnement.html", "Me positionner"),
    ("carnet.html", "Mon carnet"),
    ("mallette.html", "Ma mallette"),
    ("ressources.html", "Ressources"),
]


def page(rel, title, body, desc="", current="", formateur=False, extra_head=""):
    depth = rel.count("/")
    up = "../" * depth
    nav = "".join(
        f'<a href="{up}{href}"{ARIA if href == current else ""}>{label}</a>'
        for href, label in NAV
    )
    robots = '<meta name="robots" content="noindex, nofollow">' if formateur else ""
    brand_sub = "Espace formateur" if formateur else C.SOUS_TITRE
    home = f"{up}formateur/index.html" if formateur else f"{up}index.html"
    if formateur:
        nav = (f'<a href="{up}formateur/index.html"{ARIA if current == "formateur" else ""}>Programme</a>'
               f'<a href="{up}index.html">Vue stagiaire</a>')
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc or C.FINALITE[:150])}">
{robots}
<link rel="stylesheet" href="{up}assets/site.css">
<script src="{up}assets/data.js" defer></script>
<script src="{up}assets/site.js" defer></script>
{extra_head}
</head>
<body{FORM_CLS if formateur else ""}>
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="top">
  <div class="top-in">
    <a class="brand" href="{home}"><span class="brand-mark" aria-hidden="true">CPE</span><span><strong>{esc(C.TITRE)}</strong><small>{esc(brand_sub)}</small></span></a>
    <nav class="nav" aria-label="Navigation principale">{nav}</nav>
  </div>
</header>
<main id="contenu">
{body}
</main>
<footer class="foot">
  <div class="wrap">
    <p>Le lycée Horizon, ses personnels, ses élèves et toutes les situations sont <strong>fictifs</strong>. Ne saisissez aucune donnée réelle d'élève. Les procédures, contacts et circuits d'alerte d'un établissement réel doivent être vérifiés avec la direction.</p>
    <p class="small">{esc(C.TITRE)} · {esc(C.SOUS_TITRE)} · {esc(C.VERSION)} · Les notes saisies restent dans votre navigateur.</p>
  </div>
</footer>
</body>
</html>
"""


# --------------------------------------------------------------------------
# Numérotation des documents
# --------------------------------------------------------------------------
def numbered_docs(a):
    n = 0
    for ti, t in enumerate(a["temps"], 1):
        for d in t["docs"]:
            n += 1
            yield ti, n, d


def doc_card(a, n, d, printable=True):
    btn = (f'<button class="btn ghost small" type="button" data-print-doc aria-label="Imprimer le document {n}">Imprimer</button>'
           if printable else "")
    return f"""<article class="doc" id="a{a['n']}-doc-{n}">
  <header class="doc-head"><div><span class="doc-no">Document {n}</span><h4>{esc(d['titre'])}</h4></div>{btn}</header>
  <div class="doc-body">{d['html'].strip()}</div>
</article>"""


def chips_competences(a):
    c = "".join(f'<li><abbr title="{esc(C.C2013[k])}">{k}</abbr><span>{esc(C.C2013[k])}</span></li>' for k in a["competences"])
    return f'<ul class="comp-list">{c}</ul>'


def reperes_html(n):
    return REPERES.get(n, "")


# --------------------------------------------------------------------------
# Repères : chapitres extraits de l'ancien cours.html
# --------------------------------------------------------------------------
def load_reperes():
    src = open(os.path.join(HERE, "legacy", "cours.html"), encoding="utf-8").read()
    out = {}
    for i in range(1, 9):
        m = re.search(rf'<section class="panel read" id="c{i}">(.*?)</section>', src, re.S)
        if not m:
            continue
        sec = m.group(1)
        blocks = re.findall(r"<h3>(.*?)</h3>\s*<p>(.*?)</p>", sec, re.S)
        corpus = re.search(r'<p class="small"><strong>Corpus :</strong>(.*?)</p>', sec, re.S)
        inner = "".join(f"<h4>{h}</h4><p>{p}</p>" for h, p in blocks)
        if corpus:
            inner += f'<p class="small muted"><strong>Corpus :</strong>{corpus.group(1)}</p>'
        out[i] = inner
    return out


REPERES = load_reperes()


# --------------------------------------------------------------------------
# Atelier : vue stagiaire
# --------------------------------------------------------------------------
def atelier_page(a):
    n = a["n"]
    total = sum(t["duree"] for t in a["temps"]) + 5
    nums = {}
    docs_by_t = {}
    for ti, num, d in numbered_docs(a):
        docs_by_t.setdefault(ti, []).append((num, d))
        nums[num] = d
    steps = "".join(f'<li><a href="#a{n}-t{i}" data-step="{i}">Temps {i}</a></li>' for i in range(1, len(a["temps"]) + 1))
    steps += f'<li><a href="#a{n}-fin" data-step="fin">Clôture</a></li>'

    temps_html = []
    for i, t in enumerate(a["temps"], 1):
        docs = "".join(doc_card(a, num, d) for num, d in docs_by_t.get(i, []))
        if docs:
            docs = f'<div class="docs"><h3 class="label">Nouveau{"x" if len(docs_by_t[i]) > 1 else ""} document{"s" if len(docs_by_t[i]) > 1 else ""}</h3>{docs}</div>'
        voir = ""
        if t.get("voir"):
            links = "".join(f'<a class="chip-link" href="#a{n}-doc-{v}">Document {v} · {esc(nums[v]["titre"])}</a>' for v in t["voir"])
            voir = f'<div class="voir"><span class="label">À garder sous les yeux</span>{links}</div>'
        seq = ""
        if t.get("sequence"):
            items = "".join(
                f'<li class="event" data-event hidden><span class="event-time">{h}</span><p>{esc(txt)}</p></li>'
                for h, txt in t["sequence"])
            seq = f"""<div class="sequence" data-sequence>
  <ol class="events">{items}</ol>
  <button class="btn" type="button" data-next-event>Révéler l'événement suivant</button>
  <p class="small muted" data-seq-done hidden>Les cinq événements sont révélés. Terminez votre journal avant de passer au temps suivant.</p>
</div>"""
        rep = ""
        if t.get("reperes"):
            ap = ""
            if a.get("approfondir"):
                ap = f'<p><a class="btn ghost small" href="approfondir/{a["approfondir"]}.html">Approfondir : {esc(C.APPROFONDIR[a["approfondir"]])} →</a></p>'
            rep = f"""<details class="reperes" open>
  <summary><span class="label">Repères pour agir</span> Ce que disent les textes et la pratique professionnelle</summary>
  <div class="reperes-body">{reperes_html(n)}{ap}</div>
</details>"""
        last = i == len(a["temps"])
        nxt = (f'<button class="btn" type="button" data-next="fin">J\'ai terminé : passer à la clôture</button>' if last
               else f'<button class="btn" type="button" data-next="{i + 1}">J\'ai terminé : passer au temps {i + 1}</button>')
        temps_html.append(f"""<section class="temps" id="a{n}-t{i}" data-temps="{i}"{" hidden" if i > 1 else ""}>
  <header class="temps-head">
    <span class="temps-no">Temps {i}</span>
    <h2>{esc(t['titre'])}</h2>
    <span class="mod">{esc(t['modalite'])}</span>
  </header>
  <div class="consigne"><p>{esc(t['consigne'])}</p></div>
  {seq}
  {docs}
  {voir}
  {rep}
  <div class="note-zone">
    <label for="note-a{n}-t{i}">Mes notes · temps {i}</label>
    <textarea id="note-a{n}-t{i}" data-note="a{n}:t{i}" data-label="Atelier {n} · Temps {i} · {esc(t['titre'])}" rows="4" placeholder="Votre réponse, vos hypothèses, ce que vous retenez. Aucune donnée réelle."></textarea>
  </div>
  <div class="temps-foot">{nxt}</div>
</section>""")

    clot = "".join(f"<li>{esc(q)}</li>" for q in a["cloture"])
    refs = "".join(f"<li>{ref_link(k)}</li>" for k in a["refs"])
    ap = ""
    if a.get("approfondir"):
        ap = f'<a class="btn ghost" href="approfondir/{a["approfondir"]}.html">Approfondir : {esc(C.APPROFONDIR[a["approfondir"]])}</a>'
    prev_l = f'<a class="btn ghost" href="atelier-{n - 1}.html">← Atelier {n - 1}</a>' if n > 1 else '<a class="btn ghost" href="index.html">← Le parcours</a>'
    next_l = f'<a class="btn" href="atelier-{n + 1}.html">Atelier {n + 1} →</a>' if n < 8 else '<a class="btn" href="positionnement.html#fin">Mon positionnement final →</a>'
    pager = "".join(f'<a href="atelier-{k}.html"{ARIA if k == n else ""}>{k}</a>' for k in range(1, 9))

    body = f"""
<div class="atelier" data-atelier="{n}" data-steps="{len(a['temps'])}">
<section class="hero hero-atelier">
  <div class="wrap">
    <nav class="pager" aria-label="Ateliers">{pager}</nav>
    <p class="eyebrow">Atelier {n} sur 8</p>
    <h1>{esc(a['titre'])}</h1>
    <p class="lead">{esc(a['but'])}</p>
  </div>
</section>
<div class="wrap">
  <section class="brief">
    <div class="brief-col">
      <h2 class="label">À la fin de l'atelier, je sais</h2>
      <ul class="checks">{"".join(f"<li>{esc(o)}</li>" for o in a['objectifs'])}</ul>
    </div>
    <div class="brief-col">
      <h2 class="label">Compétences du CPE travaillées</h2>
      {chips_competences(a)}
      <p class="small muted">Référentiel de formation 2026 : {esc(a['blocs_detail'])}.</p>
      <h2 class="label">Production attendue</h2>
      <p class="production">{esc(a['production'])}</p>
    </div>
  </section>

  <section class="howto">
    <p><strong>Comment avancer ?</strong> Les documents apparaissent au fil des temps, comme dans une situation réelle où l'information arrive progressivement. Répondez d'abord, puis passez au temps suivant. Votre progression et vos notes restent sur cet appareil.</p>
    <div class="howto-actions"><button class="btn ghost small" type="button" data-reset>Recommencer l'atelier</button><button class="btn ghost small" type="button" data-print-revealed>Imprimer les documents révélés</button></div>
  </section>

  <ol class="stepper" aria-label="Étapes de l'atelier">{steps}</ol>

  {"".join(temps_html)}

  <section class="temps cloture" id="a{n}-fin" data-temps="fin" hidden>
    <header class="temps-head"><span class="temps-no">Clôture</span><h2>Ce que je retiens</h2><span class="mod">Collectif, puis individuel</span></header>
    <div class="consigne"><p>Le formateur conduit le bilan collectif. Répondez ensuite pour vous-même.</p></div>
    <ol class="questions">{clot}</ol>
    <div class="note-zone">
      <label for="note-a{n}-fin">Mon bilan de l'atelier {n}</label>
      <textarea id="note-a{n}-fin" data-note="a{n}:fin" data-label="Atelier {n} · Bilan personnel" rows="5" placeholder="Le geste professionnel que je retiens, ce que je vais vérifier dans mon établissement."></textarea>
    </div>
    <div class="refs"><h3 class="label">Textes de référence</h3><ul>{refs}</ul></div>
    <div class="actions">{ap}<a class="btn ghost" href="mallette.html#fiche-{MALLETTE_BY_ATELIER.get(n, 1)}">Compléter ma fiche de mallette</a></div>
  </section>

  <nav class="next-prev" aria-label="Atelier précédent et suivant">{prev_l}{next_l}</nav>
</div>
</div>
<noscript><style>.temps[hidden]{{display:block!important}}.event[hidden]{{display:block!important}}</style></noscript>
"""
    write(f"atelier-{n}.html", page(f"atelier-{n}.html", f"Atelier {n} · {a['titre']} · CPE", body, desc=a["but"]))
    return total


# --------------------------------------------------------------------------
# Atelier : fiche formateur
# --------------------------------------------------------------------------
def formateur_page(a):
    n = a["n"]
    f = a["formateur"]
    total = sum(t["duree"] for t in a["temps"]) + 5
    rows = []
    for i, t in enumerate(a["temps"], 1):
        rows.append(f"<tr><td><strong>Temps {i}</strong><br>{esc(t['titre'])}</td><td>{t['duree']} min</td><td>{esc(t['modalite'])}</td><td>{esc(f['deroule'][i - 1])}</td></tr>")
    rows.append(f"<tr><td><strong>Clôture</strong></td><td>5 min</td><td>Collectif</td><td>Bilan projeté, puis écrit individuel dans le carnet.</td></tr>")
    docs = "".join(doc_card(a, num, d) for _, num, d in numbered_docs(a))
    seq = ""
    for t in a["temps"]:
        if t.get("sequence"):
            seq = "<h3>Événements à révéler</h3><ol class=\"events plain\">" + "".join(
                f'<li class="event"><span class="event-time">{h}</span><p>{esc(x)}</p></li>' for h, x in t["sequence"]) + "</ol>"
    slides = []
    for k, s in enumerate(f["slides"]):
        pts = "".join(f"<li>{esc(p)}</li>" for p in s["points"])
        slides.append(f'<section class="slide{" active" if k == 0 else ""}" aria-label="Diapositive {k + 1}"><p class="eyebrow">Atelier {n} · Bilan</p><h3>{esc(s["titre"])}</h3><ul>{pts}</ul><p class="slide-ref">Référence : {esc(C.REF[s["ref"]][0])}</p></section>')
    clot = "".join(f"<li>{esc(q)}</li>" for q in a["cloture"])
    slides.append(f'<section class="slide" aria-label="Diapositive {len(f["slides"]) + 1}"><p class="eyebrow">Atelier {n} · Pour conclure</p><h3>Questions au groupe</h3><ol>{clot}</ol></section>')
    comp = "".join(f'<li><abbr title="{esc(C.C2013[k])}">{k}</abbr><span>{esc(C.C2013[k])}</span></li>' for k in a["competences"])
    pager = "".join(f'<a href="atelier-{k}.html"{ARIA if k == n else ""}>{k}</a>' for k in range(1, 9))
    body = f"""
<section class="hero hero-formateur">
  <div class="wrap">
    <nav class="pager" aria-label="Fiches formateur">{pager}</nav>
    <p class="eyebrow">Fiche formateur · Atelier {n} · {fmt_min(total)}</p>
    <h1>{esc(a['titre'])}</h1>
    <p class="lead">{esc(a['but'])}</p>
    <div class="hero-actions"><button class="btn light" type="button" data-open-bilan>Projeter le bilan</button><a class="btn light ghost" href="../atelier-{n}.html">Voir la page stagiaire</a><button class="btn light ghost" type="button" data-print-page>Imprimer la fiche</button></div>
  </div>
</section>
<div class="wrap">
  <section class="brief">
    <div class="brief-col"><h2 class="label">Objectifs</h2><ul class="checks">{"".join(f"<li>{esc(o)}</li>" for o in a['objectifs'])}</ul></div>
    <div class="brief-col"><h2 class="label">Compétences (arrêté 2013)</h2><ul class="comp-list">{comp}</ul>
      <p class="small muted">Référentiel de formation 2026 : {esc(a['blocs_detail'])}.</p>
      <h2 class="label">Matériel</h2><ul>{"".join(f"<li>{esc(m)}</li>" for m in f['materiel'])}</ul></div>
  </section>
  <section class="block"><h2>Déroulé</h2>
    <div class="tablewrap"><table class="deroule"><thead><tr><th>Temps</th><th>Durée</th><th>Modalité</th><th>Conduite du formateur</th></tr></thead><tbody>{"".join(rows)}</tbody>
    <tfoot><tr><td>Total</td><td>{fmt_min(total)}</td><td colspan="2"></td></tr></tfoot></table></div>
  </section>
  <section class="block corrige"><h2>Éléments de correction</h2>{f['corrige']}{seq}</section>
  <section class="block vigilance"><h2>Points de vigilance</h2><ul>{"".join(f"<li>{esc(v)}</li>" for v in f['vigilance'])}</ul></section>
  <section class="block"><h2>Textes de référence</h2><ul>{"".join(f"<li>{ref_link(k)}</li>" for k in a['refs'])}</ul></section>
  <section class="block"><h2>Documents de l'atelier (version imprimable)</h2><p class="small muted">Sur la page stagiaire, ces documents n'apparaissent qu'au temps prévu.</p><div class="docs all">{docs}</div></section>
</div>
<dialog class="bilan" id="bilan" aria-label="Bilan de l'atelier {n}">
  <div class="bilan-bar"><strong>Bilan · Atelier {n}</strong><span class="slidecount" aria-live="polite"></span>
    <div class="bilan-btns"><button class="btn small ghost" data-prev type="button" aria-label="Diapositive précédente">←</button><button class="btn small ghost" data-next-slide type="button" aria-label="Diapositive suivante">→</button><button class="btn small ghost" data-full type="button">Plein écran</button><button class="btn small" data-close type="button">Fermer</button></div></div>
  <div class="slides">{"".join(slides)}</div>
  <p class="bilan-help small">Flèches du clavier pour avancer · Échap pour fermer</p>
</dialog>
"""
    write(f"formateur/atelier-{n}.html", page(f"formateur/atelier-{n}.html", f"Formateur · Atelier {n} · {a['titre']}", body, formateur=True))


# --------------------------------------------------------------------------
# Accueil
# --------------------------------------------------------------------------
def index_page():
    cards = []
    for a in C.ATELIERS:
        comp = " ".join(f'<abbr title="{esc(C.C2013[k])}">{k}</abbr>' for k in a["competences"])
        cards.append(f"""<li class="card-atelier" data-card="{a['n']}">
  <a href="atelier-{a['n']}.html">
    <span class="card-no">{a['n']:02d}</span>
    <span class="card-txt"><strong>{esc(a['titre'])}</strong><span>{esc(a['accroche'])}</span><span class="card-comp">{comp}</span></span>
    <span class="card-state" data-state-for="{a['n']}"></span>
  </a>
</li>""")
    day1 = "".join(cards[:4])
    day2 = "".join(cards[4:])
    body = f"""
<section class="hero hero-home">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Parcours de formation · {esc(C.DUREE_TOTALE)}</p>
      <h1>Huit ateliers pour prendre ses fonctions de CPE en sécurité.</h1>
      <p class="lead">Vous arrivez au lycée français Horizon, un établissement fictif du réseau AEFE. À chaque atelier, une situation professionnelle se dévoile pas à pas : vous analysez, vous décidez, vous justifiez, puis vous confrontez votre réponse aux textes et au groupe.</p>
      <div class="hero-actions"><a class="btn light" href="positionnement.html">Commencer par me positionner</a><a class="btn light ghost" href="atelier-1.html">Aller à l'atelier 1</a></div>
    </div>
    <aside class="hero-aside">
      <h2 class="label">Pour qui ?</h2><p>{esc(C.PUBLIC)}</p>
      <h2 class="label">Pour quoi ?</h2><p>{esc(C.FINALITE)}</p>
    </aside>
  </div>
</section>
<div class="wrap">
  <section class="block">
    <h2>Le parcours</h2>
    <p class="muted">Suivez les ateliers dans l'ordre : chacun réinvestit les précédents, et l'atelier 8 les mobilise tous.</p>
    <div class="days">
      <div><h3 class="day">Jour 1 · Entrer dans le métier, organiser le service</h3><ol class="cards">{day1}</ol></div>
      <div><h3 class="day">Jour 2 · Accompagner, protéger, faire participer</h3><ol class="cards">{day2}</ol></div>
    </div>
  </section>

  <section class="block three">
    <div><h3>1 · Je me positionne</h3><p>Avant le premier atelier, j'évalue où j'en suis sur les huit gestes professionnels. Je recommence à la fin.</p><a href="positionnement.html">Me positionner →</a></div>
    <div><h3>2 · Je travaille les ateliers</h3><p>Chaque atelier se déroule en temps successifs. Les documents arrivent au moment prévu ; je réponds avant d'en savoir plus.</p><a href="atelier-1.html">Atelier 1 →</a></div>
    <div><h3>3 · Je garde une trace</h3><p>Mes notes alimentent mon carnet et ma mallette, que j'exporte en fin de formation pour les emporter dans mon établissement.</p><a href="carnet.html">Mon carnet →</a></div>
  </section>

  <section class="block principles">
    <h2>Trois principes pendant toute la formation</h2>
    <ul class="principles-list">
      <li><strong>Distinguer les faits des interprétations.</strong> Un relevé, une parole, une observation sont des indices ; une cause se vérifie.</li>
      <li><strong>Protéger et alerter sans délai.</strong> Dès qu'un élève peut être en danger, la protection passe avant tout le reste. On ne promet jamais le secret.</li>
      <li><strong>Savoir qui décide.</strong> Le CPE agit sous l'autorité du chef d'établissement, coopère et ne se substitue pas aux autres professionnels.</li>
    </ul>
  </section>

  <section class="block glossary">
    <h2>Sigles utilisés</h2>
    <dl><div><dt>CPE</dt><dd>Conseiller principal d'éducation</dd></div><div><dt>AED</dt><dd>Assistant d'éducation</dd></div><div><dt>AEFE</dt><dd>Agence pour l'enseignement français à l'étranger</dd></div><div><dt>CVL · CVC</dt><dd>Conseil de la vie lycéenne · collégienne</dd></div><div><dt>RI</dt><dd>Règlement intérieur</dd></div><div><dt>pHARe</dt><dd>Programme de lutte contre le harcèlement à l'école</dd></div></dl>
  </section>
</div>
"""
    write("index.html", page("index.html", f"{C.TITRE} · Formation CPE AEFE", body, current="index.html",
                             desc="Huit ateliers progressifs pour former les CPE débutants du réseau AEFE."))


# --------------------------------------------------------------------------
# Positionnement
# --------------------------------------------------------------------------
def positionnement_page():
    rows = []
    for a in C.ATELIERS:
        cells = []
        for moment in ("debut", "fin"):
            radios = "".join(
                f'<label class="pt" title="{esc(lbl)}"><input type="radio" name="pos-{moment}-{a["n"]}" value="{v}" data-pos="{moment}:{a["n"]}"><span>{v}</span></label>'
                for v, lbl in enumerate(C.ECHELLE, 1))
            cells.append(f'<td><fieldset class="scale"><legend class="sr">{"Début" if moment == "debut" else "Fin"} de formation</legend>{radios}</fieldset></td>')
        rows.append(f'<tr><th scope="row"><span class="small muted">Atelier {a["n"]}</span><br>{esc(a["but"])}</th>{"".join(cells)}<td class="delta" data-delta="{a["n"]}"></td></tr>')
    legend = "".join(f"<li><strong>{i}</strong> {esc(l)}</li>" for i, l in enumerate(C.ECHELLE, 1))
    body = f"""
<section class="hero"><div class="wrap"><p class="eyebrow">Avant et après la formation</p><h1>Me positionner</h1><p class="lead">Pour chacun des huit gestes professionnels, indiquez où vous en êtes. Faites-le une première fois avant l'atelier 1, puis à la fin de l'atelier 8. L'écart montre ce que la formation vous a apporté et ce qui reste à travailler.</p></div></section>
<div class="wrap">
  <section class="block"><h2 class="label">Échelle</h2><ol class="scale-legend">{legend}</ol>
  <p class="small muted">Soyez précis plutôt que généreux : un positionnement étayé par des faits vaut mieux qu'un sentiment général de maîtrise.</p></section>
  <section class="block" id="fin">
    <div class="tablewrap"><table class="positionnement"><thead><tr><th>Ce que je sais faire</th><th>Début</th><th>Fin</th><th>Écart</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>
    <div class="actions"><button class="btn" type="button" data-export="md">Exporter mon positionnement et mon carnet</button><button class="btn ghost" type="button" data-print-page>Imprimer</button></div>
  </section>
  <section class="block"><h2>Après la formation</h2><p>Repérez les deux gestes où votre positionnement final reste à 1 ou 2. Ce sont vos priorités de formation continue : notez-les dans votre <a href="carnet.html">carnet</a> et parlez-en à votre chef d'établissement.</p></section>
</div>"""
    write("positionnement.html", page("positionnement.html", "Me positionner · CPE", body, current="positionnement.html"))


# --------------------------------------------------------------------------
# Carnet
# --------------------------------------------------------------------------
def carnet_page():
    body = """
<section class="hero"><div class="wrap"><p class="eyebrow">Journal réflexif</p><h1>Mon carnet</h1><p class="lead">Toutes les notes saisies dans les ateliers, la mallette et les approfondissements sont réunies ici. Elles restent uniquement dans ce navigateur : exportez-les pour les conserver.</p></div></section>
<div class="wrap">
  <section class="block">
    <div class="actions">
      <button class="btn" type="button" data-export="md">Exporter en texte (Markdown)</button>
      <button class="btn ghost" type="button" data-export="json">Sauvegarder (fichier réimportable)</button>
      <label class="btn ghost file-btn">Réimporter une sauvegarde<input type="file" accept="application/json,.json" data-import hidden></label>
      <button class="btn ghost" type="button" data-print-page>Imprimer</button>
      <button class="btn danger" type="button" data-wipe>Effacer toutes mes données</button>
    </div>
    <p class="small muted">Sur un ordinateur partagé, exportez votre carnet puis effacez vos données en fin de session.</p>
  </section>
  <section class="block" id="carnet-list" aria-live="polite"><p class="muted">Chargement du carnet…</p></section>
</div>"""
    write("carnet.html", page("carnet.html", "Mon carnet · CPE", body, current="carnet.html"))


# --------------------------------------------------------------------------
# Mallette
# --------------------------------------------------------------------------
MALLETTE = [
    (1, "Ma première semaine en poste", "Acteurs et instances ; documents à demander ; cadre AEFE et circuits à vérifier ; rendez-vous prioritaires."),
    (2, "Diagnostiquer et piloter la vie scolaire", "Faits étayés ; besoins des élèves ; objectif ; postes ; transmissions ; indicateurs et date de bilan."),
    (3, "Accueillir, animer et réguler l'équipe AED", "Missions des AED ; accueil ; consignes ; réunion ; observation factuelle ; entretien de régulation."),
    (4, "Comprendre un comportement d'adolescent", "Comportement observable ; hypothèses multiples ; contexte ; informations manquantes ; réponse éducative à tester."),
    (5, "Conduire un entretien et suivre l'assiduité", "Faits d'assiduité ; questions ouvertes ; parole de l'élève ; coordination ; compte rendu ; date de suivi."),
    (6, "Analyser un incident et choisir la réponse appropriée", "Sécurité ; faits ; personnes à protéger ; qui décide ; punition ou sanction ; dimension éducative ; suivi."),
    (6, "Protéger, alerter et suivre une situation préoccupante", "Sécurité immédiate ; secours si urgence ; personnes compétentes ; protocole local ; trace factuelle ; suivi."),
    (7, "Accompagner les élus et la démocratie scolaire", "Consultation ; compétences des instances ; préparation des élus ; priorités ; décisions ; retour aux élèves."),
]
MALLETTE_BY_ATELIER = {}
for _i, (_a, _t, _d) in enumerate(MALLETTE, 1):
    MALLETTE_BY_ATELIER.setdefault(_a, _i)


def mallette_page():
    fiches = []
    for i, (an, t, d) in enumerate(MALLETTE, 1):
        fields = "".join(
            f'<div class="field"><label for="m{i}-{k}">{lbl}</label><textarea id="m{i}-{k}" data-note="mallette:{i}:{k}" data-label="Mallette · Fiche {i} · {esc(t)} · {lbl}" rows="3"></textarea></div>'
            for k, lbl in (("methode", "Ma méthode en quelques étapes"), ("contacts", "Mes interlocuteurs (fonctions, pas de noms d'élèves)"), ("verifier", "Ce que je dois vérifier dans mon établissement")))
        fiches.append(f"""<section class="fiche" id="fiche-{i}">
  <header><span class="doc-no">Fiche {i} · liée à l'atelier {an}</span><h2>{esc(t)}</h2><p class="muted">{esc(d)}</p></header>
  {fields}
  <p class="small muted">À confronter au règlement intérieur, aux personnes habilitées et aux procédures réellement applicables dans votre établissement.</p>
</section>""")
    body = f"""
<section class="hero"><div class="wrap"><p class="eyebrow">Mes outils de prise de poste</p><h1>Ma mallette professionnelle</h1><p class="lead">Huit fiches à construire au fil des ateliers, puis à personnaliser dans votre établissement. Elles ne remplacent ni un protocole validé, ni les procédures locales.</p>
<div class="hero-actions"><a class="btn light" href="ressources/04_Mallette_Reflexe_Fiches_Operationnelles.pdf">Version PDF à imprimer</a><button class="btn light ghost" type="button" data-export="md">Exporter mes fiches</button></div></div></section>
<div class="wrap"><nav class="toc">{"".join(f'<a href="#fiche-{i}">{i} · {esc(t)}</a>' for i, (_, t, _) in enumerate(MALLETTE, 1))}</nav>
{"".join(fiches)}
<section class="fiche"><header><span class="doc-no">Annexe</span><h2>Feuille de route : mes trente premiers jours</h2></header>
<div class="field"><label for="m-plan">Mes trois actions, leurs échéances, les personnes-ressources et les indicateurs de suivi</label><textarea id="m-plan" data-note="mallette:plan" data-label="Mallette · Plan des 30 premiers jours" rows="6"></textarea></div></section>
</div>"""
    write("mallette.html", page("mallette.html", "Ma mallette · CPE", body, current="mallette.html"))


# --------------------------------------------------------------------------
# Ressources
# --------------------------------------------------------------------------
PDFS = [
    ("02_Carnet_Stagiaire_Journal_Reflexif.pdf", "Carnet du stagiaire", "Version papier du carnet : une page par atelier, le positionnement et le plan des trente premiers jours."),
    ("04_Mallette_Reflexe_Fiches_Operationnelles.pdf", "Mallette réflexe", "Huit fiches opérationnelles à personnaliser dans son établissement."),
    ("03_Banque_Prompts_IA_Metier_CPE.pdf", "Banque de prompts IA", "Douze amorces pour s'entraîner et préparer son travail, sans donnée personnelle ni décision déléguée."),
]


def ressources_page():
    pdfs = "".join(f'<li><a class="res" href="ressources/{f}"><span class="res-type">PDF</span><strong>{esc(t)}</strong><span>{esc(d)}</span></a></li>' for f, t, d in PDFS)
    appr = "".join(f'<li><a class="res" href="approfondir/{k}.html"><span class="res-type">Page</span><strong>{esc(v)}</strong></a></li>' for k, v in C.APPROFONDIR.items())
    groups = "".join(
        f'<div class="refgroup"><h3>{esc(g)}</h3><ul>{"".join(f"<li>{ref_link(k)}</li>" for k in keys)}</ul></div>'
        for g, keys in C.GROUPES_REF)
    comp = "".join(f"<tr><th>{k}</th><td>{esc(v)}</td><td>{', '.join(str(a['n']) for a in C.ATELIERS if k in a['competences'])}</td></tr>" for k, v in C.C2013.items())
    blocs = "".join(f"<tr><th>Bloc {k}</th><td>{esc(v)}</td><td>{', '.join(str(a['n']) for a in C.ATELIERS if k in a['blocs'])}</td></tr>" for k, v in C.BLOCS2026.items())
    body = f"""
<section class="hero"><div class="wrap"><p class="eyebrow">Pour aller plus loin</p><h1>Ressources</h1><p class="lead">Les supports à imprimer, les approfondissements par thème et les textes de référence du métier, vérifiés en octobre 2026.</p></div></section>
<div class="wrap">
  <section class="block"><h2>Supports à imprimer</h2><ul class="res-list">{pdfs}</ul></section>
  <section class="block"><h2>Approfondir un thème</h2><p class="muted">Des apports plus développés, à lire après l'atelier correspondant.</p><ul class="res-list">{appr}</ul></section>
  <section class="block"><h2>Textes de référence</h2><div class="refgroups">{groups}</div>
  <p class="small muted">Dans le réseau AEFE, les textes nationaux donnent des repères ; le règlement intérieur, les instances et les circuits d'alerte de l'établissement et du pays d'accueil s'appliquent et doivent être vérifiés.</p></section>
  <section class="block"><h2>Compétences du CPE travaillées</h2><p class="muted">Arrêté du 1er juillet 2013, compétences spécifiques aux CPE.</p>
    <div class="tablewrap"><table><thead><tr><th>Code</th><th>Compétence</th><th>Ateliers</th></tr></thead><tbody>{comp}</tbody></table></div>
    <p class="muted">Référentiel de formation des CPE (2026), quatre blocs :</p>
    <div class="tablewrap"><table><thead><tr><th>Bloc</th><th>Intitulé</th><th>Ateliers</th></tr></thead><tbody>{blocs}</tbody></table></div>
  </section>
</div>"""
    write("ressources.html", page("ressources.html", "Ressources · CPE", body, current="ressources.html"))


# --------------------------------------------------------------------------
# Espace formateur : accueil
# --------------------------------------------------------------------------
def formateur_index():
    prog = []
    for jour, items in C.PROGRAMME:
        lines = []
        for label, m in items:
            if label.startswith("Atelier"):
                k = int(label.split()[1])
                a = C.ATELIERS[k - 1]
                lines.append(f'<tr><td><a href="atelier-{k}.html">Atelier {k}</a></td><td>{esc(a["titre"])}</td><td>{fmt_min(m)}</td></tr>')
            else:
                lines.append(f"<tr><td>—</td><td>{esc(label)}</td><td>{fmt_min(m)}</td></tr>")
        tot = sum(m for _, m in items)
        prog.append(f'<div><h3 class="day">{jour} · {fmt_min(tot)}</h3><div class="tablewrap"><table><thead><tr><th></th><th>Séquence</th><th>Durée</th></tr></thead><tbody>{"".join(lines)}</tbody></table></div></div>')
    cards = "".join(f'<li class="card-atelier"><a href="atelier-{a["n"]}.html"><span class="card-no">{a["n"]:02d}</span><span class="card-txt"><strong>{esc(a["titre"])}</strong><span>{fmt_min(sum(t["duree"] for t in a["temps"]) + 5)} · {len(a["temps"])} temps</span></span></a></li>' for a in C.ATELIERS)
    body = f"""
<section class="hero hero-formateur"><div class="wrap"><p class="eyebrow">Espace formateur · {esc(C.DUREE_TOTALE)}</p><h1>Conduire la formation</h1><p class="lead">Déroulés minutés, éléments de correction, points de vigilance et bilans à projeter. Cet espace n'est pas lié depuis les pages stagiaires.</p>
<div class="hero-actions"><a class="btn light" href="../ressources/01_Guide_Formateur_Pedagogie_Active.pdf">Guide formateur (PDF)</a></div></div></section>
<div class="wrap">
  <section class="block"><h2>Programme des deux journées</h2><div class="days">{"".join(prog)}</div></section>
  <section class="block"><h2>Fiches par atelier</h2><ol class="cards grid">{cards}</ol></section>
  <section class="block three">
    <div><h3>Avant la session</h3><ul><li>Constituer des groupes de trois ou quatre ; prévoir des rôles tournants.</li><li>Imprimer les documents à révéler séparément pour les groupes sans écran.</li><li>Préparer le règlement intérieur et les circuits d'alerte de l'établissement d'accueil, après vérification.</li></ul></div>
    <div><h3>Pendant</h3><ul><li>Faire produire une réponse avant de révéler la suite : c'est le ressort de chaque atelier.</li><li>Ne jamais faire jouer une victime : utiliser des cartes d'analyse.</li><li>Arrêter avec bienveillance tout récit de situation réelle identifiable.</li></ul></div>
    <div><h3>Évaluer</h3><ul><li>Positionnement initial avant l'atelier 1, final après l'atelier 8.</li><li>La grille de l'atelier 8 sert d'évaluation formative de tout le parcours.</li><li>Évaluer le raisonnement et l'ordre des priorités, pas une réponse unique.</li></ul></div>
  </section>
  <section class="block"><h2>Confidentialité de cet espace</h2><p>Le site est publié sur GitHub Pages : cet espace est public pour qui connaît son adresse. Il est exclu des moteurs de recherche et n'est lié depuis aucune page stagiaire, mais ce n'est pas une protection. Pour une confidentialité réelle, imprimez les fiches ou utilisez le guide PDF hors ligne.</p></section>
</div>"""
    write("formateur/index.html", page("formateur/index.html", "Espace formateur · CPE", body, formateur=True, current="formateur"))


# --------------------------------------------------------------------------
# Approfondissements : migration des anciennes pages de savoirs
# --------------------------------------------------------------------------
def approfondir_pages():
    for key, title in C.APPROFONDIR.items():
        src = open(os.path.join(HERE, "legacy", f"{key}.html"), encoding="utf-8").read()
        main = re.search(r'<main[^>]*>(.*)</main>', src, re.S).group(1)
        hero = re.search(r'<div class="hero">(.*?)</div>\s*<main', src, re.S)
        lead = ""
        if hero:
            pm = re.search(r"<p>(.*?)</p>", hero.group(1), re.S)
            lead = pm.group(1) if pm else ""
        main = re.sub(r'<p class="breadcrumbs">.*?</p>', "", main, flags=re.S)
        main = re.sub(r'<div class="modulestrip">.*?</div>\s*</div>?', "", main, flags=re.S)
        main = re.sub(r'<div class="actions">.*?</div>', "", main, flags=re.S)
        # durées : on garde la nature de l'activité, pas le minutage
        main = re.sub(r'<div class="timing">\s*\d+\s*MIN\s*·\s*(.*?)</div>',
                      lambda m: f'<div class="timing">{m.group(1).capitalize()}</div>', main, flags=re.S)
        main = re.sub(r"\s*\(\d+ heures? de formation au total\)", "", main)
        main = re.sub(r'data-journal="([^"]+)"', lambda m: f'data-note="appr:{key}:{m.group(1)}"', main)
        main = re.sub(r'data-label="([^"]+)"', lambda m: f'data-label="Approfondir · {esc(title)} · {m.group(1)}"', main)
        main = main.replace('href="index.html"', 'href="../index.html"').replace('href="ressources/', 'href="../ressources/')
        # liens vers anciennes pages supprimées
        main = re.sub(r'href="(atelier|cours|diaporamas|immersion|presentation)\.html[^"]*"', 'href="../index.html"', main)
        main = re.sub(r'href="ressources/01_[^"]*"', 'href="../ressources/02_Carnet_Stagiaire_Journal_Reflexif.pdf"', main)
        main = main.replace('href="../ressources/01_Guide_Formateur_Pedagogie_Active.pdf"', 'href="../ressources/02_Carnet_Stagiaire_Journal_Reflexif.pdf"')
        linked = [a["n"] for a in C.ATELIERS if a.get("approfondir") == key]
        back = "".join(f'<a class="btn ghost" href="../atelier-{k}.html">← Retour à l\'atelier {k}</a>' for k in linked)
        others = "".join(f'<a href="{k}.html"{ARIA if k == key else ""}>{esc(v)}</a>' for k, v in C.APPROFONDIR.items())
        body = f"""
<section class="hero"><div class="wrap"><p class="eyebrow">Approfondir · lié à l'atelier {", ".join(map(str, linked))}</p><h1>{esc(title)}</h1><p class="lead">{lead}</p></div></section>
<div class="wrap approfondir">
<nav class="toc">{others}</nav>
{main}
<nav class="next-prev">{back}<a class="btn" href="../carnet.html">Mon carnet →</a></nav>
</div>"""
        write(f"approfondir/{key}.html", page(f"approfondir/{key}.html", f"{title} · Approfondir · CPE", body, current="ressources.html"))


# --------------------------------------------------------------------------
# Données pour le JavaScript (carnet, positionnement)
# --------------------------------------------------------------------------
def site_data_js():
    import json
    data = {
        "ateliers": [{"n": a["n"], "titre": a["titre"], "but": a["but"], "temps": [t["titre"] for t in a["temps"]]} for a in C.ATELIERS],
        "mallette": [t for _, t, _ in MALLETTE],
        "approfondir": C.APPROFONDIR,
        "echelle": C.ECHELLE,
    }
    with open(os.path.join(ROOT, "assets", "data.js"), "w", encoding="utf-8") as f:
        f.write("window.CPE_DATA=" + json.dumps(data, ensure_ascii=False) + ";\n")


def main():
    site_data_js()
    index_page()
    for a in C.ATELIERS:
        atelier_page(a)
        formateur_page(a)
    positionnement_page()
    carnet_page()
    mallette_page()
    ressources_page()
    formateur_index()
    approfondir_pages()
    print("Site généré.")


if __name__ == "__main__":
    main()
