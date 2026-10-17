# -*- coding: utf-8 -*-
"""Contenu du parcours « Entrer dans le métier de CPE ».

Ce fichier est la source unique du site : ateliers stagiaires, fiches
formateur, diaporamas de bilan, carnet et PDF sont générés à partir de lui
par build.py. Toutes les situations du lycée Horizon sont fictives.
"""

TITRE = "Entrer dans le métier de CPE"
SOUS_TITRE = "Formation AEFE · CPE débutants"
DUREE_TOTALE = "12 heures sur 2 jours"
VERSION = "Version 3.0 · octobre 2026"

PUBLIC = (
    "Personnels qui exercent ou vont exercer les fonctions de conseiller "
    "principal d'éducation dans un établissement du réseau AEFE, sans "
    "formation initiale spécifique : CPE contractuels, recrutés locaux, "
    "personnels faisant fonction."
)

FINALITE = (
    "Sécuriser les premiers gestes professionnels du CPE : savoir qui décide "
    "quoi, distinguer les faits des interprétations, protéger et alerter sans "
    "délai, organiser le service, accompagner les élèves et leur famille, et "
    "préparer ses trente premiers jours. La formation ne certifie pas la "
    "maîtrise du métier : elle installe des repères et des réflexes."
)

# ---------------------------------------------------------------------------
# Références (vérifiées le 17 octobre 2026)
# ---------------------------------------------------------------------------
REF = {
    "missions": ("Circulaire n° 2015-139 du 10 août 2015 : missions des CPE",
                 "https://www.education.gouv.fr/bo/15/Hebdo31/MENH1517711C.htm"),
    "competences": ("Arrêté du 1er juillet 2013 : référentiel des compétences des métiers du professorat et de l'éducation",
                    "https://www.education.gouv.fr/bo/13/Hebdo30/MENE1315928A.htm"),
    "formation": ("Référentiel de formation des CPE (annexe 32, 2026)",
                  "https://www.education.gouv.fr/sites/default/files/document/annexe-32-referentiel-de-formation-conseillers-principaux-d-education-cpe-516761.pdf"),
    "aed": ("Circulaire du 17 septembre 2025 : cadre de gestion des AED",
            "https://www.education.gouv.fr/bo/2025/Hebdo38/MENH2516443C"),
    "discipline": ("Éduscol : les procédures disciplinaires",
                   "https://eduscol.education.gouv.fr/5043/les-procedures-disciplinaires"),
    "protection": ("Éduscol : protection de l'enfance",
                   "https://eduscol.education.gouv.fr/4350/protection-de-l-enfance"),
    "phare": ("Programme pHARe de lutte contre le harcèlement",
              "https://www.education.gouv.fr/non-au-harcelement/phare-un-dispositif-de-lutte-contre-le-harcelement-l-ecole-323435"),
    "climat": ("Éduscol : agir sur le climat scolaire",
               "https://eduscol.education.gouv.fr/6980/comment-agir-sur-le-climat-scolaire"),
    "democratie": ("Éduscol : guide de la démocratie scolaire",
                   "https://eduscol.education.gouv.fr/sites/default/files/document/guide-democratie-scolaire-70848.pdf"),
    "aefe_instances": ("AEFE : circulaire relative à l'organisation et au fonctionnement des instances",
                       "https://www.aefe.gouv.fr/fr/ressources-documentaires/circulaire-relative-lorganisation-et-au-fonctionnement-des-instances-des"),
    "ih2ef": ("IH2EF : piloter la vie scolaire",
              "https://www.ih2ef.gouv.fr/piloter-la-vie-scolaire"),
    "cps": ("Santé publique France : compétences psychosociales",
            "https://www.santepubliquefrance.fr/competences-psychosociales"),
    "toulouse_vs": ("Académie de Toulouse : le service de vie scolaire",
                    "https://pedagogie.ac-toulouse.fr/cpe-vie-scolaire/le-service-de-vie-scolaire"),
    "toulouse_aed": ("Académie de Toulouse : vademecum des assistants d'éducation",
                     "https://pedagogie.ac-toulouse.fr/cpe-vie-scolaire/vademecum-des-assistants-deducation-de-lacademie-de-toulouse"),
    "toulouse_livret": ("Académie de Toulouse : livret d'accueil et d'accompagnement des CPE",
                        "https://pedagogie.ac-toulouse.fr/cpe-vie-scolaire/le-livret-daccueil-et-daccompagnement-des-cpe-dans-lacademie"),
    "versailles": ("Académie de Versailles : site des CPE",
                   "https://cpe.ac-versailles.fr/"),
}

GROUPES_REF = [
    ("Textes qui définissent le métier", ["missions", "competences", "formation"]),
    ("Équipe de vie scolaire", ["aed", "toulouse_vs", "toulouse_aed", "ih2ef"]),
    ("Règle, discipline et protection", ["discipline", "protection", "phare", "climat"]),
    ("Élèves et démocratie scolaire", ["democratie", "aefe_instances", "cps"]),
    ("Accompagnement des CPE débutants", ["toulouse_livret", "versailles"]),
]

# Compétences spécifiques du CPE (arrêté du 1er juillet 2013)
C2013 = {
    "C1": "Organiser les conditions de vie des élèves dans l'établissement, leur sécurité, la qualité de l'organisation matérielle et la gestion du temps",
    "C2": "Garantir, en lien avec les autres personnels, le respect des règles de vie et de droit dans l'établissement",
    "C3": "Impulser et coordonner le volet éducatif du projet d'établissement",
    "C4": "Assurer la responsabilité de l'organisation et de l'animation de l'équipe de vie scolaire",
    "C5": "Accompagner le parcours de l'élève sur les plans pédagogique et éducatif",
    "C6": "Accompagner les élèves, notamment dans leur formation à une citoyenneté participative",
    "C7": "Participer à la construction des parcours des élèves",
    "C8": "Travailler dans une équipe pédagogique",
}

# Blocs du référentiel de formation 2026 (annexe 32)
BLOCS2026 = {
    "1": "Organiser la vie scolaire pour accompagner le parcours des élèves et contribuer au bien-être, à la sécurité, à la qualité des apprentissages",
    "2": "Adapter sa pratique professionnelle au contexte d'exercice et à la diversité des élèves",
    "3": "Agir dans le cadre des principes du service public d'éducation",
    "4": "S'engager dans une démarche de développement professionnel",
}

# Échelle de positionnement (début et fin de formation)
ECHELLE = [
    "Je découvre",
    "Je peux le faire avec de l'aide",
    "Je le fais seul dans une situation simple",
    "Je le fais seul et je sais l'expliquer",
]

# Programme des deux journées (formateur)
PROGRAMME = [
    ("Jour 1", [("Accueil, contrat de formation, positionnement initial", 15),
                ("Atelier 1", 75), ("Atelier 2", 90), ("Atelier 3", 90), ("Atelier 4", 75)]),
    ("Jour 2", [("Atelier 5", 90), ("Atelier 6", 105), ("Atelier 7", 75), ("Atelier 8", 90),
                ("Positionnement final et évaluation de la formation", 15)]),
]

# Approfondissements (pages de savoirs migrées)
APPROFONDIR = {
    "posture": "Compétences et posture professionnelle",
    "organisation": "Organiser ses tâches, ses temps et son service",
    "management": "Manager, former et accompagner les AED",
    "adolescence": "Comprendre l'adolescent : psychologie, émotions et éducabilité",
    "accompagnement": "Accompagner, réguler et protéger",
    "integration": "Transférer : les trente premiers jours",
}
