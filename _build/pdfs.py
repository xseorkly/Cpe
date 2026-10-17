# -*- coding: utf-8 -*-
"""Génère le guide formateur et le carnet stagiaire (PDF) à partir de content.py.

Usage : python3 _build/pdfs.py   (depuis la racine du dépôt)
"""
import os
import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (KeepTogether, PageBreak, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import content as C  # noqa: E402
import build as B  # noqa: E402,F401  (charge les ateliers dans C.ATELIERS)

FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("Sans", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("Sans-B", FD + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Sans-I", FD + "DejaVuSans-Oblique.ttf"))
pdfmetrics.registerFont(TTFont("Serif-B", FD + "DejaVuSerif-Bold.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily  # noqa: E402
registerFontFamily("Sans", normal="Sans", bold="Sans-B", italic="Sans-I", boldItalic="Sans-B")

NAVY = colors.HexColor("#1f2f52")
ACCENT = colors.HexColor("#b4532a")
LINE = colors.HexColor("#ddd5c6")
SOFT = colors.HexColor("#f0ebe1")

S = {
    "h1": ParagraphStyle("h1", fontName="Serif-B", fontSize=22, leading=27, textColor=NAVY, spaceAfter=8),
    "h2": ParagraphStyle("h2", fontName="Serif-B", fontSize=15, leading=19, textColor=NAVY, spaceBefore=8, spaceAfter=6),
    "h3": ParagraphStyle("h3", fontName="Sans-B", fontSize=10.5, leading=14, textColor=ACCENT, spaceBefore=8, spaceAfter=4),
    "p": ParagraphStyle("p", fontName="Sans", fontSize=9.5, leading=13.5, spaceAfter=5, alignment=TA_LEFT),
    "small": ParagraphStyle("small", fontName="Sans", fontSize=8, leading=11, textColor=colors.HexColor("#555b66")),
    "cell": ParagraphStyle("cell", fontName="Sans", fontSize=8.3, leading=11),
    "li": ParagraphStyle("li", fontName="Sans", fontSize=9.5, leading=13.5, leftIndent=12, bulletIndent=2, spaceAfter=2),
    "eyebrow": ParagraphStyle("eyebrow", fontName="Sans-B", fontSize=8, leading=11, textColor=ACCENT, spaceAfter=4),
}


def clean(s):
    s = s.replace("<strong>", "<b>").replace("</strong>", "</b>")
    s = re.sub(r"<a [^>]*>(.*?)</a>", r"\1", s, flags=re.S)
    s = re.sub(r"<(?!/?(b|i|br)\b)[^>]+>", "", s)
    s = s.replace("<br>", "<br/>")
    return re.sub(r"\s+", " ", s).strip()


def table(rows, widths=None, header=True):
    data = [[Paragraph(clean(c), S["cell"]) for c in r] for r in rows]
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    st = [("GRID", (0, 0), (-1, -1), .5, LINE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
          ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]
    if header:
        st.append(("BACKGROUND", (0, 0), (-1, 0), SOFT))
    t.setStyle(TableStyle(st))
    return t


def html_flow(h):
    """Convertit le HTML simple du contenu en éléments ReportLab."""
    out = []
    for m in re.finditer(r"<table[^>]*>(.*?)</table>|<p[^>]*>(.*?)</p>|<(ul|ol)[^>]*>(.*?)</\3>|<h3>(.*?)</h3>|<blockquote>(.*?)</blockquote>|<div class=\"cards[^\"]*\">(.*?)</div>\s*$", h, re.S):
        if m.group(1):
            rows = []
            for tr in re.findall(r"<tr>(.*?)</tr>", m.group(1), re.S):
                cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", tr, re.S)
                rows.append(cells)
            if rows:
                ncol = max(len(r) for r in rows)
                rows = [r + [""] * (ncol - len(r)) for r in rows]
                lens = [max(4, sum(len(clean(r[i])) for r in rows) / len(rows)) for i in range(ncol)]
                lens = [min(l, 60) ** 0.6 for l in lens]
                w = [max(18 * mm, 170 * mm * l / sum(lens)) for l in lens]
                k = 170 * mm / sum(w)
                out += [table(rows, [x * k for x in w]), Spacer(1, 5)]
        elif m.group(2):
            out.append(Paragraph(clean(m.group(2)), S["p"]))
        elif m.group(4):
            for i, li in enumerate(re.findall(r"<li[^>]*>(.*?)</li>", m.group(4), re.S), 1):
                out.append(Paragraph(clean(li), S["li"], bulletText=f"{i}." if m.group(3) == "ol" else "•"))
        elif m.group(5):
            out.append(Paragraph(clean(m.group(5)), S["h3"]))
        elif m.group(6):
            out.append(Paragraph("<i>" + clean(m.group(6)) + "</i>", S["p"]))
    return out


def footer(title):
    def draw(canv, doc):
        canv.saveState()
        canv.setFont("Sans", 7.5)
        canv.setFillColor(colors.HexColor("#777777"))
        canv.drawString(20 * mm, 12 * mm, f"{C.TITRE} · {title} · {C.VERSION}")
        canv.drawRightString(190 * mm, 12 * mm, str(doc.page))
        canv.restoreState()
    return draw


def fmt(m):
    h, r = divmod(m, 60)
    return f"{h} h {r:02d}" if h and r else (f"{h} h" if h else f"{r} min")


def build_guide():
    path = os.path.join(ROOT, "ressources", "01_Guide_Formateur_Pedagogie_Active.pdf")
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm, topMargin=18 * mm, bottomMargin=20 * mm,
                            title="Guide du formateur", author="Formation CPE AEFE")
    f = [Paragraph(f"FORMATION CPE · {C.DUREE_TOTALE.upper()}", S["eyebrow"]),
         Paragraph("Guide du formateur", S["h1"]),
         Paragraph("Déroulés minutés, éléments de correction, points de vigilance et bilans des huit ateliers.", S["p"]),
         Paragraph("Public", S["h3"]), Paragraph(C.PUBLIC, S["p"]),
         Paragraph("Finalité", S["h3"]), Paragraph(C.FINALITE, S["p"]),
         Paragraph("Programme des deux journées", S["h2"])]
    rows = [["Journée", "Séquence", "Durée"]]
    for jour, items in C.PROGRAMME:
        for label, m in items:
            if label.startswith("Atelier"):
                k = int(label.split()[1])
                label = f"Atelier {k} · {C.ATELIERS[k - 1]['titre']}"
            rows.append([jour, label, fmt(m)])
    f += [table(rows, [25 * mm, 120 * mm, 25 * mm]), Spacer(1, 8),
          Paragraph("Principes de conduite", S["h2"])]
    for t in ["Faire produire une réponse avant de révéler la suite : c'est le ressort de chaque atelier. Les documents à révéler sont imprimés séparément pour les groupes sans écran.",
              "Ne jamais faire jouer une victime : les situations sensibles s'analysent avec des cartes.",
              "N'utiliser que des données fictives ; arrêter avec bienveillance tout récit de situation réelle identifiable et proposer un échange individuel.",
              "Préparer le règlement intérieur et les circuits d'alerte de l'établissement d'accueil, après vérification avec la direction.",
              "Positionnement initial avant l'atelier 1, positionnement final après l'atelier 8. Évaluer le raisonnement et l'ordre des priorités, pas une réponse unique."]:
        f.append(Paragraph(t, S["li"], bulletText="•"))
    f.append(Paragraph("Espace formateur en ligne : ajouter « formateur/ » à l'adresse du site. Il est exclu des moteurs de recherche et n'est lié depuis aucune page stagiaire.", S["small"]))
    for a in C.ATELIERS:
        fo = a["formateur"]
        total = sum(t["duree"] for t in a["phases"]) + 15
        f += [PageBreak(), Paragraph(f"ATELIER {a['n']} · {fmt(total).upper()}", S["eyebrow"]), Paragraph(a["titre"], S["h1"]),
              Paragraph("<b>Problématique.</b> " + a["problematique"], S["p"]),
              Paragraph("La situation", S["h3"])]
        f += html_flow(a["situation"])
        f.append(Paragraph("Objectifs", S["h3"]))
        f += [Paragraph(o, S["li"], bulletText="•") for o in a["objectifs"]]
        f.append(Paragraph("Compétences : " + " ; ".join(f"<b>{k}</b> {C.C2013[k]}" for k in a["competences"]) + f". Référentiel 2026 : {a['blocs_detail']}.", S["small"]))
        f.append(Paragraph("Matériel : " + " ; ".join(fo["materiel"]) + ".", S["small"]))
        f.append(Paragraph("Déroulé", S["h3"]))
        rows = [["Étape", "Durée", "Modalité", "Consigne aux stagiaires", "Conduite du formateur"]]
        for i, t in enumerate(a["phases"], 1):
            rows.append([f"<b>{i}. {t['titre']}</b>", f"{t['duree']} min", t["modalite"], t["consigne"], fo["deroule"][i - 1]])
        rows.append(["<b>Bilan</b>", "15 min", "Collectif", " ".join(a["cloture"]), "Retour sur les pièges du dossier, puis diaporama d'apports."])
        f.append(table(rows, [26 * mm, 14 * mm, 24 * mm, 54 * mm, 52 * mm]))
        if a["groupes"]:
            f.append(Paragraph("Missions des groupes experts", S["h3"]))
            f.append(table([["Groupe", "Question", "Documents pistes"]] + [[f"{i}. {g['nom']}", g["angle"] + "<br/>" + " ".join(g["questions"]), ", ".join(map(str, g["docs"]))] for i, g in enumerate(a["groupes"], 1)], [32 * mm, 110 * mm, 28 * mm]))
        f.append(Paragraph("Le dossier documentaire", S["h3"]))
        f.append(table([["N°", "Document", "Type"]] + [[str(k), d["titre"], d.get("type", "")] for k, d in enumerate(a["docs"], 1)], [12 * mm, 120 * mm, 38 * mm]))
        for t in a["phases"]:
            if t.get("sequence"):
                f.append(Paragraph("Événements à révéler", S["h3"]))
                f.append(table([["Heure", "Événement"]] + [[h, x] for h, x in t["sequence"]], [20 * mm, 150 * mm]))
        f.append(Paragraph("Questions pour mettre en difficulté", S["h3"]))
        f += [Paragraph(r, S["li"], bulletText="•") for r in fo["relances"]]
        f.append(Paragraph("Ce que l'on attend", S["h2"]))
        f += html_flow(fo["attendus"])
        f.append(Paragraph("Points de vigilance", S["h3"]))
        f += [Paragraph(v, S["li"], bulletText="•") for v in fo["vigilance"]]
        f.append(Paragraph("Le diaporama de bilan", S["h3"]))
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
            if s_.get("source"):
                txt += f" <font size=7.5 color='#555b66'>({s_['source']})</font>"
            f.append(KeepTogether([Paragraph(txt, S["p"])]))
        f.append(Paragraph("Références : " + " ; ".join(C.REF[k][0] for k in a["refs"]) + ". Le dossier complet est imprimable depuis la fiche formateur en ligne.", S["small"]))
    f += [PageBreak(), Paragraph("Textes de référence", S["h1"])]
    for g, keys in C.GROUPES_REF:
        f.append(Paragraph(g, S["h3"]))
        f += [Paragraph(f"{C.REF[k][0]}<br/><font size=7.5 color='#555b66'>{C.REF[k][1]}</font>", S["li"], bulletText="•") for k in keys]
    doc.build(f, onFirstPage=footer("Guide du formateur"), onLaterPages=footer("Guide du formateur"))
    return path


def lines(n):
    return table([[""] for _ in range(n)], [170 * mm], header=False)


def build_carnet():
    path = os.path.join(ROOT, "ressources", "02_Carnet_Stagiaire_Journal_Reflexif.pdf")
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm, topMargin=18 * mm, bottomMargin=20 * mm,
                            title="Carnet du stagiaire", author="Formation CPE AEFE")
    f = [Paragraph(f"FORMATION CPE · {C.DUREE_TOTALE.upper()}", S["eyebrow"]), Paragraph("Carnet du stagiaire", S["h1"]),
         Paragraph("Mon journal réflexif, mon positionnement et mon plan des trente premiers jours. Écrivez d'abord votre réponse spontanée, puis complétez-la après l'échange collectif.", S["p"]),
         Paragraph("N'inscrivez ni nom d'élève, ni donnée personnelle, ni élément réel confidentiel.", S["small"]),
         Paragraph("Mon positionnement", S["h2"]),
         Paragraph("1 " + C.ECHELLE[0] + " · 2 " + C.ECHELLE[1] + " · 3 " + C.ECHELLE[2] + " · 4 " + C.ECHELLE[3], S["small"]), Spacer(1, 4)]
    rows = [["Ce que je sais faire", "Début (1 à 4)", "Fin (1 à 4)"]] + [[f"<b>Atelier {a['n']}</b> · {a['but']}", "", ""] for a in C.ATELIERS]
    f += [table(rows, [130 * mm, 20 * mm, 20 * mm]), Spacer(1, 8), Paragraph("Avant de commencer : pour moi, être CPE, c'est…", S["h3"]), lines(4)]
    for a in C.ATELIERS:
        f += [PageBreak(), Paragraph(f"ATELIER {a['n']} · {a['titre'].upper()}", S["eyebrow"]), Paragraph(a["problematique"], S["h2"]),
              Paragraph(f"<b>Production attendue :</b> {a['production']}", S["p"])]
        for i, t in enumerate(a["phases"], 1):
            f += [Paragraph(f"Étape {i} · {t['titre']}", S["h3"]), Paragraph(t["consigne"], S["small"]), lines(3 if i == 1 else 2)]
        f += [Paragraph("Ce que je retiens", S["h3"])]
        f += [Paragraph(q, S["li"], bulletText="•") for q in a["cloture"]]
        f.append(lines(3))
    f += [PageBreak(), Paragraph("Mes trente premiers jours", S["h2"])]
    rows = [["Semaine", "Intention", "Action", "Partenaire", "Échéance", "Preuve attendue"],
            ["1", "Rencontrer, observer, vérifier le cadre", "", "", "", ""],
            ["2", "Sécuriser l'organisation et les transmissions", "", "", "", ""],
            ["3", "Structurer les suivis et les partenariats", "", "", "", ""],
            ["4", "Bilan avec la direction, deux ou trois priorités", "", "", "", ""]]
    t = table(rows, [16 * mm, 40 * mm, 40 * mm, 26 * mm, 20 * mm, 28 * mm])
    t.setStyle(TableStyle([("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white]), ("TOPPADDING", (0, 1), (-1, -1), 16), ("BOTTOMPADDING", (0, 1), (-1, -1), 16)]))
    f += [t, Spacer(1, 10), Paragraph("Mes deux priorités de formation continue", S["h3"]), lines(3)]
    doc.build(f, onFirstPage=footer("Carnet du stagiaire"), onLaterPages=footer("Carnet du stagiaire"))
    return path


if __name__ == "__main__":
    print(build_guide())
    print(build_carnet())
