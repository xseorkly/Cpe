# -*- coding: utf-8 -*-
"""Contenu du parcours « Entrer dans le métier de CPE ».

Ce fichier est la source unique du site : ateliers stagiaires, fiches
formateur, diaporamas de bilan, carnet et PDF sont générés à partir de lui
par build.py. Toutes les situations du lycée Horizon sont fictives.
"""

TITRE = "Entrer dans le métier de CPE"
SOUS_TITRE = "Formation AEFE · CPE débutants"
DUREE_TOTALE = ""  # calculée par build.py à partir des ateliers
VERSION = "Version 3.1 · octobre 2026"

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
# Références (vérifiées le 17 octobre 2026 ; circulaire AED et annexe 32 revérifiées le 24 octobre 2026)
# ---------------------------------------------------------------------------
REF = {
    "missions": ("Circulaire n° 2015-139 du 10 août 2015 : missions des CPE",
                 "https://www.education.gouv.fr/bo/15/Hebdo31/MENH1517711C.htm"),
    "competences": ("Arrêté du 1er juillet 2013 : référentiel des compétences des métiers du professorat et de l'éducation",
                    "https://www.education.gouv.fr/bo/13/Hebdo30/MENE1315928A.htm"),
    "formation": ("Référentiel de formation des CPE (annexe 32, 2026)",
                  "https://www.education.gouv.fr/sites/default/files/document/annexe-32-referentiel-de-formation-conseillers-principaux-d-education-cpe-516761.pdf"),
    "aed": ("Circulaire du 17 septembre 2025 : cadre de gestion des AED recrutés en France (une référence pour les contrats locaux)",
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

# Durée du bilan de chaque atelier (minutes)
BILAN_MIN = 20

# Déroulé indicatif du parcours (formateur). Les ateliers prennent leur durée
# dans scenarios.py (somme des étapes + bilan). Aucun découpage en journées :
# le parcours se répartit librement entre sessions en présence et à distance.
PROGRAMME = [
    ("Entrer dans le métier, organiser l'année et le service",
     [("Accueil, contrat de formation, positionnement initial", 20), "Atelier 1", "Atelier 2", "Atelier 3", "Atelier 4"]),
    ("Accompagner, protéger, faire participer",
     [("Quiz de réactivation, à chaque reprise après une pause", 15), "Atelier 5", "Atelier 6", "Atelier 7", "Atelier 8", "Atelier 9",
      ("Positionnement final et évaluation de la formation", 15)]),
]

# Quel texte s'applique à moi ? (encadré de l'accueil et des ressources)
STATUTS = [
    ("Fonctionnaire titulaire du corps des CPE, détaché dans le réseau",
     "Votre statut de CPE, votre contrat de détachement, votre lettre de mission ou fiche de poste.",
     "Les textes du métier (circulaire de 2015, arrêté de 2013) s'appliquent à votre corps, avec les adaptations liées à l'établissement et au pays."),
    ("Contractuel ou recruté local",
     "Votre contrat de travail de droit local, votre fiche de poste, le règlement du personnel de l'établissement, le droit du travail du pays.",
     "Des références professionnelles : elles décrivent le métier, mais ne vous donnent ni droits ni obligations par elles-mêmes."),
    ("Personnel « faisant fonction » de CPE",
     "Votre contrat d'origine et la lettre de mission qui vous confie ces fonctions.",
     "Des références pour exercer la fonction."),
]

# Comment fonctionne chaque format pédagogique (une ligne affichée sous le format)
FORMATS = {
    "Débat mouvant": "Le formateur lit une affirmation ; chacun se place côté « d'accord » ou « pas d'accord » de la salle, puis quelques volontaires justifient leur place. On peut changer de côté si un argument convainc.",
    "Puzzle (groupes experts) et affiche": "Chaque groupe devient « expert » d'une partie du dossier. Puis on forme de nouveaux groupes avec un expert de chaque partie, qui mettent leurs découvertes en commun sur une affiche.",
    "Message reçu": "Un message arrive au milieu du travail, comme dans la vraie vie : il faut y répondre vite et précisément.",
    "Prise de parole chronométrée": "Un groupe parle devant la salle, dans un temps strict ; la salle joue le public et vérifie les critères de réussite.",
    "Jeu chronométré": "Une première réponse rapide, sans documents : elle montre ce que l'on sait déjà, erreurs comprises.",
    "Enquête documentaire sur la frise": "Chaque équipe vérifie et complète une partie du travail avec les documents du dossier.",
    "Galerie": "Les productions sont affichées ; les équipes tournent de l'une à l'autre et y laissent des remarques sur post-it.",
    "Annonce du formateur": "Le formateur annonce une nouvelle qui oblige à revoir ce que l'on a construit.",
    "Production": "Le moment où l'on rédige la production de l'atelier, en vérifiant chaque critère de réussite.",
    "Engagement individuel": "Chacun écrit, pour lui-même, ce qu'il fera concrètement dans son établissement.",
    "Vote à chaud": "On vote tout de suite, sans calculer ni chercher : on comparera avec la réponse de fin d'atelier.",
    "Enquête en binômes et mur des preuves": "Chaque binôme cherche les pièges du dossier ; chaque piège trouvé est affiché au mur avec sa preuve (un calcul ou un document).",
    "Défi chronométré au mur": "On construit une solution sur une grande feuille, en temps limité, et le binôme voisin la vérifie.",
    "Message en temps réel": "Une mauvaise nouvelle arrive au dernier moment : il faut réagir dans un temps très court.",
    "Pitch debout avec contradicteur": "On présente sa proposition en deux minutes, debout ; une personne joue la contradiction et pose des objections.",
    "3-2-1": "Trois choses que je retiens, deux questions que je me pose, une action que je mènerai.",
    "Tour de table oral": "Chacun, à son tour, dit sa réponse en une phrase, sans débat.",
    "Stations tournantes": "Chaque table traite une question ; les groupes passent d'une table à l'autre et complètent l'affiche laissée par le groupe précédent.",
    "Forum-théâtre": "Deux joueurs jouent une scène ; à tout moment, quelqu'un du public peut dire « Stop ! », prendre la place du CPE et rejouer autrement.",
    "Simulation": "Une situation jouée avec des rôles ; des observateurs relèvent ce qui se passe et en rendent compte.",
    "Le formateur joue la proviseure": "Le formateur joue un personnage ; un groupe lui répond en direct, comme dans la réalité.",
    "Charte affichée et signée": "On rédige des règles communes sur une affiche, puis on les signe, comme on le ferait avec son équipe.",
    "Mur des étiquettes": "Chacun écrit sur un post-it le premier mot qui lui vient, et le colle au mur, sans commentaire. On y reviendra à la fin.",
    "Jeu de rôles de perspective": "Chaque groupe adopte le point de vue d'une personne et le défend honnêtement, y compris ce qui le contredit.",
    "Cercle structuré": "Un porte-parole par groupe parle au centre ; les autres n'ont le droit qu'à des questions de clarification, pas à des avis.",
    "Le document qui change tout": "Un nouveau document oblige à revoir ce que l'on pensait avoir compris.",
    "Mur des étiquettes et vote": "On retourne au mur du début, on retire les étiquettes qui ne tiennent pas face aux faits, puis on vote.",
    "Baromètre": "Chacun place la situation sur une échelle, de la moins grave à la plus grave ; on refera l'exercice à la fin.",
    "Révélation progressive": "Les documents arrivent un par un : à chaque pièce, on révise son jugement.",
    "Triades, puis aquarium": "Par trois : un joue le CPE, un joue la personne reçue, un observe. Puis, en « aquarium », deux joueurs au centre et une chaise vide que chacun peut venir occuper pour remplacer le CPE.",
    "Vote des groupes : accompagner ou alerter ?": "Chaque groupe tranche et justifie sa réponse par des faits.",
    "Écriture à quatre mains sur affiche": "Certains écrivent, les autres relisent et barrent tout ce qui n'est pas un fait ; les mots barrés restent visibles.",
    "Baromètre et conseil à un collègue": "On se replace sur l'échelle du début, puis on écrit le conseil que l'on donnerait à un collègue débutant.",
    "Course contre la montre": "On classe des actions dans l'ordre où on les ferait, en temps très limité, comme dans une vraie crise.",
    "Tables tournantes": "Chaque table traite une question ; les équipes passent d'une table à l'autre et complètent l'affiche laissée par l'équipe précédente.",
    "Le formateur joue Yanis": "Le formateur joue un élève ; la salle l'interroge. Il ne s'ouvre qu'aux bonnes questions.",
    "Simulation à rôles": "Une réunion jouée, chacun avec son rôle ; les observateurs vérifient des points précis et rendent compte.",
    "Arbres affichés": "On dessine sur une affiche les décisions possibles, sous forme d'arbre : chaque branche est une question ou une décision.",
    "Écrit flash": "On écrit une réponse très courte, en temps très limité, comme on répondrait sur une messagerie.",
    "Enquête et restitution d'une minute": "Chaque groupe enquête dans le dossier, puis présente l'essentiel en une minute exactement.",
    "Atelier de conception": "On fabrique un outil, puis un autre groupe le teste et cherche ses défauts : c'est le « crash-test ».",
    "Répétition coachée": "Un élève répète sa présentation ; le CPE coach écoute sans intervenir, puis donne deux points forts, une question et une suggestion.",
    "Le formateur joue le gestionnaire": "Le formateur entre dans un rôle, sous pression : il faut lui répondre sans quitter son propre rôle de CPE.",
    "Écrit individuel": "Chacun écrit pour soi, en silence.",
    "Simulation chronométrée": "Les événements arrivent un par un, sans attendre que le précédent soit traité : il faut choisir.",
    "Le formateur joue au téléphone": "Le formateur appelle, en jouant un personnage : on répond en direct.",
    "Analyse de pratique entre pairs": "Un membre du groupe raconte une décision difficile ; les autres posent des questions puis proposent des lectures, sans juger ni conseiller.",
    "Lettre à soi-même": "On écrit une lettre que l'on relira dans trente jours.",
}

# Lexique du CPE débutant : terme -> (définition, atelier où il apparaît, variantes repérées dans les pages)
LEXIQUE = {
    # Atelier 1
    "chef d'établissement": ("Le proviseur (ou le principal, ou le directeur) : il dirige l'établissement, préside les instances et décide des sanctions.", 1, []),
    "conseil pédagogique": ("Réunion d'enseignants autour du chef d'établissement, pour préparer les choix pédagogiques de l'établissement.", 1, []),
    "conseil d'établissement": ("Instance où siègent des personnels, des parents et des élèves élus ; elle adopte notamment le règlement intérieur.", 1, []),
    "punition": ("Réponse à un manquement mineur, donnée par un personnel dans le cadre du règlement intérieur (retenue, devoir supplémentaire…).", 1, ["punitions", "punition scolaire", "punitions scolaires"]),
    "sanction": ("Réponse à un manquement grave, prononcée par le chef d'établissement ou le conseil de discipline (avertissement, blâme, exclusion…).", 1, ["sanctions", "sanction disciplinaire", "sanctions disciplinaires"]),
    "exclusion de cours": ("Punition : l'enseignant fait sortir un élève de son cours, pour cette heure ; l'élève est accueilli à la vie scolaire.", 1, ["exclusions de cours"]),
    "exclusion temporaire": ("Sanction prononcée par le chef d'établissement : l'élève ne vient plus en classe, ou plus dans l'établissement, pendant huit jours au plus.", 1, ["exclusions temporaires"]),
    "circulaire": ("Texte par lequel le ministère explique comment appliquer les lois et les décrets. Elle a moins de force qu'un arrêté.", 1, []),
    "arrêté": ("Décision écrite d'un ministre, qui fixe des règles précises (par exemple un référentiel de compétences).", 1, []),
    "abroger": ("Supprimer un texte officiel : un texte abrogé ne s'applique plus.", 1, ["abroge", "abrogé"]),
    "Bulletin officiel": ("Publication du ministère de l'Éducation nationale où paraissent les textes officiels.", 1, []),
    "hiérarchie des normes": ("Un texte de rang inférieur ne peut pas contredire un texte de rang supérieur : loi, décret, arrêté, circulaire, règlement intérieur, fiche de poste.", 1, []),
    "fiche de poste": ("Document qui décrit les missions, les horaires et les responsabilités d'un poste.", 1, []),
    "recruté local": ("Personnel embauché par l'établissement avec un contrat de travail du pays d'accueil.", 1, ["recrutés locaux", "recrutés localement"]),
    "droit local": ("Le droit du pays d'accueil, et non le droit français de la fonction publique.", 1, []),
    "RGPD": ("Règlement européen sur la protection des données personnelles : on ne collecte et ne transmet que les données nécessaires, de façon sécurisée.", 1, []),
    "spécialité": ("Au lycée général, enseignement que l'élève choisit (trois en 1re, deux en terminale).", 1, []),
    "équipe de suivi": ("Réunion des adultes qui accompagnent un élève en difficulté, pour faire le point et décider d'actions.", 1, ["équipes de suivi"]),
    # Atelier 2
    "pré-rentrée": ("Journée de travail des personnels avant l'arrivée des élèves.", 2, []),
    "projet d'établissement": ("Document qui fixe les priorités de l'établissement pour plusieurs années.", 2, []),
    "volet éducatif": ("Partie du projet d'établissement consacrée à la vie des élèves, à la citoyenneté et au climat scolaire.", 2, []),
    "projet de la vie scolaire": ("Document qui fixe, pour l'année, les objectifs et l'organisation de la vie scolaire, en lien avec le projet d'établissement.", 2, ["projet de vie scolaire"]),
    "délégués de classe": ("Élèves élus par leur classe pour la représenter, notamment au conseil de classe.", 2, ["délégué de classe"]),
    "éco-délégués": ("Élèves élus pour porter des actions de développement durable.", 2, []),
    "inter-CVL": ("Regroupement des élus des CVL de plusieurs établissements d'une même zone.", 2, []),
    "conseil de classe": ("Réunion de fin de trimestre où l'équipe pédagogique, les délégués et les parents élus font le point sur chaque élève.", 2, ["conseils de classe"]),
    "Parcours Avenir": ("Parcours d'orientation des élèves, de la 6e à la terminale : découverte des métiers et des formations.", 2, []),
    "commission d'appel": ("Commission qui réexamine une décision d'orientation contestée par la famille.", 2, ["commissions d'appel"]),
    "examens blancs": ("Épreuves d'entraînement organisées dans l'établissement avant un examen.", 2, []),
    "période d'essai": ("Début du contrat pendant lequel l'employeur ou le salarié peut y mettre fin plus facilement.", 2, []),
    "rétroplanning": ("Planning construit à rebours, à partir d'une date qui ne bouge pas.", 2, []),
    "inspecteur": ("Dans le réseau, des inspecteurs de zone accompagnent et évaluent les établissements ; l'un d'eux est chargé de la vie scolaire.", 2, []),
    # Atelier 3
    "transmissions": ("Informations, écrites ou orales, que l'équipe se passe sur les élèves et le service, pour que rien ne se perde.", 3, ["transmission"]),
    "entretien de régulation": ("Entretien pour corriger un écart de fonctionnement avec un membre de l'équipe, avant qu'il ne devienne un conflit. Ce n'est pas une sanction.", 3, []),
    "autorité hiérarchique": ("Pouvoir de donner des ordres à un personnel et de décider de son contrat ou de sa discipline : il appartient au chef d'établissement.", 3, []),
    "coordination fonctionnelle": ("Le CPE organise le travail des AED (planning, consignes) sans être leur employeur.", 3, []),
    "crédit d'heures": ("Temps de travail réservé à la formation, prévu pour les AED recrutés en France.", 3, []),
    "déontologie": ("Règles de conduite d'une profession : respect des élèves, discrétion, neutralité.", 3, []),
    "traçabilité": ("Possibilité de retrouver qui a écrit quoi, et quand.", 3, ["traçable"]),
    "DESC": ("Méthode d'entretien en quatre temps : décrire les faits, exprimer ce qu'ils produisent, spécifier ce que l'on attend, conclure sur les conséquences.", 3, []),
    # Atelier 4
    "indicateur": ("Chiffre choisi à l'avance pour suivre une situation (par exemple : retards par jour de classe).", 4, ["indicateurs"]),
    "dénominateur": ("Le nombre par lequel on divise pour comparer : par jour, par élève, par semaine.", 4, []),
    "artefact": ("Résultat trompeur produit par la façon de mesurer, et non par la réalité.", 4, []),
    "trianguler": ("Croiser au moins trois sources (chiffres, observation, paroles) avant de conclure.", 4, ["triangulation"]),
    "structurel": ("Qui vient de l'organisation (horaires, locaux, moyens) et non du comportement d'une personne.", 4, ["structurelle"]),
    "serre-files": ("Adultes qui vérifient, lors d'une évacuation, que personne ne reste dans les locaux.", 4, ["serre-file"]),
    "intendance": ("Ancien nom du service de gestion : budget, bâtiments, cantine.", 4, []),
    # Atelier 5
    "fiche d'incident": ("Écrit qui rapporte un incident ; elle doit décrire des faits observables, sans jugement.", 5, ["fiches d'incident"]),
    "neuromythe": ("Idée fausse ou déformée sur le cerveau, qui circule comme si elle était scientifique.", 5, ["neuromythes"]),
    "cortex préfrontal": ("Partie avant du cerveau, qui aide à planifier et à freiner une réaction.", 5, []),
    "TDAH": ("Trouble du déficit de l'attention avec ou sans hyperactivité. Seul un médecin peut le diagnostiquer.", 5, []),
    "compétences psychosociales": ("Capacités qui permettent de faire face aux situations de la vie : se connaître, gérer ses émotions, communiquer, résoudre des difficultés.", 5, []),
    "secret professionnel": ("Obligation de ne pas révéler ce que l'on apprend dans son métier ; l'infirmière et la psychologue y sont soumises.", 5, []),
    "secret partagé": ("Des professionnels qui accompagnent le même élève échangent les seules informations nécessaires pour l'aider.", 5, []),
    "PAP": ("Plan d'accompagnement personnalisé : aménagements pour un élève qui a un trouble des apprentissages.", 5, []),
    "PAI": ("Projet d'accueil individualisé : aménagements pour un élève malade (allergie, maladie chronique…).", 5, []),
    "PPS": ("Projet personnalisé de scolarisation : aménagements pour un élève en situation de handicap.", 5, []),
    # Atelier 6
    "autorité parentale": ("Droits et devoirs des parents envers leur enfant. Les deux parents l'exercent, même séparés, sauf décision d'un juge.", 6, []),
    "garde alternée": ("L'enfant vit alternativement chez chacun de ses parents.", 6, []),
    "signaux faibles": ("Petits indices qui, pris seuls, ne disent rien, mais qui, réunis, doivent alerter.", 6, []),
    "individualisation": ("Une réponse tient compte de la situation de chaque élève : pas de punition automatique ni de sanction collective.", 6, []),
    "autorité académique": ("En France, le rectorat ou la direction des services départementaux de l'Éducation nationale.", 6, []),
    "écoute active": ("Écouter sans juger, reformuler ce que l'on a compris, poser des questions ouvertes.", 6, []),
    "coéducation": ("Les parents et l'école éduquent ensemble l'enfant, chacun dans son rôle.", 6, []),
    "information préoccupante": ("En France, information transmise au département quand un enfant est en danger ou risque de l'être.", 6, ["informations préoccupantes"]),
    # Atelier 7
    "harcèlement": ("Violences répétées (moqueries, mises à l'écart, coups), avec un rapport de force et l'isolement de la victime.", 7, []),
    "cyberharcèlement": ("Harcèlement par les téléphones et les réseaux sociaux ; il poursuit la victime hors de l'établissement.", 7, []),
    "contradictoire": ("Principe : avant toute sanction, l'élève et ses parents connaissent les faits reprochés et peuvent se défendre.", 7, []),
    "proportionnalité": ("Principe : la sanction est graduée selon la gravité des faits.", 7, []),
    "légalité": ("Principe : on ne prononce que les sanctions prévues par les textes et le règlement intérieur.", 7, []),
    "non bis in idem": ("« Pas deux fois pour la même chose » : on ne sanctionne pas deux fois les mêmes faits.", 7, []),
    "mesure conservatoire": ("Interdiction temporaire d'accès à l'établissement, décidée par le chef d'établissement pendant une procédure. Ce n'est pas une sanction.", 7, ["titre conservatoire"]),
    "sursis": ("Sanction prononcée mais pas appliquée, sauf nouvelle faute.", 7, []),
    "mesure de responsabilisation": ("Sanction qui consiste à participer à des activités utiles (solidarité, culture, formation), en dehors des heures de cours.", 7, []),
    "commission éducative": ("Instance qui cherche une réponse éducative pour un élève ; elle ne prononce pas de sanction.", 7, []),
    "conseil de discipline": ("Instance qui peut prononcer toutes les sanctions, y compris l'exclusion définitive.", 7, []),
    "cellule de suivi": ("Groupe (direction, CPE, infirmière, psychologue) qui examine les situations d'élèves préoccupantes et décide des mesures.", 7, []),
    "CRIP": ("En France, cellule départementale qui reçoit les informations préoccupantes sur les enfants en danger.", 7, []),
    "procureur": ("En France, magistrat qui reçoit les signalements de faits graves et décide des poursuites.", 7, []),
    "article 40": ("En France, article du code de procédure pénale qui oblige tout fonctionnaire à signaler au procureur un crime ou un délit dont il a connaissance.", 7, []),
    "signalement": ("En France, saisine directe du procureur en cas de danger grave ou de faits pouvant constituer une infraction.", 7, []),
    "préoccupation partagée": ("Méthode de prise en charge du harcèlement : des entretiens individuels répétés avec les auteurs, sans les accuser, pour faire cesser les faits.", 7, []),
    "poste consulaire": ("Représentation de la France à l'étranger, qui protège notamment les ressortissants français.", 7, []),
    # Atelier 8
    "taux de participation": ("Part des inscrits qui ont voté.", 8, []),
    "représentativité": ("Un groupe de répondants est représentatif s'il ressemble à l'ensemble de la population concernée (tous les niveaux, toutes les classes).", 8, ["représentatif"]),
    "biais": ("Défaut d'une enquête qui fausse le résultat : question orientée, diffusion limitée, réponses volontaires…", 8, []),
    "pluralisme": ("Diversité des opinions, qui doivent toutes pouvoir s'exprimer.", 8, []),
    "neutralité": ("Principe du service public : l'établissement ne prend pas parti, ni politiquement ni religieusement.", 8, []),
    "diffamation": ("Accuser publiquement une personne d'un fait précis qui atteint son honneur, sans preuve.", 8, ["diffamatoire", "diffamatoires"]),
    "droit de réponse": ("Droit d'une personne mise en cause par une publication de faire publier sa réponse.", 8, []),
    "motion": ("Texte voté par une instance pour exprimer une position ou une demande.", 8, []),
    "gestionnaire": ("Membre de la direction chargé du budget, des achats, des bâtiments et de la cantine (on dit aussi intendant ou directeur administratif et financier).", 8, []),
    # Atelier 9
    "sortie facultative": ("Sortie scolaire qui n'est pas obligatoire ou dépasse les horaires habituels : elle demande l'autorisation écrite des parents.", 9, []),
    "droit à l'image": ("On ne publie pas la photo d'une personne sans son accord (celui des parents pour un mineur).", 9, []),
    "fouille": ("Un personnel de l'établissement ne fouille ni un élève ni son sac ; il peut seulement lui demander de montrer volontairement ce qu'il contient.", 9, []),
    "analyse de pratique": ("Temps où des professionnels examinent ensemble une situation vécue, pour la comprendre, sans juger ni conseiller.", 9, []),
    "praticien réflexif": ("Professionnel qui revient sur ce qu'il a fait pour en tirer des enseignements.", 9, []),
}
# Approfondissements (pages de savoirs migrées)
APPROFONDIR = {
    "posture": "Compétences et posture professionnelle",
    "organisation": "Organiser ses tâches, ses temps et son service",
    "management": "Manager, former et accompagner les AED",
    "adolescence": "Comprendre l'adolescent : psychologie, émotions et éducabilité",
    "accompagnement": "Accompagner, réguler et protéger",
    "integration": "Transférer : les trente premiers jours",
}
