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
        p = re.sub(r"(\d) h (\d)", "\\1\u00a0h\u00a0\\2", p)
        p = re.sub(r"(\d) (min|h|%)\b", "\\1\u00a0\\2", p)
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
    ("lexique.html", "Lexique"),
]


def _ver():
    import hashlib
    h = hashlib.sha1()
    for f in ("assets/site.css", "assets/site.js", "assets/data.js"):
        p = os.path.join(ROOT, f)
        if os.path.exists(p):
            h.update(open(p, "rb").read())
    return h.hexdigest()[:10]


def page(rel, title, body, desc="", current="", formateur=False, extra_head=""):
    VER = _ver()
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
<link rel="stylesheet" href="{up}assets/site.css?v={VER}">
<script src="{up}assets/data.js?v={VER}" defer></script>
<script src="{up}assets/site.js?v={VER}" defer></script>
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
# Ateliers (stagiaire et formateur) : voir atelier_pages.py
# --------------------------------------------------------------------------
import ateliers as A  # noqa: E402
import atelier_pages as AP  # noqa: E402

BUT = {
    "Découvrir mon métier de CPE": "Situer ce qui relève de mes missions, de la coopération et de la décision d'une autre autorité.",
    "Construire mon année de CPE": "Anticiper l'année de la vie scolaire : instances, AED, conseils, orientation, prévention.",
    "Organiser et piloter la vie scolaire": "Poser un diagnostic de vie scolaire à partir de données fiables et organiser le service sous contraintes.",
    "Animer et accompagner l'équipe AED": "Animer une équipe d'AED, réguler un écart et conduire une réunion qui décide.",
    "Comprendre les adolescents": "Analyser un comportement sans diagnostiquer et tenir le cadre sans humilier.",
    "Accompagner un élève et sa famille": "Repérer des signaux faibles et construire une alliance avec les deux parents.",
    "Gérer un incident et protéger les élèves": "Traiter un incident dans le respect du droit disciplinaire et protéger tous les élèves concernés.",
    "Faire vivre la démocratie scolaire": "Accompagner les élus vers une participation réelle, sans la confisquer.",
    "Une matinée dans la peau du CPE": "Prioriser sous pression, refuser ce qui excède mon rôle et rendre compte de mes choix.",
}
for _a in A.ATELIERS:
    _a["but"] = BUT[_a["titre"]]
    _a["temps"] = _a["phases"]
C.ATELIERS = A.ATELIERS


def total_parcours():
    hors = sum(m for _, items in C.PROGRAMME for it in items if isinstance(it, tuple) for m in [it[1]])
    return hors + sum(AP.duree(C, a) for a in C.ATELIERS)


def arrondi(m):
    h = round(m / 30) / 2
    return (f"{int(h)} h" if h == int(h) else f"{int(h)} h 30")


C.DUREE_TOTALE = f"environ {arrondi(total_parcours())} de travail, temps indicatifs"


def atelier_page(a):
    body = AP.atelier_page(C, a, MALLETTE_BY_ATELIER)
    write(f"atelier-{a['n']}.html", page(f"atelier-{a['n']}.html", f"Atelier {a['n']} · {a['titre']} · CPE", body, desc=a["problematique"]))


def formateur_page(a):
    body = AP.formateur_page(C, a)
    write(f"formateur/atelier-{a['n']}.html", page(f"formateur/atelier-{a['n']}.html", f"Formateur · Atelier {a['n']} · {a['titre']}", body, formateur=True))


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
    <span class="card-txt"><strong>{esc(a['titre'])}</strong><span>{esc(a['accroche'])}</span><span class="card-comp">{comp} <span class="card-time">· temps indicatif {fmt_min(AP.duree(C, a))}</span></span></span>
    <span class="card-state" data-state-for="{a['n']}"></span>
  </a>
</li>""")
    part1 = "".join(cards[:4])
    part2 = "".join(cards[4:])
    statuts = "".join(f"<tr><th scope=\"row\">{esc(a)}</th><td>{esc(b)}</td><td>{esc(c)}</td></tr>" for a, b, c in C.STATUTS)
    body = f"""
<section class="hero hero-home">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Parcours de formation · {esc(C.DUREE_TOTALE)}</p>
      <h1>Neuf situations-problèmes pour entrer dans le métier de CPE.</h1>
      <p class="lead">Vous prenez votre poste au lycée Horizon, un établissement fictif du réseau AEFE. Chaque atelier part d'une vraie difficulté de début de carrière. Vous réagissez d'abord seul. Puis vous enquêtez en groupe dans un dossier où tout n'est pas fiable, vous affrontez un rebondissement et vous défendez vos choix. Le formateur conclut par un bilan et des apports théoriques.</p>
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
    <p class="muted">Suivez les ateliers dans l'ordre : chacun réinvestit les précédents, et le dernier atelier les mobilise tous. Les temps sont indicatifs : le parcours se répartit librement entre plusieurs sessions, en présence ou à distance, et un atelier commencé peut se terminer à la session suivante.</p>
    <div class="days">
      <div><h3 class="day">Entrer dans le métier, organiser l'année et le service</h3><ol class="cards">{part1}</ol></div>
      <div><h3 class="day">Accompagner, protéger, faire participer</h3><p class="small"><a href="quiz.html">Pour reprendre après une pause : le quiz de réactivation →</a></p><ol class="cards">{part2}</ol></div>
    </div>
  </section>

  <section class="block statuts" id="statut">
    <h2>Quel texte s'applique à moi ?</h2>
    <p class="muted">Dans le réseau AEFE, tous les CPE ne relèvent pas des mêmes règles. Ce qui fait foi dépend de votre statut et du statut de votre établissement. Gardez ce tableau en tête dans tous les ateliers.</p>
    <div class="tablewrap"><table><thead><tr><th>Votre situation</th><th>Ce qui fait foi pour vous</th><th>Ce que sont les textes français</th></tr></thead><tbody>{statuts}</tbody></table></div>
    <p class="small muted">Dans tous les cas, les règles de l'établissement (règlement intérieur, protocoles, circuit de protection) s'appliquent à tous, et le CPE agit sous l'autorité du chef d'établissement. Votre situation exacte se vérifie auprès de la direction.</p>
  </section>

  <section class="block three">
    <div><h3>1 · Je me positionne</h3><p>Avant le premier atelier, j'évalue où j'en suis sur les neuf gestes professionnels. Je recommence à la fin.</p><a href="positionnement.html">Me positionner →</a></div>
    <div><h3>2 · J'affronte des situations</h3><p>Chaque atelier a son propre déroulé : débat mouvant, forum-théâtre, simulation de commission, crash-test, enquête de données. Je produis à chaque fois un écrit professionnel jugé sur des critères précis.</p><a href="atelier-1.html">Atelier 1 →</a></div>
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
    <p class="muted">Tous les autres termes du métier sont expliqués dans le <a href="lexique.html">lexique</a>, et au survol dans les ateliers.</p>
    <dl><div><dt>CPE</dt><dd>Conseiller principal d'éducation</dd></div><div><dt>AED</dt><dd>Assistant d'éducation</dd></div><div><dt>AEFE</dt><dd>Agence pour l'enseignement français à l'étranger</dd></div><div><dt>CVL · CVC</dt><dd>Conseil de la vie lycéenne · collégienne</dd></div><div><dt>RI</dt><dd>Règlement intérieur</dd></div><div><dt>pHARe</dt><dd>Programme de lutte contre le harcèlement à l'école</dd></div><div><dt>PAP · PAI · PPS</dt><dd>Plans et projets d'aménagement de la scolarité (voir le lexique)</dd></div><div><dt>IA-IPR EVS</dt><dd>Inspecteur chargé de l'établissement et de la vie scolaire</dd></div></dl>
  </section>
</div>
"""
    write("index.html", page("index.html", f"{C.TITRE} · Formation CPE AEFE", body, current="index.html",
                             desc="Neuf ateliers progressifs pour former les CPE débutants du réseau AEFE."))


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
<section class="hero"><div class="wrap"><p class="eyebrow">Avant et après la formation</p><h1>Me positionner</h1><p class="lead">Pour chacun des neuf gestes professionnels, indiquez où vous en êtes. Faites-le une première fois avant l'atelier 1, puis à la fin du dernier atelier. L'écart montre ce que la formation vous a apporté et ce qui reste à travailler.</p></div></section>
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
    (2, "Mon calendrier annuel de la vie scolaire", "Temps forts mois par mois ; démocratie scolaire ; cycle des AED ; conseils et orientation ; prévention ; périodes de vigilance."),
    (3, "Accueillir, animer et réguler l'équipe AED", "Missions et fiche de poste des AED ; accueil ; consignes ; réunion ; observation factuelle ; entretien de régulation."),
    (4, "Diagnostiquer et piloter la vie scolaire", "Faits étayés ; besoins des élèves ; objectif ; postes ; transmissions ; indicateurs et date de bilan."),
    (5, "Comprendre un comportement d'adolescent", "Comportement observable ; hypothèses multiples ; contexte ; informations manquantes ; réponse éducative à tester."),
    (6, "Conduire un entretien et suivre l'assiduité", "Faits d'assiduité ; questions ouvertes ; parole de l'élève ; coordination ; compte rendu ; date de suivi."),
    (7, "Analyser un incident et choisir la réponse appropriée", "Sécurité ; faits ; personnes à protéger ; qui décide ; punition ou sanction ; dimension éducative ; suivi."),
    (7, "Protéger, alerter et suivre une situation préoccupante", "Sécurité immédiate ; secours si urgence ; personnes compétentes ; protocole local ; trace factuelle ; suivi."),
    (8, "Accompagner les élus et la démocratie scolaire", "Consultation ; compétences des instances ; préparation des élus ; priorités ; décisions ; retour aux élèves."),
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
<section class="hero"><div class="wrap"><p class="eyebrow">Mes outils de prise de poste</p><h1>Ma mallette professionnelle</h1><p class="lead">Neuf fiches à construire au fil des ateliers, puis à personnaliser dans votre établissement. Elles ne remplacent ni un protocole validé, ni les procédures locales.</p>
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
  <section class="block statuts"><h2>Quel texte s'applique à moi ?</h2><div class="tablewrap"><table><thead><tr><th>Votre situation</th><th>Ce qui fait foi pour vous</th><th>Ce que sont les textes français</th></tr></thead><tbody>{"".join(f"<tr><th scope='row'>{esc(x)}</th><td>{esc(y)}</td><td>{esc(z)}</td></tr>" for x, y, z in C.STATUTS)}</tbody></table></div></section>
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
# Lexique du CPE débutant
# --------------------------------------------------------------------------
def lexique_page():
    import unicodedata
    cle = lambda t: unicodedata.normalize("NFD", t.lower()).encode("ascii", "ignore").decode()
    blocs = []
    for a in C.ATELIERS:
        termes = sorted(((t, d) for t, (d, n, _) in C.LEXIQUE.items() if n == a["n"]), key=lambda x: cle(x[0]))
        if not termes:
            continue
        dl = "".join(f'<div><dt id="lex-{cle(t).replace(" ", "-").replace(chr(39), "")}">{esc(t)}</dt><dd>{esc(d)}</dd></div>' for t, d in termes)
        blocs.append(f'<section class="block lexique"><h2>Atelier {a["n"]} · {esc(a["titre"])}</h2><dl>{dl}</dl></section>')
    fmts = sorted({p["format"] for a in C.ATELIERS for p in a["phases"] if p.get("format") in C.FORMATS}, key=cle)
    dlf = "".join(f"<div><dt>{esc(f)}</dt><dd>{esc(C.FORMATS[f])}</dd></div>" for f in fmts)
    body = f"""
<section class="hero"><div class="wrap"><p class="eyebrow">Pour comprendre chaque mot</p><h1>Lexique du CPE débutant</h1><p class="lead">Les mots du métier, rangés par atelier, dans l'ordre où vous les rencontrez. Dans les ateliers, ils sont soulignés en pointillé : survolez-les ou touchez-les pour lire leur définition.</p></div></section>
<div class="wrap">
  {"".join(blocs)}
  <section class="block lexique"><h2>Les formats des ateliers</h2><p class="muted">Comment fonctionne chaque activité proposée par le formateur.</p><dl>{dlf}</dl></section>
  <p class="small muted">Les définitions sont simplifiées pour la formation. Plusieurs d'entre elles décrivent le droit français : dans le réseau AEFE, vérifiez ce qui s'applique dans votre établissement.</p>
</div>"""
    write("lexique.html", page("lexique.html", "Lexique · CPE", body, current="lexique.html"))


# --------------------------------------------------------------------------
# Quiz de réactivation (à chaque reprise après une pause)
# --------------------------------------------------------------------------
QUIZ = [
    ("Quel texte définit aujourd'hui les missions du CPE ?", ["La circulaire de 1982", "La circulaire de 2015", "L'arrêté de 2013", "La fiche de poste de l'établissement"], 1, "La circulaire n° 2015-139 a abrogé celle de 1982. L'arrêté de 2013 fixe les compétences, pas les missions."),
    ("Qui peut prononcer une exclusion temporaire de l'établissement ?", ["Le CPE", "Le professeur qui a constaté les faits", "Le chef d'établissement ou le conseil de discipline", "Le conseil pédagogique"], 2, "Le CPE établit les faits et conseille ; la sanction appartient au chef d'établissement ou au conseil de discipline."),
    ("Un parent exige le nom de l'élève qui a frappé son fils. Vous…", ["Le donnez, c'est son droit", "Refusez, et recentrez l'échange sur son enfant", "Le renvoyez vers le professeur principal", "Lui promettez une sanction rapide"], 1, "On ne communique jamais les données d'un autre élève. On accueille l'inquiétude et l'on parle de ce qui est fait pour son enfant."),
    ("Au lycée Horizon, avant quel rendez-vous les délégués doivent-ils être élus et formés ?", ["Les vacances de fin d'année", "Le premier conseil d'établissement", "Les conseils de classe du troisième trimestre", "La réunion parents-professeurs"], 1, "Les élus siègent au premier conseil d'établissement du 12 novembre : des élections « en novembre » le rendaient impossible."),
    ("Quand se prépare le recrutement des AED de la rentrée ?", ["En septembre, quand on connaît les besoins", "En mai et juin de l'année précédente", "Pendant les vacances d'été", "Après la période d'essai"], 1, "Anticiper en mai et juin permet une prise de poste à la pré-rentrée ; septembre sert aux derniers ajustements."),
    ("Antoine conteste devant l'équipe : « Ici, on a toujours fait comme ça. » La meilleure première réponse ?", ["Le recadrer publiquement", "Céder pour garder la paix", "Reconnaître l'expérience de l'équipe, maintenir la règle, proposer d'en parler en tête-à-tête", "Ne rien répondre"], 2, "Ni épreuve de force en public, ni renoncement : on reconnaît, on maintient, on reprend en entretien."),
    ("La circulaire AED de 2025 s'applique-t-elle à un AED en contrat de droit local ?", ["Oui, c'est un texte national", "Non, son contrat relève du droit local et du règlement de l'établissement", "Seulement pour les heures de formation", "Seulement s'il est français"], 1, "La circulaire vise les AED recrutés en France sur le fondement du code de l'éducation."),
    ("Des photos d'élèves circulent sur le groupe de messagerie personnel des AED. Vous…", ["Laissez faire : c'est leur vie privée", "Rejoignez le groupe pour surveiller", "Informez la direction et mettez fin à l'usage de cet outil pour le service", "Supprimez vous-même les messages"], 2, "Déontologie et protection des données : le CPE informe sans délai la direction ; la suite concernant les personnels relève de l'employeur."),
    ("61 retards la semaine 2, 45 la semaine 3, qui comptait un jour férié. Les retards…", ["Ont baissé de 26 %", "Ont un peu baissé", "N'ont pas baissé de façon démontrée", "Ont augmenté"], 2, "Il faut compter par jour de classe : 11,6 en semaine 1 et 11,25 en semaine 3, soit −3 %. La semaine 2 est incomplète à cause d'une panne de saisie. Les « −26 % » comparent une semaine de quatre jours à une semaine incomplète."),
    ("280 élèves arrivent en sept minutes par un seul portillon. Le retard est d'abord…", ["Un problème de discipline", "Un problème d'organisation", "Un problème de motivation", "Un problème de familles"], 1, "Le CPE regarde le système avant de regarder les élèves : second portillon, horaires des cars, contrôle des carnets."),
]


def quiz_page():
    items = []
    for i, (q, opts, ok, why) in enumerate(QUIZ, 1):
        o = "".join(f'<li><span class="qz-l">{"ABCD"[j]}</span>{esc(x)}</li>' for j, x in enumerate(opts))
        items.append(f"""<li class="qz" data-qz>
  <p class="qz-q"><span class="qz-n">{i}</span>{esc(q)}</p>
  <ol class="qz-opts">{o}</ol>
  <button class="btn ghost small" type="button" data-qz-show>Afficher la réponse</button>
  <div class="qz-a" hidden><p><strong>Réponse {"ABCD"[ok]} · {esc(opts[ok])}.</strong> {esc(why)}</p></div>
</li>""")
    body = f"""
<section class="hero"><div class="wrap"><p class="eyebrow">Ateliers 1 à 4 · environ 15 minutes</p><h1>Quiz de réactivation</h1><p class="lead">À faire à chaque reprise après une pause, avant l'atelier 5 ou en ouverture d'une session à distance. Par équipes, avec une ardoise ou une feuille : le formateur lit la question, chaque équipe écrit sa lettre et la lève en même temps. Une réponse juste vaut un point ; une justification juste en vaut un deuxième.</p>
<div class="hero-actions"><button class="btn light" type="button" data-qz-all>Afficher toutes les réponses</button></div></div></section>
<div class="wrap"><ol class="quiz">{"".join(items)}</ol>
<nav class="next-prev"><a class="btn ghost" href="index.html">← Le parcours</a><a class="btn" href="atelier-5.html">Atelier 5 →</a></nav></div>"""
    write("quiz.html", page("quiz.html", "Quiz de réactivation · CPE", body, current="index.html"))


# --------------------------------------------------------------------------
# Espace formateur : accueil
# --------------------------------------------------------------------------
def formateur_index():
    SCEN = "".join(
        f'<tr><td><a href="atelier-{a["n"]}.html">{a["n"]} · {esc(a["titre"])}</a></td><td>{esc(" · ".join(a.get("moteur", [])))}</td><td class="small">{esc(" → ".join(p.get("format", p["titre"]) for p in a["phases"]))}</td></tr>'
        for a in C.ATELIERS)
    prog = []
    for jour, items in C.PROGRAMME:
        lines = []
        tot = 0
        for it in items:
            if isinstance(it, str):
                k = int(it.split()[1])
                a = C.ATELIERS[k - 1]
                m = AP.duree(C, a)
                tot += m
                lines.append(f'<tr><td><a href="atelier-{k}.html">Atelier {k}</a></td><td>{esc(a["titre"])}</td><td>{fmt_min(m)}</td></tr>')
                continue
            label, m = it
            tot += m
            if label.startswith("Quiz"):
                lines.append(f'<tr><td><a href="../quiz.html">Quiz</a></td><td>{esc(label)}</td><td>{fmt_min(m)}</td></tr>')
            else:
                lines.append(f"<tr><td>—</td><td>{esc(label)}</td><td>{fmt_min(m)}</td></tr>")
        prog.append(f'<div><h3 class="day">{jour} · {fmt_min(tot)}</h3><div class="tablewrap"><table><thead><tr><th></th><th>Séquence</th><th>Durée</th></tr></thead><tbody>{"".join(lines)}</tbody></table></div></div>')
    cards = "".join(f'<li class="card-atelier"><a href="atelier-{a["n"]}.html"><span class="card-no">{a["n"]:02d}</span><span class="card-txt"><strong>{esc(a["titre"])}</strong><span>{fmt_min(AP.duree(C, a))} · {len(a["temps"])} étapes</span></span></a></li>' for a in C.ATELIERS)
    body = f"""
<section class="hero hero-formateur"><div class="wrap"><p class="eyebrow">Espace formateur · {esc(C.DUREE_TOTALE)}</p><h1>Conduire la formation</h1><p class="lead">Déroulés, éléments de correction, points de vigilance et bilans à projeter. Les fiches de chaque atelier et le guide PDF s'ouvrent avec le mot de passe de la formation.</p>
<div class="hero-actions"><a class="btn light" href="../ressources/01_Guide_Formateur_Pedagogie_Active.pdf">Guide formateur (PDF protégé)</a></div></div></section>
<div class="wrap">
  <section class="block"><h2>Le parcours et ses temps indicatifs</h2><p class="muted">Aucun découpage en journées : enchaînez les ateliers dans l'ordre, au rythme du groupe. Un atelier commencé peut se terminer à la session suivante, en présence ou à distance. À chaque reprise, ouvrez par le quiz de réactivation. Total indicatif : {fmt_min(total_parcours())}.</p><div class="days">{"".join(prog)}</div></section>
  <section class="block"><h2>La scénarisation des neuf ateliers</h2>
    <p class="muted">Chaque atelier a son propre moteur, pour que les stagiaires ne retrouvent jamais deux fois le même déroulé. Les formats alternent l'individuel, le groupe, le mouvement et la simulation.</p>
    <div class="tablewrap"><table><thead><tr><th>Atelier</th><th>Moteur</th><th>Enchaînement des étapes</th></tr></thead><tbody>{SCEN}</tbody></table></div>
  </section>
  <section class="block"><h2>Fiches par atelier</h2><ol class="cards grid">{cards}</ol></section>
  <section class="block three">
    <div><h3>Avant la session</h3><ul><li>Constituer des groupes de trois ou quatre ; prévoir des rôles tournants.</li><li>Imprimer les documents à révéler séparément pour les groupes sans écran, et découper les cartes secrètes des jeux de rôle (dans le PDF complet de chaque atelier).</li><li>Préparer le règlement intérieur et les circuits d'alerte de l'établissement d'accueil, après vérification.</li></ul></div>
    <div><h3>Pendant</h3><ul><li>Faire produire une réponse avant de révéler la suite : c'est le ressort de chaque atelier.</li><li>Ne jamais faire jouer une victime : utiliser des cartes d'analyse.</li><li>Arrêter avec bienveillance tout récit de situation réelle identifiable.</li></ul></div>
    <div><h3>Évaluer</h3><ul><li>Positionnement initial avant l'atelier 1, final après le dernier atelier, même si le parcours s'étale sur plusieurs sessions.</li><li>La grille du dernier atelier sert d'évaluation formative de tout le parcours.</li><li>Évaluer le raisonnement et l'ordre des priorités, pas une réponse unique.</li></ul></div>
  </section>
  <section class="block"><h2>Confidentialité de cet espace</h2><p>Les corrigés, les déroulés détaillés, les cartes secrètes, les bilans, le guide PDF et les dossiers complets sont chiffrés avec le mot de passe de la formation. Cette page d'accueil, elle, est lisible par qui connaît son adresse. Ne communiquez pas le mot de passe aux stagiaires avant la fin de l'atelier concerné.</p></section>
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
    quiz_page()
    lexique_page()
    approfondir_pages()
    print("Site généré.")


if __name__ == "__main__":
    main()
