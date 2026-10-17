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

# ---------------------------------------------------------------------------
# Les huit ateliers
# ---------------------------------------------------------------------------
# Chaque temps : titre, consigne, duree (min), modalite, docs (documents
# introduits à ce temps), voir (numéros de documents déjà révélés),
# reperes (True = les repères de savoirs s'ouvrent à ce temps).

ATELIERS = []

# ----------------------------------------------------------------- Atelier 1
ATELIERS.append(dict(
    n=1,
    titre="Découvrir mon métier de CPE",
    accroche="Missions, responsabilités et repères AEFE.",
    but="Situer ce qui relève de mon action, de la coopération et de la décision d'une autre autorité.",
    objectifs=[
        "Énoncer les trois domaines de missions du CPE définis par la circulaire de 2015.",
        "Pour une demande reçue, identifier qui décide, avec qui coopérer et quelle information manque.",
        "Repérer les deux situations qui imposent une réaction immédiate : un danger et une demande de données sur autrui.",
        "Établir la liste des documents et interlocuteurs à identifier dès l'arrivée en poste.",
    ],
    competences=["C2", "C8"],
    blocs=["3", "1"],
    blocs_detail="3.3 et 3.4 (système éducatif, place du CPE) ; 1.8 (communauté éducative)",
    production="Le tableau des douze demandes et ma check-list de prise de fonction.",
    temps=[
        dict(titre="Je découvre la situation", duree=10, modalite="Individuel",
             consigne="Lisez les documents 1 et 2. Formulez le rôle du CPE en trois phrases : une par domaine de missions.",
             docs=[
                 dict(titre="Le lycée Horizon", html="""
<p>Établissement fictif du réseau AEFE : <strong>780 élèves</strong>, dont 480 collégiens et 300 lycéens.</p>
<ul>
<li><strong>Direction :</strong> Mme Laurent, proviseure ; M. Vidal, proviseur adjoint.</li>
<li><strong>Vie scolaire :</strong> un CPE (vous) et six assistants d'éducation, désignés A à F.</li>
<li><strong>Autres personnels :</strong> professeurs principaux, une infirmière, une psychologue intervenante.</li>
<li><strong>Instances élèves :</strong> conseil de la vie lycéenne (CVL), conseil de la vie collégienne (CVC), délégués de classe.</li>
</ul>
<p class="note">Les rôles exacts et les procédures locales d'un établissement réel sont toujours à vérifier auprès de la direction.</p>"""),
                 dict(titre="Les missions du CPE en trois domaines", html="""
<p>Synthèse de la circulaire n° 2015-139 du 10 août 2015. Le CPE exerce ses missions sous l'autorité du chef d'établissement.</p>
<table><thead><tr><th>Domaine</th><th>Ce que cela recouvre</th></tr></thead><tbody>
<tr><td><strong>1. Politique éducative de l'établissement</strong></td><td>Contribuer au volet éducatif du projet d'établissement, au climat scolaire, à l'apprentissage de la citoyenneté et à la vie démocratique.</td></tr>
<tr><td><strong>2. Suivi des élèves</strong></td><td>Suivre l'assiduité, accompagner individuellement et collectivement les élèves, travailler avec les familles et les équipes, contribuer à l'orientation et à la prévention du décrochage.</td></tr>
<tr><td><strong>3. Organisation de la vie scolaire</strong></td><td>Organiser le service et l'équipe de vie scolaire, les temps et espaces hors la classe, la sécurité des élèves et le respect des règles.</td></tr>
</tbody></table>
<p class="note">Texte intégral : <a href="https://www.education.gouv.fr/bo/15/Hebdo31/MENH1517711C.htm" target="_blank" rel="noopener">Bulletin officiel n° 31 du 27 août 2015</a>.</p>"""),
             ]),
        dict(titre="Je prends position", duree=25, modalite="Groupes de 3 ou 4",
             consigne="Pour chacune des douze demandes du document 3, complétez une ligne : mon premier geste, qui décide, avec qui coopérer, l'information qui me manque.",
             docs=[
                 dict(titre="Douze demandes reçues en une semaine", html="""
<ol>
<li>Un professeur demande une sanction immédiate après un bavardage.</li>
<li>Un AED signale trois absences inhabituelles d'un même élève.</li>
<li>La direction souhaite améliorer l'accueil au portail le matin.</li>
<li>Une famille conteste un article du règlement intérieur.</li>
<li>Un élève demande de l'aide pour son orientation.</li>
<li>Les délégués veulent consulter les élèves sur la cantine.</li>
<li>Deux AED contestent la répartition des postes.</li>
<li>Un élève révèle un risque immédiat pour sa sécurité.</li>
<li>Un professeur principal demande un suivi des retards de sa classe.</li>
<li>Un parent exige des informations sur un autre élève.</li>
<li>Deux élèves demandent de l'aide pour résoudre un désaccord.</li>
<li>La direction demande un bilan des activités du service.</li>
</ol>
<table class="blank"><thead><tr><th>N°</th><th>Mon premier geste</th><th>Qui décide ?</th><th>Avec qui coopérer ?</th><th>Information manquante</th></tr></thead>
<tbody><tr><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td></tr><tr><td>…</td><td></td><td></td><td></td><td></td></tr></tbody></table>"""),
             ]),
        dict(titre="Je vérifie et je justifie", duree=20, modalite="Groupes, puis mise en commun",
             consigne="Confrontez vos réponses au document 4 et aux repères ci-dessous. Corrigez celles qui dépassent le champ du CPE. Quelles sont les deux demandes qui imposent d'agir sans attendre ?",
             docs=[
                 dict(titre="Qui décide quoi au lycée Horizon ?", html="""
<table><thead><tr><th>Domaine</th><th>Qui décide</th><th>Rôle du CPE</th></tr></thead><tbody>
<tr><td>Sanction disciplinaire</td><td>Le chef d'établissement, ou le conseil de discipline</td><td>Établir les faits, informer, proposer ; ne décide pas seul d'une sanction</td></tr>
<tr><td>Punition scolaire</td><td>Les personnels, selon le règlement intérieur</td><td>Peut en prononcer ; veille à la cohérence et à la dimension éducative</td></tr>
<tr><td>Règlement intérieur</td><td>Adopté par le conseil d'établissement</td><td>L'explique, contribue à son évolution</td></tr>
<tr><td>Orientation</td><td>L'élève et sa famille, avec le conseil de classe</td><td>Accompagne, oriente vers le professeur principal et la psychologue</td></tr>
<tr><td>Danger pour un élève</td><td>Circuit de protection de l'établissement, direction, secours si urgence</td><td>Protège, alerte sans délai, trace les faits</td></tr>
<tr><td>Contrats des AED</td><td>L'employeur (établissement ou organisme gestionnaire)</td><td>Organise le service ; ne modifie pas le contrat</td></tr>
<tr><td>Données personnelles</td><td>Direction, dans le respect du RGPD</td><td>Ne communique jamais les informations d'un élève à un tiers non habilité</td></tr>
</tbody></table>
<p class="note">Tableau fictif construit pour l'exercice. Dans un établissement réel, vérifier le règlement intérieur, l'organigramme et la circulaire AEFE sur les instances.</p>"""),
             ],
             voir=[3], reperes=True),
        dict(titre="Je produis", duree=15, modalite="Individuel",
             consigne="Rédigez votre check-list de prise de fonction : au moins dix documents et interlocuteurs à identifier dès la première semaine, classés par priorité.",
             docs=[], voir=[1, 4]),
    ],
    cloture=[
        "Quelle demande avez-vous d'abord cru relever de votre seule décision ?",
        "Quels sont les deux gestes qui ne souffrent aucun délai ?",
        "Quel document irez-vous demander en premier dans votre établissement ?",
    ],
    approfondir="posture",
    refs=["missions", "competences", "formation", "aefe_instances"],
    formateur=dict(
        materiel=["Documents 3 et 4 imprimés par groupe", "Tableau vierge à cinq colonnes (projeté ou sur papier)"],
        deroule=[
            "Lecture individuelle silencieuse. Recueillir oralement deux ou trois formulations, sans corriger.",
            "Chaque groupe traite les douze lignes. Circuler : relancer avec « Qui décide, au final ? ».",
            "Ne distribuer ou révéler le document 4 qu'une fois le tableau rempli. Mise en commun ciblée sur les demandes 1, 7, 8 et 10.",
            "Écrit individuel. Inviter à classer la liste en trois niveaux : jour 1, semaine 1, mois 1.",
        ],
        corrige="""
<table><thead><tr><th>N°</th><th>Premier geste</th><th>Qui décide</th><th>Coopérer avec</th><th>Information manquante</th></tr></thead><tbody>
<tr><td>1</td><td>Établir les faits ; distinguer punition et sanction</td><td>Punition : le professeur selon le RI ; sanction : le chef d'établissement</td><td>Le professeur</td><td>Faits précis, répétition, ce que prévoit le RI</td></tr>
<tr><td>2</td><td>Vérifier la saisie, contacter la famille selon la procédure</td><td>CPE pour le suivi de l'assiduité</td><td>AED, professeur principal, famille</td><td>Justificatifs, historique</td></tr>
<tr><td>3</td><td>Observer et diagnostiquer avant de changer le planning</td><td>Direction, sur proposition du CPE</td><td>AED</td><td>Flux, horaires, incidents</td></tr>
<tr><td>4</td><td>Écouter, expliquer la règle, orienter vers la direction</td><td>Conseil d'établissement pour toute modification</td><td>Direction</td><td>Article concerné, situation à l'origine</td></tr>
<tr><td>5</td><td>Écouter, orienter</td><td>L'élève et sa famille, avec le conseil de classe</td><td>Professeur principal, psychologue</td><td>Besoin précis, calendrier</td></tr>
<tr><td>6</td><td>Aider à préparer la consultation, sans la faire à leur place</td><td>Les élus proposent ; les instances décident</td><td>Direction</td><td>Objet, modalités, règles de l'instance</td></tr>
<tr><td>7</td><td>Recevoir les deux AED, expliciter les critères</td><td>CPE pour l'organisation du service ; employeur pour le contrat</td><td>Direction</td><td>Critères actuels, contraintes contractuelles</td></tr>
<tr><td><strong>8</strong></td><td><strong>Protéger, ne pas laisser l'élève seul, alerter sans délai, secours si urgence</strong></td><td>Direction et circuit de protection</td><td>Infirmière, direction</td><td>Aucune information manquante ne doit retarder l'alerte</td></tr>
<tr><td>9</td><td>Relevé factuel, croisement des observations</td><td>CPE</td><td>AED, professeur principal, famille</td><td>Période, régularité ; la cause n'est pas à déduire</td></tr>
<tr><td><strong>10</strong></td><td><strong>Refuser poliment ; recentrer sur son propre enfant</strong></td><td>Direction</td><td>Direction</td><td>La véritable inquiétude du parent</td></tr>
<tr><td>11</td><td>Écouter ; médiation possible si aucune emprise ni répétition</td><td>CPE</td><td>AED</td><td>Exclure un harcèlement avant toute médiation</td></tr>
<tr><td>12</td><td>Produire des données agrégées, sans nom</td><td>Direction</td><td>Équipe de vie scolaire</td><td>Format, échéance</td></tr>
</tbody></table>""",
        vigilance=[
            "Ne pas transformer l'atelier en quiz juridique : l'enjeu est le réflexe « qui décide ? ».",
            "Les demandes 8 et 10 sont des pièges volontaires. Les nommer explicitement au bilan.",
            "Le référentiel 2013 (compétences C1 à C8) et le référentiel de formation 2026 (quatre blocs) n'ont pas la même fonction : le second organise la formation, il ne remplace pas le premier.",
        ],
        slides=[
            dict(titre="Le CPE : une fonction éducative", points=["Contribuer à la politique éducative de l'établissement", "Suivre les élèves, individuellement et collectivement", "Organiser la vie scolaire"], ref="missions"),
            dict(titre="Trois niveaux d'action", points=["Ce que j'organise dans mon champ", "Ce que je prépare ou partage avec un collègue", "Ce que je signale à l'autorité compétente"], ref="missions"),
            dict(titre="Deux réflexes sans délai", points=["Un danger : protéger, alerter, ne jamais promettre le secret", "Les données d'un autre élève : ne jamais les divulguer"], ref="protection"),
            dict(titre="Deux textes complémentaires", points=["2013 : huit compétences spécifiques du CPE, C1 à C8", "2026 : référentiel de formation en quatre blocs", "Le second organise la formation ; il ne remplace pas le premier"], ref="formation"),
        ],
    ),
))

# ----------------------------------------------------------------- Atelier 2
ATELIERS.append(dict(
    n=2,
    titre="Organiser et piloter la vie scolaire",
    accroche="Diagnostic, données, planning et priorités éducatives.",
    but="Passer de données et d'observations à une organisation du service juste, couverte et évaluable.",
    objectifs=[
        "Formuler un diagnostic fondé sur des données et des paroles, en distinguant constats et hypothèses.",
        "Construire un tableau d'affectation qui respecte trois contraintes : couverture, disponibilité, équité.",
        "Adapter l'organisation à un imprévu et justifier l'arbitrage.",
        "Définir un objectif éducatif avec un indicateur quantitatif, un indicateur qualitatif et une date de bilan.",
    ],
    competences=["C1", "C3", "C4"],
    blocs=["1", "2"],
    blocs_detail="1.1 et 1.2 (équipe, conditions de vie des élèves) ; 2.1 (culture de l'évaluation)",
    production="Mon diagnostic en trois constats, le tableau des postes et deux priorités du projet de service.",
    temps=[
        dict(titre="Je lis le dossier", duree=10, modalite="Individuel",
             consigne="Lisez le document 1. Repérez les lieux, les créneaux et les règles d'affectation.",
             docs=[
                 dict(titre="Les postes à tenir", html="""
<p>Quatre créneaux fictifs. Chaque créneau demande trois postes, soit douze postes par jour.</p>
<table><thead><tr><th>Créneau</th><th>Horaire</th><th>Postes à tenir</th></tr></thead><tbody>
<tr><td>T1</td><td>08:00–08:30</td><td>Portail · Cour · Accueil vie scolaire</td></tr>
<tr><td>T2</td><td>10:00–10:30</td><td>Cour · Étude · Accueil vie scolaire</td></tr>
<tr><td>T3</td><td>12:00–12:30</td><td>Cantine · Cour · Accueil vie scolaire</td></tr>
<tr><td>T4</td><td>13:15–13:45</td><td>Portail · Étude · Accueil vie scolaire</td></tr>
</tbody></table>
<p><strong>Trois règles d'affectation :</strong></p>
<ol>
<li>Un AED ne tient qu'un poste à la fois.</li>
<li>Un AED n'est affecté qu'à un créneau où il est disponible.</li>
<li>Les postes sont répartis équitablement : pas plus de deux postes par AED et par jour.</li>
</ol>"""),
             ]),
        dict(titre="Je diagnostique", duree=20, modalite="Groupes de 3 ou 4",
             consigne="À partir des documents 2 et 3, rédigez trois constats, chacun fondé sur une donnée ou une parole, puis deux points encore à vérifier.",
             docs=[
                 dict(titre="Trois semaines de données", html="""
<table><thead><tr><th>Indicateur (total hebdomadaire)</th><th>S1</th><th>S2</th><th>S3</th></tr></thead><tbody>
<tr><td>Retards au créneau T1</td><td>58</td><td>61</td><td>45</td></tr>
<tr><td>Retards au créneau T4</td><td>12</td><td>16</td><td>11</td></tr>
<tr><td>Incidents relevés dans la cour</td><td>9</td><td>12</td><td>8</td></tr>
<tr><td>Incidents relevés en étude</td><td>6</td><td>6</td><td>5</td></tr>
</tbody></table>
<p class="note">Chaque semaine compte cinq jours. Données fictives, agrégées, sans identité. Les modalités de saisie n'ont pas changé, à ce que l'on sait.</p>"""),
                 dict(titre="Paroles recueillies", html="""
<ul>
<li><strong>Des élèves :</strong> « L'entrée du matin crée de l'attente. »</li>
<li><strong>L'AED B :</strong> « Les transmissions changent selon la personne. »</li>
<li><strong>Le professeur principal de 3e :</strong> « Plusieurs élèves arrivent après le début du cours. »</li>
</ul>
<p class="note">Ce sont des indices, pas des preuves de causalité.</p>"""),
             ], reperes=True),
        dict(titre="J'organise", duree=25, modalite="Groupes",
             consigne="Avec le document 4, construisez le tableau des affectations T1 à T4. Vérifiez les trois règles du document 1 pour chaque case.",
             docs=[
                 dict(titre="Disponibilités des six AED", html="""
<table class="center"><thead><tr><th>AED</th><th>T1</th><th>T2</th><th>T3</th><th>T4</th></tr></thead><tbody>
<tr><td>A</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
<tr><td>B</td><td>✓</td><td>✓</td><td>✓</td><td>—</td></tr>
<tr><td>C</td><td>✓</td><td>✓</td><td>—</td><td>✓</td></tr>
<tr><td>D</td><td>✓</td><td>—</td><td>✓</td><td>✓</td></tr>
<tr><td>E</td><td>—</td><td>✓</td><td>✓</td><td>✓</td></tr>
<tr><td>F</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
</tbody></table>
<table class="blank"><thead><tr><th>Créneau</th><th colspan="3">Postes et AED affecté</th></tr></thead><tbody>
<tr><td>T1</td><td>Portail :</td><td>Cour :</td><td>Accueil :</td></tr>
<tr><td>T2</td><td>Cour :</td><td>Étude :</td><td>Accueil :</td></tr>
<tr><td>T3</td><td>Cantine :</td><td>Cour :</td><td>Accueil :</td></tr>
<tr><td>T4</td><td>Portail :</td><td>Étude :</td><td>Accueil :</td></tr>
</tbody></table>
<p class="note">Données de l'exercice. Dans un établissement réel, les conditions d'emploi des AED sont à vérifier auprès de l'employeur.</p>"""),
             ], voir=[1]),
        dict(titre="Je régule", duree=15, modalite="Groupes",
             consigne="Découvrez le document 5. Adaptez votre tableau, puis justifiez votre arbitrage entre continuité du service et équité.",
             docs=[
                 dict(titre="Un imprévu", html="""
<p>Ce matin, l'AED <strong>D</strong> prévient qu'il sera absent au créneau <strong>T3</strong>.</p>
<p>Reprenez votre tableau : les trois postes de T3 doivent rester tenus par trois personnes réellement disponibles. Que devient la règle d'équité ? Comment l'expliquez-vous à l'équipe ?</p>"""),
             ], voir=[4]),
        dict(titre="Je pilote", duree=15, modalite="Groupes, puis mise en commun",
             consigne="Définissez deux priorités pour le projet de service. Pour chacune : un objectif éducatif, un indicateur quantitatif, un indicateur qualitatif et une date de bilan.",
             docs=[], voir=[2, 3]),
    ],
    cloture=[
        "Quel constat aviez-vous d'abord présenté comme une cause ?",
        "Qu'est-ce qui peut expliquer la baisse des retards en S3 ?",
        "Dans votre établissement, qui valide le tableau des postes ?",
    ],
    approfondir="organisation",
    refs=["missions", "ih2ef", "toulouse_vs", "formation"],
    formateur=dict(
        materiel=["Documents 1 à 4 imprimés par groupe", "Document 5 imprimé à part, distribué au temps 4"],
        deroule=[
            "Lecture individuelle. Vérifier que les trois règles sont comprises avant de lancer les groupes.",
            "Exiger que chaque constat cite sa source (une donnée ou une parole). Relancer sur la baisse de S3.",
            "Laisser chercher ; il existe plusieurs solutions. Faire vérifier les trois règles case par case.",
            "Distribuer le document 5 seulement quand le tableau est terminé.",
            "Mise en commun : une priorité par groupe, présentée en une minute.",
        ],
        corrige="""
<p><strong>Diagnostic attendu.</strong> Les retards se concentrent au créneau T1 (environ 11 à 12 par jour) bien plus qu'en T4. La cour concentre plus d'incidents que l'étude. Les paroles convergent vers l'attente à l'entrée et des transmissions hétérogènes, sans le prouver. À vérifier : la cause de la baisse en S3 (une action ? un hasard ? un changement de saisie ?) et l'organisation réelle du portail.</p>
<p><strong>Une affectation valide</strong> (deux postes exactement par AED) :</p>
<table class="center"><thead><tr><th>Créneau</th><th>Postes</th></tr></thead><tbody>
<tr><td>T1</td><td>Portail D · Cour C · Accueil B</td></tr>
<tr><td>T2</td><td>Cour F · Étude E · Accueil A</td></tr>
<tr><td>T3</td><td>Cantine D · Cour B · Accueil A</td></tr>
<tr><td>T4</td><td>Portail F · Étude C · Accueil E</td></tr>
</tbody></table>
<p><strong>Imprévu.</strong> D absent à T3 : seuls E et F sont disponibles et libres. L'un d'eux prend la cantine et passe à trois postes. La continuité du service et la sécurité priment ; l'écart d'équité est expliqué à l'équipe et compensé dans la semaine.</p>
<p><strong>Exemple de priorité.</strong> Objectif : fluidifier l'entrée du matin. Indicateur quantitatif : retards T1 par semaine. Indicateur qualitatif : trois questions posées à dix élèves et aux AED. Bilan dans quatre semaines.</p>""",
        vigilance=[
            "Les élèves cherchent souvent une solution unique : valoriser les solutions alternatives qui respectent les trois règles.",
            "L'équité est un critère explicite ici ; elle prépare la demande de l'AED D à l'atelier 3.",
            "Un indicateur qualitatif n'est pas une impression : il repose sur un recueil défini à l'avance.",
        ],
        slides=[
            dict(titre="Diagnostiquer avant de planifier", points=["Observer les temps, les espaces et les besoins des élèves", "Croiser chiffres et paroles", "Ne jamais déduire une cause d'un seul indicateur"], ref="ih2ef"),
            dict(titre="Une affectation valide", points=["T1 : Portail D · Cour C · Accueil B", "T2 : Cour F · Étude E · Accueil A", "T3 : Cantine D · Cour B · Accueil A", "T4 : Portail F · Étude C · Accueil E"], ref="toulouse_vs"),
            dict(titre="Face à l'imprévu", points=["D absent à T3 : E ou F prend la cantine", "La continuité du service prime sur l'équité du jour", "Expliquer l'arbitrage et compenser dans la semaine"], ref="missions"),
            dict(titre="Du diagnostic au projet", points=["Une priorité éducative documentée", "Objectif, action, responsable, échéance", "Un indicateur chiffré, un indicateur qualitatif, une date de bilan"], ref="formation"),
        ],
    ),
))

# ----------------------------------------------------------------- Atelier 3
ATELIERS.append(dict(
    n=3,
    titre="Animer et accompagner l'équipe AED",
    accroche="Accueil, entretien, réunion et transmissions.",
    but="Construire un collectif de travail : accueillir, réguler un écart et conduire une réunion qui décide.",
    objectifs=[
        "Distinguer, dans une demande ou un écart, une difficulté d'organisation, un besoin de formation et un désaccord.",
        "Conduire un entretien de régulation à partir de faits observables.",
        "Conduire une réunion qui aboutit à des décisions, des responsables et des échéances.",
        "Situer le rôle du CPE par rapport au chef d'établissement et à l'employeur des AED.",
    ],
    competences=["C4", "C8"],
    blocs=["1", "4"],
    blocs_detail="1.1 (encadrer et animer l'équipe de vie scolaire) ; 4.2 (collectif professionnel)",
    production="Ma trame d'entretien de régulation et le relevé de décisions de la réunion.",
    temps=[
        dict(titre="Je comprends l'équipe", duree=10, modalite="Groupes de 3 ou 4",
             consigne="Lisez les documents 1 à 3. Pour chaque AED, classez la situation : organisation, besoin de formation, désaccord ou écart à vérifier.",
             docs=[
                 dict(titre="Les six AED", html="""
<table><thead><tr><th>AED</th><th>Ce que l'on sait</th></tr></thead><tbody>
<tr><td>A</td><td>Connaît bien l'accueil, en poste depuis trois ans.</td></tr>
<tr><td>B</td><td>Débute et souhaite un tutorat.</td></tr>
<tr><td>C</td><td>Demande un outil commun de transmission.</td></tr>
<tr><td>D</td><td>Questionne l'équité des postes du midi.</td></tr>
<tr><td>E</td><td>Demande des consignes plus explicites.</td></tr>
<tr><td>F</td><td>Transmet irrégulièrement ses interventions.</td></tr>
</tbody></table>"""),
                 dict(titre="Deux messages reçus", html="""
<p><strong>D :</strong> « Peut-on revoir ensemble les critères d'affectation du midi ? »</p>
<p><strong>B :</strong> « Quand le CPE est en entretien, je ne sais pas à qui transmettre les retards. Chaque collègue me donne une réponse différente. »</p>"""),
                 dict(titre="Deux comptes rendus du même incident", html="""
<p><strong>F :</strong> « Élève agressif, incident grave. »</p>
<p><strong>C :</strong> « Deux élèves ont élevé la voix devant la cantine ; séparés sans blessure constatée ; direction informée. »</p>
<p class="note">Comparez les deux formulations. Qu'est-ce qui est un fait ? Qu'est-ce qui est un jugement ?</p>"""),
             ]),
        dict(titre="Je prépare l'accueil", duree=15, modalite="Groupes",
             consigne="Concevez le plan d'accueil de B en cinq rubriques : lieux, missions, transmissions, personne-ressource, point de bilan à quinze jours.",
             docs=[], voir=[1, 2]),
        dict(titre="Je régule", duree=25, modalite="Triades : CPE, F, observateur",
             consigne="Jouez l'entretien de régulation avec F à partir des cartes du document 4. Changez de rôle après le retour de l'observateur.",
             docs=[
                 dict(titre="Cartes de l'entretien avec F", html="""
<div class="cards">
<div class="card"><h4>Carte CPE</h4><p>Vous menez un entretien de régulation, pas un entretien disciplinaire : partez de faits observables, écoutez, rappelez la règle de transmission, proposez un appui et fixez une date de point.</p></div>
<div class="card"><h4>Carte F</h4><p>Vous pensiez qu'un collègue transmettrait l'information. Vous acceptez une clarification, mais vous contestez une accusation générale du type « tu ne transmets jamais ».</p></div>
<div class="card"><h4>Carte observateur</h4><p>Relevez : les faits cités, la qualité d'écoute, le rappel de la règle, l'appui proposé, la conclusion et l'échéance.</p></div>
</div>"""),
             ], voir=[3], reperes=True),
        dict(titre="Je conduis une réunion", duree=25, modalite="Groupe de 7 : un CPE, six AED",
             consigne="Répartissez les rôles du document 5. Le CPE conduit la réunion avec la trame du document 6 et doit obtenir au moins deux décisions, chacune avec un responsable et une date.",
             docs=[
                 dict(titre="Cartes de la réunion d'équipe", html="""
<ul>
<li><strong>A</strong> défend les habitudes actuelles.</li>
<li><strong>B</strong> demande un exemple concret de transmission.</li>
<li><strong>C</strong> propose un outil de transmission unique.</li>
<li><strong>D</strong> demande un critère d'équité pour les postes du midi.</li>
<li><strong>E</strong> demande une courte formation.</li>
<li><strong>F</strong> craint une surcharge de travail.</li>
</ul>"""),
                 dict(titre="Trame de réunion", html="""
<table class="blank"><tbody>
<tr><th>Objectif commun</th><td></td></tr>
<tr><th>Ordre du jour</th><td>1. Transmissions · 2. Postes de la pause méridienne · 3. Accueil des nouveaux AED</td></tr>
<tr><th>Décision 1</th><td>Responsable : · Échéance :</td></tr>
<tr><th>Décision 2</th><td>Responsable : · Échéance :</td></tr>
<tr><th>Date du point de vérification</th><td></td></tr>
</tbody></table>"""),
             ]),
        dict(titre="Je formalise", duree=10, modalite="Individuel",
             consigne="Rédigez la procédure de transmission factuelle en cinq rubriques (qui, quoi, quand, à qui, par quel outil). Le guide d'accueil complet est à finaliser dans votre carnet.",
             docs=[], voir=[3, 6]),
    ],
    cloture=[
        "Dans l'entretien avec F, à quel moment la conversation a-t-elle basculé, dans un sens ou dans l'autre ?",
        "Quelle décision de la réunion serait vérifiable dans quinze jours ?",
        "Dans votre établissement, qui est l'employeur des AED ?",
    ],
    approfondir="management",
    refs=["aed", "toulouse_aed", "ih2ef", "missions"],
    formateur=dict(
        materiel=["Cartes du document 4 découpées par triade", "Cartes du document 5 distribuées individuellement", "Trame du document 6 projetée"],
        deroule=[
            "Classement rapide. Faire remarquer que F relève d'un écart à vérifier, pas d'une faute établie.",
            "Plan d'accueil bref : il sera repris dans le carnet. Ne pas laisser ce temps déborder.",
            "Deux passages par triade. Rappeler avant de jouer : l'entretien de régulation n'est ni disciplinaire ni une évaluation.",
            "Une réunion jouée devant le groupe, les autres observent. Arrêter à 20 minutes et faire lister les décisions obtenues.",
            "Écrit individuel ; ramasser ou faire photographier deux productions pour le bilan.",
        ],
        corrige="""
<p><strong>Classement.</strong> B : besoin de formation et d'organisation (tutorat, circuit de transmission). C et E : organisation (outil commun, consignes écrites). D : désaccord légitime qui appelle des critères explicites. F : écart à vérifier, à traiter en entretien. A : ressource pour le tutorat de B.</p>
<p><strong>Comptes rendus.</strong> Celui de C décrit des faits, des lieux et une action. Celui de F porte un jugement (« agressif », « grave ») sans fait vérifiable.</p>
<p><strong>Entretien de régulation réussi.</strong> Faits datés, écoute de la version de F, rappel de la règle de transmission, appui proposé (outil commun), date de point. Aucune généralisation.</p>
<p><strong>Réunion réussie.</strong> Exemple : outil de transmission unique en test sur deux semaines (responsable C) ; critère de rotation des postes du midi (responsable CPE, avec D) ; point le vendredi suivant.</p>""",
        vigilance=[
            "Le CPE organise le service de vie scolaire sous l'autorité du chef d'établissement ; le pouvoir disciplinaire sur les personnels et le contrat relèvent de l'employeur.",
            "La circulaire du 17 septembre 2025 fixe le cadre de gestion des AED de droit français. Dans le réseau AEFE, de nombreux AED sont recrutés localement : leurs contrats relèvent d'autres règles, à vérifier.",
            "Une réunion ne doit pas devenir une réprimande collective : couper court si le jeu dérive.",
        ],
        slides=[
            dict(titre="Point AEFE d'abord", points=["Le CPE coordonne le service ; il n'est pas l'employeur", "Vérifier les contrats et règles des personnels recrutés localement"], ref="aed"),
            dict(titre="Encadrer une équipe, c'est…", points=["Donner du sens aux missions éducatives", "Expliquer le cadre et organiser les moyens", "Écouter, former, réguler et reconnaître"], ref="toulouse_aed"),
            dict(titre="L'entretien de régulation", points=["Partir de faits observables, jamais d'une étiquette", "Écouter la version de la personne", "Définir une règle, un appui et une échéance"], ref="ih2ef"),
            dict(titre="Une réunion utile se conclut", points=["Des décisions explicites", "Un responsable pour chacune", "Une date de mise en œuvre et une date de bilan"], ref="toulouse_vs"),
        ],
    ),
))

# ----------------------------------------------------------------- Atelier 4
ATELIERS.append(dict(
    n=4,
    titre="Comprendre les adolescents",
    accroche="Faits, hypothèses et posture éducative.",
    but="Observer un comportement, formuler des hypothèses sans diagnostic et tenir un cadre sans humilier.",
    objectifs=[
        "Distinguer un fait observable d'une interprétation.",
        "Formuler au moins deux hypothèses alternatives et les informations qui permettraient de les départager.",
        "Proposer une réponse éducative qui maintient la règle sans humiliation, avec une date de réévaluation.",
    ],
    competences=["C5", "C2"],
    blocs=["1", "2"],
    blocs_detail="1.4 (développement de l'adolescent, suivi) ; 2.2 (diversité des élèves)",
    production="Ma grille faits / hypothèses / informations manquantes / réponse à tester, avec une date de réévaluation.",
    temps=[
        dict(titre="Je décris", duree=10, modalite="Individuel",
             consigne="Relevez uniquement les faits observables du document 1. Barrez tout ce qui relève d'une interprétation.",
             docs=[
                 dict(titre="Une semaine d'observations sur Noah, élève de 4e", html="""
<ul>
<li><strong>Lundi :</strong> Noah quitte l'étude trois fois sans demander.</li>
<li><strong>Mardi :</strong> il discute calmement dans la cour.</li>
<li><strong>Mercredi :</strong> il hausse la voix après une remarque faite devant le groupe.</li>
<li><strong>Jeudi :</strong> il reste concentré quarante minutes dans une salle moins bruyante.</li>
</ul>
<p class="note">Aucun diagnostic n'est connu. Noah est un élève fictif.</p>"""),
             ]),
        dict(titre="Je questionne", duree=15, modalite="Binômes",
             consigne="Formulez deux hypothèses différentes, sans poser de diagnostic. Listez les informations qui permettraient de les départager.",
             docs=[], voir=[1]),
        dict(titre="Je confronte", duree=15, modalite="Binômes, puis mise en commun",
             consigne="Découvrez les documents 2 et 3. Vos hypothèses tiennent-elles toujours ? Révisez-les.",
             docs=[
                 dict(titre="La parole de Noah", html="""<blockquote>« Quand on me reprend devant les autres, je me sens humilié. Je ne comprends pas toujours ce qu'on attend en étude. »</blockquote>"""),
                 dict(titre="Deux réponses d'adultes observées", html="""
<ul>
<li><strong>AED A :</strong> rappel à l'ordre devant le groupe, puis escalade verbale.</li>
<li><strong>AED C :</strong> échange bref à l'écart, consigne précise, puis retour au travail.</li>
</ul>
<p class="note">Ces observations ne prouvent pas une cause unique.</p>"""),
             ], reperes=True),
        dict(titre="J'agis", duree=20, modalite="Binômes",
             consigne="Complétez la grille du document 4 : une réponse éducative qui maintient la règle sans humilier, un éventuel relais, une date de réévaluation.",
             docs=[
                 dict(titre="Grille de travail", html="""
<table class="blank"><thead><tr><th>Fait observable</th><th>Hypothèses alternatives</th><th>Informations manquantes</th><th>Réponse à tester</th><th>Réévaluation le</th></tr></thead>
<tbody><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>"""),
             ], voir=[1, 2, 3]),
        dict(titre="Je transfère", duree=10, modalite="Collectif",
             consigne="Formulez la consigne que vous donneriez demain à toute l'équipe d'AED pour les rappels à la règle en étude.",
             docs=[]),
    ],
    cloture=[
        "Quelle interprétation aviez-vous prise pour un fait ?",
        "Qu'est-ce qui distingue comprendre un comportement et l'excuser ?",
        "Quand faut-il solliciter l'infirmière ou la psychologue ?",
    ],
    approfondir="adolescence",
    refs=["cps", "climat", "missions"],
    formateur=dict(
        materiel=["Document 1 seul au départ", "Documents 2 et 3 imprimés à part", "Grille du document 4"],
        deroule=[
            "Faire lire à voix haute deux relevés. Corriger toute formulation interprétative (« il provoque »).",
            "Interdire les termes diagnostiques. Exiger au moins une hypothèse liée au contexte.",
            "Révéler les documents 2 et 3. Apport de 5 minutes sur les compétences psychosociales (voir l'approfondissement).",
            "Grilles en binôme ; en faire présenter deux.",
            "Une consigne d'équipe par binôme, la meilleure est retenue collectivement.",
        ],
        corrige="""
<p><strong>Faits.</strong> Trois sorties d'étude sans demander ; discussion calme ; voix haussée après une remarque publique ; concentration dans un lieu calme.</p>
<p><strong>Hypothèses possibles.</strong> Consignes de l'étude mal comprises ; sensibilité au bruit ou au groupe ; vécu d'humiliation lors des rappels publics. Aucune n'est un diagnostic.</p>
<p><strong>Réponse à tester.</strong> Rappels à l'écart, consigne écrite et précise en étude, place dans un lieu plus calme si possible, échange avec le professeur principal ; réévaluation à deux semaines. Relais vers l'infirmière ou la psychologue si une détresse apparaît.</p>""",
        vigilance=[
            "Ne jamais laisser un stagiaire poser un diagnostic, même « pour l'exemple ».",
            "La réponse de l'AED C est plus efficace ici, mais cela ne prouve pas une cause unique : le dire.",
            "Comprendre n'est pas excuser : la règle reste, c'est la manière de la rappeler qui change.",
        ],
        slides=[
            dict(titre="Comprendre n'est pas excuser", points=["L'adolescence implique des transformations variables", "Pairs, émotions, contexte et appartenance interagissent", "Aucune explication automatique d'un comportement"], ref="cps"),
            dict(titre="Fait ou interprétation ?", points=["« Trois sorties d'étude » : un fait", "« Il provoque volontairement » : une hypothèse", "Chercher les informations manquantes"], ref="climat"),
            dict(titre="La posture éducative", points=["Accueillir l'émotion sans valider tous les actes", "Maintenir un cadre explicite et digne", "Une réponse testable, une date, un relais si besoin"], ref="missions"),
        ],
    ),
))

# ----------------------------------------------------------------- Atelier 5
ATELIERS.append(dict(
    n=5,
    titre="Accompagner un élève et sa famille",
    accroche="Assiduité, entretien et plan de suivi.",
    but="Passer d'un relevé de retards à une démarche de suivi éducatif, sans refermer trop tôt les hypothèses.",
    objectifs=[
        "Réviser ses hypothèses à mesure que de nouvelles informations arrivent.",
        "Repérer les signaux qu'une explication plausible ne couvre pas.",
        "Préparer et conduire deux entretiens distincts : avec l'élève, avec la famille.",
        "Rédiger un compte rendu factuel et un plan de suivi partagé avec les seules personnes habilitées.",
    ],
    competences=["C5", "C7", "C8"],
    blocs=["1", "3"],
    blocs_detail="1.4, 1.5 et 1.7 (suivi, parcours, communication) ; 3.5 (relations avec les familles)",
    production="Ma trame d'entretien, un compte rendu factuel et le plan de suivi de Mila.",
    temps=[
        dict(titre="Je découvre le relevé", duree=10, modalite="Individuel",
             consigne="Lisez le document 1. Notez les faits, vos hypothèses et vos questions.",
             docs=[
                 dict(titre="Relevé d'assiduité de Mila, élève de 3e", html="""
<p>Quinze retards constatés en septembre : les 2, 3, 4, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 21 et 22. Tous avant le premier cours, d'une durée de 4 à 18 minutes.</p>
<p class="note">Le relevé ne dit rien des causes ni des justifications.</p>"""),
             ]),
        dict(titre="Je croise les regards", duree=10, modalite="Binômes",
             consigne="Découvrez les documents 2 et 3. Qu'est-ce qui change dans vos hypothèses ?",
             docs=[
                 dict(titre="Message du professeur principal", html="""<blockquote>« Ses résultats baissent depuis trois semaines et elle participe moins. Je souhaite croiser nos observations sans lui attribuer d'intention. »</blockquote>"""),
                 dict(titre="Observation d'un AED", html="""<blockquote>« Mila est restée seule pendant deux récréations. Je ne connais pas la raison. »</blockquote>"""),
             ], voir=[1]),
        dict(titre="J'entends la famille", duree=10, modalite="Binômes, puis mise en commun",
             consigne="Découvrez le document 4. Quels faits cette information explique-t-elle ? Lesquels n'explique-t-elle pas ?",
             docs=[
                 dict(titre="Courriel de la famille", html="""<blockquote>« Le trajet est devenu plus compliqué et nous trouvons le rythme difficile. Pouvons-nous échanger et chercher une solution ? »</blockquote>"""),
             ], voir=[2, 3]),
        dict(titre="Je prépare deux entretiens", duree=15, modalite="Binômes",
             consigne="Préparez deux trames distinctes, une pour Mila, une pour sa famille. Pour chacune : un objectif, deux questions ouvertes, deux relances, une formule de conclusion.",
             docs=[], voir=[1, 2, 3, 4], reperes=True),
        dict(titre="Je m'entraîne", duree=25, modalite="Triades : CPE, Mila ou famille, observateur",
             consigne="Utilisez les cartes du document 5. Jouez d'abord l'entretien avec Mila, puis celui avec la famille. Recommencez après le retour de l'observateur.",
             docs=[
                 dict(titre="Cartes des entretiens", html="""
<div class="cards">
<div class="card"><h4>Carte Mila</h4><p>Au départ : « Je suis fatiguée des remarques sur mes retards. »</p><p>Si le CPE pose une question ouverte : « Le trajet a changé. »</p><p>Si le CPE reformule avec bienveillance : « Et puis, en ce moment, je ne me sens pas très bien avec ma classe. »</p></div>
<div class="card"><h4>Carte famille</h4><p>« Nous voulons coopérer, mais il existe de vraies contraintes de transport. »</p><p>Si le CPE évoque l'isolement observé : « Elle ne nous en a pas parlé. »</p></div>
<div class="card"><h4>Carte observateur</h4><p>Relevez : l'accueil, les questions ouvertes, les reformulations, le respect du cadre, l'annonce des limites de la confidentialité, la conclusion et la date de suivi.</p></div>
</div>"""),
             ]),
        dict(titre="Je construis le suivi", duree=15, modalite="Binômes",
             consigne="Complétez le document 6 : faits vérifiés, actions concertées, personnes habilitées à être informées, date de réévaluation.",
             docs=[
                 dict(titre="Modèle de compte rendu et de plan de suivi", html="""
<table class="blank"><thead><tr><th>Date et objet</th><th>Faits vérifiés</th><th>Paroles recueillies utiles</th><th>Actions décidées</th><th>Responsable</th><th>Échéance</th></tr></thead>
<tbody><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>
<p class="note">Écrire des faits, pas des jugements ni des diagnostics. Partager uniquement avec les personnes qui ont besoin de l'information pour agir.</p>"""),
             ]),
    ],
    cloture=[
        "À quel moment avez-vous été tenté de refermer le cas ?",
        "Qu'est-ce que l'explication du transport n'explique pas ?",
        "Avec qui partageriez-vous votre compte rendu, et avec qui jamais ?",
    ],
    approfondir="accompagnement",
    refs=["missions", "climat", "phare"],
    formateur=dict(
        materiel=["Documents révélés un par un (imprimés séparément)", "Cartes du document 5 découpées par triade"],
        deroule=[
            "Lecture individuelle. Recueillir les hypothèses au tableau, sans trier.",
            "Révéler les documents 2 et 3. Faire barrer au tableau les hypothèses qui ne tiennent plus.",
            "Révéler le document 4. Question pivot : que reste-t-il d'inexpliqué ?",
            "Deux trames bien distinctes. Vérifier que chacune annonce les limites de la confidentialité.",
            "Les cartes sont à déclencheurs : la parole de Mila ne s'ouvre que si le CPE pose des questions ouvertes et reformule.",
            "Plan de suivi : vérifier que l'infirmière ou la psychologue apparaît si les signaux persistent.",
        ],
        corrige="""
<p><strong>Faits.</strong> Quinze retards sur quinze jours de classe consécutifs (du mercredi 2 au mardi 22 septembre), tous en début de journée. Baisse des résultats et de la participation depuis trois semaines. Isolement observé deux fois.</p>
<p><strong>Point pivot.</strong> Le changement de trajet explique de façon plausible les retards. Il n'explique ni la baisse des résultats, ni l'isolement. Ces signaux, qui coïncident dans le temps, justifient de garder ouverte l'hypothèse d'un mal-être ou d'une difficulté avec le groupe, et de rester attentif à un possible harcèlement.</p>
<p><strong>Plan de suivi attendu.</strong> Solution concertée sur l'horaire ou le trajet ; point régulier avec le professeur principal ; attention portée aux récréations par les AED ; proposition d'un rendez-vous avec l'infirmière ou la psychologue ; réévaluation à trois semaines. Compte rendu partagé avec la direction et le professeur principal, pas avec l'ensemble de l'équipe.</p>""",
        vigilance=[
            "Le piège principal : conclure « c'est le transport » et clore le suivi.",
            "L'entretien avec l'élève et celui avec la famille n'ont pas les mêmes objectifs ; ne pas les fusionner.",
            "Ne jamais promettre une confidentialité absolue à l'élève : annoncer qu'une information inquiétante sera partagée avec les personnes compétentes.",
        ],
        slides=[
            dict(titre="Une donnée n'est pas une explication", points=["Quinze retards constatés : un fait", "Le trajet : une information de la famille, à examiner", "Ne pas conclure à un manque de motivation"], ref="missions"),
            dict(titre="Ce que le transport n'explique pas", points=["La baisse des résultats et de la participation", "L'isolement en récréation", "Garder l'hypothèse d'un mal-être ouverte ; associer infirmière ou psychologue"], ref="phare"),
            dict(titre="Conduire l'entretien", points=["Accueillir, clarifier l'objet, écouter", "Questions ouvertes, reformulations, puis précisions", "Un accord réaliste et une date de suivi"], ref="climat"),
            dict(titre="Écrire et partager avec mesure", points=["Des faits utiles, ni jugement ni diagnostic", "Partager avec les seules personnes habilitées", "Adapter le circuit de suivi au contexte local"], ref="missions"),
        ],
    ),
))

# ----------------------------------------------------------------- Atelier 6
ATELIERS.append(dict(
    n=6,
    titre="Gérer un incident et protéger les élèves",
    accroche="Deux démarches distinctes : discipline et protection.",
    but="Distinguer réponse éducative, procédure disciplinaire et situation préoccupante, et savoir qui protéger.",
    objectifs=[
        "Établir les faits, les inconnues et les personnes à protéger dans un incident.",
        "Énoncer les garanties d'une procédure disciplinaire : légalité, contradictoire, proportionnalité, individualisation.",
        "Reconnaître ce qui impose une protection et une alerte plutôt qu'une simple réponse disciplinaire.",
        "Rejeter les gestes contre-productifs : secret absolu, confrontation, diffusion nominative.",
    ],
    competences=["C2", "C1"],
    blocs=["1", "3"],
    blocs_detail="1.3 (règles de vie et de droit) ; 3.6 (protection de l'enfance)",
    production="Deux arbres de décision distincts : gestion d'un incident, protection et alerte.",
    temps=[
        dict(titre="Je traite l'incident A", duree=15, modalite="Groupes de 3 ou 4",
             consigne="À partir des documents 1 et 2, distinguez les faits, les inconnues, les actions immédiates et les autorités compétentes. Qui doit être protégé dans cette situation ?",
             docs=[
                 dict(titre="Situation A : des messages dégradants", html="""
<p>Une caricature de deux camarades et des propos dégradants envers un adulte de l'établissement circulent dans une messagerie. Un élève de seconde est désigné par plusieurs élèves, mais l'auteur exact n'est pas établi.</p>"""),
                 dict(titre="Règlement du lycée Horizon (extrait fictif)", html="""<blockquote>« Les faits sont consignés objectivement, les besoins de protection sont examinés et les décisions disciplinaires relèvent de l'autorité compétente et des procédures applicables. »</blockquote>
<p class="note">Cet extrait ne remplace aucun texte réglementaire réel.</p>"""),
             ]),
        dict(titre="Je réévalue", duree=20, modalite="Groupes",
             consigne="Découvrez le document 3. Précisez les suites éducatives possibles et les garanties de toute procédure disciplinaire éventuelle.",
             docs=[
                 dict(titre="Informations nouvelles sur la situation A", html="""
<ul>
<li>Le témoin 1 a vu les messages, pas leur auteur.</li>
<li>Le témoin 2 évoque un téléphone utilisé par deux élèves.</li>
<li>L'élève mis en cause reconnaît avoir transféré des messages, pas les avoir tous rédigés.</li>
</ul>
<p class="note">Toute déclaration reste à vérifier.</p>"""),
             ], voir=[1, 2], reperes=True),
        dict(titre="Je change de raisonnement", duree=20, modalite="Groupes",
             consigne="Découvrez le document 4. Qu'est-ce qui impose ici une protection et une alerte, plutôt qu'une réponse disciplinaire ? Analysez la situation : on ne la joue pas.",
             docs=[
                 dict(titre="Situation B : une confidence préoccupante", html="""
<p>Une AED rapporte qu'une élève lui a confié craindre de retourner en classe après des humiliations répétées. L'élève lui a montré des messages dégradants reçus depuis plusieurs semaines.</p>
<p class="note">La sécurité immédiate de l'élève doit être évaluée. Cette situation s'analyse avec des cartes : aucun stagiaire ne joue le rôle de la victime.</p>"""),
             ]),
        dict(titre="Je construis les premiers réflexes", duree=25, modalite="Groupes",
             consigne="Classez les neuf cartes du document 5 en deux colonnes : à faire, à rejeter. Complétez ensuite le circuit du document 6 sans inventer de règle locale.",
             docs=[
                 dict(titre="Neuf cartes d'action", html="""
<div class="cards nine">
<div class="card">Protéger et écouter, sans enquête intrusive</div>
<div class="card">Promettre le secret absolu</div>
<div class="card">Prévenir la direction et les personnels compétents</div>
<div class="card">Confronter immédiatement tous les élèves concernés</div>
<div class="card">Consigner les faits dans le circuit habilité</div>
<div class="card">Vérifier et activer le protocole de l'établissement</div>
<div class="card">Organiser le suivi de la protection</div>
<div class="card">Solliciter les secours en cas d'urgence</div>
<div class="card">Diffuser à toute l'équipe un compte rendu nominatif</div>
</div>"""),
                 dict(titre="Circuit local à compléter", html="""
<table class="blank"><tbody>
<tr><th>Direction ou référent protection</th><td></td></tr>
<tr><th>Professionnel de santé ou du social</th><td></td></tr>
<tr><th>Référents harcèlement (dispositif pHARe ou équivalent)</th><td></td></tr>
<tr><th>Secours compétents du pays d'accueil</th><td></td></tr>
<tr><th>Canal de transmission écrit</th><td></td></tr>
<tr><th>Personne responsable du suivi</th><td></td></tr>
</tbody></table>
<p class="note">À faire valider par la direction avant tout usage réel.</p>"""),
             ], voir=[4]),
        dict(titre="Je produis", duree=20, modalite="Groupes",
             consigne="Dessinez deux arbres de décision distincts : l'un pour un incident, l'autre pour une situation préoccupante. Marquez le point où un incident peut basculer dans le second arbre.",
             docs=[], voir=[5, 6]),
    ],
    cloture=[
        "Dans la situation A, qui aviez-vous oublié de protéger ?",
        "Quelle carte « à rejeter » avez-vous hésité à garder ?",
        "Qui est votre interlocuteur pour une situation préoccupante dans votre établissement ?",
    ],
    approfondir="accompagnement",
    refs=["discipline", "protection", "phare", "climat"],
    formateur=dict(
        materiel=["Documents 3 et 4 imprimés à part", "Neuf cartes découpées par groupe", "Affiche ou tableau à deux colonnes"],
        deroule=[
            "Relancer sur la question « qui protéger ? » : les deux élèves caricaturés et l'adulte visé.",
            "Révéler le document 3. Faire énoncer les garanties : légalité, contradictoire, proportionnalité, individualisation.",
            "Révéler le document 4. Rappeler qu'on ne joue pas la victime.",
            "Classement des cartes, puis circuit local : les cases restent vides si l'information n'est pas connue.",
            "Arbres affichés et comparés.",
        ],
        corrige="""
<p><strong>Situation A.</strong> Faits : des messages circulent ; un élève est désigné. Inconnues : l'auteur, la diffusion réelle. Actions immédiates : préserver les traces, informer la direction, protéger et rencontrer les deux élèves caricaturés et l'adulte visé. La décision disciplinaire éventuelle relève du chef d'établissement, après établissement des faits et dans le respect du contradictoire.</p>
<p><strong>Après le document 3.</strong> Responsabilités à individualiser : transférer n'est pas rédiger. Suites éducatives possibles : mesure de responsabilisation, travail sur l'usage des réseaux, réparation envers les personnes visées.</p>
<p><strong>Situation B.</strong> Répétition, crainte, messages : c'est une situation préoccupante et un possible harcèlement. Protéger, alerter la direction et les référents, tracer, organiser le suivi. Pas de médiation ni de confrontation.</p>
<p><strong>Cartes.</strong> À faire : 1, 3, 5, 6, 7, 8. À rejeter : 2 (secret absolu), 4 (confrontation), 9 (diffusion nominative).</p>""",
        vigilance=[
            "La frontière entre A et B n'est pas étanche : un incident peut révéler une situation de harcèlement. Le montrer.",
            "En France, les références sont le programme pHARe et les procédures de protection de l'enfance ; à l'étranger, le circuit et les secours du pays d'accueil sont à identifier avec la direction.",
            "Si un stagiaire évoque une situation réelle, l'arrêter avec bienveillance et proposer un échange individuel.",
        ],
        slides=[
            dict(titre="Pour un incident : une décision juste", points=["Protéger d'abord, y compris les personnes visées", "Établir les faits ; distinguer punition et sanction", "Légalité, contradictoire, proportionnalité, individualisation"], ref="discipline"),
            dict(titre="Pour une situation préoccupante", points=["Protéger et écouter, sans enquête solitaire", "Alerter les professionnels compétents ; secours si urgence", "Tracer les faits et assurer le suivi"], ref="protection"),
            dict(titre="Gestes à exclure", points=["Promettre un secret absolu", "Confronter en cas de harcèlement présumé", "Diffuser des données nominatives"], ref="phare"),
            dict(titre="La vérification AEFE", points=["Les protocoles nationaux donnent des repères", "Identifier le circuit réel de l'établissement et du pays", "Faire valider contacts et procédures"], ref="protection"),
        ],
    ),
))

# ----------------------------------------------------------------- Atelier 7
ATELIERS.append(dict(
    n=7,
    titre="Faire vivre la démocratie scolaire",
    accroche="Accompagner les élus et leurs projets.",
    but="Aider les élus à consulter, prioriser et porter leurs projets sans décider à leur place.",
    objectifs=[
        "Lire des résultats de consultation avec rigueur : effectif, représentativité, limites.",
        "Préparer une réunion d'élus qui distingue propositions des élèves et décisions des instances.",
        "Articuler les instances du collège et du lycée.",
        "Organiser le retour aux élèves représentés.",
    ],
    competences=["C6", "C3"],
    blocs=["1", "3"],
    blocs_detail="1.6 (citoyenneté participative) ; 3.1 (principes et valeurs de la République)",
    production="L'ordre du jour de la réunion, la fiche projet et la feuille de route des élus.",
    temps=[
        dict(titre="Je découvre la demande", duree=15, modalite="Groupes de 3 ou 4",
             consigne="Analysez les documents 1 et 2. Qu'est-ce que ces résultats permettent réellement de dire ? Qu'est-ce qu'ils ne permettent pas de dire ?",
             docs=[
                 dict(titre="La demande des élus", html="""
<p><strong>Les élus du CVL</strong> portent trois projets : un espace calme, l'accueil des nouveaux élèves, une consultation sur la cantine. Ils demandent comment consulter, prioriser et présenter leurs propositions.</p>
<p><strong>Une élue du CVC</strong> (conseil de la vie collégienne) demande que les collégiens soient associés au projet d'espace calme.</p>"""),
                 dict(titre="Résultats d'une première consultation", html="""
<table><thead><tr><th>Première priorité</th><th>Réponses</th></tr></thead><tbody>
<tr><td>Espace calme</td><td>54</td></tr><tr><td>Accueil des nouveaux élèves</td><td>31</td></tr><tr><td>Cantine</td><td>15</td></tr>
</tbody></table>
<p class="note">100 réponses volontaires sur 300 lycéens. Les 480 collégiens n'ont pas été consultés.</p>"""),
             ]),
        dict(titre="Je prépare", duree=15, modalite="Groupes",
             consigne="Proposez une consultation complémentaire, puis l'ordre du jour de la réunion des élus. Tenez compte du document 3.",
             docs=[
                 dict(titre="Calendrier de travail", html="""
<ul><li><strong>J+7 :</strong> réunion préparatoire des élus</li><li><strong>J+14 :</strong> note de proposition</li><li><strong>J+21 :</strong> échange avec la direction</li></ul>
<p class="note">Le budget et les compétences de décision ne sont pas fournis : ce sont des informations à demander, pas à inventer.</p>"""),
             ], voir=[1, 2], reperes=True),
        dict(titre="Je simule", duree=25, modalite="Groupe : élus, CPE, direction, observateur",
             consigne="Avec les cartes du document 4, conduisez la réunion. Distinguez à voix haute les propositions des élus et les décisions qui relèvent des instances.",
             docs=[
                 dict(titre="Cartes de la réunion", html="""
<div class="cards">
<div class="card"><h4>Élus</h4><p>Défendre le point de vue recueilli ; demander à consulter davantage, y compris les collégiens.</p></div>
<div class="card"><h4>CPE</h4><p>Faciliter le cadre, faire circuler la parole, sans imposer le projet.</p></div>
<div class="card"><h4>Direction</h4><p>Exposer les contraintes vérifiées, sans promesse prématurée.</p></div>
<div class="card"><h4>Observateur</h4><p>Vérifier qui décide quoi et comment la parole circule.</p></div>
</div>"""),
             ]),
        dict(titre="Je produis", duree=15, modalite="Groupes",
             consigne="Rédigez la feuille de route des élus et la manière dont ils rendront compte à tous les élèves.",
             docs=[], voir=[3]),
    ],
    cloture=[
        "Qu'avez-vous failli décider à la place des élus ?",
        "Que pouvez-vous dire, et ne pas dire, à partir de 100 réponses sur 300 ?",
        "Quelles instances existent dans votre établissement, et qui les réunit ?",
    ],
    approfondir=None,
    refs=["democratie", "aefe_instances", "missions"],
    formateur=dict(
        materiel=["Documents 1 à 3", "Cartes du document 4"],
        deroule=[
            "Question pivot : peut-on dire que « les lycéens veulent un espace calme » ?",
            "Faire inclure les collégiens dans la consultation complémentaire.",
            "Réunion jouée devant le groupe ; l'observateur rend compte en premier.",
            "Feuilles de route affichées ; vérifier la présence du retour aux élèves.",
        ],
        corrige="""
<p><strong>Lecture des chiffres.</strong> 100 réponses volontaires sur 300 lycéens : un tiers, non représentatif. On peut dire que parmi les répondants, l'espace calme arrive en tête. On ne peut pas parler au nom de tous les lycéens, encore moins des collégiens.</p>
<p><strong>Consultation complémentaire.</strong> Courte, ouverte aux collégiens via le CVC et les délégués, avec une question précise sur l'usage de l'espace calme.</p>
<p><strong>Réunion réussie.</strong> Les élus formulent la proposition ; la direction expose les contraintes ; les décisions relèvent des instances compétentes (conseil d'établissement, selon les règles AEFE). Le CPE facilite sans trancher.</p>""",
        vigilance=[
            "Le CPE accompagne sans confisquer : intervenir si un stagiaire-CPE « porte » le projet à la place des élus.",
            "Les compétences exactes des instances dans un établissement AEFE sont fixées par la circulaire AEFE et le règlement de l'établissement : à vérifier.",
        ],
        slides=[
            dict(titre="Une citoyenneté participative", points=["Former les élus à consulter, représenter, argumenter", "Permettre une décision éclairée des instances", "Rendre compte des suites à tous les élèves"], ref="democratie"),
            dict(titre="Le CPE accompagne sans confisquer", points=["Aider à structurer, débattre et prioriser", "Vérifier les compétences des instances AEFE", "Ne pas promettre ce qui relève d'une autre autorité"], ref="aefe_instances"),
            dict(titre="Lire les chiffres avec rigueur", points=["100 réponses volontaires sur 300 lycéens", "Aucune réponse des 480 collégiens", "Compléter la consultation avant de conclure"], ref="democratie"),
        ],
    ),
))

# ----------------------------------------------------------------- Atelier 8
ATELIERS.append(dict(
    n=8,
    titre="Une matinée dans la peau du CPE",
    accroche="Mobiliser ses acquis et préparer ses premiers jours.",
    but="Prioriser sous contrainte de temps dans une situation inédite, justifier ses décisions et préparer ses trente premiers jours.",
    objectifs=[
        "Prioriser des événements simultanés : la protection d'abord, puis la continuité du service.",
        "Décider dans son champ, coopérer et transmettre.",
        "Rendre compte à la direction de façon factuelle.",
        "Établir son plan des trente premiers jours et ses besoins de formation.",
    ],
    competences=["C1", "C2", "C4", "C5", "C8"],
    blocs=["4", "2"],
    blocs_detail="4.2 (collectif professionnel, analyse de pratique) ; 2.1 (évaluation)",
    production="Mon journal des décisions, le point rendu à la direction et mon plan des trente premiers jours.",
    temps=[
        dict(titre="Je prends mon poste", duree=10, modalite="Groupes : un CPE, des observateurs",
             consigne="Répartissez les rôles. Ouvrez le journal des décisions (document 1) et relisez les disponibilités habituelles (document 2).",
             docs=[
                 dict(titre="Journal des décisions", html="""
<table class="blank"><thead><tr><th>Heure</th><th>Événement</th><th>Priorité</th><th>Action</th><th>Qui agit ?</th><th>Vérification, suivi</th></tr></thead>
<tbody><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>"""),
                 dict(titre="Tableau des postes de ce jour", html="""
<table class="center"><thead><tr><th>Créneau</th><th>Postes prévus</th><th>AED disponibles ce jour-là</th></tr></thead><tbody>
<tr><td>T1</td><td>Portail D<br>Cour C<br>Accueil B</td><td>A, B, C, D, F</td></tr>
<tr><td>T2</td><td>Cour F<br>Étude E<br>Accueil A</td><td>A, B, C, E, F</td></tr>
<tr><td>T3</td><td>Cantine D<br>Cour B<br>Accueil A</td><td>A, B, D, E, F</td></tr>
<tr><td>T4</td><td>Portail F<br>Étude C<br>Accueil E</td><td>A, C, D, E, F</td></tr>
</tbody></table>"""),
             ]),
        dict(titre="Je traite les événements", duree=35, modalite="Groupes",
             consigne="Révélez les événements un par un, au signal du formateur. Consignez chaque décision dans le journal avant de passer au suivant.",
             docs=[], sequence=[
                 ("07:52", "L'AED B prévient par message qu'il sera absent toute la journée."),
                 ("08:10", "Un professeur principal de 4e signale qu'un élève cumule six absences non justifiées en trois semaines, sans cause connue."),
                 ("08:25", "Une AED rapporte qu'une élève de 5e lui a confié recevoir depuis un mois des messages humiliants et ne plus vouloir aller en EPS."),
                 ("08:30", "Un parent se présente sans rendez-vous et exige d'être reçu immédiatement au sujet d'une punition donnée il y a deux semaines."),
                 ("09:00", "La proviseure demande pour 11 heures un point écrit et factuel sur les mesures prises ce matin."),
             ], voir=[1, 2]),
        dict(titre="Je justifie", duree=20, modalite="Groupes, devant un observateur",
             consigne="Présentez en trois minutes votre point à la direction. Les observateurs utilisent la grille du document 3.",
             docs=[
                 dict(titre="Grille d'observation", html="""
<table class="blank"><thead><tr><th>Critère</th><th>Non démontré</th><th>Démontré avec aide</th><th>Démontré en simulation</th></tr></thead><tbody>
<tr><td>Faits distingués des hypothèses</td><td></td><td></td><td></td></tr>
<tr><td>Protection et urgence traitées en priorité</td><td></td><td></td><td></td></tr>
<tr><td>Champ de responsabilité et coopération</td><td></td><td></td><td></td></tr>
<tr><td>Communication claire et respectueuse</td><td></td><td></td><td></td></tr>
<tr><td>Transmissions et suivi</td><td></td><td></td><td></td></tr>
<tr><td>Capacité à réviser une décision</td><td></td><td></td><td></td></tr>
</tbody></table>"""),
             ], voir=[1]),
        dict(titre="Je me projette", duree=20, modalite="Individuel",
             consigne="À partir du document 4, établissez votre plan des trente premiers jours. Faites ensuite votre positionnement de fin de formation.",
             docs=[
                 dict(titre="Mon plan des trente premiers jours", html="""
<table class="blank"><thead><tr><th>Semaine</th><th>Intention</th><th>Action</th><th>Partenaire</th><th>Échéance</th><th>Preuve attendue</th></tr></thead><tbody>
<tr><td>1</td><td>Rencontrer, observer, vérifier le cadre</td><td></td><td></td><td></td><td></td></tr>
<tr><td>2</td><td>Sécuriser l'organisation et les transmissions</td><td></td><td></td><td></td><td></td></tr>
<tr><td>3</td><td>Structurer les suivis et les partenariats</td><td></td><td></td><td></td><td></td></tr>
<tr><td>4</td><td>Bilan avec la direction, deux ou trois priorités</td><td></td><td></td><td></td><td></td></tr>
</tbody></table>"""),
             ], reperes=True),
    ],
    cloture=[
        "Quel événement avez-vous traité trop tard, et pourquoi ?",
        "Quelle décision avez-vous révisée en cours de matinée ?",
        "Quelles sont vos deux priorités pour votre première semaine ?",
    ],
    approfondir="integration",
    refs=["formation", "competences", "missions", "phare"],
    formateur=dict(
        materiel=["Événements imprimés un par un (ou révélés à l'écran)", "Grille du document 3 par observateur", "Chronomètre"],
        deroule=[
            "Constituer des groupes de quatre : un CPE, trois observateurs. Changer de CPE à chaque événement si le groupe le souhaite.",
            "Donner le signal de révélation toutes les cinq à sept minutes, sans attendre que tout soit traité : la pression temporelle fait partie de l'exercice.",
            "Trois minutes chrono par point. Retour de l'observateur avant le formateur.",
            "Écrit individuel, puis positionnement final sur le site.",
        ],
        corrige="""
<p><strong>Ordre de priorité attendu.</strong> 08:25 (la confidence) passe devant tout le reste dès qu'elle arrive. Puis la continuité du service (07:52), le parent (08:30), l'assiduité (08:10) et le point écrit (09:00).</p>
<p><strong>07:52, B absent.</strong> T1 : F à l'accueil (disponible et libre). T3 : E à la cour. Prévenir l'équipe et noter l'écart d'équité pour compensation.</p>
<p><strong>08:10, absences.</strong> Vérifier les saisies, contacter la famille selon la procédure, croiser avec le professeur principal ; aucune cause à déduire.</p>
<p><strong>08:25, confidence.</strong> Rencontrer l'élève avec l'AED dans un lieu calme, évaluer la sécurité immédiate, informer la direction et les référents, tracer les faits, ne pas confronter. Organiser le suivi.</p>
<p><strong>08:30, parent.</strong> Accueillir, ne pas traiter dans le hall, proposer un rendez-vous rapide ; prévenir la direction si la tension monte.</p>
<p><strong>09:00, point écrit.</strong> Factuel, daté, sans détail de la confidence au-delà de ce que le circuit de protection prévoit.</p>""",
        vigilance=[
            "Les événements sont inédits par rapport à l'atelier 2 : ne pas fournir de solution de remplacement.",
            "Évaluer le raisonnement, l'ordre des priorités et la capacité à réviser, pas une « bonne réponse » unique.",
            "Le positionnement final se fait en fin d'atelier, avant l'évaluation de la formation.",
        ],
        slides=[
            dict(titre="L'évaluation porte sur le raisonnement", points=["Identifier faits, inconnues et risques", "Prioriser la protection, puis la continuité du service", "Décider dans son champ, coopérer, transmettre, réévaluer"], ref="competences"),
            dict(titre="La matinée en une ligne", points=["La confidence passe devant tout", "B absent : F à l'accueil en T1, E à la cour en T3", "Le parent est reçu, mais pas dans le hall"], ref="phare"),
            dict(titre="Continuer à apprendre", points=["Décrire une situation sans l'interpréter", "Confronter aux références et aux pairs", "Choisir deux ou trois améliorations vérifiables"], ref="formation"),
            dict(titre="Mes trente premiers jours", points=["S1 : rencontrer et vérifier", "S2 : organiser", "S3 : assurer les suivis", "S4 : faire le bilan et prioriser"], ref="missions"),
        ],
    ),
))

# Approfondissements (pages de savoirs migrées)
APPROFONDIR = {
    "posture": "Compétences et posture professionnelle",
    "organisation": "Organiser ses tâches, ses temps et son service",
    "management": "Manager, former et accompagner les AED",
    "adolescence": "Comprendre l'adolescent : psychologie, émotions et éducabilité",
    "accompagnement": "Accompagner, réguler et protéger",
    "integration": "Transférer : les trente premiers jours",
}
