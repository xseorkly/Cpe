# -*- coding: utf-8 -*-
"""Scénarisation des neuf ateliers.

Chaque atelier a son propre moteur pédagogique, pour éviter que les stagiaires
retrouvent neuf fois le même déroulé. Ce fichier fixe, pour chaque atelier :
- moteur    : les trois modalités qui le caractérisent (affichées en tête) ;
- materiel  : le matériel à préparer ;
- phases    : les étapes, avec leur format, leur durée, leur modalité,
              la consigne aux stagiaires et la conduite du formateur.

Les contenus (situation, documents, attendus, diaporama) restent dans
ateliers.py et atelier_annee.py.
"""

ROLES = "Animateur · gardien du temps · rapporteur · avocat du diable (il défend la position inverse de celle du groupe)"

S = {}

# ---------------------------------------------------------------- 1
S["Découvrir mon métier de CPE"] = dict(
    moteur=["Débat mouvant", "Puzzle de documents", "Discours au conseil pédagogique"],
    materiel=["Deux affichettes « D'accord » et « Pas d'accord » aux deux bouts de la salle", "Dossier documentaire en quatre jeux", "Document 9 imprimé à part", "Chronomètre"],
    phases=[
        dict(titre="Le débat mouvant", format="Débat mouvant", duree=10, modalite="Toute la salle, debout",
             consigne="Le formateur lit quatre affirmations. Pour chacune, placez-vous du côté « d'accord » ou « pas d'accord » de la salle : pas de milieu possible. Deux volontaires de chaque côté justifient leur choix en une phrase. Notez ensuite vos quatre positions.",
             affirmations=["Le CPE est d'abord là pour faire respecter l'ordre.", "Un CPE peut décider d'exclure un élève de cours.", "Le CPE doit soutenir les professeurs en toutes circonstances.", "Un élève peut tout confier au CPE : il gardera le secret."],
             conduite="Lire chaque affirmation sans commentaire. Interdire la position médiane. Noter au tableau la répartition de la salle : elle sera rejouée à la fin."),
        dict(titre="Le puzzle de documents", format="Puzzle (groupes experts) et affiche", duree=15, modalite="4 groupes experts, puis groupes mixtes",
             consigne="Lisez d'abord votre boîte de réception et le mot de Mme Martel. Puis chaque groupe prend une mission et cherche ses réponses dans le dossier : certains documents sont périmés ou contraires aux textes. Au bout de 10 minutes, formez des groupes mixtes, un membre de chaque groupe expert, et reconstituez le puzzle sur une affiche A3.",
             docs=[1, 2], dossier=True, mission=True, roles=True,
             affiche="Les textes en vigueur (et celui qui est périmé) · les lignes illégales de la fiche de poste · les quatre verbes : je décide, je conseille, je coopère, je signale.",
             conduite="Ne pas désigner les pièges. Circuler avec les questions dérangeantes. Former les groupes mixtes à 10 minutes. Les affiches restent au mur jusqu'au discours."),
        dict(titre="Le rebondissement", format="Message reçu", duree=10, modalite="Groupes mixtes",
             consigne="Mardi, 17 h 12 : lisez le document 9. Faut-il répondre à M. Garnier, quand, par quel canal ? Écrivez mot pour mot la première phrase que vous lui direz.",
             docs=[9],
             conduite="Distribuer le document 9 sans commentaire. Exiger une phrase exacte, pas une intention. En faire lire trois et faire voter la plus juste."),
        dict(titre="Le discours", format="Prise de parole chronométrée", duree=20, modalite="Groupes mixtes, puis deux passages devant la salle",
             consigne="Préparez l'intervention de trois minutes au conseil pédagogique, puis votre check-list de prise de fonction. Deux groupes la prononcent devant la salle, qui joue les professeurs ; un stagiaire joue M. Garnier et pose une question.",
             production=True,
             conduite="Chronométrer strictement trois minutes. La salle évalue avec les critères de réussite. Donner la parole à « M. Garnier » à la fin de chaque passage."),
        dict(titre="Le débat, rejoué", format="Débat mouvant", duree=5, modalite="Toute la salle, debout",
             consigne="Les quatre affirmations sont relues. Replacez-vous. Ceux qui ont changé de côté expliquent ce qui les a fait bouger.",
             rappel=True,
             conduite="Comparer avec la répartition notée au début. Faire parler en priorité ceux qui ont changé de côté."),
    ],
)

# ---------------------------------------------------------------- 2
S["Construire mon année de CPE"] = dict(
    moteur=["Course aux cartes", "Frise murale", "Marche des calendriers"],
    materiel=["Une frise murale septembre–juillet par équipe (papier kraft), à quatre lignes de couleur", "Les douze cartes « moments forts » découpées par équipe", "Post-it de trois couleurs pour la marche des calendriers", "Document 10 lu par le formateur"],
    phases=[
        dict(titre="La course aux cartes", format="Jeu chronométré", duree=10, modalite="Équipes de 4 ou 5, debout devant la frise",
             consigne="Lisez le message de la proviseure et l'agenda de Mme Martel. Puis, sans autre document, placez les douze cartes « moments forts » sur votre frise de septembre à juillet. Vous avez 6 minutes. Notez dans votre carnet les trois cartes sur lesquelles l'équipe a hésité.",
             docs=[1, 2, 8], roles=True,
             conduite="Lancer le chrono à voix haute et annoncer les dernières 60 secondes. Ne rien corriger : les erreurs nourriront la marche des calendriers."),
        dict(titre="Chaque équipe corrige une ligne", format="Enquête documentaire sur la frise", duree=15, modalite="4 équipes, une ligne de la frise chacune",
             consigne="Chaque équipe prend une ligne de l'année : démocratie scolaire, équipe AED, suivi des élèves, prévention et pilotage. Elle corrige les cartes de sa ligne avec le dossier et la complète. Pour chaque moment : quoi, qui pilote, avec qui, date au plus tard. Remplissez votre ligne dans le calendrier ci-dessous.",
             dossier=True, mission=True, mission_titre="Une ligne de l'année par équipe", planner=True,
             conduite="Relancer avec les questions dérangeantes, en particulier sur les élections « en novembre » et le renouvellement des AED en juin."),
        dict(titre="La marche des calendriers", format="Galerie", duree=20, modalite="Les équipes tournent d'une frise à l'autre",
             consigne="Les frises sont affichées. Toutes les 3 minutes, votre équipe passe à la frise suivante et y colle trois post-it : rouge pour un oubli, orange pour une collision de dates, vert pour une bonne idée à reprendre. De retour devant votre frise, lisez ce que les autres y ont laissé.",
             conduite="Donner le signal de rotation toutes les 3 minutes. Faire nommer à voix haute les deux collisions les plus citées."),
        dict(titre="Flash info", format="Annonce du formateur", duree=10, modalite="Équipes",
             consigne="Le formateur annonce trois nouvelles comme un flash d'information (document 10). Reprenez votre frise : que déplacez-vous, que maintenez-vous coûte que coûte, que produisez-vous pour l'inspection ?",
             docs=[10],
             conduite="Lire le document 10 sur le ton d'un flash radio, sans le distribuer d'abord. Exiger une liste en deux colonnes : ce qui bouge, ce qui ne bouge pas."),
        dict(titre="La page pour la proviseure", format="Production", duree=15, modalite="Équipes",
             consigne="Mettez au propre le calendrier annuel sur une page : qui fait quoi et quand, et les trois périodes de vigilance de l'année.",
             production=True,
             conduite="Photographier chaque calendrier. Comparer devant la salle deux choix opposés sur la formation des délégués ou les entretiens d'AED."),
        dict(titre="Le post-it de lundi", format="Engagement individuel", duree=5, modalite="Individuel",
             consigne="Sur un post-it, écrivez les trois dates que vous vérifierez dès lundi dans votre établissement. Collez-le sur votre carnet : c'est votre premier geste de rentrée.",
             conduite="Inviter trois volontaires à lire leur post-it."),
    ],
)

# ---------------------------------------------------------------- 3
S["Organiser et piloter la vie scolaire"] = dict(
    moteur=["Pari", "Détectives des données", "Pitch face à la direction"],
    materiel=["Dossier complet par binôme", "Calculatrices", "Document 10 envoyé par message ou lu à 7 h 30 précises", "Chronomètre"],
    phases=[
        dict(titre="Le pari", format="Vote à chaud", duree=5, modalite="Individuel",
             consigne="Lisez le message de la proviseure et le planning hérité. Votez, sans calculer, puis écrivez vos trois premières décisions pour lundi.",
             docs=[1, 2], vote=dict(id="v1", question="Les retards du matin ont-ils baissé de 26 % en septembre ?", options=["Oui, le tableau le montre", "Oui, mais moins que 26 %", "Non", "Impossible à dire avec ces données"]),
             conduite="Annoncer la répartition des votes sans commentaire. La plupart des stagiaires votent « oui »."),
        dict(titre="Les détectives des données", format="Enquête en binômes et mur des preuves", duree=15, modalite="Binômes, dossier complet, debout au mur",
             consigne="Le dossier contient trois pièges : un calendrier, une panne, une porte. Chaque binôme mène l'enquête avec les quatre séries de questions. Chaque piège trouvé s'écrit sur un post-it « preuve » collé au mur des preuves, avec sa justification : un calcul ou un document. Le premier binôme qui a ses trois preuves validées choisit son ordre de passage au pitch.",
             dossier=True, mission=True, mission_titre="Les questions de l'enquête, pour chaque binôme", roles=False,
             affiche="Le mur des preuves : un post-it par piège, avec le calcul ou le document qui le démontre.",
             conduite="Ne valider une preuve au mur que si elle est justifiée par un calcul ou un document. Annoncer à voix haute quand un binôme a ses trois preuves."),
        dict(titre="Le casse-tête du planning", format="Défi chronométré au mur", duree=20, modalite="Binômes, debout devant une grande feuille",
             consigne="Construisez le planning de lundi sur une grande feuille au mur, avec des post-it au nom de chaque AED. Treize postes à tenir, douze possibles avec la règle d'équité : quel arbitrage proposez-vous ? Ajoutez au moins une action qui ne relève pas du planning des AED.",
             conduite="Afficher le chronomètre. Faire vérifier chaque case contre le document 8 par le binôme voisin."),
        dict(titre="Vendredi, 7 h 30", format="Message en temps réel", duree=10, modalite="Binômes",
             consigne="Le formateur vous envoie le document 10 à l'instant. Vous avez 8 minutes pour recomposer le planning et rédiger le message à l'équipe.",
             docs=[10],
             conduite="Envoyer le document par message, ou le lire, sans prévenir. Le temps court fait partie de l'exercice."),
        dict(titre="Le pitch au conseil d'établissement", format="Pitch debout avec contradicteur", duree=20, modalite="Chaque binôme, 2 minutes debout devant M. Vidal",
             consigne="Rédigez la note d'une page, puis présentez-la en deux minutes. Le formateur joue M. Vidal et vous interrompt avec ses objections : tenez vos chiffres sans perdre la relation.",
             production=True,
             conduite="Jouer M. Vidal : « Un graphique en baisse suffira. Ne compliquez pas. » Les autres binômes notent la meilleure réponse entendue."),
        dict(titre="Le ticket de sortie", format="3-2-1", duree=5, modalite="Individuel",
             consigne="Comparez avec votre pari du début. Puis écrivez : trois choses que vous regarderez désormais dans un tableau de chiffres, deux questions que vous poserez à votre direction, une action pour votre établissement.",
             rappel_vote="v1",
             conduite="Recueillir trois tickets à voix haute."),
    ],
)

# ---------------------------------------------------------------- 4
S["Animer et accompagner l'équipe AED"] = dict(
    moteur=["Phrase à chaud", "Forum-théâtre", "Réunion à cartes secrètes"],
    materiel=["Cartes du document 12 pour le forum-théâtre", "Cartes du document 10 découpées, distribuées face cachée", "Une chaise « CPE » au centre de la salle", "Document 11 lu par le formateur"],
    phases=[
        dict(titre="La phrase à chaud", format="Tour de table oral", duree=5, modalite="Toute la salle",
             consigne="Lisez la scène de mardi. Antoine vient de parler devant toute l'équipe. Vous avez cinq secondes : à tour de rôle, dites à voix haute la phrase que vous lui répondez. Puis notez la vôtre.",
             docs=[1, 2],
             conduite="Faire le tour de la salle sans commenter. Noter au tableau trois réponses typiques : l'autorité, la fuite, la négociation."),
        dict(titre="Les quatre stations", format="Stations tournantes", duree=15, modalite="4 groupes, rotation toutes les 5 minutes",
             consigne="Quatre stations, une par mission, chacune avec ses documents imprimés et une affiche. Chaque groupe commence à une station et en visite trois, 5 minutes chacune : il lit, répond, puis complète l'affiche laissée par le groupe précédent. Attention, un texte officiel figure dans le dossier : vérifiez à qui il s'applique.",
             dossier=True, mission=True, mission_titre="Les quatre stations", roles=True,
             affiche="À chaque station : ce que le groupe précédent a trouvé, ce que vous ajoutez, ce que vous contestez.",
             conduite="Donner le signal de rotation toutes les 5 minutes. À la fin, laisser une minute pour lire les quatre affiches. Ne pas signaler que la circulaire ne s'applique pas à Elsa."),
        dict(titre="Le forum-théâtre", format="Forum-théâtre", duree=20, modalite="Deux joueurs au centre, toute la salle en public",
             consigne="Un volontaire joue le CPE, un autre joue Antoine, avec les cartes du document 12. Le public peut dire « Stop ! » à tout moment, prendre la place du CPE et rejouer la dernière réplique autrement. On ne remplace jamais Antoine.",
             docs=[12],
             conduite="Lancer la scène, puis encourager les premiers « Stop ! ». Après chaque remplacement, demander à Antoine ce qu'il a ressenti. Viser quatre à cinq remplacements."),
        dict(titre="La réunion à cartes secrètes", format="Simulation", duree=15, modalite="1 CPE, 6 AED, observateurs",
             consigne="Chaque joueur tire une carte du document 10 et la garde secrète. Le CPE conduit la réunion pendant 10 minutes et doit obtenir deux décisions, chacune avec un responsable et une date. L'observateur rend compte en premier.",
             conduite="Choisir comme CPE un stagiaire qui n'a pas joué au forum-théâtre. Arrêter à 10 minutes, même sans décision."),
        dict(titre="Lundi, 8 h 50 : la convocation", format="Le formateur joue la proviseure", duree=10, modalite="Binômes",
             consigne="La proviseure vous convoque (document 11). Préparez en binôme votre réponse en trois volets : l'élève et sa famille, l'équipe, la direction. Un binôme vient la donner « en direct » au formateur.",
             docs=[11],
             conduite="Jouer Mme Laurent, ferme et pressée : « Depuis quand saviez-vous ? » Ne pas laisser le binôme s'en tirer par une généralité."),
        dict(titre="La charte et la trame", format="Charte affichée et signée", duree=10, modalite="Groupes, puis binômes",
             consigne="Écrivez la charte de transmissions de l'équipe sur une affiche, et signez-la comme vous la feriez signer à votre équipe. Puis rédigez en binôme la trame de l'entretien de régulation avec Antoine. Terminez par une phrase que vous ne direz plus jamais à un AED.",
             production=True, affiche="La charte : cinq règles vérifiables au moins, dont une sur les outils autorisés et une sur la confidentialité, et les signatures du groupe.",
             conduite="Lire deux chartes. Recueillir quelques « phrases que je ne dirai plus »."),
    ],
)

# ---------------------------------------------------------------- 5
S["Comprendre les adolescents"] = dict(
    moteur=["Mur des étiquettes", "Jeu des points de vue", "Cercle des regards"],
    materiel=["Dossier en quatre jeux, un « regard » par groupe", "Document 9 imprimé à part", "Post-it et un pan de mur libre"],
    groupes=[
        dict(nom="Le regard de Mme Roche", angle="Que voit-elle, et qu'est-ce qui est fondé dans sa demande ?",
             questions=["Réécrivez ses fiches d'incident en ne gardant que les faits observables.", "Qu'est-ce qui est légitime dans sa demande ? Qu'est-ce qui ne l'est pas ?", "De quoi aurait-elle besoin pour continuer à faire cours à Noah ?"],
             docs=[1, 2, 3]),
        dict(nom="Le regard d'Antoine", angle="Sur quoi repose « il le fait exprès » ?",
             questions=["Quels faits fondent cette lecture ? Lesquels la contredisent ?", "Dans l'article affiché, qu'est-ce qui est solide ? Qu'est-ce qui est abusif ?", "Quel effet produit cet affichage sur l'équipe ?"],
             docs=[2, 4, 6]),
        dict(nom="Le regard de Camille et de Mme Okafor", angle="Pourquoi Noah va-t-il bien avec elles ?",
             questions=["Que font-elles concrètement qui fonctionne ?", "Quelles compétences psychosociales sont en jeu pour Noah ?", "Comment transformer leur pratique en consigne pour toute l'équipe ?"],
             docs=[4, 7]),
        dict(nom="Le regard de la famille et de l'infirmière", angle="Que sait-on, que ne sait-on pas ?",
             questions=["Que dit la mère, et que ne dit-elle pas ?", "Que faire de la proposition de « test TDAH » ?", "Que peut-on attendre de l'infirmière, et dans quel cadre ?"],
             docs=[5, 8, 3]),
    ],
    phases=[
        dict(titre="Le mur des étiquettes", format="Mur des étiquettes", duree=5, modalite="Individuel, puis au mur",
             consigne="Lisez le message de Mme Roche. Sur un post-it, écrivez le premier mot qui vous vient pour décrire Noah. Collez-le au mur sans le commenter, et notez-le ici.",
             docs=[1],
             conduite="Laisser le mur se remplir en silence. Ne rien dire des mots choisis : ils seront relus à la fin."),
        dict(titre="Le jeu des points de vue", format="Jeu de rôles de perspective", duree=15, modalite="4 groupes, un regard d'adulte chacun",
             consigne="Chaque groupe endosse le regard d'un adulte sur Noah et prépare, avec le dossier, la défense la plus solide de ce regard. Ce que vous découvrez qui le contredit, gardez-le aussi : vous devrez le dire.",
             dossier=True, mission=True, mission_titre="Les quatre regards · un par groupe", roles=True,
             affiche="Le regard de votre adulte : ce qu'il voit, ce qui le fonde, ce qui le contredit. Le porte-parole s'en sert au cercle.",
             conduite="Exiger que chaque groupe défende honnêtement son adulte, y compris Antoine et Mme Roche. Repérer l'article piège sans le désigner."),
        dict(titre="Le cercle des regards", format="Cercle structuré", duree=15, modalite="Un porte-parole par groupe au centre, les autres autour",
             consigne="Chaque porte-parole a deux minutes pour présenter son regard. Les autres ne peuvent poser que des questions de clarification, pas donner d'avis. Puis la salle écrit ensemble trois faits, deux hypothèses et les informations qui manquent.",
             conduite="Faire respecter strictement la règle : questions de clarification seulement. Écrire la synthèse au tableau sous la dictée de la salle."),
        dict(titre="Jeudi : la mère revient", format="Le document qui change tout", duree=10, modalite="Groupes",
             consigne="Lisez le document 9. Que faites-vous du compte rendu de la psychologue ? À qui transmettez-vous quoi, et sous quelle forme ? Que répondez-vous à Mme Roche ?",
             docs=[9],
             conduite="Le document oppose deux pressions : tout diffuser et se défausser. Exiger une réponse précise à chacune."),
        dict(titre="La grille d'observation", format="Production", duree=10, modalite="Binômes",
             consigne="Construisez la grille d'observation que les AED rempliront pendant deux semaines, puis rédigez votre réponse à Mme Roche. Vérifiez chaque critère de réussite.",
             production=True,
             conduite="Vérifier qu'aucune grille ne contient de case de jugement ni d'information de santé."),
        dict(titre="On décolle les étiquettes", format="Mur des étiquettes et vote", duree=5, modalite="Toute la salle, puis individuel",
             consigne="Retournez au mur. Décollez chaque étiquette qui ne résiste pas aux faits du dossier. Puis votez : faut-il exclure Noah des cours de français jusqu'aux vacances ?",
             vote=dict(id="v1", question="Faut-il exclure Noah des cours de français jusqu'aux vacances ?", options=["Oui", "Non", "Oui, mais pas comme ça", "Je ne peux pas encore répondre"]),
             rappel=True,
             conduite="Faire décoller les post-it par ceux qui ne les ont pas écrits. Compter ce qui reste au mur."),
    ],
)

# ---------------------------------------------------------------- 6
S["Accompagner un élève et sa famille"] = dict(
    moteur=["Baromètre", "Dossier pièce par pièce", "Triades et aquarium"],
    materiel=["Un baromètre dessiné au tableau, de « simple problème de retard » à « élève qui pourrait être en danger »", "Dossier en quatre jeux", "Cartes du document 9 par triade", "Document 10 remis seulement aux triades où Mila a parlé", "Six chaises en cercle pour l'aquarium"],
    phases=[
        dict(titre="Le baromètre", format="Baromètre", duree=5, modalite="Individuel",
             consigne="Lisez le message du professeur principal. Où placez-vous Mila sur le baromètre ? Votez, puis écrivez ce que vous lui diriez si vous la croisiez maintenant.",
             docs=[2], vote=dict(id="v1", question="À ce stade, Mila est pour vous…", options=["Une élève qui ne respecte pas le règlement", "Une élève qui a un problème de transport", "Une élève en difficulté, sans que je sache pourquoi", "Une élève qui pourrait être en danger"]),
             conduite="Reporter les votes sur le baromètre au tableau avec des aimants ou des croix."),
        dict(titre="Le dossier pièce par pièce", format="Révélation progressive", duree=15, modalite="Groupes de 4",
             consigne="Le formateur annonce une pièce du dossier toutes les deux minutes, dans cet ordre : 1, 5, 3, 4, 6, 7, puis 8. N'ouvrez que la pièce annoncée. À chaque pièce, le groupe répond aux questions qui la concernent et déplace son curseur sur le baromètre.",
             dossier=True, mission=True, mission_titre="Les questions à se poser au fil des pièces", roles=True,
             conduite="Annoncer chaque pièce à voix haute et faire déplacer les curseurs au tableau. Marquer un temps sur la pièce 5 et sur le courriel du père."),
        dict(titre="L'entretien, en triades puis en aquarium", format="Triades, puis aquarium", duree=20, modalite="Triades, puis un cercle de six chaises",
             consigne="En triades, jouez l'entretien avec Mila avec les cartes du document 9 (10 minutes). Puis l'entretien avec le père se joue en aquarium : deux joueurs au centre, et une chaise vide que n'importe qui peut venir occuper pour remplacer le CPE.",
             conduite="Ne remettre le document 10 qu'aux triades où le CPE a ouvert la parole. Dans l'aquarium, encourager les relais sur la chaise vide."),
        dict(titre="Ce que Mila finit par dire", format="Vote des groupes : accompagner ou alerter ?", duree=10, modalite="Groupes",
             consigne="Lisez le document 10. Est-ce une situation à accompagner ou une situation de danger ? Que répondez-vous à Mila ? Qui associez-vous, dans quel ordre ? Que devient la question des retenues ?",
             docs=[10],
             conduite="Faire voter les groupes : accompagner ou alerter ? Exiger une justification par les faits, pas par l'émotion."),
        dict(titre="Le compte rendu et le courrier", format="Écriture à quatre mains sur affiche", duree=20, modalite="Groupes de 4 : deux écrivent, deux relisent",
             consigne="Le compte rendu de l'entretien s'écrit à quatre mains sur une affiche : deux stagiaires écrivent, deux relisent et barrent tout ce qui n'est pas un fait ou une parole rapportée. Puis rédigez le plan de suivi de Mila et le courrier identique adressé à ses deux parents.",
             production=True, affiche="Le compte rendu : date, personnes présentes, faits, paroles entre guillemets, décisions, responsables, échéance. Les mots barrés restent visibles.",
             conduite="Lire un courrier aux parents : vérifier qu'il ne prend pas parti."),
        dict(titre="Le second baromètre", format="Baromètre et conseil à un collègue", duree=5, modalite="Individuel",
             consigne="Placez à nouveau Mila sur le baromètre et comparez avec votre premier vote. Puis écrivez le conseil que vous donneriez à un collègue débutant face à « une élève qui accumule les retards ».",
             vote=dict(id="v2", question="Après l'atelier, Mila est pour vous…", options=["Une élève qui ne respecte pas le règlement", "Une élève qui a un problème de transport", "Une élève en difficulté, sans que je sache pourquoi", "Une élève qui pourrait être en danger", "Une élève aidante, à accompagner avec sa famille"]),
             rappel_vote="v1",
             conduite="Comparer les deux baromètres au tableau."),
    ],
)

# ---------------------------------------------------------------- 7
S["Gérer un incident et protéger les élèves"] = dict(
    moteur=["Course contre la montre", "Tables tournantes", "Commission éducative simulée"],
    materiel=["Les douze cartes du document 11 découpées par équipe", "Une frise 8 h 05 – 9 h 05 par équipe", "Quatre tables thématiques avec leurs documents", "Cartes du document 12 pour la commission", "Chronomètre"],
    phases=[
        dict(titre="Les soixante premières minutes", format="Course contre la montre", duree=10, modalite="Équipes de 4",
             consigne="Lisez ce que vous savez à 8 h 05 et le message des parents d'Inès. Puis placez les douze cartes du document 11 sur une frise de 8 h 05 à 9 h 05, dans l'ordre où vous les feriez. Mettez de côté celles que vous ne feriez jamais. Vous avez 6 minutes.",
             docs=[1, 2, 11], roles=True,
             conduite="Annoncer le temps restant toutes les deux minutes. Photographier chaque frise : elles seront comparées au bilan."),
        dict(titre="Les tables tournantes", format="Tables tournantes", duree=15, modalite="Quatre tables, les équipes tournent toutes les 4 minutes",
             consigne="Chaque table traite une question avec ses documents : le droit disciplinaire, le harcèlement, la protection, la communication. Votre équipe passe 4 minutes à chaque table et complète l'affiche laissée par l'équipe précédente.",
             dossier=True, mission=True, mission_titre="Les quatre tables",
             conduite="Donner le signal de rotation. À chaque table, un document piège : la fiche sur la protection de l'enfance en France. Vérifier qu'une équipe le signale."),
        dict(titre="Mardi, 14 h : Yanis", format="Le formateur joue Yanis", duree=10, modalite="Toute la salle interroge",
             consigne="Le formateur joue Yanis. Posez-lui vos questions, une par équipe. Puis lisez le document 10 : Yanis est-il auteur, victime, ou les deux ? Que change ce qu'il dit pour la suite ?",
             docs=[10],
             conduite="Jouer Yanis fermé, qui ne s'ouvre qu'aux questions ouvertes et non accusatrices. Refuser de nommer les terminales."),
        dict(titre="La commission éducative", format="Simulation à rôles", duree=25, modalite="Six rôles, le reste de la salle observe",
             consigne="Avec les cartes du document 12, jouez la commission éducative réunie pour Yanis (15 minutes). Les observateurs vérifient les principes : contradictoire, individualisation, proportionnalité, protection de Yanis. Puis ils rendent compte.",
             docs=[12],
             conduite="Distribuer les rôles en veillant à ce que le CPE ne soit pas joué par un stagiaire déjà très présent. Arrêter si Yanis est sommé de nommer les terminales : c'est le moment d'apprentissage."),
        dict(titre="Les deux arbres et la proposition", format="Arbres affichés", duree=15, modalite="Équipes",
             affiche="Deux arbres côte à côte, incident et protection, avec une flèche rouge au point de bascule.",
             consigne="Dessinez sur une affiche les deux arbres de décision, incident et protection, et marquez en rouge le point où l'un bascule dans l'autre. Puis rédigez la proposition que vous remettez à la proviseure, communication comprise.",
             production=True,
             conduite="Afficher les arbres et les comparer aux frises du début."),
        dict(titre="Ma ligne rouge", format="Engagement individuel", duree=5, modalite="Individuel",
             consigne="Écrivez la ligne rouge que vous ne franchirez jamais, même sous la pression d'une famille ou de votre hiérarchie.",
             conduite="Inviter trois volontaires à lire leur ligne rouge."),
    ],
)

# ---------------------------------------------------------------- 8
S["Faire vivre la démocratie scolaire"] = dict(
    moteur=["Message à chaud", "Crash-test du questionnaire", "Répétition coachée"],
    materiel=["Dossier en quatre jeux", "Feuilles A4 pour les questionnaires réécrits", "Cartes du document 10 par trio", "Document 11 : le formateur joue le gestionnaire"],
    phases=[
        dict(titre="Le message à Tom", format="Écrit flash", duree=5, modalite="Individuel",
             consigne="Lisez la demande des élus et le message de Tom. Vous avez 60 secondes pour répondre à Tom, comme sur une messagerie : trois lignes au plus.",
             docs=[1, 2],
             conduite="Chronométrer 60 secondes. Lire trois réponses : interdire, ignorer ou proposer autre chose."),
        dict(titre="Le diagnostic éclair", format="Enquête et restitution d'une minute", duree=15, modalite="4 groupes",
             affiche="Une affiche A3 : une phrase choc, un chiffre, une question à poser à la direction.",
             consigne="Chaque groupe mène son enquête dans le dossier pendant 10 minutes, puis la restitue en une minute exactement, debout, devant son affiche. Ne reprenez aucune conclusion des élus sans l'avoir vérifiée.",
             dossier=True, mission=True, mission_titre="Quatre enquêtes, une minute de restitution chacune", roles=True,
             conduite="Couper chaque restitution à une minute pile."),
        dict(titre="Le crash-test du questionnaire", format="Atelier de conception", duree=15, modalite="Groupes, puis échange avec le groupe voisin",
             consigne="Sur une feuille A4, réécrivez la question du questionnaire et la façon de le diffuser (8 minutes). Échangez avec le groupe voisin : il a 4 minutes pour trouver tous les biais qui restent dans le vôtre. Corrigez.",
             conduite="Encourager les groupes à être impitoyables pendant le crash-test."),
        dict(titre="La répétition des élus", format="Répétition coachée", duree=10, modalite="Trios : un élu, M. Vidal, un CPE coach",
             consigne="Avec les cartes du document 10, l'élu présente le projet en deux minutes à M. Vidal, qui l'interrompt une fois. Le CPE coach se tait, puis donne deux points forts, une question et une suggestion. Changez de rôle.",
             conduite="Rappeler que le CPE coach ne réécrit pas le discours à la place de l'élu."),
        dict(titre="Vendredi : le journal lycéen", format="Le formateur joue le gestionnaire", duree=10, modalite="Groupes",
             consigne="Le gestionnaire fait irruption : « Faites retirer ce journal, tout de suite ! » (document 11). Que faites-vous avec les rédacteurs, avec le cuisinier, avec les élèves ? Qui peut décider d'un retrait ?",
             docs=[11],
             conduite="Entrer en jouant le gestionnaire, en colère, journal à la main. Ne pas sortir du rôle avant d'avoir obtenu une réponse."),
        dict(titre="La feuille de route", format="Production", duree=5, modalite="Groupes",
             consigne="Finalisez le questionnaire et la feuille de route des élus. Terminez par ce que vous ferez différemment lors des prochaines élections dans votre établissement.",
             production=True,
             conduite="La production peut être finalisée dans le carnet."),
    ],
)

# ---------------------------------------------------------------- 9
S["Une matinée dans la peau du CPE"] = dict(
    moteur=["Simulation chronométrée", "Analyse de pratique", "Lettre à soi-même"],
    materiel=["Les six événements imprimés séparément, ou révélés à l'écran", "Un téléphone pour les appels joués par le formateur", "Grille d'observation par observateur", "Chronomètre", "Enveloppes pour la lettre"],
    phases=[
        dict(titre="Mes trois critères", format="Écrit individuel", duree=5, modalite="Groupes de quatre : un CPE, trois observateurs",
             consigne="Répartissez les rôles. Avant le premier événement, écrivez les trois critères qui guideront vos priorités. Ouvrez le journal des décisions et relisez le tableau des postes du jour.",
             docs=[1, 2],
             conduite="Exiger les trois critères écrits avant de commencer."),
        dict(titre="La matinée", format="Simulation chronométrée", duree=30, modalite="Groupes",
             consigne="Révélez les événements au signal du formateur, pas avant. Consignez chaque décision et son critère dans le journal. Vous ne pourrez pas tout traiter : choisissez. Le CPE change à chaque événement.",
             sequence=[
                 ("07:50", "M. Bernard part en sortie à 8 h avec sa classe de 4e. Un élève n'a pas d'autorisation parentale signée. « Sa mère m'a dit oui au téléphone, je l'emmène. »"),
                 ("08:05", "Un élève de 6e confie à l'AED de l'accueil qu'il est seul chez lui depuis deux jours : ses parents sont en voyage et doivent rentrer samedi."),
                 ("08:20", "Un élève de 1re arrive en retard, les propos confus. L'AED du portail sent une forte odeur d'alcool."),
                 ("08:40", "Une mère appelle, furieuse : la photo de sa fille figure sur le site du lycée sans son accord. Elle parle de porter plainte."),
                 ("08:45", "M. Garnier vous amène un élève : « Il a un téléphone volé dans son sac, j'en suis sûr. Fouillez-le, c'est votre rôle. »"),
                 ("09:00", "La proviseure demande pour 11 h un point écrit et factuel sur la matinée."),
             ],
             conduite="Révéler un événement toutes les quatre à cinq minutes, sans attendre que le précédent soit traité. L'événement de 8 h 20 tombe volontairement pendant le traitement de celui de 8 h 05."),
        dict(titre="9 h 20 : deux appels", format="Le formateur joue au téléphone", duree=10, modalite="Groupes",
             consigne="Le formateur vous appelle deux fois (document 5). Répondez en direct, puis rédigez le point écrit de 11 h.",
             docs=[5],
             conduite="Jouer le père depuis l'étranger, puis la proviseure. Exiger une réponse écrite à la proviseure."),
        dict(titre="L'analyse de pratique", format="Analyse de pratique entre pairs", duree=15, modalite="Groupes de quatre",
             consigne="Avec la grille du document 3, un membre du groupe expose la décision qui l'a le plus fait hésiter. Respectez strictement les étapes et les temps.",
             docs=[3],
             conduite="Le formateur est garant du cadre : pas de conseil pendant la phase de clarification."),
        dict(titre="Mes trente premiers jours", format="Production", duree=10, modalite="Individuel",
             consigne="Établissez votre plan des trente premiers jours avec le document 4, puis faites votre positionnement de fin de formation.",
             docs=[4], production=True,
             conduite="Laisser le temps du positionnement final sur le site."),
        dict(titre="La lettre à moi-même", format="Lettre à soi-même", duree=5, modalite="Individuel",
             consigne="Relisez vos trois critères du début. Puis écrivez une lettre à vous-même, à ouvrir dans trente jours : ce que vous voulez avoir fait, ce que vous ne voulez jamais faire. Le formateur vous la renverra.",
             rappel=True,
             conduite="Distribuer les enveloppes. Proposer de photographier la lettre ou de l'envoyer par courriel différé."),
    ],
)


def appliquer(ateliers):
    for a in ateliers:
        sc = S.get(a["titre"])
        if not sc:
            continue
        a["moteur"] = sc["moteur"]
        a["phases"] = sc["phases"]
        if "groupes" in sc:
            a["groupes"] = sc["groupes"]
        a["formateur"]["materiel"] = sc["materiel"]
        a["formateur"]["deroule"] = [p["conduite"] for p in sc["phases"]]
