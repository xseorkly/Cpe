# -*- coding: utf-8 -*-
"""Cahier du formateur (PDF) : la conduite de la formation, point par point.

Pour chaque atelier : préparation, impressions, plan de distribution, déroulé
étape par étape (ce que je dis, ce que je distribue, ce que je fais), bilan,
corrigé, points de vigilance, puis tous les documents à photocopier.

Usage (depuis la racine du dépôt, après avoir défini le mot de passe comme
pour pdfs.py) :
    python3 _build/cahier.py
Variable CAHIER_CLAIR=1 : génère une version non chiffrée, pour relecture
locale uniquement (ne pas la publier).
"""
import os
import re
import sys

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (CondPageBreak, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import pdfs as P  # noqa: E402  (polices, styles, conversion HTML, chiffrement)

C, B, AP, S = P.C, P.B, P.B.AP, P.S
clean, fmt, html_flow, doc_flow = P.clean, P.fmt, P.html_flow, P.doc_flow

NAVY, ACCENT, LINE, SOFT = P.NAVY, P.ACCENT, P.LINE, P.SOFT
RED = colors.HexColor("#a3312b")
GREEN = colors.HexColor("#2f6b4f")
INK = colors.HexColor("#555b66")
W = 170 * mm

S2 = {
    "tag": ParagraphStyle("tag", fontName="Sans-B", fontSize=7.4, leading=9.5, textColor=colors.white),
    "act": ParagraphStyle("act", fontName="Sans", fontSize=9.2, leading=12.8),
    "actli": ParagraphStyle("actli", fontName="Sans", fontSize=9.2, leading=12.8, leftIndent=10, bulletIndent=0),
    "quote": ParagraphStyle("quote", fontName="Sans-I", fontSize=9.2, leading=12.8, textColor=colors.HexColor("#1d2433")),
    "step": ParagraphStyle("step", fontName="Serif-B", fontSize=13, leading=16, textColor=colors.white),
    "stepsub": ParagraphStyle("stepsub", fontName="Sans", fontSize=8.4, leading=11, textColor=colors.white),
    "cover": ParagraphStyle("cover", fontName="Serif-B", fontSize=34, leading=40, textColor=NAVY),
    "coversub": ParagraphStyle("coversub", fontName="Sans", fontSize=12.5, leading=17, textColor=INK),
    "big": ParagraphStyle("big", fontName="Serif-B", fontSize=64, leading=74, alignment=1, textColor=NAVY),
    "card": ParagraphStyle("card", fontName="Sans", fontSize=10.5, leading=14.5),
    "cardh": ParagraphStyle("cardh", fontName="Sans-B", fontSize=11.5, leading=15, textColor=NAVY),
    "toc": ParagraphStyle("toc", fontName="Sans", fontSize=10, leading=15),
}

TAGS = {
    "J'INSTALLE": colors.HexColor("#5b6472"),
    "JE DISTRIBUE": ACCENT,
    "JE DIS": NAVY,
    "JE LIS": NAVY,
    "JE FAIS VOTER": NAVY,
    "JE RÉVÈLE": RED,
    "JE JOUE": RED,
    "JE CONDUIS": GREEN,
    "JE RELANCE": colors.HexColor("#7a4d8c"),
    "J'ATTENDS": colors.HexColor("#8a6d1d"),
    "JE REPRENDS": colors.HexColor("#5b6472"),
    "J'ENCHAÎNE": colors.HexColor("#333a46"),
    "JE POSE": NAVY,
    "JE PROJETTE": NAVY,
    "JE FAIS ÉCRIRE": GREEN,
    "JE RAMASSE": colors.HexColor("#333a46"),
}


# ---------------------------------------------------------------- outils
def hm(m):
    h, r = divmod(m, 60)
    return f"{h}:{r:02d}"


def phrases(t):
    t = clean(t)
    return [x for x in re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-ÝÉ«])", t) if x.strip()]


def para(t, st="act"):
    return Paragraph(t, S2[st] if st in S2 else S[st])


def bullets(items, st="actli", num=False):
    return [Paragraph(clean(x), S2.get(st, S.get(st)), bulletText=(f"{i}." if num else "•")) for i, x in enumerate(items, 1)]


def action_table(rows):
    """rows : liste de (tag, [flowables])."""
    data = []
    st = [("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), .4, LINE),
          ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
          ("LEFTPADDING", (0, 0), (0, -1), 5)]
    for i, (tag, flow) in enumerate(rows):
        data.append([Paragraph(tag, S2["tag"]), flow])
        st.append(("BACKGROUND", (0, i), (0, i), TAGS.get(tag, NAVY)))
    t = Table(data, colWidths=[27 * mm, W - 27 * mm])
    t.setStyle(TableStyle(st))
    return t


def bar(text, sub=None, color=NAVY):
    cells = [Paragraph(text, S2["step"])]
    if sub:
        cells.append(Paragraph(sub, S2["stepsub"]))
    t = Table([[cells]], colWidths=[W])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), color), ("TOPPADDING", (0, 0), (-1, -1), 6),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 7), ("LEFTPADDING", (0, 0), (-1, -1), 8)]))
    return t


def box(flow, color=SOFT, border=LINE):
    t = Table([[flow]], colWidths=[W])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), color), ("BOX", (0, 0), (-1, -1), .6, border),
                           ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                           ("LEFTPADDING", (0, 0), (-1, -1), 9), ("RIGHTPADDING", (0, 0), (-1, -1), 9)]))
    return t


def check_table(items, widths=(8 * mm, W - 8 * mm)):
    t = Table([[Paragraph("☐", S["cell"]), Paragraph(clean(x), S["cell"])] for x in items], colWidths=list(widths))
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), .3, LINE),
                           ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    return t


def doc_label(a, k):
    d = a["docs"][k - 1]
    return f"Doc. {k} · {d['titre']}"


def mat_pour(a, k):
    """Ligne de matériel qui parle du document k, s'il y en a une."""
    rx = re.compile(r"[Dd]ocuments? %d(?!\d)" % k)
    return next((m for m in a["formateur"]["materiel"] if rx.search(m)), None)


def mode_doc(a, k):
    d = a["docs"][k - 1]
    m = mat_pour(a, k)
    if m:
        return m
    if d.get("secret"):
        return "Cartes secrètes découpées, remises face cachée aux seuls joueurs concernés."
    if d.get("type") == "Rebondissement":
        return "Un exemplaire par groupe, imprimé à part, sous enveloppe fermée : remis à ce moment précis, sans commentaire."
    if d.get("type") == "Simulation":
        return "Un jeu de cartes par groupe de joueurs, découpé à l'avance."
    if d.get("type") == "Outil":
        return "Un exemplaire par stagiaire (ou par binôme)."
    return "Un exemplaire par stagiaire."


def groupe_label(a):
    return next((q.get("mission_label") for q in a["phases"] if q.get("mission")), None) or "Groupe"


def debuts(a):
    t, out = 0, []
    for p in a["phases"]:
        out.append(t)
        t += p["duree"]
    return out, t


# ---------------------------------------------------------------- parties communes
def couverture():
    f = [Spacer(1, 40 * mm), Paragraph("FORMATION DES CPE DU RÉSEAU AEFE", S["eyebrow"]),
         Paragraph("Cahier du formateur", S2["cover"]), Spacer(1, 4),
         Paragraph(f"« {C.TITRE} » · neuf ateliers · {fmt(B.total_parcours())} de travail en temps indicatifs", S2["coversub"]),
         Spacer(1, 14 * mm),
         box([Paragraph("Ce cahier vous accompagne pendant l'animation. Pour chaque atelier : ce que vous préparez, ce que vous imprimez, "
                        "ce que vous dites, ce que vous distribuez et à quel moment, ce que vous faites pendant que les stagiaires travaillent, "
                        "comment vous concluez. Tous les documents à photocopier suivent chaque atelier.", S["p"])]),
         Spacer(1, 50 * mm),
         Paragraph("Document réservé au formateur : il contient les rebondissements, les cartes secrètes et les éléments de correction. "
                   "Ne le transmettez pas aux stagiaires.", S["small"]),
         Paragraph(C.VERSION, S["small"]), PageBreak()]
    return f


def sommaire():
    f = [Paragraph("Sommaire", S["h1"])]
    items = ["Mode d'emploi du cahier", "Le parcours et ses temps indicatifs", "Préparer la formation : la liste de contrôle",
             "Les principes de conduite", "Ouvrir, reprendre et clore la formation", "Récapitulatif des impressions"]
    items += [f"Atelier {a['n']} · {a['titre']} ({fmt(AP.duree(C, a))})" for a in C.ATELIERS]
    items += ["Textes de référence"]
    f += [Paragraph(x, S2["toc"], bulletText="•") for x in items]
    f.append(Spacer(1, 6))
    f.append(Paragraph("Chaque fiche d'atelier suit le même ordre : 1. l'atelier en bref · 2. préparer · 3. le plan de distribution · "
                       "4. le déroulé point par point · 5. le bilan · 6. le corrigé · 7. les points de vigilance · 8. si le temps manque · "
                       "9. les documents à photocopier.", S["p"]))
    return f


def mode_emploi():
    f = [Paragraph("Mode d'emploi du cahier", S["h1"]),
         Paragraph("Chaque étape d'atelier se lit de haut en bas, dans l'ordre où vous agissez. Une étiquette de couleur dit la nature de chaque geste :", S["p"])]
    rows = [("J'INSTALLE", "La disposition de la salle et le matériel à mettre en place avant de lancer l'étape."),
            ("JE DISTRIBUE", "Ce que vous remettez, à qui et comment. Le numéro renvoie au document photocopiable placé après la fiche."),
            ("JE DIS", "La consigne à lire telle qu'elle est écrite : elle est identique à celle que les stagiaires voient sur le site."),
            ("JE LIS", "Un texte à lire à voix haute (affirmations, annonce)."),
            ("JE FAIS VOTER", "La question et les réponses possibles, à main levée ou sur le site."),
            ("JE RÉVÈLE", "Des événements à faire apparaître un par un, à l'heure indiquée."),
            ("JE JOUE", "Vous tenez un rôle (proviseure, élève, gestionnaire, parent au téléphone)."),
            ("JE CONDUIS", "Ce que vous faites pendant que les stagiaires travaillent."),
            ("JE RELANCE", "Les questions pour mettre en difficulté, à poser en circulant entre les groupes."),
            ("J'ATTENDS", "Ce qui doit figurer sur l'affiche ou dans la production."),
            ("JE REPRENDS", "Le retour sur un vote ou une position du début de l'atelier."),
            ("J'ENCHAÎNE", "Comment vous clôturez l'étape et passez à la suivante.")]
    f.append(action_table([(t, [Paragraph(x, S2["act"])]) for t, x in rows]))
    f += [Spacer(1, 8), Paragraph("Les repères de temps", S["h3"]),
          Paragraph("Les horaires « 0:00 → 0:10 » sont comptés depuis le début de l'atelier. Ce sont des temps indicatifs : "
                    "aucun découpage en journées n'est imposé. Un atelier commencé peut se terminer à la session suivante, en présence ou à distance. "
                    "Chaque fiche indique ce qui ne se coupe jamais et ce qui peut se poursuivre à distance.", S["p"]),
          Paragraph("Les deux versions des documents", S["h3"]),
          Paragraph("Le site propose pour chaque atelier un <b>dossier stagiaire</b> (ressources/kits/atelier-N-dossier.pdf), sans les rebondissements ni les cartes secrètes, "
                    "et un <b>dossier complet</b> protégé. Les documents reproduits dans ce cahier correspondent au dossier complet : "
                    "ceux qui portent un bandeau rouge ne se distribuent qu'au moment prévu.", S["p"]),
          Paragraph("Où trouver le reste en ligne", S["h3"])]
    f += bullets(["Les fiches formateur en ligne (formateur/atelier-N.html) : même déroulé, avec le diaporama de bilan à projeter.",
                  "La page de chaque atelier côté stagiaire : consignes, dossier, zones de prise de notes. Projetez-la pour lancer une étape si la salle n'a pas d'écrans individuels.",
                  "Le carnet du stagiaire (ressources/02), la banque de prompts IA (ressources/03) et la mallette réflexe (ressources/04)."])
    return f


def parcours():
    f = [PageBreak(), Paragraph("Le parcours et ses temps indicatifs", S["h1"]),
         Paragraph("Enchaînez les ateliers dans l'ordre, au rythme du groupe. Ce qui déborde se poursuit à distance ou lors d'une session ultérieure. "
                   "À chaque reprise après une pause de plusieurs jours, ouvrez par le quiz de réactivation.", S["p"])]
    rows = [["Partie", "Séquence", "Temps", "Production"]]
    for partie, items in C.PROGRAMME:
        for it in items:
            if isinstance(it, str):
                a = C.ATELIERS[int(it.split()[1]) - 1]
                rows.append([partie, f"<b>Atelier {a['n']}</b> · {a['titre']}<br/><i>{' · '.join(a.get('moteur', []))}</i>", fmt(AP.duree(C, a)), a["production"]])
            else:
                rows.append([partie, it[0], fmt(it[1]), ""])
    rows.append(["", "<b>Total indicatif</b>", f"<b>{fmt(B.total_parcours())}</b>", ""])
    f.append(P.table(rows, [34 * mm, 66 * mm, 18 * mm, 52 * mm]))
    f += [Spacer(1, 8), Paragraph("Public", S["h3"]), Paragraph(C.PUBLIC, S["p"]),
          Paragraph("Finalité", S["h3"]), Paragraph(C.FINALITE, S["p"])]
    return f


def preparer():
    f = [PageBreak(), Paragraph("Préparer la formation : la liste de contrôle", S["h1"])]
    blocs = [
        ("Deux à trois semaines avant", [
            "Récupérer le mot de passe de la formation. Vérifier que les fiches formateur en ligne, le guide et les dossiers complets s'ouvrent.",
            "Demander à la direction de l'établissement d'accueil son règlement intérieur, son organigramme et ses circuits d'alerte (protection de l'enfance, harcèlement, incident grave). Ils servent de point de comparaison dans les ateliers 1, 4 et 7 : les vérifier avec la direction avant de les citer.",
            "Recenser le statut de chaque stagiaire (fonctionnaire détaché, contractuel, recruté local, faisant fonction) et son ancienneté dans la fonction : les ateliers 1 et 2 s'appuient dessus.",
            "Arrêter le calendrier des sessions en présence et à distance. Prévoir de s'arrêter de préférence à la fin d'un atelier, sinon après sa production.",
            "Envoyer aux stagiaires l'adresse du site et leur demander d'apporter un ordinateur ou une tablette. Les notes sont enregistrées dans le navigateur : il faut revenir avec le même appareil et le même navigateur.",
        ]),
        ("Une semaine avant", [
            "Composer quatre groupes de trois à cinq stagiaires (pour 12 à 20 personnes). Mélanger les statuts et les établissements. Avec moins de huit stagiaires : deux groupes, chacun prend deux missions.",
            "Lancer les impressions avec le récapitulatif des pages suivantes. Classer par atelier, puis par étape.",
            "Préparer une pochette par atelier et par groupe, et une enveloppe fermée par groupe pour chaque rebondissement, marquée « À ouvrir quand le formateur le dit ».",
            "Découper les cartes : cartes « moments forts » (atelier 2), cartes secrètes (ateliers 3, 6 et 7), cartes de commission et de course contre la montre (atelier 7), cartes de trio (atelier 8), événements de la matinée (atelier 9).",
            "Réunir le matériel : papier kraft, affiches A3, post-it de trois couleurs, marqueurs, pâte adhésive, minuteur visible de toute la salle, calculatrices (atelier 4), un téléphone (atelier 9), des enveloppes (lettre de l'atelier 9).",
        ]),
        ("La veille ou le matin", [
            "Disposer la salle en îlots de quatre ou cinq, garder un espace dégagé pour le débat mouvant, le forum-théâtre et l'aquarium, libérer des pans de mur pour les affiches.",
            "Tester le vidéoprojecteur avec la fiche formateur de l'atelier du jour : c'est elle qui porte le diaporama de bilan.",
            "Afficher au mur le programme de la session et les quatre rôles de groupe : animateur, gardien du temps, rapporteur, avocat du diable.",
            "Poser sur votre table les pochettes de l'atelier dans l'ordre des étapes, et relire la fiche du cahier : consignes, relances, corrigé.",
        ]),
    ]
    for titre, items in blocs:
        f += [Paragraph(titre, S["h3"]), check_table(items), Spacer(1, 4)]
    return f


def principes():
    f = [Paragraph("Les principes de conduite", S["h2"])]
    f += bullets([
        "Faire produire une réponse avant de révéler la suite : c'est le ressort de chaque atelier. Ne pas désigner les documents pièges avant le bilan.",
        "Lire les consignes telles qu'elles sont écrites, puis annoncer à voix haute chaque changement de temps.",
        "Faire tourner les rôles de groupe d'un atelier à l'autre, avocat du diable compris.",
        "Ne jamais faire jouer une victime : les situations sensibles s'analysent avec des cartes.",
        "N'utiliser que des données fictives. Arrêter avec bienveillance tout récit de situation réelle identifiable et proposer un échange individuel après la séance.",
        "Évaluer le raisonnement et l'ordre des priorités, pas une réponse unique.",
    ], "li")
    return f


def hors_ateliers():
    f = [PageBreak(), Paragraph("Ouvrir, reprendre et clore la formation", S["h1"]),
         bar("Accueil, contrat de formation, positionnement initial", "20 min · toute la salle · avant l'atelier 1")]
    f.append(action_table([
        ("J'INSTALLE", [para("Tables en îlots selon les groupes prévus, programme et rôles affichés, site ouvert au vidéoprojecteur sur la page d'accueil.")]),
        ("JE DIS", [para("0:00 → 0:05 · Accueil et tour de présentation en une phrase : prénom, établissement, statut, depuis quand en poste.")]),
        ("JE DIS", [para("0:05 → 0:10 · Le contrat de formation :"), *bullets([
            "on part de situations-problèmes : vous répondez d'abord, les apports viennent ensuite ;",
            "toutes les situations sont fictives : on ne cite ni élève, ni collègue, ni établissement réels ;",
            "ce qui se dit dans le groupe reste dans le groupe ; on a le droit de se tromper ;",
            "les temps sont indicatifs : ce qui déborde se poursuit à distance ou à la session suivante ;",
            "chaque groupe a quatre rôles qui tournent : animateur, gardien du temps, rapporteur, avocat du diable."])]),
        ("JE PROJETTE", [para("0:10 → 0:13 · Le site : les neuf ateliers, « Mon carnet » (toutes les notes, export et sauvegarde), la mallette réflexe, le lexique. Rappeler que les notes restent dans le navigateur de l'appareil.")]),
        ("JE FAIS ÉCRIRE", [para("0:13 → 0:20 · Le positionnement initial (page « Positionnement »), seul, sur l'échelle de 1 à 4. Sans appareil : la première page du carnet PDF. Je ne ramasse pas : il sera repris à la fin de la formation.")]),
    ]))
    f += [Spacer(1, 8), bar("Quiz de réactivation", "15 min · à chaque reprise après une pause de plusieurs jours")]
    f.append(action_table([
        ("JE PROJETTE", [para("Le quiz (page « Quiz »). Chacun répond seul sur son appareil, ou à main levée question par question.")]),
        ("JE CONDUIS", [para("0:00 → 0:08 · réponses individuelles. 0:08 → 0:13 · correction collective : pour chaque erreur fréquente, faire retrouver la règle par un stagiaire plutôt que la donner.")]),
        ("J'ENCHAÎNE", [para("0:13 → 0:15 · Rappeler ce qui a été vu, l'atelier du jour et sa production. Si un atelier est resté inachevé, repartir de son étape suivante avec la fiche de ce cahier.")]),
    ]))
    f += [Spacer(1, 8), bar("Positionnement final et évaluation de la formation", "15 min · après l'atelier 9")]
    f.append(action_table([
        ("JE FAIS ÉCRIRE", [para("0:00 → 0:07 · Le positionnement final, sur la même page que le positionnement initial : chacun compare ses deux colonnes.")]),
        ("JE POSE", [para("0:07 → 0:10 · Un tour de table : « Sur quel point avez-vous le plus bougé ? Sur lequel demandez-vous encore de l'aide ? » Noter les besoins de formation continue qui reviennent.")]),
        ("JE DISTRIBUE", [para("0:10 → 0:15 · Le questionnaire d'évaluation de la formation prévu par la zone, et le rappel des ressources : mallette réflexe, banque de prompts, carnet exportable. Rappeler d'exporter « Mon carnet » avant de changer d'appareil.")]),
    ]))
    return f


def impressions(a):
    """Lignes du tableau d'impressions d'un atelier : (quoi, combien, quand)."""
    n = a["n"]
    debut, _ = debuts(a)
    inl, sec = AP.inline_ids(a), AP.secret_ids(a)
    lab = groupe_label(a)
    rows, vus = [], set()
    for i, p in enumerate(a["phases"], 1):
        quand = f"Étape {i} · {hm(debut[i - 1])}"
        for k in p.get("docs", []):
            if k in vus:
                continue
            vus.add(k)
            rows.append([doc_label(a, k), mode_doc(a, k), quand])
        if p.get("dossier") and a["groupes"]:
            for gi, g in enumerate(a["groupes"], 1):
                ks = [k for k in g["docs"] if k not in inl and k not in sec]
                rows.append([f"Jeu du {lab.lower()} {gi} · {g['nom']} : doc. {', '.join(map(str, ks))}",
                             "Un exemplaire par membre du groupe. Gardez deux dossiers complets sur votre table pour les autres pistes.", quand])
                vus.update(ks)
        if p.get("mission") and a["groupes"]:
            rows.append([f"Fiches mission ({len(a['groupes'])})", f"Une par {lab.lower()} (annexe de l'atelier).", quand])
        if p.get("production"):
            rows.append(["Grille des critères de réussite", "Une par groupe, plus une par observateur (annexe de l'atelier).", quand])
    for k in sorted(sec):
        if k not in vus:
            vus.add(k)
            ph = next((i for i, p in enumerate(a["phases"], 1) if k in p.get("docs", [])), None)
            rows.append([doc_label(a, k), mode_doc(a, k), f"Étape {ph}" if ph else "Au moment du jeu"])
    for k in range(1, len(a["docs"]) + 1):
        if k not in vus:
            rows.append([doc_label(a, k), mode_doc(a, k), "Dossier"])
    if n == 1:
        rows.insert(0, ["Affichettes « D'accord » et « Pas d'accord »", "Une de chaque, A4 ou A3 (annexe de l'atelier).", "Avant l'étape 1"])
    if any(p.get("sequence") for p in a["phases"]):
        rows.append(["Cartes « événements »", "Un jeu par groupe, découpé, retourné, dans l'ordre des heures (annexe).", "Étape 2"])
    return rows


def recap_impressions():
    f = [PageBreak(), Paragraph("Récapitulatif des impressions", S["h1"]),
         Paragraph("Quantités pour quatre groupes. « Par stagiaire » : comptez un exemplaire de plus que le nombre de participants. "
                   "Les documents portant un bandeau rouge (rebondissements, cartes secrètes) s'impriment à part.", S["p"])]
    for a in C.ATELIERS:
        f.append(CondPageBreak(40 * mm))
        f.append(Paragraph(f"Atelier {a['n']} · {a['titre']}", S["h3"]))
        f.append(P.table([["Document ou fiche", "Combien et comment", "Quand"]] + impressions(a), [62 * mm, 82 * mm, 26 * mm]))
    return f


# ---------------------------------------------------------------- fiche atelier
def en_bref(a):
    n = a["n"]
    total = AP.duree(C, a)
    f = [PageBreak(), Paragraph(f"ATELIER {n} · TEMPS INDICATIF {fmt(total).upper()}", S["eyebrow"]),
         Paragraph(a["titre"], S["h1"]),
         box([Paragraph("<b>Problématique.</b> " + clean(a["problematique"]), S["p"]),
              Paragraph("<b>Ce que les stagiaires produisent :</b> " + clean(a["production"]), S["p"]),
              Paragraph("<b>Le moteur de l'atelier :</b> " + " · ".join(a.get("moteur", [])), S["p"])]),
         Paragraph("1. L'atelier en bref", S["h2"]),
         Paragraph("La situation de départ", S["h3"])]
    f += html_flow(a["situation"])
    f.append(Paragraph("Objectifs", S["h3"]))
    f += bullets(a["objectifs"], "li")
    f.append(Paragraph("Compétences : " + " ; ".join(f"<b>{k}</b> {C.C2013[k]}" for k in a["competences"]) + f". Référentiel 2026 : {a['blocs_detail']}.", S["small"]))
    debut, fin = debuts(a)
    rows = [["Horaire", "Étape", "Format", "Modalité", "Documents"]]
    for i, p in enumerate(a["phases"], 1):
        docs = ", ".join(map(str, p.get("docs", [])))
        if p.get("dossier"):
            docs = (docs + " + " if docs else "") + "dossier"
        rows.append([f"{hm(debut[i - 1])} → {hm(debut[i - 1] + p['duree'])}", f"<b>{i}. {p['titre']}</b>", p.get("format", ""), p["modalite"], docs])
    rows.append([f"{hm(fin)} → {hm(fin + C.BILAN_MIN)}", "<b>Bilan</b>", "Retour collectif et diaporama", "Toute la salle", "—"])
    f += [Paragraph("Le minutage", S["h3"]), P.table(rows, [22 * mm, 42 * mm, 36 * mm, 46 * mm, 24 * mm])]
    return f


def preparation(a):
    f = [CondPageBreak(60 * mm), Paragraph("2. Préparer l'atelier", S["h2"]), Paragraph("Le matériel prévu", S["h3"]),
         check_table(a["formateur"]["materiel"] + ["Ce cahier ouvert à la fiche de l'atelier, la fiche formateur en ligne prête à projeter pour le bilan."])]
    if a["groupes"]:
        lab = groupe_label(a)
        f += [Paragraph(f"Les {lab.lower()}s et leurs missions", S["h3"]),
              P.table([[lab, "La question", "Pistes dans le dossier"]] +
                      [[f"<b>{i}. {g['nom']}</b>", g["angle"], "doc. " + ", ".join(map(str, g["docs"]))] for i, g in enumerate(a["groupes"], 1)],
                      [42 * mm, 98 * mm, 30 * mm])]
    f += [Paragraph("Ce que j'imprime", S["h3"]),
          P.table([["Document ou fiche", "Combien et comment", "Quand"]] + impressions(a), [62 * mm, 82 * mm, 26 * mm])]
    return f


def plan_distribution(a):
    debut, _ = debuts(a)
    rows = [["Moment", "Je remets", "À qui, comment"]]
    for i, p in enumerate(a["phases"], 1):
        m = f"Étape {i} · {hm(debut[i - 1])}<br/><i>{p['titre']}</i>"
        items = []
        for k in p.get("docs", []):
            items.append((doc_label(a, k), mode_doc(a, k)))
        if p.get("dossier"):
            items.append(("Le dossier documentaire", "Chaque groupe reçoit son jeu ; le dossier complet reste disponible sur votre table et sur le site."))
        if p.get("mission"):
            items.append(("La fiche mission", "Une par groupe."))
        if p.get("production"):
            items.append(("La grille des critères de réussite", "Une par groupe et par observateur."))
        if p.get("sequence"):
            items.append(("Les cartes « événements »", "Une à une, à l'heure indiquée, ou révélées à l'écran."))
        if not items:
            items.append(("—", "Rien à distribuer : on travaille avec ce qui est déjà sur les tables."))
        for j, (q, c) in enumerate(items):
            rows.append([m if j == 0 else "", q, c])
    return [CondPageBreak(50 * mm), Paragraph("3. Le plan de distribution", S["h2"]),
            Paragraph("Ce qui n'est pas encore distribué reste sur votre table, dans l'ordre. Ne remettez jamais un rebondissement en avance.", S["p"]),
            P.table(rows, [36 * mm, 58 * mm, 76 * mm])]


def etape(a, i, p, t0, relances_ici):
    n = a["n"]
    lab = groupe_label(a)
    fin = t0 + p["duree"]
    rows = []
    fmt_txt = C.FORMATS.get(p.get("format", ""))
    inst = [para(f"<b>Disposition :</b> {clean(p['modalite'])}.")]
    if fmt_txt:
        inst.append(para(f"<b>Le format :</b> {clean(fmt_txt)}"))
    if p.get("roles"):
        inst.append(para(f"<b>Rôles :</b> je fais attribuer dans chaque groupe animateur, gardien du temps, rapporteur et avocat du diable (il défend la position inverse de celle du groupe). Les rôles tournent d'un atelier à l'autre."))
    rows.append(("J'INSTALLE", inst))
    dist = []
    for k in p.get("docs", []):
        dist.append(Paragraph(f"<b>{doc_label(a, k)}</b> — {clean(mode_doc(a, k))}", S2["actli"], bulletText="•"))
    if p.get("dossier") and a["groupes"]:
        inl, sec = AP.inline_ids(a), AP.secret_ids(a)
        for gi, g in enumerate(a["groupes"], 1):
            ks = [k for k in g["docs"] if k not in sec]
            dist.append(Paragraph(f"<b>{lab} {gi} · {g['nom']}</b> : sa fiche mission et les doc. {', '.join(map(str, ks))}", S2["actli"], bulletText="•"))
    if p.get("production"):
        dist.append(Paragraph("<b>La grille des critères de réussite</b>, une par groupe et par observateur.", S2["actli"], bulletText="•"))
    if p.get("sequence"):
        dist.append(Paragraph("<b>Les cartes « événements »</b>, retournées, à révéler une par une (voir ci-dessous).", S2["actli"], bulletText="•"))
    if dist:
        rows.append(("JE DISTRIBUE", dist))
    if "formateur joue" in p.get("format", "").lower():
        rows.append(("JE JOUE", [para(clean(p.get("format", "")) + ". Tenir le rôle sans en sortir ; ne répondre qu'aux questions posées.")]))
    rows.append(("JE DIS", [Paragraph("« " + clean(p["consigne"]) + " »", S2["quote"])]))
    if p.get("affirmations"):
        rows.append(("JE LIS", [para("Une par une, sans commentaire. Après chaque affirmation : laisser se placer, faire justifier deux volontaires de chaque côté, noter la répartition au tableau."),
                                *bullets(p["affirmations"], num=True)]))
    if p.get("vote"):
        v = p["vote"]
        rows.append(("JE FAIS VOTER", [para(f"<b>{clean(v['question'])}</b> — à main levée ou sur le site. Je note la répartition au tableau : elle sera reprise plus tard."),
                                       *bullets(v["options"])]))
    if p.get("sequence"):
        t = Table([[Paragraph(f"<b>{h}</b>", S["cell"]), Paragraph(clean(x), S["cell"])] for h, x in p["sequence"]], colWidths=[16 * mm, W - 27 * mm - 22 * mm])
        t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), .3, LINE)]))
        rows.append(("JE RÉVÈLE", [para("Les événements, un par un, à l'heure fictive indiquée. Ne pas attendre que le groupe ait fini le précédent : c'est la pression du réel."), t]))
    rows.append(("JE CONDUIS", bullets(phrases(p.get("conduite") or a["formateur"]["deroule"][i - 1]))))
    if relances_ici:
        rows.append(("JE RELANCE", [para("En circulant, choisir une ou deux questions par groupe, adressées à l'avocat du diable ou au rapporteur :"),
                                    *bullets(a["formateur"]["relances"])]))
    if p.get("affiche"):
        rows.append(("J'ATTENDS", [para("<b>Sur l'affiche :</b> " + clean(p["affiche"]))]))
    if p.get("production"):
        rows.append(("J'ATTENDS", [para(f"<b>La production :</b> {clean(a['production'])} Critères de réussite :"), *bullets(a["criteres"], num=True)]))
    if p.get("rappel"):
        rows.append(("JE REPRENDS", [para("Je ressors ce qui a été noté au début de l'atelier (répartition, positions, étiquettes) et je fais parler en priorité ceux qui ont changé d'avis.")]))
    if p.get("rappel_vote"):
        k = next((j for j, q in enumerate(a["phases"], 1) if q.get("vote", {}).get("id") == p["rappel_vote"]), None)
        rows.append(("JE REPRENDS", [para(f"Je remets au tableau la répartition du vote de l'étape {k} et je fais comparer : qu'est-ce qui a fait bouger ?")]))
    nxt = a["phases"][i]["titre"] if i < len(a["phases"]) else "le bilan"
    ench = [f"À {hm(fin - 2)}, j'annonce « deux minutes ». À {hm(fin)}, je clôture, même si tout n'est pas fini : on en reparle au bilan."]
    if p.get("affiche"):
        ench.append("Les affiches restent au mur jusqu'à la fin de l'atelier.")
    if p.get("production"):
        ench.append("Je photographie ou je ramasse les productions : elles servent au bilan.")
    ench.append(f"J'annonce la suite : « {nxt} ».")
    rows.append(("J'ENCHAÎNE", bullets(ench)))
    head = bar(f"Étape {i} · {clean(p['titre'])}", f"{hm(t0)} → {hm(fin)} · {p['duree']} min · {clean(p.get('format', ''))}")
    return [CondPageBreak(55 * mm), head, Spacer(1, 2), action_table(rows), Spacer(1, 10)]


def slides_flow(a):
    out = []
    for s_ in a["slides"]:
        if s_["t"] == "titre":
            txt = f"<b>{s_['titre']}</b>"
        elif s_["t"] == "points":
            txt = f"<b>{s_['titre']}</b> — " + " ; ".join(s_["points"])
        elif s_["t"] == "deux":
            txt = f"<b>{s_['titre']}</b> — {s_['a'][0]} : " + " ; ".join(s_["a"][1]) + f". {s_['b'][0]} : " + " ; ".join(s_["b"][1])
        elif s_["t"] == "etapes":
            txt = f"<b>{s_['titre']}</b> — " + " ; ".join(f"{l} : {x}" for l, x in s_["etapes"])
        elif s_["t"] == "def":
            txt = f"<b>{s_['titre']}</b> — <i>{s_['terme']}</i>. {s_['definition']}"
        else:
            txt = f"<b>À retenir</b> — {s_['texte']}"
        out.append(Paragraph(clean(txt), S2["actli"], bulletText="▸"))
    return out


def bilan(a):
    _, fin = debuts(a)
    rows = [
        ("JE POSE", [para(f"{hm(fin)} → {hm(fin + 7)} · Les trois questions de clôture, une à une, à toute la salle :"), *bullets(a["cloture"], num=True)]),
        ("JE CONDUIS", [para(f"{hm(fin + 7)} → {hm(fin + 12)} · Le retour sur les pièges du dossier : faire nommer par la salle les documents qui pouvaient induire en erreur, puis confirmer avec le corrigé ci-après. Revenir sur les affiches et productions encore au mur.")]),
        ("JE PROJETTE", [para(f"{hm(fin + 12)} → {hm(fin + 18)} · Le diaporama de bilan, depuis la fiche formateur en ligne de l'atelier :"), *slides_flow(a)]),
        ("JE FAIS ÉCRIRE", [para(f"{hm(fin + 18)} → {hm(fin + C.BILAN_MIN)} · Dans « Mon carnet » ou le carnet PDF : « Ce que je retiens » et la fiche réflexe de l'atelier dans la mallette.")]),
    ]
    return [CondPageBreak(60 * mm), Paragraph("5. Le bilan", S["h2"]),
            bar("Bilan", f"{hm(fin)} → {hm(fin + C.BILAN_MIN)} · {C.BILAN_MIN} min · toute la salle"), Spacer(1, 2), action_table(rows)]


def corrige(a):
    f = [CondPageBreak(40 * mm), Paragraph("6. Le corrigé : ce que l'on attend", S["h2"])]
    f += html_flow(a["formateur"]["attendus"])
    f += [Paragraph("7. Les points de vigilance", S["h2"])]
    f += bullets(a["formateur"]["vigilance"], "li")
    return f


def si_temps_manque(a):
    debut, _ = debuts(a)
    keep = [i for i, p in enumerate(a["phases"], 1) if p.get("production") or any(a["docs"][k - 1].get("type") == "Rebondissement" for k in p.get("docs", []))]
    indiv = [i for i, p in enumerate(a["phases"], 1) if "individuel" in p["modalite"].lower() and i not in keep and i > 1]
    f = [Paragraph("8. Si le temps manque", S["h2"])]
    items = [f"Ne coupez jamais : {', '.join(f'l’étape {i} ({a['phases'][i - 1]['titre']})' for i in keep)}. C'est là que l'atelier fait apprendre.",
             "Raccourcissez plutôt les temps de lecture et les restitutions : faites passer deux groupes au lieu de trois ou quatre."]
    if indiv:
        items.append("Peut se poursuivre à distance, dans « Mon carnet » : " + ", ".join(f"l'étape {i} ({a['phases'][i - 1]['titre']})" for i in indiv) + ".")
    items.append("Si vous devez arrêter avant le bilan : faites au moins écrire « ce que je retiens », et ouvrez la session suivante par le quiz puis le diaporama de bilan.")
    f += bullets(items, "li")
    return f


# ---------------------------------------------------------------- annexes photocopiables
def doc_bar(text, red=False):
    t = Table([[Paragraph(text, ParagraphStyle("kh", fontName="Sans-B", fontSize=9, leading=12, textColor=colors.white))]], colWidths=[W])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), RED if red else NAVY), ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    return t


def fiche_mission(a, gi, g, p):
    lab = groupe_label(a)
    flow = [Paragraph(f"ATELIER {a['n']} · {lab.upper()} {gi}", S["eyebrow"]), Paragraph(clean(g["nom"]), S2["cardh"]),
            Paragraph(f"<i>{clean(g['angle'])}</i>", S2["card"]), Spacer(1, 3)]
    flow += [Paragraph(clean(q), S2["card"], bulletText=f"{j}.") for j, q in enumerate(g["questions"], 1)]
    flow += [Spacer(1, 3), Paragraph(f"<b>Pistes dans le dossier :</b> doc. {', '.join(map(str, g['docs']))}. Les pistes ne suffisent pas, et certains documents sont à lire avec méfiance.", S2["card"])]
    if p.get("roles"):
        flow.append(Paragraph("<b>Rôles :</b> animateur · gardien du temps · rapporteur · avocat du diable.", S2["card"]))
    t = Table([[flow]], colWidths=[W])
    t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), .8, colors.HexColor("#999999")), ("TOPPADDING", (0, 0), (-1, -1), 9),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 11), ("LEFTPADDING", (0, 0), (-1, -1), 11), ("RIGHTPADDING", (0, 0), (-1, -1), 11)]))
    return KeepTogether([t, Spacer(1, 4), Paragraph("✂ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", S["small"]), Spacer(1, 6)])


def grille_criteres(a):
    rows = [["Critère de réussite", "Oui", "En partie", "Non", "Ce qui le montre"]]
    rows += [[f"{j}. {c}", "", "", "", ""] for j, c in enumerate(a["criteres"], 1)]
    t = P.table(rows, [76 * mm, 12 * mm, 16 * mm, 12 * mm, 54 * mm])
    t.setStyle(TableStyle([("TOPPADDING", (0, 1), (-1, -1), 10), ("BOTTOMPADDING", (0, 1), (-1, -1), 12)]))
    return [doc_bar(f"Atelier {a['n']} · Grille des critères de réussite"), Spacer(1, 6), Paragraph(clean(a["production"]), S["h2"]),
            Paragraph("Groupe évalué : ……………………………   Évalué par : ……………………………", S["p"]), Spacer(1, 4), t]


def annexes(a):
    n = a["n"]
    f = [PageBreak(), Paragraph(f"ATELIER {n} · DOCUMENTS À PHOTOCOPIER", S["eyebrow"]), Paragraph("9. Les documents de l'atelier", S["h1"]),
         Paragraph("Dans l'ordre : les fiches à découper ou à remettre aux groupes, puis tous les documents du dossier. Un bandeau bleu : document du dossier stagiaire. "
                   "Un bandeau rouge : rebondissement ou carte secrète, à imprimer à part et à ne remettre qu'au moment prévu.", S["p"])]
    if n == 1:
        for txt in ("D'accord", "Pas d'accord"):
            f += [PageBreak(), Spacer(1, 70 * mm), Paragraph(txt, S2["big"]), Spacer(1, 10),
                  Paragraph("Atelier 1 · débat mouvant · affichette à placer à un bout de la salle", ParagraphStyle("c", parent=S["small"], alignment=1))]
    mp = next((p for p in a["phases"] if p.get("mission")), None)
    if mp and a["groupes"]:
        f += [PageBreak(), doc_bar(f"Atelier {n} · Fiches mission · une par groupe"), Spacer(1, 8)]
        f += [fiche_mission(a, gi, g, mp) for gi, g in enumerate(a["groupes"], 1)]
    for p in a["phases"]:
        if p.get("sequence"):
            f += [PageBreak(), doc_bar(f"Atelier {n} · Cartes « événements » · à découper, à révéler une par une", red=True), Spacer(1, 8)]
            cells = [[Paragraph(f"<b>{h}</b>", S2["cardh"]), Spacer(1, 3), Paragraph(clean(x), S2["card"])] for h, x in p["sequence"]]
            rows = [cells[i:i + 2] + ([[]] if len(cells[i:i + 2]) == 1 else []) for i in range(0, len(cells), 2)]
            t = Table(rows, colWidths=[85 * mm, 85 * mm])
            t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), .6, colors.HexColor("#999999")), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                                   ("TOPPADDING", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 14), ("LEFTPADDING", (0, 0), (-1, -1), 9)]))
            f.append(t)
    if a["criteres"]:
        f += [PageBreak()] + grille_criteres(a)
    for k, d in enumerate(a["docs"], 1):
        reb, sec = d.get("type") == "Rebondissement", bool(d.get("secret"))
        tag = "  ·  À DISTRIBUER AU MOMENT PRÉVU" if reb else ("  ·  CARTES SECRÈTES À DÉCOUPER" if sec else "")
        f += [PageBreak(), doc_bar(f"Atelier {n} · Document {k} · {d.get('type', '')}{tag}", red=reb or sec), Spacer(1, 6), Paragraph(d["titre"], S["h2"])]
        f += doc_flow(d["html"])
    return f


def fiche_atelier(a):
    f = en_bref(a) + preparation(a) + plan_distribution(a)
    f += [CondPageBreak(60 * mm), Paragraph("4. Le déroulé point par point", S["h2"])]
    debut, _ = debuts(a)
    i_rel = next((i for i, p in enumerate(a["phases"], 1) if p.get("dossier")), None) or next((i for i, p in enumerate(a["phases"], 1) if p.get("sequence")), 2)
    for i, p in enumerate(a["phases"], 1):
        f += etape(a, i, p, debut[i - 1], i == i_rel)
    f += bilan(a) + corrige(a) + si_temps_manque(a)
    f.append(Paragraph("Références : " + " ; ".join(C.REF[k][0] for k in a["refs"]) + ".", S["small"]))
    f += annexes(a)
    return f


def references():
    f = [PageBreak(), Paragraph("Textes de référence", S["h1"])]
    for g, keys in C.GROUPES_REF:
        f.append(Paragraph(g, S["h3"]))
        f += [Paragraph(f"{C.REF[k][0]}<br/><font size=7.5 color='#555b66'>{C.REF[k][1]}</font>", S["li"], bulletText="•") for k in keys]
    return f


def build_cahier(path=None):
    path = path or os.path.join(ROOT, "ressources", "05_Cahier_du_formateur.pdf")
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm, topMargin=16 * mm, bottomMargin=20 * mm,
                            title="Cahier du formateur", author="Formation CPE AEFE", subject=C.TITRE)
    f = couverture() + sommaire() + [PageBreak()] + mode_emploi() + parcours() + preparer() + principes() + hors_ateliers() + recap_impressions()
    for a in C.ATELIERS:
        f += fiche_atelier(a)
    f += references()
    doc.build(f, onFirstPage=lambda c, d: None, onLaterPages=P.footer("Cahier du formateur"))
    if os.environ.get("CAHIER_CLAIR") != "1":
        P.proteger(path)
    return path


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else None
    print(build_cahier(out))
