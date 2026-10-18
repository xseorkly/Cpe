# -*- coding: utf-8 -*-
"""Les huit ateliers, construits comme des situations-problèmes.

Structure d'un atelier
- problematique : la question professionnelle que le stagiaire doit trancher
- situation     : le récit de départ, à la deuxième personne
- docs          : le dossier documentaire (ordre = numérotation). Certains
                  documents sont des pièges volontaires (texte remplacé, texte
                  non applicable à l'étranger, fiche de poste hors cadre,
                  données trompeuses) : le stagiaire doit les débusquer.
- phases        : déroulé ; chaque phase révèle des documents (docs), ouvre le
                  dossier (dossier=True), confie des missions (groupes), pose
                  une controverse (positions) ou rappelle la première réaction
                  (rappel=True)
- formateur     : déroulé, relances pour mettre en difficulté, attendus,
                  vigilance
- slides        : le diaporama de bilan, avec les apports théoriques

L'équipe fictive du lycée Horizon (réseau AEFE, 780 élèves) :
Mme Laurent (proviseure), M. Vidal (proviseur adjoint), Mme Martel (CPE
précédente, partie en juin), Mme Benali (infirmière), Mme Sorel (psychologue),
AED : Antoine (A), Bérénice (B), Camille (C), David (D), Elsa (E), Fabien (F).
"""

ATELIERS = []

# ======================================================================
# ATELIER 1
# ======================================================================
ATELIERS.append(dict(
    n=1,
    titre="Découvrir mon métier de CPE",
    accroche="Tout le monde attend quelque chose de moi : qu'est-ce qui relève vraiment de moi ?",
    problematique="Dès ma première semaine, chacun projette sur moi sa vision du CPE. Sur quoi m'appuyer pour savoir ce qui relève vraiment de mes missions, et comment le faire entendre sans me mettre l'équipe à dos ?",
    situation="""
<p>Lundi, 7 h 45. Vous prenez votre poste de CPE au lycée Horizon, établissement du réseau AEFE de 780 élèves. Votre prédécesseure, Mme Martel, est partie en juin après onze ans dans la maison. Elle vous a laissé son bureau, un classeur de textes et un mot sur l'écran.</p>
<p>À 8 h 10, la proviseure, Mme Laurent, passe la tête : « Je compte sur vous pour tenir la maison. Jeudi, au conseil pédagogique, vous présenterez en cinq minutes votre conception du métier et vos priorités. Les collègues attendent de voir à qui ils ont affaire. »</p>
<p>À 9 h, votre boîte de réception contient douze messages. Dans le couloir, un professeur vous lance : « Alors, c'est vous le nouveau surveillant général ? »</p>""",
    objectifs=[
        "Identifier les textes qui définissent les missions du CPE et repérer un texte remplacé.",
        "Confronter une fiche de poste locale au cadre réglementaire et formuler un écart sans conflit ouvert.",
        "Distinguer ce que je décide, ce que je conseille, ce que je partage et ce que je signale.",
        "Répondre à une mise en cause publique en restant sur le terrain de l'institution.",
        "Présenter ma conception du métier à une équipe en m'appuyant sur des références.",
    ],
    competences=["C2", "C8"],
    blocs=["3", "1"],
    blocs_detail="3.3 et 3.4 (système éducatif, place du CPE dans l'équipe) ; 1.8 (communauté éducative)",
    production="Une intervention de trois minutes au conseil pédagogique, et ma check-list de prise de fonction.",
    criteres=[
        "L'intervention s'appuie sur au moins deux textes en vigueur, cités correctement.",
        "Elle distingue explicitement ce que le CPE décide, conseille, partage et signale.",
        "Elle répond à la mise en cause du professeur sans le désavouer ni se désavouer.",
        "Elle annonce deux priorités concrètes et vérifiables pour le premier trimestre.",
        "La check-list nomme au moins dix documents ou interlocuteurs, classés par urgence.",
    ],
    docs=[
        dict(titre="Votre boîte de réception, lundi 9 h", type="Messages", html="""
<table><thead><tr><th>De</th><th>Objet</th><th>Extrait</th></tr></thead><tbody>
<tr><td>M. Garnier, professeur de mathématiques</td><td>Exclusion</td><td>« J'ai mis Lucas dehors ce matin. Je veux une exclusion de trois jours, il faut marquer le coup dès la rentrée. »</td></tr>
<tr><td>Bérénice, AED</td><td>Absences</td><td>« Une élève de 4e est absente depuis jeudi sans nouvelles. Je fais quoi ? »</td></tr>
<tr><td>M. Vidal, adjoint</td><td>Portail</td><td>« Il faudrait revoir l'accueil du matin, c'est l'embouteillage. »</td></tr>
<tr><td>Mme Haddad, parent</td><td>Règlement</td><td>« L'article sur les téléphones est illégal, je vais saisir l'ambassade. »</td></tr>
<tr><td>Rayan, 1re</td><td>Orientation</td><td>« Je veux changer de spécialité, mes parents ne sont pas d'accord. »</td></tr>
<tr><td>Les délégués de 2nde</td><td>Sondage</td><td>« On veut faire un questionnaire sur la cantine, vous pouvez l'imprimer ? »</td></tr>
<tr><td>David et Elsa, AED</td><td>Planning</td><td>« Les postes du midi sont toujours pour nous. Ce n'est pas juste. »</td></tr>
<tr><td>Camille, AED</td><td>Urgent</td><td>« Une élève de 3e pleure dans les toilettes, elle dit qu'elle ne veut pas rentrer chez elle ce soir. »</td></tr>
<tr><td>Mme Roche, professeure principale</td><td>Retards</td><td>« Pouvez-vous suivre les retards de ma classe ? Je n'ai pas le temps. »</td></tr>
<tr><td>M. Ferrand, parent</td><td>Information</td><td>« Je veux savoir qui a frappé mon fils et quelle sanction il aura. Donnez-moi son nom. »</td></tr>
<tr><td>Inès et Léa, 5e</td><td>Dispute</td><td>« On ne se parle plus, vous pouvez nous aider ? »</td></tr>
<tr><td>Mme Laurent, proviseure</td><td>Bilan</td><td>« Pour le conseil d'établissement, il me faudra un bilan chiffré de la vie scolaire. »</td></tr>
</tbody></table>"""),
        dict(titre="Le mot de Mme Martel", type="Établissement", html="""
<blockquote>« Bienvenue ! Ici, le CPE gère tout : la discipline, les surveillances, les remplacements quand un prof est absent, les conflits entre collègues. Les profs t'enverront les élèves, tu tranches. Garde le classeur rouge, tout y est. Bon courage. »</blockquote>
<p class="note">Le « classeur rouge » contient notamment le document 4.</p>"""),
        dict(titre="Les missions du CPE aujourd'hui", type="Texte officiel", groupe=1, html="""
<p><strong>Circulaire n° 2015-139 du 10 août 2015</strong> (synthèse reformulée). Le CPE exerce ses responsabilités éducatives sous l'autorité du chef d'établissement et, le cas échéant, de son adjoint. Ses missions s'organisent en trois domaines :</p>
<ol>
<li><strong>La politique éducative de l'établissement</strong> : il contribue au volet éducatif du projet d'établissement, au climat scolaire, à la citoyenneté et à la vie démocratique.</li>
<li><strong>Le suivi des élèves</strong> : assiduité, accompagnement individuel et collectif, travail avec les familles et les équipes pédagogiques, prévention du décrochage, contribution à l'orientation.</li>
<li><strong>L'organisation de la vie scolaire</strong> : organisation du service et animation de l'équipe de vie scolaire, temps et espaces hors la classe, sécurité des élèves, respect des règles.</li>
</ol>
<p>Le texte précise que le CPE conseille le chef d'établissement dans son domaine, mais qu'il ne se substitue ni à lui ni aux autres personnels. Il abroge la circulaire de 1982.</p>
<p class="note"><a href="https://www.education.gouv.fr/bo/15/Hebdo31/MENH1517711C.htm" target="_blank" rel="noopener">Texte intégral au Bulletin officiel n° 31 du 27 août 2015</a>.</p>"""),
        dict(titre="Le texte du classeur rouge", type="Texte officiel", groupe=1, html="""
<p><strong>Circulaire n° 82-482 du 28 octobre 1982</strong> relative au rôle des CPE (synthèse reformulée, photocopie jaunie).</p>
<p>Le texte organise l'activité du CPE en trois domaines : le fonctionnement de l'établissement (contrôle des effectifs, organisation de la surveillance), la collaboration avec le personnel enseignant, l'animation éducative.</p>
<p class="note">Document affiché au mur du bureau de la vie scolaire depuis plusieurs années.</p>"""),
        dict(titre="Les compétences du CPE", type="Texte officiel", groupe=1, html="""
<p><strong>Arrêté du 1er juillet 2013</strong> : référentiel des compétences des métiers du professorat et de l'éducation. Il comprend quatorze compétences communes à tous les personnels et huit compétences spécifiques aux CPE :</p>
<ol>
<li>Organiser les conditions de vie des élèves, leur sécurité, l'organisation matérielle et la gestion du temps.</li>
<li>Garantir, en lien avec les autres personnels, le respect des règles de vie et de droit.</li>
<li>Impulser et coordonner le volet éducatif du projet d'établissement.</li>
<li>Assurer la responsabilité de l'organisation et de l'animation de l'équipe de vie scolaire.</li>
<li>Accompagner le parcours de l'élève sur les plans pédagogique et éducatif.</li>
<li>Accompagner les élèves dans leur formation à une citoyenneté participative.</li>
<li>Participer à la construction des parcours des élèves.</li>
<li>Travailler dans une équipe pédagogique.</li>
</ol>
<p class="note"><a href="https://www.education.gouv.fr/bo/13/Hebdo30/MENE1315928A.htm" target="_blank" rel="noopener">Bulletin officiel n° 30 du 25 juillet 2013</a>.</p>"""),
        dict(titre="Votre fiche de poste", type="Établissement", groupe=2, html="""
<p><strong>Lycée Horizon · Fiche de poste du CPE</strong> (rédigée en 2019 par la direction précédente, jamais révisée).</p>
<ul>
<li>Organise le service des assistants d'éducation et en établit le planning.</li>
<li>Assure le suivi de l'assiduité et le lien avec les familles.</li>
<li><strong>Décide des exclusions de cours et des exclusions temporaires.</strong></li>
<li><strong>Remplace les enseignants absents en assurant la surveillance des classes.</strong></li>
<li>Anime le conseil de la vie lycéenne.</li>
<li><strong>Gère les absences et les congés des personnels administratifs.</strong></li>
<li>Participe aux conseils de classe et aux équipes de suivi.</li>
</ul>"""),
        dict(titre="Qui décide quoi au lycée Horizon ?", type="Établissement", groupe=2, html="""
<table><thead><tr><th>Domaine</th><th>Qui décide</th></tr></thead><tbody>
<tr><td>Sanction disciplinaire (avertissement, exclusion…)</td><td>Le chef d'établissement, ou le conseil de discipline</td></tr>
<tr><td>Punition scolaire (retenue, devoir supplémentaire…)</td><td>Les personnels, dans le cadre du règlement intérieur</td></tr>
<tr><td>Règlement intérieur</td><td>Adopté par le conseil d'établissement</td></tr>
<tr><td>Orientation</td><td>L'élève et sa famille, avec le conseil de classe ; décision finale par le chef d'établissement</td></tr>
<tr><td>Situation de danger pour un élève</td><td>Circuit de protection de l'établissement, direction, secours si urgence</td></tr>
<tr><td>Contrats et congés des personnels</td><td>Le chef d'établissement, en lien avec l'employeur</td></tr>
<tr><td>Communication de données personnelles</td><td>La direction, dans le respect du RGPD</td></tr>
</tbody></table>
<p class="note">Document fictif construit pour l'exercice. Dans un établissement réel, il se vérifie dans le règlement intérieur, l'organigramme et la circulaire AEFE sur les instances.</p>"""),
        dict(titre="Ce qu'ils attendent du CPE", type="Témoignages", groupe=3, html="""
<ul>
<li><strong>La proviseure :</strong> « Un CPE, c'est quelqu'un sur qui je peux compter pour que ça tourne. Je ne veux pas être dérangée pour chaque bavardage. »</li>
<li><strong>M. Garnier, mathématiques :</strong> « Le CPE est là pour soutenir les profs. Quand j'envoie un élève, j'attends une sanction, pas une discussion. »</li>
<li><strong>Mme Roche, professeure principale :</strong> « J'ai besoin de quelqu'un qui connaisse les élèves autrement que par leurs notes. »</li>
<li><strong>Antoine, AED depuis trois ans :</strong> « Mme Martel nous laissait faire. Elle disait : c'est vous le terrain. »</li>
<li><strong>Une déléguée de terminale :</strong> « Le CPE, c'est le seul adulte à qui on peut parler sans que ça finisse dans le bulletin. »</li>
<li><strong>Un parent d'élève élu :</strong> « On attend du CPE qu'il nous appelle avant que ce soit trop tard. »</li>
</ul>"""),
        dict(titre="Mardi, 17 h 12 : deux messages", type="Rebondissement", html="""
<p><strong>De M. Garnier à toute la liste « salle des professeurs » :</strong></p>
<blockquote>« Chers collègues, j'apprends que le nouveau CPE a refusé d'exclure l'élève que j'avais mis dehors hier. Il a préféré "discuter". Si la vie scolaire ne soutient plus les enseignants, il faudra en tirer les conséquences. »</blockquote>
<p><strong>De Mme Laurent, à vous seul :</strong></p>
<blockquote>« J'ai vu le message. Je vous laisse en parler jeudi au conseil pédagogique. Je ne veux pas que cela tourne au conflit. »</blockquote>
<p class="note">Vous n'aviez pas « refusé » : vous aviez reçu l'élève, établi les faits et indiqué que la décision d'une exclusion appartenait à la proviseure.</p>"""),
    ],
    groupes=[
        dict(nom="Les textes", angle="Quel texte fait foi ?",
             questions=["Quels sont les textes en vigueur ? Lequel est périmé, et comment le savez-vous ?",
                        "Qu'est-ce qui a changé entre 1982 et 2015 dans la conception du métier ?",
                        "Quelles phrases des textes pourriez-vous citer jeudi ?"],
             docs=[3, 4, 5]),
        dict(nom="L'établissement", angle="Ma fiche de poste est-elle légale ?",
             questions=["Quelles lignes de la fiche de poste sont conformes aux textes ? Lesquelles ne le sont pas ?",
                        "Que risquez-vous à appliquer la fiche telle quelle ? À la contester frontalement ?",
                        "Comment demander sa révision à la proviseure ?"],
             docs=[6, 7, 3]),
        dict(nom="Les attentes", angle="Quelles représentations du métier circulent ?",
             questions=["Quelle image du CPE porte chaque témoignage (surveillant général, pompier, confident, adjoint…) ?",
                        "Lesquelles sont compatibles avec les textes ? Lesquelles faut-il faire évoluer, et comment ?",
                        "Qu'est-ce que le mot de Mme Martel vous apprend sur l'histoire de la maison ?"],
             docs=[8, 2, 3]),
        dict(nom="Les compétences", angle="Pour chaque message : je décide, je conseille, je coopère ou je signale ?",
             questions=["Classez les douze messages dans les quatre verbes : je décide, je conseille, je coopère, je signale.",
                        "Quels messages appellent un refus ? Formulez-le sans fermer la porte.",
                        "Deux messages relèvent d'un réflexe immédiat de signalement : lesquels, et vers qui ?"],
             docs=[1, 7]),
    ],
    phases=[
        dict(titre="Ma première réaction", duree=5, modalite="Individuel, sans document",
             consigne="Lisez la situation, la boîte de réception et le mot de Mme Martel. Sans rien consulter d'autre, écrivez : 1) les trois phrases que vous diriez jeudi au conseil pédagogique ; 2) les trois messages que vous traitez en premier. Vous relirez ce texte à la fin de l'atelier.",
             docs=[1, 2]),
        dict(titre="L'enquête en groupes experts", duree=20, modalite="4 groupes experts, puis groupes mixtes",
             consigne="Chaque groupe prend une mission et va chercher ses réponses dans le dossier documentaire. Attention : certains documents sont périmés ou contraires aux textes. Au bout de 12 minutes, formez des groupes mixtes (un membre de chaque groupe expert) et mettez vos découvertes en commun.",
             dossier=True, mission=True),
        dict(titre="Le rebondissement", duree=10, modalite="Groupes mixtes",
             consigne="Lisez le document 9. Faut-il répondre à M. Garnier, et si oui, comment, quand, par quel canal ? Écrivez la première phrase que vous lui direz, et ce que vous direz jeudi devant l'équipe.",
             docs=[9]),
        dict(titre="La controverse", duree=10, modalite="Débat en deux camps",
             consigne="Le formateur attribue une position à chaque moitié du groupe. Défendez-la avec au moins deux documents du dossier. Puis chacun dit ce qu'il retient de juste dans la position adverse.",
             positions=[
                 ("Le CPE est d'abord le garant de l'ordre", "Sans cadre tenu, aucun travail éducatif n'est possible. Les enseignants doivent pouvoir compter sur une réponse rapide et ferme."),
                 ("Le CPE est d'abord un éducateur et un conseiller", "La sanction n'est pas son pouvoir propre. Sa valeur ajoutée est la connaissance de l'élève, le suivi et la coopération."),
             ]),
        dict(titre="Je produis", duree=10, modalite="Groupes mixtes, puis passage de deux groupes",
             consigne="Rédigez votre intervention de trois minutes pour le conseil pédagogique, puis votre check-list de prise de fonction. Vérifiez chaque critère de réussite.",
             production=True),
        dict(titre="Retour sur ma première réaction", duree=5, modalite="Individuel",
             consigne="Relisez votre première réaction. Qu'auriez-vous dit jeudi sans l'enquête ? Quelle représentation du métier aviez-vous en arrivant ?",
             rappel=True),
    ],
    cloture=[
        "Quel document du dossier vous aurait induit en erreur si vous l'aviez cru sur parole ?",
        "Quelle demande avez-vous d'abord cru relever de votre seule décision ?",
        "Quel document irez-vous demander en premier dans votre établissement ?",
    ],
    approfondir="posture",
    refs=["missions", "competences", "formation", "aefe_instances"],
    formateur=dict(
        materiel=["Dossier documentaire imprimé en quatre jeux (un par groupe expert)", "Document 9 imprimé à part", "Deux affichettes pour la controverse"],
        deroule=[
            "Écrit individuel et silencieux. Ne rien corriger. Recueillir trois premières phrases à voix haute : elles serviront au bilan.",
            "Ne pas dire quels documents sont des pièges. Circuler et relancer avec les questions dérangeantes ci-dessous. Former les groupes mixtes à 15 minutes.",
            "Distribuer le document 9 sans commentaire. Exiger une phrase exacte, pas une intention.",
            "Attribuer les positions à contre-emploi : ceux qui penchaient vers l'ordre défendent le conseil, et inversement.",
            "Deux groupes passent devant le collectif en trois minutes chrono ; les autres évaluent avec les critères.",
            "Écrit individuel. Inviter deux volontaires à lire ce qui a changé.",
        ],
        relances=[
            "« La fiche de poste est signée par la direction. Vous allez désobéir à votre proviseure dès la première semaine ? »",
            "« Le texte de 1982 est au mur depuis des années et personne n'a rien dit. Qu'est-ce qui vous prouve qu'il n'est plus valable ? »",
            "« M. Garnier a plus d'ancienneté que vous. Si vous ne l'exclurez pas, qui vous soutiendra quand vous aurez besoin de lui ? »",
            "« La proviseure ne veut pas de conflit. Ne vaut-il pas mieux ne rien dire jeudi ? »",
            "« L'élève qui pleure peut attendre la fin de votre réunion, non ? »",
        ],
        attendus="""
<p><strong>Groupe « Les textes ».</strong> La circulaire de 2015 abroge celle de 1982 : le document 4 est périmé. Le passage du « fonctionnement de l'établissement » à une « politique éducative » et au « suivi des élèves » marque le glissement d'un métier de surveillance vers un métier d'éducation.</p>
<p><strong>Groupe « L'établissement ».</strong> Trois lignes de la fiche de poste sont hors cadre : décider des exclusions (compétence du chef d'établissement), remplacer les enseignants absents (ce n'est pas une mission du CPE), gérer les congés des personnels administratifs. Stratégie attendue : demander un entretien à la proviseure, s'appuyer sur la circulaire, proposer une version révisée plutôt que refuser.</p>
<p><strong>Groupe « Les attentes ».</strong> Les représentations du « surveillant général », du « bras armé des enseignants », du « confident » coexistent. Le texte de 2015 les dépasse : il faut les entendre, sans les laisser définir le poste.</p>
<p><strong>Groupe « Les compétences ».</strong> Deux messages ne peuvent pas attendre : l'élève qui ne veut pas rentrer chez elle (protection, alerte immédiate) et l'élève absente depuis jeudi sans nouvelles (contact famille dans la journée). Deux appellent un refus motivé : le nom de l'autre élève (données personnelles) et l'exclusion de trois jours (pas la compétence du CPE).</p>
<p><strong>Rebondissement.</strong> Ne pas répondre à la liste de diffusion. Rencontrer M. Garnier en tête-à-tête avant jeudi, revenir aux faits et à la règle (qui décide d'une exclusion), lui proposer ce que le CPE peut faire (suivi de l'élève, retour sur la situation). Jeudi : présenter le cadre sans régler de comptes.</p>""",
        vigilance=[
            "Les stagiaires veulent souvent « gagner » contre M. Garnier. Ramener à l'objectif : construire une relation de travail durable.",
            "La circulaire de 2015 s'applique aux CPE fonctionnaires ; dans le réseau AEFE, le statut de l'établissement et du personnel conditionne ce qui s'applique. À faire vérifier.",
            "Ne pas laisser passer « l'élève qui pleure peut attendre » : c'est le réflexe de protection que l'atelier installe.",
        ],
    ),
    slides=[
        dict(t="titre", titre="Ce qui relève vraiment de moi", sous="Bilan de l'atelier 1 · Découvrir mon métier de CPE"),
        dict(t="points", titre="Ce que vous avez dû trancher", points=["Un texte au mur depuis des années… et abrogé depuis 2015", "Une fiche de poste signée… qui attribue au CPE des pouvoirs qu'il n'a pas", "Des attentes contradictoires sur ce qu'est « un bon CPE »", "Une mise en cause publique dès la deuxième journée"]),
        dict(t="etapes", titre="Un métier qui a changé de nature", etapes=[("1970", "Création du corps des CPE, qui succède aux surveillants généraux"), ("1982", "Première circulaire de missions : fonctionnement, collaboration, animation"), ("2013", "Référentiel de compétences : 14 compétences communes et 8 spécifiques (C1 à C8)"), ("2015", "Nouvelle circulaire : politique éducative, suivi des élèves, organisation de la vie scolaire"), ("2026", "Référentiel de formation en quatre blocs")], source="Décret n° 70-738 du 12 août 1970 ; circulaires de 1982 et 2015 ; arrêté du 1er juillet 2013"),
        dict(t="deux", titre="De la surveillance à l'éducation", a=("Hier : le surveillant général", ["Faire respecter l'ordre", "Contrôler les effectifs", "Sanctionner"]), b=("Aujourd'hui : le CPE", ["Contribuer à la politique éducative", "Suivre chaque élève et coopérer", "Organiser la vie scolaire au service des apprentissages"]), source="Circulaire n° 2015-139"),
        dict(t="def", titre="La hiérarchie des normes, appliquée", terme="Loi › décret › arrêté › circulaire › règlement intérieur › fiche de poste", definition="Un document de rang inférieur ne peut pas contredire un texte supérieur. Une fiche de poste ne peut pas confier au CPE une décision que le code de l'éducation réserve au chef d'établissement, comme une exclusion.", source="Dans le réseau AEFE, le statut de l'établissement et le droit local s'ajoutent : à vérifier avec la direction"),
        dict(t="etapes", titre="Quatre verbes pour situer chaque demande", etapes=[("Je décide", "Ce qui relève de mon champ : organisation du service, suivi de l'assiduité, punitions prévues au RI"), ("Je conseille", "J'éclaire la décision de la direction : sanction, organisation, priorités"), ("Je coopère", "Je travaille avec le professeur principal, l'infirmière, la psychologue, la famille"), ("Je signale", "Je transmets sans délai à l'autorité compétente : danger, faits graves")]),
        dict(t="def", titre="L'identité professionnelle", terme="Identité pour soi et identité pour autrui", definition="Pour le sociologue Claude Dubar, l'identité professionnelle se construit dans la négociation entre l'image que l'on a de son métier et celle que les autres nous attribuent. Les représentations des collègues ne définissent pas le métier, mais on ne peut pas les ignorer : on les fait évoluer par la pratique et par l'explicitation.", source="Claude Dubar, La socialisation, 1991"),
        dict(t="etapes", titre="Répondre à une mise en cause", etapes=[("Ne pas répondre à chaud", "Ni par courriel collectif, ni dans le couloir"), ("Rencontrer la personne", "En tête-à-tête, avant toute réunion"), ("Revenir aux faits et au cadre", "Ce qui s'est passé, qui décide de quoi"), ("Proposer ce que je peux faire", "Suivi de l'élève, retour d'information"), ("Informer la direction", "Sans dramatiser ni se plaindre")]),
        dict(t="cle", texte="Deux réflexes ne souffrent aucun délai : un élève en danger, on protège et on alerte ; les données d'un autre élève, on ne les communique jamais."),
        dict(t="points", titre="Mes questions pour la première semaine", points=["Quels textes s'appliquent à mon établissement et à mon statut ?", "Qui est mon interlocuteur pour une situation de danger ?", "Ma fiche de poste est-elle à jour ? Qui peut la réviser ?", "Quelles représentations du CPE circulent dans cette maison ?"]),
    ],
))

# ======================================================================
# ATELIER 2
# ======================================================================
ATELIERS.append(dict(
    n=2,
    titre="Organiser et piloter la vie scolaire",
    accroche="On me demande un planning et des chiffres : et si le problème était ailleurs ?",
    problematique="La proviseure exige un nouveau planning pour lundi et « des chiffres en baisse » pour le conseil d'établissement. Comment organiser le service à partir d'un vrai diagnostic, plutôt que de boucher les trous et de produire les chiffres attendus ?",
    situation="""
<p>Troisième semaine de septembre. Chaque matin, une file d'élèves s'étire devant le portail jusqu'à 8 h 15. Les professeurs de première heure se plaignent d'élèves qui arrivent par vagues. Mercredi, une bousculade dans la cour a fini à l'infirmerie.</p>
<p>Mme Laurent vous écrit : elle veut un nouveau planning des AED pour lundi, et des retards « en nette baisse » à présenter au conseil d'établissement du 15 octobre. Les professeurs réclament un AED par couloir. Les parents demandent plus de monde au portail. Vous n'aurez aucun poste supplémentaire.</p>
<p>Vous héritez du planning de Mme Martel, d'un tableau de chiffres et de beaucoup d'avis.</p>""",
    objectifs=[
        "Lire un indicateur de façon critique : dénominateur, période, mode de saisie.",
        "Croiser trois sources (données, observation, parole) pour poser un diagnostic.",
        "Distinguer une cause structurelle d'un comportement individuel.",
        "Construire une organisation sous contraintes et justifier ses arbitrages.",
        "Rendre compte à la direction avec des indicateurs honnêtes.",
    ],
    competences=["C1", "C3", "C4"],
    blocs=["1", "2"],
    blocs_detail="1.1 et 1.2 (équipe, conditions de vie des élèves) ; 2.1 (culture de l'évaluation)",
    production="Une note d'une page à la proviseure : diagnostic, planning, arbitrages et indicateurs.",
    criteres=[
        "Le diagnostic contient trois constats, chacun appuyé sur une source citée.",
        "Il signale au moins une limite des données présentées.",
        "Le planning respecte les disponibilités et les règles d'emploi, et nomme l'arbitrage fait.",
        "La note propose au moins une action qui ne relève pas du planning des AED.",
        "Elle fixe un indicateur chiffré, un indicateur qualitatif et une date de bilan.",
    ],
    docs=[
        dict(titre="Le message de la proviseure", type="Messages", html="""
<blockquote>« Les retards du matin sont devenus inacceptables et les parents s'en plaignent. Je veux un nouveau planning des AED pour lundi. Pour le conseil d'établissement du 15 octobre, j'aurai besoin de chiffres qui montrent une nette amélioration. Je compte sur vous. »</blockquote>"""),
        dict(titre="Le planning hérité de Mme Martel", type="Établissement", html="""
<table class="center"><thead><tr><th>Créneau</th><th>Portail</th><th>Cour</th><th>Étude</th><th>Cantine</th><th>Accueil VS</th></tr></thead><tbody>
<tr><td>T1 · 08:00–08:30</td><td>Bérénice</td><td>Camille</td><td>—</td><td>—</td><td>Antoine</td></tr>
<tr><td>T2 · 10:00–10:30</td><td>—</td><td>Antoine</td><td>Elsa</td><td>—</td><td>Fabien</td></tr>
<tr><td>T3 · 12:00–12:30</td><td>—</td><td>Antoine</td><td>—</td><td>David</td><td>Camille</td></tr>
<tr><td>T4 · 13:15–13:45</td><td>Antoine</td><td>—</td><td><em>à voir</em></td><td>—</td><td>Elsa</td></tr>
</tbody></table>"""),
        dict(titre="Trois semaines de chiffres", type="Données", groupe=1, html="""
<table><thead><tr><th>Indicateur (total de la semaine)</th><th>S1 · 7–11 sept.</th><th>S2 · 14–18 sept.</th><th>S3 · 21–25 sept.</th></tr></thead><tbody>
<tr><td>Retards au créneau T1</td><td>58</td><td>61</td><td>45</td></tr>
<tr><td>Retards au créneau T4</td><td>12</td><td>16</td><td>11</td></tr>
<tr><td>Incidents relevés dans la cour</td><td>9</td><td>12</td><td>8</td></tr>
<tr><td>Incidents relevés en étude</td><td>6</td><td>6</td><td>5</td></tr>
</tbody></table>
<p class="note">Extraction du logiciel de vie scolaire. M. Vidal a noté en marge : « S3 : -26 % de retards, c'est déjà un bon signe ! »</p>"""),
        dict(titre="Le calendrier de septembre", type="Établissement", groupe=1, html="""
<table class="center"><thead><tr><th>Semaine</th><th>Jours de classe</th><th>Remarque</th></tr></thead><tbody>
<tr><td>S1 · 7–11 sept.</td><td>5</td><td></td></tr>
<tr><td>S2 · 14–18 sept.</td><td>5</td><td></td></tr>
<tr><td>S3 · 21–25 sept.</td><td>4</td><td>Lundi 21 : jour férié national du pays d'accueil</td></tr>
</tbody></table>"""),
        dict(titre="Note du référent numérique", type="Établissement", groupe=1, html="""
<blockquote>« Du 14 au 16 septembre, la tablette de saisie du portail était hors service. Les AED ont noté les retards sur papier. Une partie seulement a été ressaisie ensuite dans le logiciel. »</blockquote>"""),
        dict(titre="Observation d'un matin au portail", type="Observation", groupe=2, html="""
<p>Comptage réalisé par vous, mardi 23 septembre.</p>
<table class="center"><thead><tr><th>Tranche</th><th>Élèves entrés</th><th>Remarque</th></tr></thead><tbody>
<tr><td>07:40–07:50</td><td>95</td><td></td></tr>
<tr><td>07:50–07:58</td><td>160</td><td></td></tr>
<tr><td>07:58–08:05</td><td>280</td><td>Arrivée simultanée des quatre cars scolaires</td></tr>
<tr><td>08:05–08:15</td><td>110</td><td>File d'attente continue</td></tr>
</tbody></table>
<p>Un seul portillon est ouvert. Chaque carnet est contrôlé par l'AED du portail. Le deuxième portillon reste fermé : « la clé est à l'intendance ».</p>"""),
        dict(titre="Paroles recueillies", type="Témoignages", groupe=2, html="""
<ul>
<li><strong>Des élèves de 3e :</strong> « On descend du car à 8 h, et on attend dix minutes pour entrer. Après on se fait engueuler pour le retard. »</li>
<li><strong>Bérénice, AED :</strong> « Seule au portail, je ne peux pas contrôler les carnets et surveiller la rue en même temps. »</li>
<li><strong>Mme Roche, professeure principale :</strong> « Ce sont toujours les mêmes élèves qui arrivent après 8 h 05. »</li>
<li><strong>Un chauffeur de car :</strong> « On nous a demandé d'arriver tous à 7 h 58, pour l'horaire du lycée. »</li>
</ul>"""),
        dict(titre="L'équipe et ses règles d'emploi", type="Établissement", groupe=3, html="""
<table class="center"><thead><tr><th>AED</th><th>T1</th><th>T2</th><th>T3</th><th>T4</th><th>Particularité</th></tr></thead><tbody>
<tr><td>Antoine (A)</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>Trois ans d'ancienneté</td></tr>
<tr><td>Bérénice (B)</td><td>✓</td><td>✓</td><td>✓</td><td>—</td><td>En première année : binôme obligatoire au portail jusqu'aux vacances</td></tr>
<tr><td>Camille (C)</td><td>✓</td><td>✓</td><td>—</td><td>✓</td><td></td></tr>
<tr><td>David (D)</td><td>✓</td><td>—</td><td>✓</td><td>✓</td><td></td></tr>
<tr><td>Elsa (E)</td><td>—</td><td>✓</td><td>✓</td><td>✓</td><td></td></tr>
<tr><td>Fabien (F)</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td></td></tr>
</tbody></table>
<p><strong>Règles fixées par la direction :</strong> un AED ne tient qu'un poste à la fois ; deux postes au plus par AED et par jour, pour garder du temps de suivi et de transmission ; chaque créneau exige le portail (T1 et T4), la cour (T1 à T3), l'étude (T2 et T4), la cantine (T3) et l'accueil vie scolaire (tous les créneaux).</p>"""),
        dict(titre="Trois demandes concurrentes", type="Messages", groupe=4, html="""
<ul>
<li><strong>Coordination des professeurs :</strong> « Nous demandons un AED dans chaque couloir pendant la récréation de 10 h. »</li>
<li><strong>Association des parents :</strong> « Nous demandons deux adultes au portail le matin, pour la sécurité dans la rue. »</li>
<li><strong>M. Vidal :</strong> « Pour le conseil d'établissement, un graphique en baisse suffira. Ne compliquez pas. »</li>
</ul>"""),
        dict(titre="Vendredi, 7 h 30 : deux nouvelles", type="Rebondissement", html="""
<ul>
<li>David prévient qu'il sera absent toute la journée.</li>
<li>La proviseure rappelle que l'exercice d'évacuation a lieu ce matin à 10 h 10 : deux AED doivent être serre-files pendant quinze minutes.</li>
</ul>
<p>Reprenez votre planning. Quels postes maintenez-vous ? Lesquels fermez-vous ? Comment l'expliquez-vous à l'équipe et à la direction ?</p>"""),
    ],
    groupes=[
        dict(nom="Les chiffres", angle="Les retards baissent-ils vraiment ?",
             questions=["Calculez les retards par jour de classe, semaine par semaine.", "La remarque de M. Vidal est-elle juste ?", "Que peut-on affirmer avec certitude ? Que ne peut-on pas affirmer ?"],
             docs=[3, 4, 5]),
        dict(nom="Le terrain", angle="D'où viennent les retards ?",
             questions=["Que montre le comptage du portail ?", "Les retards relèvent-ils de comportements individuels ou d'une organisation ?", "Quelle action ne dépend pas des AED ?"],
             docs=[6, 7]),
        dict(nom="L'équipe", angle="Quelles contraintes sont non négociables ?",
             questions=["Combien de postes faut-il tenir chaque jour, binôme du portail compris ?", "Le planning hérité respecte-t-il les règles ? Relevez chaque erreur.", "Une organisation équitable est-elle possible ? Sinon, quel arbitrage ?"],
             docs=[2, 8]),
        dict(nom="Les demandes", angle="Que satisfaire, que refuser, comment le justifier ?",
             questions=["Quelles demandes sont compatibles avec les moyens ?", "Comment refuser une demande des professeurs sans perdre leur confiance ?", "Que répondre à M. Vidal sur le graphique ?"],
             docs=[9, 1]),
    ],
    phases=[
        dict(titre="Ma première réaction", duree=5, modalite="Individuel",
             consigne="Lisez la situation, le message de la proviseure et le planning hérité. Écrivez vos trois premières décisions pour lundi, comme si vous deviez les envoyer ce soir.",
             docs=[1, 2]),
        dict(titre="L'enquête en groupes experts", duree=25, modalite="4 groupes experts, puis groupes mixtes",
             consigne="Chaque groupe mène son enquête dans le dossier. Faites les calculs vous-mêmes : ne croyez aucune conclusion écrite dans les documents. Au bout de 15 minutes, formez des groupes mixtes.",
             dossier=True, mission=True),
        dict(titre="Je construis l'organisation", duree=20, modalite="Groupes mixtes",
             consigne="Construisez le planning de lundi. Si une règle ne peut pas être tenue, écrivez laquelle, pourquoi, et ce que vous proposez à la direction. Ajoutez au moins une action hors planning.",
             docs=[]),
        dict(titre="Le rebondissement", duree=10, modalite="Groupes mixtes",
             consigne="Lisez le document 10. Adaptez votre organisation en dix minutes, puis rédigez le message que vous envoyez à l'équipe à 7 h 45.",
             docs=[10]),
        dict(titre="Je produis", duree=10, modalite="Groupes mixtes",
             consigne="Rédigez la note d'une page à la proviseure. Vérifiez chaque critère de réussite.",
             production=True),
        dict(titre="Retour sur ma première réaction", duree=5, modalite="Individuel",
             consigne="Relisez vos trois premières décisions. Lesquelles tenez-vous encore ? Laquelle aurait aggravé la situation ?",
             rappel=True),
    ],
    cloture=[
        "Qui, dans le groupe, avait cru à la baisse de 26 % ? Qu'est-ce qui vous a fait douter ?",
        "Quelle part du problème ne relevait pas du planning ?",
        "Que présenterez-vous au conseil d'établissement si les chiffres ne baissent pas ?",
    ],
    approfondir="organisation",
    refs=["missions", "ih2ef", "toulouse_vs", "climat"],
    formateur=dict(
        materiel=["Dossier documentaire en quatre jeux", "Calculatrices", "Document 10 imprimé à part", "Grand tableau vierge du planning"],
        deroule=[
            "Écrit individuel. La plupart des stagiaires proposent de « mettre plus de monde au portail » : le noter.",
            "Ne pas révéler le jour férié ni la panne. Laisser le groupe « Les chiffres » trouver. Groupes mixtes à 20 minutes.",
            "Exiger que chaque case soit vérifiée contre le document 8. Faire nommer l'arbitrage.",
            "Distribuer le document 10 sans délai supplémentaire : la contrainte de temps fait partie de l'exercice.",
            "Deux notes lues au collectif, évaluées avec les critères.",
            "Écrit individuel, puis deux volontaires.",
        ],
        relances=[
            "« M. Vidal a raison : 45, c'est moins que 61. Pourquoi compliquer ? »",
            "« Les mêmes élèves sont toujours en retard, dit Mme Roche. Ce n'est donc pas l'organisation. »",
            "« La proviseure veut un planning, pas une réflexion sur les cars. Vous sortez de votre rôle. »",
            "« Il suffit de faire travailler Antoine un peu plus, il est disponible partout. »",
            "« Pendant l'évacuation, l'étude est vide : pourquoi garder quelqu'un à l'accueil ? »",
        ],
        attendus="""
<p><strong>Les chiffres.</strong> Retards T1 par jour de classe : S1 = 11,6 ; S2 = 12,2 (sous-estimé à cause de la panne) ; S3 = 11,25. Aucune baisse n'est démontrée : la « baisse de 26 % » est un artefact du jour férié. Présenter ce graphique au conseil d'établissement serait trompeur.</p>
<p><strong>Le terrain.</strong> 280 élèves arrivent en sept minutes par un seul portillon, avec un contrôle carnet par carnet. Le retard est d'abord structurel. Actions hors planning : ouvrir le second portillon (décision de la direction et de l'intendance), décaler l'arrivée des cars, contrôler les carnets autrement. Les « mêmes élèves » sont probablement ceux des derniers cars.</p>
<p><strong>L'équipe.</strong> Le planning hérité contient trois erreurs : Antoine tient quatre postes ; Bérénice est seule au portail malgré l'obligation de binôme ; Camille est placée à T3 où elle n'est pas disponible ; l'étude T4 n'est pas couverte. Avec le binôme, il faut tenir 13 postes alors que la règle d'équité en permet 12 : un AED doit prendre un troisième poste (avec compensation), ou le CPE tient lui-même un poste, ou la direction tranche.</p>
<p><strong>Une solution possible.</strong> T1 : Portail A + B, Cour C, Accueil D. T2 : Cour F, Étude E, Accueil B. T3 : Cantine D, Cour F, Accueil A. T4 : Portail C, Étude E, Accueil : à arbitrer (A, D ou F à un troisième poste, ou le CPE).</p>
<p><strong>Les demandes.</strong> Un AED par couloir est impossible : expliquer les moyens, proposer une alternative (surveillance partagée des couloirs avec les professeurs, zones prioritaires). Le binôme du portail répond à la demande des parents. À M. Vidal : présenter des taux par jour et l'action engagée, plutôt qu'un graphique flatteur.</p>
<p><strong>Rebondissement.</strong> Sans David : T1 et T3 sont à recomposer. Pendant l'évacuation, l'étude se vide et peut fermer ; l'accueil reste tenu pour la sécurité. Message à l'équipe : bref, factuel, avec le nouveau planning et l'heure de reprise normale.</p>""",
        vigilance=[
            "C'est l'atelier où l'on apprend à dire à sa hiérarchie que les chiffres ne disent pas ce qu'elle espère. Le travailler sans complaisance, mais aussi sans insolence.",
            "Faire repérer que la pression pour « des chiffres en baisse » pousse à des indicateurs trompeurs.",
        ],
    ),
    slides=[
        dict(t="titre", titre="Et si le problème était ailleurs ?", sous="Bilan de l'atelier 2 · Organiser et piloter la vie scolaire"),
        dict(t="deux", titre="Ce que disaient vraiment les chiffres", a=("Ce qu'on vous montrait", ["61 puis 45 retards : « -26 % »", "Un bon signe pour le conseil d'établissement"]), b=("Ce qu'il fallait calculer", ["11,6 · 12,2 · 11,25 retards par jour", "Une semaine de 4 jours, une panne de saisie", "Aucune baisse démontrée"])),
        dict(t="points", titre="Lire un indicateur", points=["Quel dénominateur ? Par jour, par élève, par semaine ?", "Quelle période ? Est-elle comparable ?", "Comment les données ont-elles été saisies ?", "Plus de signalements peut vouloir dire un meilleur repérage, pas plus de faits"]),
        dict(t="def", titre="Trianguler le diagnostic", terme="Données · observation · parole", definition="Un diagnostic de vie scolaire croise au moins trois sources : des données quantitatives, une observation directe des lieux et des moments, et la parole des élèves, des personnels et des familles. Une source seule produit une interprétation ; leur croisement produit un constat.", source="IH2EF, Piloter la vie scolaire"),
        dict(t="cle", texte="280 élèves en sept minutes par un seul portillon : ce n'est pas un problème de discipline, c'est un problème d'organisation. Le CPE regarde d'abord le système avant de regarder les élèves."),
        dict(t="etapes", titre="Agir sur le climat scolaire : sept leviers", etapes=[("1", "Stratégie d'équipe"), ("2", "Justice scolaire"), ("3", "Pédagogie et coopération"), ("4", "Prévention des violences et du harcèlement"), ("5", "Coéducation avec les familles"), ("6", "Pratiques partenariales"), ("7", "Qualité de vie à l'école")], source="Éduscol, agir sur le climat scolaire"),
        dict(t="etapes", titre="Le cycle de l'amélioration continue", etapes=[("Planifier", "Un objectif, des actions, des responsables"), ("Faire", "Mettre en œuvre sur une période définie"), ("Vérifier", "Mesurer avec les indicateurs choisis à l'avance"), ("Ajuster", "Garder, corriger ou abandonner")], source="Roue de Deming (PDCA)"),
        dict(t="deux", titre="Deux indicateurs, toujours", a=("Quantitatif", ["Retards T1 par jour de classe", "Défini avant l'action", "Comparé sur des périodes équivalentes"]), b=("Qualitatif", ["Trois questions posées à dix élèves et aux AED", "Recueil prévu à date fixe", "Pas une simple impression"])),
        dict(t="etapes", titre="Arbitrer quand tout ne tient pas", etapes=[("1. Sécurité", "Les postes qui protègent les élèves d'abord"), ("2. Continuité", "Le service minimum qui permet d'accueillir"), ("3. Équité", "Répartir la charge, compenser ce qui ne l'est pas"), ("4. Confort", "Ce qui peut attendre")]),
        dict(t="points", titre="Rendre compte à sa hiérarchie", points=["Présenter des indicateurs honnêtes, même décevants", "Accompagner le chiffre d'une action et d'une date de bilan", "Proposer à la direction ce qui relève d'elle (portillon, cars)", "Un planning est un outil, pas une politique éducative"]),
    ],
))

# ======================================================================
# ATELIER 3
# ======================================================================
ATELIERS.append(dict(
    n=3,
    titre="Animer et accompagner l'équipe AED",
    accroche="Ils étaient là avant moi : comment faire équipe sans être ni copain ni petit chef ?",
    problematique="J'arrive à la tête d'une équipe de six AED, dont certains connaissent la maison mieux que moi et contestent mes premiers changements. Comment asseoir ma légitimité, réguler les écarts et faire de cette équipe un collectif éducatif, dans un cadre d'emploi que je ne maîtrise pas encore ?",
    situation="""
<p>Deuxième semaine. Vous avez demandé aux AED d'utiliser un cahier de transmissions unique. Le lendemain, en salle de vie scolaire, Antoine vous dit devant les autres : « Ici, on a toujours fait comme ça. Mme Martel nous faisait confiance. »</p>
<p>Depuis, les signaux s'accumulent. Fabien ne transmet presque rien. Bérénice, qui débute, a été secouée par une bagarre et n'ose plus aller dans la cour. David réclame des critères pour les postes du midi. Elsa prépare un concours et demande des aménagements. Et vous découvrez que l'équipe communique par un groupe de messagerie dont vous ne faites pas partie.</p>
<p>Vendredi, vous réunissez l'équipe pour la première fois.</p>""",
    objectifs=[
        "Situer mon rôle d'organisateur du service face à la direction, employeur des AED.",
        "Repérer un texte qui ne s'applique pas aux personnels recrutés localement.",
        "Conduire un entretien de régulation fondé sur des faits, sans glisser vers le disciplinaire.",
        "Conduire une réunion qui débouche sur des décisions suivies.",
        "Traiter une atteinte à la confidentialité des données d'élèves.",
    ],
    competences=["C4", "C8"],
    blocs=["1", "4"],
    blocs_detail="1.1 (encadrer et animer l'équipe de vie scolaire) ; 1.7 (RGPD) ; 4.2 (collectif professionnel)",
    production="Ma trame d'entretien de régulation avec Antoine et la charte de transmissions de l'équipe.",
    criteres=[
        "La trame part de faits datés et observables, sans jugement sur la personne.",
        "Elle prévoit un temps où Antoine expose sa lecture de la situation.",
        "Elle se conclut par une règle, un appui et une date de point.",
        "La charte fixe au moins cinq règles, dont une sur les outils autorisés et une sur la confidentialité.",
        "Chaque règle est formulée de façon vérifiable.",
    ],
    docs=[
        dict(titre="La scène de mardi", type="Situation", html="""
<p>Mardi, 10 h 35, salle de vie scolaire. Cinq AED sont présents. Vous venez de rappeler l'usage du cahier de transmissions.</p>
<blockquote>Antoine : « Ici, on a toujours fait comme ça. Mme Martel nous faisait confiance, elle. On sait ce qu'on a à faire, on n'a pas besoin d'un cahier pour se parler. »</blockquote>
<p>Deux AED sourient. Bérénice regarde ses pieds. Le téléphone d'Antoine vibre : un message sur le groupe de l'équipe.</p>"""),
        dict(titre="L'équipe en un coup d'œil", type="Établissement", html="""
<table><thead><tr><th>AED</th><th>Ancienneté</th><th>Contrat</th><th>Ce que l'on observe</th></tr></thead><tbody>
<tr><td>Antoine (A)</td><td>3 ans</td><td>Droit local, 35 h</td><td>Très apprécié des élèves ; leader informel ; conteste les changements</td></tr>
<tr><td>Bérénice (B)</td><td>3 semaines</td><td>Droit local, 30 h</td><td>Débute ; ébranlée par une bagarre ; évite la cour</td></tr>
<tr><td>Camille (C)</td><td>1 an</td><td>Droit local, 35 h</td><td>Rigoureuse ; demande un outil commun</td></tr>
<tr><td>David (D)</td><td>2 ans</td><td>Droit local, 35 h</td><td>Conteste l'équité des postes du midi</td></tr>
<tr><td>Elsa (E)</td><td>1 an</td><td>Droit local, 30 h</td><td>Prépare un concours ; demande des aménagements</td></tr>
<tr><td>Fabien (F)</td><td>2 ans</td><td>Droit local, 35 h</td><td>Transmet peu ; présent et fiable sur ses postes</td></tr>
</tbody></table>"""),
        dict(titre="Le cadre de gestion des AED", type="Texte officiel", groupe=1, html="""
<p><strong>Circulaire du 17 septembre 2025</strong> (synthèse reformulée) : elle fixe le cadre de recrutement, d'emploi et de rémunération des assistants d'éducation recrutés en France par les établissements publics, sur le fondement du code de l'éducation. Elle précise le temps de service, le crédit d'heures de formation et l'organisation du service, notamment par le CPE dans le second degré.</p>
<p class="note"><a href="https://www.education.gouv.fr/bo/2025/Hebdo38/MENH2516443C" target="_blank" rel="noopener">Bulletin officiel n° 38 du 9 octobre 2025</a>. Document photocopié par Elsa, qui souligne le crédit d'heures pour préparer un concours.</p>"""),
        dict(titre="Extrait du contrat de travail d'Elsa", type="Établissement", groupe=1, html="""
<p><strong>Contrat de droit local</strong> conclu entre l'établissement et Mme Elsa N. (extrait).</p>
<ul>
<li>Article 2 : fonctions d'assistante d'éducation, sous l'autorité du chef d'établissement.</li>
<li>Article 4 : durée hebdomadaire de 30 heures ; horaires fixés par le planning du service de vie scolaire.</li>
<li>Article 7 : congés et absences autorisées selon le droit du travail du pays d'accueil et le règlement du personnel de l'établissement.</li>
</ul>
<p class="note">Aucun article ne mentionne de crédit d'heures de formation.</p>"""),
        dict(titre="Note de la direction sur les rôles", type="Établissement", groupe=1, html="""
<blockquote>« Le CPE organise et anime le service de vie scolaire. Les décisions relatives aux contrats, aux congés, aux avertissements et à toute procédure concernant les personnels relèvent de la proviseure, en lien avec la gestionnaire des ressources humaines. »</blockquote>"""),
        dict(titre="Comment l'équipe transmet aujourd'hui", type="Écrits professionnels", groupe=2, html="""
<table><thead><tr><th>Canal</th><th>Qui l'utilise</th><th>Ce que l'on observe</th></tr></thead><tbody>
<tr><td>Papier volant posé sur le bureau</td><td>Fabien</td><td>Souvent perdu ; jamais daté</td></tr>
<tr><td>Cahier de vie scolaire</td><td>Camille, Bérénice</td><td>Lisible, mais il reste dans le bureau : inaccessible quand le CPE est en réunion</td></tr>
<tr><td>Groupe de messagerie personnel</td><td>Toute l'équipe sauf le CPE</td><td>Rapide ; voir le document 7</td></tr>
<tr><td>Logiciel de vie scolaire</td><td>Personne</td><td>Un module « observations » existe ; aucun AED n'a été formé</td></tr>
<tr><td>Oral, « au passage »</td><td>Antoine, David</td><td>Aucune trace ; l'information se perd au changement de poste</td></tr>
</tbody></table>"""),
        dict(titre="Extraits du groupe de messagerie de l'équipe", type="Écrits professionnels", groupe=2, html="""
<p>Capture fournie par Camille, qui « n'est plus à l'aise ».</p>
<ul>
<li>Antoine : « Le boulet de 4e B a encore séché, je l'ai vu au café d'en face 😂 »</li>
<li>Fabien : « Lui c'est un cas, sa mère aussi d'ailleurs »</li>
<li>David : « Qui me remplace au portail demain ? »</li>
<li>Antoine : « Photo du carnet de la petite de 6e qui a encore oublié son mot, trop drôle »</li>
</ul>"""),
        dict(titre="Trois demandes individuelles", type="Messages", groupe=3, html="""
<ul>
<li><strong>Bérénice :</strong> « Depuis la bagarre de lundi, j'ai peur d'aller dans la cour. Je n'ose pas le dire aux autres. Est-ce que je peux rester à l'accueil ? »</li>
<li><strong>David :</strong> « Ça fait deux ans que je fais la cantine tous les jours. Je veux savoir sur quels critères on répartit les postes. »</li>
<li><strong>Elsa :</strong> « D'après la circulaire, j'ai droit à des heures pour préparer mon concours. Je voudrais être libérée le jeudi après-midi. »</li>
</ul>"""),
        dict(titre="La dernière réunion de Mme Martel", type="Écrits professionnels", groupe=4, html="""
<p><strong>Compte rendu de la réunion d'équipe du 14 mars</strong> (intégral) :</p>
<blockquote>« Réunion avec l'équipe. On a parlé des retards, de la cantine et des transmissions. Tout le monde a pu s'exprimer. Bonne ambiance. »</blockquote>
<p><strong>Ordre du jour proposé par Antoine pour vendredi :</strong> « 1. Retour à l'ancien fonctionnement. 2. Questions diverses. »</p>"""),
        dict(titre="Cartes de la réunion de vendredi", type="Simulation", groupe=4, html="""
<div class="cards">
<div class="card"><h4>Antoine</h4><p>Vous voulez rester la référence de l'équipe. Vous contestez le cahier, mais vous accepteriez un outil si on vous demande votre avis.</p></div>
<div class="card"><h4>Bérénice</h4><p>Vous ne parlez que si on vous pose une question directe. Vous n'évoquez pas votre peur devant les autres.</p></div>
<div class="card"><h4>Camille</h4><p>Vous voulez un outil unique et des consignes écrites. Vous êtes gênée par le groupe de messagerie.</p></div>
<div class="card"><h4>David</h4><p>Vous ne lâchez pas la question des critères du midi.</p></div>
<div class="card"><h4>Elsa</h4><p>Vous ramenez la discussion vers vos heures de concours.</p></div>
<div class="card"><h4>Fabien</h4><p>Vous craignez une surcharge d'écrit. Vous dites : « Moi, je suis sur le terrain, pas dans les papiers. »</p></div>
<div class="card"><h4>Observateur</h4><p>Relevez : l'objectif annoncé, la circulation de la parole, les décisions obtenues, les responsables et les échéances.</p></div>
</div>"""),
        dict(titre="Le lundi suivant, 8 h 50", type="Rebondissement", html="""
<p>La proviseure vous convoque. Une mère d'élève de 4e B lui a transmis une capture d'écran : son fils l'a photographiée sur le téléphone d'un AED, posé sur le bureau de l'accueil. On y lit le message « Le boulet de 4e B a encore séché ».</p>
<blockquote>Mme Laurent : « La famille parle de porter plainte. Je veux savoir ce que vous saviez, depuis quand, et ce que vous proposez. »</blockquote>"""),
        dict(titre="Cartes du forum-théâtre : l'entretien avec Antoine", type="Simulation", html="""
<div class="cards">
<div class="card"><h4>Carte CPE</h4><p>Objectif : rétablir l'usage d'un outil commun de transmission et faire d'Antoine un allié. Vous partez des faits, vous reconnaissez son expérience, vous ne cédez pas sur la règle.</p></div>
<div class="card"><h4>Carte Antoine</h4><p>Vous êtes blessé qu'on change les habitudes sans vous consulter. Vous vous braquez si le CPE parle d'emblée d'autorité ou de règlement. Vous vous ouvrez s'il reconnaît votre expérience et vous demande votre avis : vous proposez alors d'accompagner Bérénice.</p></div>
<div class="card"><h4>Le public</h4><p>À tout moment, un spectateur peut dire « Stop ! », prendre la place du CPE et rejouer la dernière réplique autrement. On ne remplace jamais Antoine.</p></div>
</div>"""),
    ],
    groupes=[
        dict(nom="Le cadre", angle="Qui décide quoi pour ces personnels ?",
             questions=["La circulaire de 2025 s'applique-t-elle à Elsa ? Justifiez.", "Que pouvez-vous décider seul ? Que devez-vous renvoyer à la proviseure ?", "Que répondre à Elsa, et qui doit lui répondre ?"],
             docs=[3, 4, 5]),
        dict(nom="Les écrits", angle="Qu'est-ce qu'une transmission professionnelle ?",
             questions=["Comparez les cinq canaux : lequel est sûr, traçable et accessible au bon destinataire ?", "Qu'est-ce qui pose problème dans le groupe de messagerie ? Sur quels plans (déontologie, données personnelles, sécurité) ?", "Que devez-vous faire maintenant que vous savez ?"],
             docs=[6, 7]),
        dict(nom="Les personnes", angle="Besoins individuels ou règles collectives ?",
             questions=["Que cache la demande de Bérénice ? Comment l'accompagner sans l'exposer ?", "La demande de David est-elle légitime ? Que lui proposer ?", "Antoine est-il un problème ou une ressource ?"],
             docs=[8, 2]),
        dict(nom="La réunion", angle="Comment conduire une réunion qui décide ?",
             questions=["Qu'est-ce qui manque au compte rendu de mars ?", "Faut-il accepter l'ordre du jour d'Antoine ? Que proposer à la place ?", "Quelles décisions viser vendredi, au minimum ?"],
             docs=[9, 10]),
    ],
    phases=[
        dict(titre="Ma première réaction", duree=5, modalite="Individuel",
             consigne="Lisez la situation et le document 1. Écrivez mot pour mot ce que vous répondez à Antoine, là, devant les autres. Puis écrivez ce que vous feriez dans l'heure qui suit.",
             docs=[1, 2]),
        dict(titre="L'enquête en groupes experts", duree=25, modalite="4 groupes experts, puis groupes mixtes",
             consigne="Chaque groupe mène son enquête dans le dossier. Un texte officiel figure dans le dossier : vérifiez à qui il s'applique avant de vous en servir. Groupes mixtes au bout de 15 minutes.",
             dossier=True, mission=True),
        dict(titre="La réunion d'équipe", duree=20, modalite="Simulation : 1 CPE, 6 AED, observateurs",
             consigne="Chaque joueur tire une carte du document 10 et la garde secrète. Le CPE conduit la réunion pendant 15 minutes. Il doit obtenir au moins deux décisions, chacune avec un responsable et une date. Puis l'observateur rend compte.",
             docs=[]),
        dict(titre="Le rebondissement", duree=10, modalite="Groupes mixtes",
             consigne="Lisez le document 11. Que répondez-vous à la proviseure ? Que faites-vous pour l'élève et sa famille ? Pour l'équipe ? Qu'est-ce qui ne relève pas de vous ?",
             docs=[11]),
        dict(titre="Je produis", duree=10, modalite="Binômes",
             consigne="Rédigez la trame de l'entretien de régulation avec Antoine, puis la charte de transmissions de l'équipe.",
             production=True),
        dict(titre="Retour sur ma première réaction", duree=5, modalite="Individuel",
             consigne="Relisez la phrase que vous auriez dite à Antoine. Quel effet aurait-elle eu sur lui, et sur les cinq autres ?",
             rappel=True),
    ],
    cloture=[
        "Sur quoi repose votre légitimité face à un AED plus ancien que vous ?",
        "Aviez-vous vérifié à qui s'appliquait la circulaire de 2025 ?",
        "Dans votre établissement, quels outils de transmission sont autorisés ?",
    ],
    approfondir="management",
    refs=["aed", "toulouse_aed", "ih2ef", "missions"],
    formateur=dict(
        materiel=["Dossier en quatre jeux", "Cartes du document 10 découpées, distribuées face cachée", "Document 11 imprimé à part", "Grille d'observation"],
        deroule=[
            "Recueillir trois réponses à Antoine à voix haute, sans commentaire. Les garder pour le bilan.",
            "Ne pas signaler que la circulaire ne s'applique pas. Laisser le groupe « Le cadre » le découvrir par le contrat d'Elsa.",
            "Choisir un CPE volontaire, pas le plus à l'aise. Interrompre à 15 minutes, même sans décision.",
            "Distribuer le document 11. Exiger une réponse en trois volets : élève et famille, équipe, direction.",
            "Productions en binômes ; en lire deux.",
            "Écrit individuel.",
        ],
        relances=[
            "« Antoine vous a humilié devant l'équipe. Si vous ne le recadrez pas tout de suite, vous ne serez jamais respecté. »",
            "« La circulaire est un texte officiel du ministère. Elsa a raison, non ? »",
            "« Le groupe de messagerie, c'est leur vie privée. Ça ne vous regarde pas. »",
            "« Bérénice n'a qu'à rester à l'accueil, c'est plus simple pour tout le monde. »",
            "« Vous saviez pour le groupe depuis jeudi. Pourquoi n'avez-vous rien dit à la proviseure ? »",
        ],
        attendus="""
<p><strong>Forum-théâtre.</strong> Les arrêts les plus utiles portent sur la première phrase du CPE : celles qui commencent par « Je suis le CPE » ou « Le règlement dit » ferment l'échange ; celles qui reconnaissent l'expérience d'Antoine avant de poser la règle l'ouvrent.</p>
<p><strong>Réponse immédiate à Antoine.</strong> Ne pas engager l'épreuve de force en public ni céder. Une réponse attendue : « J'entends que l'équipe fonctionnait bien. Je veux qu'on en parle tous les deux, et en réunion vendredi. D'ici là, on utilise le cahier. » Puis un entretien individuel rapide.</p>
<p><strong>Le cadre.</strong> La circulaire de 2025 concerne les AED recrutés en France sur le fondement du code de l'éducation. Elsa a un contrat de droit local qui ne prévoit pas de crédit d'heures : la circulaire ne lui ouvre aucun droit. La réponse relève de la proviseure ; le CPE peut appuyer une demande d'aménagement de planning si le service le permet.</p>
<p><strong>Les écrits.</strong> Aucun canal actuel n'est à la fois sûr, traçable et accessible : le logiciel de vie scolaire est la seule solution conforme, à condition de former l'équipe. Le groupe de messagerie pose trois problèmes : propos dégradants sur des élèves et une famille (déontologie), photo et données d'élèves sur un outil personnel (protection des données), traçabilité nulle. Dès qu'il en a connaissance, le CPE en informe la direction et met fin à l'usage de cet outil pour le service.</p>
<p><strong>Les personnes.</strong> Bérénice : entretien individuel, debriefing de l'incident, binôme dans la cour, retour progressif. David : critères explicites de rotation, publiés. Antoine : ressource possible (tutorat de Bérénice), à condition d'expliciter son rôle.</p>
<p><strong>Rebondissement.</strong> Dire la vérité à la proviseure, y compris depuis quand vous saviez. Proposer : recevoir la famille avec la direction, protéger l'élève, rappeler par écrit les règles à toute l'équipe. La suite à donner concernant l'AED relève de la proviseure et de l'employeur, pas du CPE.</p>""",
        vigilance=[
            "Le CPE n'est pas l'employeur : toute suite disciplinaire concernant un AED appartient au chef d'établissement.",
            "Ne pas laisser l'atelier tourner au procès d'Antoine : il est aussi la mémoire et une ressource de l'équipe.",
            "Le rebondissement met le stagiaire face à sa propre inaction. L'accueillir sans culpabiliser : c'est le cœur de la posture réflexive.",
        ],
    ),
    slides=[
        dict(t="titre", titre="Faire équipe sans être ni copain ni petit chef", sous="Bilan de l'atelier 3 · Animer et accompagner l'équipe AED"),
        dict(t="points", titre="Ce que vous avez dû trancher", points=["Répondre à une contestation publique, à chaud", "Un texte officiel… qui ne s'appliquait pas", "Des besoins individuels face à des règles collectives", "Un outil de l'équipe qui exposait des élèves"]),
        dict(t="deux", titre="Autorité hiérarchique et coordination fonctionnelle", a=("La proviseure", ["Autorité hiérarchique sur les personnels", "Contrats, congés, procédures, avertissements", "En lien avec l'employeur"]), b=("Le CPE", ["Organise et anime le service", "Fixe le planning et les consignes", "Accompagne, forme, régule au quotidien"]), source="Circulaire n° 2015-139 ; dans le réseau AEFE, contrats de droit local"),
        dict(t="etapes", titre="Trois sources de légitimité", etapes=[("Légale", "Celle que donne la fonction : vous l'avez dès le premier jour"), ("Traditionnelle", "Celle de l'ancienneté et des habitudes : Antoine l'a"), ("Charismatique", "Celle de la personne et de la relation : elle se construit")], source="D'après les types d'autorité décrits par Max Weber"),
        dict(t="cle", texte="La légitimité du CPE ne se gagne pas en public contre l'équipe. Elle se construit par la clarté du cadre, la cohérence des décisions et la reconnaissance du travail de chacun."),
        dict(t="etapes", titre="L'entretien de régulation : la méthode DESC", etapes=[("Décrire", "Les faits observables, datés, sans jugement"), ("Exprimer", "Ce que cela produit pour le service et pour les élèves"), ("Spécifier", "Ce que l'on attend désormais, concrètement"), ("Conséquences", "Les effets positifs attendus, l'appui proposé, la date du point")], source="Sharon et Gordon Bower, 1976"),
        dict(t="points", titre="Une réunion qui décide", points=["Un objectif annoncé dès la première minute", "Un ordre du jour fixé par le responsable, ouvert aux propositions", "Chaque point se conclut : décision, responsable, échéance", "Un compte rendu diffusé dans les 48 heures et relu au point suivant"]),
        dict(t="def", titre="Transmettre, c'est protéger", terme="Factuel · nécessaire · sécurisé", definition="Une transmission décrit des faits, au bon destinataire, par un outil validé par l'établissement. Les données d'élèves ne circulent jamais sur une messagerie personnelle : le RGPD impose finalité, minimisation et sécurité des données.", source="Référentiel de formation 2026, compétence 1.7"),
        dict(t="points", titre="Accompagner un AED qui débute", points=["Un tuteur nommé et un poste en binôme", "Un debriefing après tout incident marquant", "Un retour progressif sur les postes exposés", "Un point à quinze jours, puis à un mois"]),
        dict(t="points", titre="Ce qui ne relève pas de vous", points=["Les contrats, les congés, les droits à formation", "Toute suite disciplinaire concernant un AED", "Mais vous informez la direction de ce que vous savez, sans délai"]),
    ],
))

# ======================================================================
# ATELIER 4
# ======================================================================
ATELIERS.append(dict(
    n=4,
    titre="Comprendre les adolescents",
    accroche="Un élève « impossible » : comprendre sans excuser, tenir sans humilier.",
    problematique="Un élève de 4e met plusieurs adultes à bout et un professeur exige son exclusion de cours. Comment comprendre ce qui se joue sans excuser ni diagnostiquer, et tenir le cadre sans humilier, quand les adultes eux-mêmes ne sont pas d'accord ?",
    situation="""
<p>Noah, 13 ans, est en 4e. En trois semaines, il a cumulé quatre fiches d'incident, surtout en français et en étude. Mme Roche, sa professeure de français, vous écrit qu'elle « ne le prendra plus en cours ». Antoine, AED, est catégorique : « Il le fait exprès. » Un autre AED a lu un article et pense que « c'est sûrement un TDAH ».</p>
<p>Pourtant, en EPS, Noah est décrit comme un élève moteur. Sa mère a demandé un rendez-vous. Le conseil de classe du premier trimestre approche, et l'équipe attend votre avis.</p>""",
    objectifs=[
        "Réécrire une fiche d'incident en séparant faits, interprétations et jugements.",
        "Formuler des hypothèses alternatives et identifier les informations manquantes.",
        "Distinguer un savoir solide sur l'adolescence d'un neuromythe.",
        "Situer le rôle du CPE face à un diagnostic sauvage et au secret médical.",
        "Partager une information de santé au seul bénéfice de l'élève, sans la divulguer ni s'en servir comme excuse.",
    ],
    competences=["C5", "C2", "C8"],
    blocs=["1", "2"],
    blocs_detail="1.4 (développement de l'adolescent, suivi) ; 2.2 (diversité des élèves, équipes pluriprofessionnelles)",
    production="Une grille d'observation de deux semaines confiée aux AED et la réponse que j'adresse à Mme Roche.",
    criteres=[
        "La grille ne porte que sur des faits observables : moment, lieu, consigne donnée, réponse de l'adulte, réaction de Noah.",
        "Elle ne contient ni case de jugement, ni information de santé, ni formulation diagnostique.",
        "Elle précise qui observe, quand, et à qui la grille est remise.",
        "La réponse à Mme Roche ne la désavoue pas, ne lui donne pas raison par principe, et propose un appui concret en classe.",
        "Elle fixe une date de bilan partagé avec l'équipe.",
    ],
    docs=[
        dict(titre="Le message de Mme Roche", type="Messages", html="""
<blockquote>« Je ne prendrai plus Noah en cours. Il est insolent, provocateur, il cherche systématiquement l'affrontement et il détruit l'ambiance de la classe. Je demande une exclusion de mes cours jusqu'aux vacances. Il faut que la vie scolaire me soutienne. »</blockquote>"""),
        dict(titre="Les quatre fiches d'incident", type="Écrits professionnels", groupe=1, html="""
<table><thead><tr><th>Date</th><th>Lieu</th><th>Rédacteur</th><th>Texte de la fiche</th></tr></thead><tbody>
<tr><td>8 sept.</td><td>Étude</td><td>Antoine, AED</td><td>« Noah est sorti trois fois sans autorisation. Comportement de défi permanent. »</td></tr>
<tr><td>15 sept.</td><td>Français</td><td>Mme Roche</td><td>« Insolence. A répondu "c'est bon, lâchez-moi" après une remarque. Provocateur. »</td></tr>
<tr><td>18 sept.</td><td>Étude</td><td>Antoine, AED</td><td>« A refusé de se rasseoir. Élève ingérable. »</td></tr>
<tr><td>22 sept.</td><td>Français</td><td>Mme Roche</td><td>« A claqué la porte en sortant. Attitude inadmissible, aucune envie de travailler. »</td></tr>
</tbody></table>"""),
        dict(titre="Le relevé de vie scolaire de Noah", type="Données", groupe=1, html="""
<ul>
<li>Absences : aucune. Retards : un.</li>
<li>Passages à l'infirmerie : trois en septembre (lundi, jeudi, lundi).</li>
<li>Changement de classe à la rentrée, à la demande de la famille.</li>
<li>Bulletin de l'an dernier : « élève agréable, investi, doit gagner en confiance à l'écrit ».</li>
</ul>"""),
        dict(titre="Ce que disent les adultes", type="Témoignages", groupe=2, html="""
<ul>
<li><strong>Mme Okafor, EPS :</strong> « Noah est un moteur du groupe. Il aide les autres, il est capitaine de son équipe. Je n'ai aucun problème avec lui. »</li>
<li><strong>Antoine, AED :</strong> « Il le fait exprès, il teste. Il faut le casser tout de suite. »</li>
<li><strong>Camille, AED :</strong> « Avec moi, en étude, ça se passe bien quand je lui parle à part et que je lui montre ce qu'il doit faire. »</li>
<li><strong>Le professeur principal :</strong> « En maths ça va. Il décroche à l'écrit long. »</li>
</ul>"""),
        dict(titre="Le courriel de la mère", type="Messages", groupe=2, html="""
<blockquote>« Depuis le changement de classe, Noah dort mal et il a mal au ventre le dimanche soir. Il dit que certains profs l'ont "dans le viseur". Je voudrais comprendre ce qui se passe. Je ne veux pas qu'il soit étiqueté. »</blockquote>"""),
        dict(titre="Un article partagé en salle des professeurs", type="Article", groupe=3, html="""
<p><strong>« Le cerveau des ados n'est pas fini : voilà pourquoi ils sont insupportables »</strong> (magazine grand public, extrait reformulé).</p>
<p>L'article explique que le cortex préfrontal, siège du contrôle des impulsions, ne serait « mature qu'à 25 ans ». Il en conclut que « les ados ne peuvent pas se contrôler », qu'« il est inutile de leur demander de réfléchir avant d'agir » et que « les élèves qui provoquent ont simplement un cerveau en retard ».</p>
<p class="note">Antoine l'a affiché au tableau de la vie scolaire.</p>"""),
        dict(titre="Les compétences psychosociales", type="Ressource", groupe=3, html="""
<p><strong>Santé publique France</strong> (synthèse reformulée, référentiel 2022). Les compétences psychosociales sont un ensemble de capacités qui permettent de faire face aux situations de la vie quotidienne. Elles se répartissent en trois catégories :</p>
<ul>
<li><strong>Cognitives :</strong> avoir conscience de soi, maîtriser ses impulsions, prendre des décisions constructives.</li>
<li><strong>Émotionnelles :</strong> identifier ses émotions, les réguler, gérer son stress.</li>
<li><strong>Sociales :</strong> communiquer de façon constructive, développer des relations positives, résoudre des difficultés.</li>
</ul>
<p>Elles se développent et s'apprennent, notamment à l'école, par des pratiques éducatives explicites.</p>
<p class="note"><a href="https://www.santepubliquefrance.fr/competences-psychosociales" target="_blank" rel="noopener">Santé publique France, compétences psychosociales</a>.</p>"""),
        dict(titre="Deux propositions dans la boîte du CPE", type="Messages", groupe=4, html="""
<p><strong>D'un AED :</strong> « J'ai fait un test en ligne avec la description de Noah, ça ressort TDAH à 80 %. Il faudrait le dire à la mère pour qu'elle le fasse soigner. »</p>
<p><strong>De Mme Benali, infirmière :</strong> « Noah est venu trois fois. Je ne peux pas vous dire pourquoi, mais je pense qu'il faudrait que l'on se voie, avec la psychologue, pour réfléchir ensemble à ce qu'on peut faire pour lui. »</p>"""),
        dict(titre="Jeudi : la mère de Noah revient", type="Rebondissement", html="""
<p>La mère de Noah vous remet le compte rendu d'une psychologue libérale : « anxiété de performance, forte sensibilité au jugement d'autrui ; éviter les remarques publiques ; privilégier des consignes écrites et explicites ».</p>
<blockquote>« Je veux que tous les professeurs et tous les AED en reçoivent une copie. Et je demande que Noah soit dispensé des oraux en français. »</blockquote>
<p>Une heure plus tard, Mme Roche, qui en a entendu parler :</p>
<blockquote>« Si c'est médical, ce n'est plus mon problème. Quand ça ne va pas, qu'il aille à l'infirmerie. »</blockquote>"""),
    ],
    groupes=[
        dict(nom="Les faits", angle="Que s'est-il réellement passé ?",
             questions=["Réécrivez chaque fiche d'incident en ne gardant que les faits observables.", "Que reste-t-il de « défi permanent », « ingérable », « aucune envie » ?", "Que vous apprend le relevé sur les moments et les lieux ?"],
             docs=[2, 3]),
        dict(nom="Les regards", angle="Pourquoi les adultes ne voient-ils pas le même élève ?",
             questions=["Où et avec qui Noah va-t-il bien ? Où et avec qui va-t-il mal ?", "Qu'est-ce qui distingue les réponses de Camille et d'Antoine ?", "Que vous apprend le courriel de la mère, et que ne vous apprend-il pas ?"],
             docs=[4, 5]),
        dict(nom="Les savoirs", angle="Que sait-on vraiment de l'adolescence ?",
             questions=["Dans l'article, qu'est-ce qui est solide ? Qu'est-ce qui est abusif ?", "Quelles compétences psychosociales sont en jeu pour Noah ?", "Quel effet produit l'affichage de cet article dans la vie scolaire ?"],
             docs=[6, 7]),
        dict(nom="Les limites", angle="Qu'est-ce qui n'est pas mon rôle ?",
             questions=["Que faire de la proposition de « test TDAH » ?", "Que pouvez-vous attendre de l'infirmière, et que ne pouvez-vous pas lui demander ?", "Qui associer, et dans quel cadre ?"],
             docs=[8, 1]),
    ],
    phases=[
        dict(titre="Ma première réaction", duree=5, modalite="Individuel",
             consigne="Lisez la situation et le message de Mme Roche. Que lui répondez-vous ? Que proposez-vous pour Noah ? Écrivez-le avant toute autre lecture.",
             docs=[1]),
        dict(titre="L'enquête en groupes experts", duree=20, modalite="4 groupes experts, puis groupes mixtes",
             consigne="Chaque groupe mène son enquête. Un document du dossier contient des affirmations scientifiques abusives : repérez-les. Groupes mixtes au bout de 12 minutes.",
             dossier=True, mission=True),
        dict(titre="Le rebondissement", duree=10, modalite="Groupes mixtes",
             consigne="Lisez le document 9. Noah met en cause une adulte et vous demande de ne rien dire. Que lui répondez-vous ? Que faites-vous de cette parole ? Que ne faites-vous surtout pas ?",
             docs=[9]),
        dict(titre="La controverse", duree=10, modalite="Débat en deux camps",
             consigne="« Faut-il exclure Noah des cours de français jusqu'aux vacances ? » Défendez la position attribuée avec des éléments du dossier.",
             positions=[
                 ("Oui, il faut l'exclure", "Protéger la classe et soutenir la collègue : un adulte qui n'est pas soutenu se retire, et c'est toute la classe qui en pâtit."),
                 ("Non, il ne faut pas l'exclure", "L'exclusion confirmerait l'étiquette, nourrirait l'escalade et laisserait sans réponse ce que Noah a révélé."),
             ]),
        dict(titre="Je produis", duree=10, modalite="Binômes",
             consigne="Rédigez le plan d'action éducatif pour Noah, puis le message à Mme Roche. Vérifiez chaque critère de réussite.",
             production=True),
        dict(titre="Retour sur ma première réaction", duree=5, modalite="Individuel",
             consigne="Relisez votre première réponse. Quels mots de Mme Roche aviez-vous repris à votre compte ?",
             rappel=True),
    ],
    cloture=[
        "Quel mot d'une fiche d'incident aviez-vous pris pour un fait ?",
        "Qu'est-ce qui distingue comprendre un élève et l'excuser ?",
        "Comment soutenir une collègue sans transformer une information de santé en excuse ?",
    ],
    approfondir="adolescence",
    refs=["cps", "climat", "missions"],
    formateur=dict(
        materiel=["Dossier en quatre jeux", "Document 9 imprimé à part", "Deux affichettes pour la controverse"],
        deroule=[
            "Écrit individuel. Beaucoup reprennent « insolent » ou « provocateur » : le relever discrètement.",
            "Ne pas désigner l'article piège. Groupes mixtes à 15 minutes.",
            "Le document 9 change tout. Laisser un temps de silence, puis exiger trois réponses : à Noah, à la direction, à Mme Roche.",
            "Attribuer les positions à contre-emploi.",
            "Productions en binômes ; en lire deux, dont un message à Mme Roche.",
            "Écrit individuel.",
        ],
        relances=[
            "« Quatre fiches en trois semaines, ce sont des faits. Qu'est-ce qu'il vous faut de plus ? »",
            "« Si l'infirmière ne vous dit rien, vous ne pouvez rien faire. »",
            "« Le test dit 80 %. Ne pas prévenir la mère, c'est lui faire perdre du temps. »",
            "« La mère a le droit de demander que tout le monde soit informé : c'est son fils. »",
            "« Un compte rendu de psychologue, c'est un diagnostic : vous pouvez enfin dire aux collègues qu'il est anxieux. »",
        ],
        attendus="""
<p><strong>Les faits.</strong> Trois sorties d'étude sans autorisation ; un « c'est bon, lâchez-moi » après une remarque ; un refus de se rasseoir ; une porte claquée. Les mots « défi », « ingérable », « provocateur », « aucune envie » sont des interprétations ou des jugements. Les incidents se concentrent en français et en étude, depuis le changement de classe.</p>
<p><strong>Les regards.</strong> Noah va bien quand la consigne est explicite et la relation individuelle (EPS, Camille). Il va mal dans les situations d'écrit long et de remarque publique. Les maux du dimanche soir et les passages à l'infirmerie sont des signaux de mal-être, pas un diagnostic.</p>
<p><strong>Les savoirs.</strong> La maturation tardive du cortex préfrontal et la sensibilité au regard des pairs sont des tendances documentées à l'échelle des groupes. En conclure qu'un adolescent « ne peut pas se contrôler » ou expliquer un élève par son cerveau est abusif : c'est un neuromythe. L'affichage de l'article légitime l'étiquetage.</p>
<p><strong>Note sur les fiches.</strong> Les quatre fiches mêlent faits et verdicts : « défi permanent », « ingérable », « aucune envie » ne décrivent rien d'observable. C'est le seul atelier où l'on travaille la réécriture des écrits : y passer le temps nécessaire.</p>
<p><strong>Les limites.</strong> Le CPE ne pose pas de diagnostic et n'en suggère pas à la famille. L'infirmière est tenue au secret ; elle propose justement le bon cadre : une réunion avec la psychologue, où l'on partage ce qui est nécessaire pour agir.</p>
<p><strong>Rebondissement.</strong> Le document appartient à la famille : l'établissement ne le photocopie pas pour tout le monde. Avec l'accord de la mère, et en lien avec l'infirmière, on traduit le contenu en besoins éducatifs (pas de remarque publique, consignes écrites) transmis aux seuls adultes qui en ont besoin, sans diagnostic. Un aménagement durable relève du plan d'accompagnement prévu par l'établissement et du médecin ; une dispense d'oral est une décision pédagogique, qui ne relève pas du CPE. À Mme Roche : l'information n'est ni une excuse ni un transfert vers l'infirmerie ; la règle demeure, c'est la manière de l'exiger qui s'ajuste.</p>
<p><strong>Controverse.</strong> Pas d'exclusion des cours (ce n'est pas la compétence du CPE et ce serait une réponse sans traitement de la cause). Mais soutenir réellement la collègue : rencontre, médiation pédagogique, place dans la classe, consignes explicites.</p>""",
        vigilance=[
            "Le rebondissement oppose deux pressions : tout diffuser (la famille) et se défausser (la professeure). Le travail consiste à traduire une information de santé en besoins éducatifs, sans la divulguer.",
            "Ne jamais laisser une formulation diagnostique circuler dans la salle, même pour plaisanter.",
            "Rappeler que le secret professionnel de l'infirmière n'empêche pas le travail en équipe : il le cadre.",
        ],
    ),
    slides=[
        dict(t="titre", titre="Comprendre sans excuser, tenir sans humilier", sous="Bilan de l'atelier 4 · Comprendre les adolescents"),
        dict(t="points", titre="Ce que vous avez dû trancher", points=["Des fiches d'incident écrites comme des verdicts", "Des adultes qui ne voient pas le même élève", "Un article qui donne une caution scientifique à l'étiquette", "Une famille qui veut tout diffuser, une collègue qui veut se défausser"]),
        dict(t="etapes", titre="L'échelle d'inférence", etapes=[("Ce que j'observe", "Il sort trois fois de l'étude"), ("Ce que je sélectionne", "Il sort sans demander"), ("Ce que j'interprète", "Il teste les règles"), ("Ce que je conclus", "Il provoque volontairement"), ("Ce que je fais", "« Il faut le casser »")], source="D'après Chris Argyris"),
        dict(t="cle", texte="Plus on monte l'échelle, plus on parle de soi et moins on parle de l'élève. Une fiche d'incident professionnelle reste sur le premier barreau."),
        dict(t="deux", titre="Ce que l'on sait, ce que l'on extrapole", a=("Solide, à l'échelle des groupes", ["Le cerveau poursuit sa maturation à l'adolescence", "Le regard des pairs pèse davantage", "La variabilité individuelle est très grande"]), b=("Abusif, à l'échelle d'un élève", ["« Il ne peut pas se contrôler »", "« Son cerveau est en retard »", "« Inutile de lui demander de réfléchir »"])),
        dict(t="def", titre="Trois besoins psychologiques fondamentaux", terme="Autonomie · compétence · affiliation", definition="Selon la théorie de l'autodétermination, la motivation et le bien-être reposent sur trois besoins : se sentir à l'origine de ses actes, se sentir capable, se sentir relié aux autres. Une remarque humiliante devant la classe atteint à la fois la compétence et l'affiliation.", source="Edward Deci et Richard Ryan"),
        dict(t="etapes", titre="Les compétences psychosociales", etapes=[("Cognitives", "Conscience de soi, maîtrise des impulsions, prise de décision"), ("Émotionnelles", "Identifier, réguler ses émotions, gérer son stress"), ("Sociales", "Communiquer, coopérer, résoudre des difficultés")], source="Santé publique France, 2022"),
        dict(t="points", titre="Le CPE ne diagnostique pas", points=["Il décrit, il observe, il croise les regards", "Il n'évoque jamais un trouble devant la famille", "Il oriente vers l'infirmière, la psychologue, le médecin", "Le secret médical cadre le partage d'informations, il n'empêche pas le travail en équipe"]),
        dict(t="etapes", titre="Partager une information sensible", etapes=[("Qui en a besoin ?", "Seulement les adultes qui agissent auprès de l'élève"), ("Pour quoi faire ?", "Une adaptation concrète, pas une étiquette"), ("Sous quelle forme ?", "Des besoins éducatifs, jamais un diagnostic"), ("Avec quel accord ?", "Celui de la famille, et de l'élève selon son âge"), ("Par quel circuit ?", "Infirmière, médecin, direction ; plan d'accompagnement si nécessaire")], source="Secret professionnel partagé : le « besoin d'en connaître »"),
        dict(t="points", titre="Tenir le cadre sans humilier", points=["Le rappel à la règle se fait à l'écart, pas en public", "La consigne est explicite, montrée, vérifiée", "La réparation est possible et proposée", "Une réponse testée a une date de réévaluation"], source="Éduscol, levier « justice scolaire » du climat scolaire"),
    ],
))

# ======================================================================
# ATELIER 5
# ======================================================================
ATELIERS.append(dict(
    n=5,
    titre="Accompagner un élève et sa famille",
    accroche="Des retards, des signaux faibles, deux parents qui ne disent pas la même chose.",
    problematique="Une élève accumule les retards, ses résultats baissent, elle s'isole, et ses deux parents me donnent des versions différentes. Comment construire une alliance éducative avec la famille sans appliquer mécaniquement le règlement et sans refermer trop vite le dossier ?",
    situation="""
<p>Mila est en 3e. Depuis la rentrée, elle arrive en retard plusieurs fois par semaine. Le règlement intérieur prévoit une retenue tous les trois retards : elle en a cinq de retard, qu'elle n'a pas faites. Son professeur principal vous demande de « faire appliquer le règlement ».</p>
<p>Dans le même temps, ses résultats baissent, un AED l'a vue seule à plusieurs récréations, et la professeure d'EPS l'a vue s'endormir deux fois pendant l'échauffement. Ses parents sont séparés. Sa mère vous écrit poliment ; son père vous écrit en colère.</p>""",
    objectifs=[
        "Repérer la convergence de signaux faibles derrière un problème d'assiduité.",
        "Distinguer retard et absence, punition automatique et réponse individualisée.",
        "Distinguer une difficulté familiale à accompagner d'une situation de danger qui impose une alerte.",
        "Respecter les droits des deux parents exerçant l'autorité parentale.",
        "Conduire un entretien qui permet à l'élève de parler et de chercher elle-même des solutions.",
    ],
    competences=["C5", "C7", "C8"],
    blocs=["1", "3"],
    blocs_detail="1.4, 1.5 et 1.7 (suivi, parcours, communication) ; 3.5 (relations avec les familles) ; 3.6 (protection)",
    production="Le compte rendu factuel de l'entretien, le plan de suivi de Mila et le message adressé à ses deux parents.",
    criteres=[
        "Le compte rendu ne contient que des faits datés et des paroles rapportées entre guillemets.",
        "Le plan de suivi nomme les personnes associées, ce qu'elles font et une date de réévaluation.",
        "Le plan traite à la fois l'assiduité et les autres signaux.",
        "Le message aux parents est identique pour les deux, sans prendre parti.",
        "Le plan dit, en le justifiant, si la situation relève d'un accompagnement ou d'une alerte.",
    ],
    docs=[
        dict(titre="Le relevé d'assiduité de Mila", type="Données", groupe=2, html="""
<table class="center"><thead><tr><th>Semaine</th><th>Retards</th><th>Durée</th><th>Garde (information de la famille)</th></tr></thead><tbody>
<tr><td>2–4 sept.</td><td>0</td><td>—</td><td>Mère</td></tr>
<tr><td>7–11 sept.</td><td>5</td><td>8 à 18 min</td><td>Père</td></tr>
<tr><td>14–18 sept.</td><td>1</td><td>4 min</td><td>Mère</td></tr>
<tr><td>21–25 sept.</td><td>4</td><td>10 à 15 min</td><td>Père</td></tr>
<tr><td>28 sept.–2 oct.</td><td>5</td><td>6 à 20 min</td><td>Mère</td></tr>
</tbody></table>
<p class="note">Quinze retards en cinq semaines, tous au premier cours. Aucune absence.</p>"""),
        dict(titre="Le message du professeur principal", type="Messages", html="""
<blockquote>« Mila en est à quinze retards, donc cinq retenues, et elle n'en a fait aucune. Le règlement est clair : il faut l'appliquer, sinon on perd toute crédibilité auprès des autres élèves. Je compte sur vous pour la convoquer et mettre les retenues. »</blockquote>"""),
        dict(titre="L'article du règlement intérieur", type="Établissement", groupe=1, html="""
<blockquote>« Article 12 : tout élève en retard doit se présenter à la vie scolaire. Trois retards non justifiés donnent lieu à une retenue d'une heure le mercredi après-midi. »</blockquote>"""),
        dict(titre="La procédure française en cas d'absentéisme", type="Texte officiel", groupe=1, html="""
<p><strong>Code de l'éducation, article L131-8</strong> (synthèse reformulée). En France, lorsqu'un élève a manqué la classe sans motif légitime au moins quatre demi-journées dans le mois, le chef d'établissement saisit l'autorité académique, qui peut adresser un avertissement aux personnes responsables et engager un accompagnement.</p>
<p class="note">Fiche trouvée dans le classeur de Mme Martel, avec la mention manuscrite : « à appliquer systématiquement ».</p>"""),
        dict(titre="Les autres signaux", type="Observation", groupe=2, html="""
<ul>
<li><strong>Bulletin de mi-trimestre :</strong> moyenne générale passée de 14,2 à 10,8 ; « participation en net recul » (trois professeurs).</li>
<li><strong>Elsa, AED :</strong> « Mila est restée seule pendant trois récréations cette semaine. Avant, elle était toujours avec le même groupe de filles. »</li>
<li><strong>Mme Okafor, EPS :</strong> « Deux fois ce mois-ci, Mila s'est endormie sur le banc pendant l'échauffement. Elle dit qu'elle se couche tard. »</li>
</ul>"""),
        dict(titre="Le courriel de la mère", type="Messages", groupe=3, html="""
<blockquote>« Bonjour, je suis désolée pour les retards. Les semaines où Mila est chez son père, le trajet est plus long. Mais ces derniers temps elle traîne aussi chez moi, elle n'a plus envie d'aller au lycée et elle ne veut pas me dire pourquoi. Pouvons-nous nous rencontrer ? »</blockquote>"""),
        dict(titre="Le courriel du père", type="Messages", groupe=3, html="""
<blockquote>« Votre établissement harcèle ma fille avec des retenues pour quelques minutes de retard. Ce n'est pas elle le problème. Je vous demande de ne pas impliquer sa mère, c'est moi qui gère la scolarité. Si vous la sanctionnez, je saisis l'ambassade. »</blockquote>
<p class="note">Selon le dossier administratif, les deux parents exercent l'autorité parentale. Aucune décision de justice ne limite les droits de l'un d'eux.</p>"""),
        dict(titre="Fiche méthode : conduire un entretien", type="Ressource", groupe=4, html="""
<ol>
<li><strong>Accueillir :</strong> lieu calme, temps protégé, présentation de l'objet de l'entretien.</li>
<li><strong>Annoncer le cadre :</strong> ce qui restera entre nous, et ce que je devrai partager si j'apprends qu'un élève est en danger.</li>
<li><strong>Ouvrir :</strong> questions ouvertes (« Comment ça se passe pour toi en ce moment ? »).</li>
<li><strong>Reformuler :</strong> redire avec ses mots ce que l'on a compris, sans interpréter.</li>
<li><strong>Préciser :</strong> questions factuelles, seulement après avoir écouté.</li>
<li><strong>Conclure :</strong> ce que l'on a convenu, ce qui va se passer, la date du prochain point.</li>
</ol>"""),
        dict(titre="Cartes des entretiens", type="Simulation", groupe=4, html="""
<div class="cards">
<div class="card"><h4>Mila</h4><p>Au départ : « Je suis fatiguée des remarques sur mes retards. »</p><p>Si le CPE pose une question ouverte : « Le matin, je n'ai pas envie de venir. »</p><p>Si le CPE reformule sans juger et annonce le cadre : vous finissez par expliquer vos matins (voir le document 10, que le formateur vous remettra).</p><p>Si le CPE parle d'abord des retenues : vous vous fermez.</p></div>
<div class="card"><h4>Le père</h4><p>Vous êtes en colère et vous menacez. Vous vous apaisez si le CPE ne se justifie pas, reconnaît votre inquiétude et vous présente des faits.</p><p>Vous demandez à nouveau que la mère ne soit pas informée.</p></div>
<div class="card"><h4>Observateur</h4><p>Relevez : l'annonce du cadre, les questions ouvertes, les reformulations, ce qui a ouvert ou fermé la parole, la conclusion et la date de suivi.</p></div>
</div>"""),
        dict(titre="Ce que Mila finit par dire", type="Rebondissement", html="""
<blockquote>« Les semaines chez papa, il part travailler à 6 h. C'est moi qui emmène mon petit frère à son école, à l'autre bout de la ville, puis je cours prendre le bus. Le soir, je le garde jusqu'à 20 h. Les semaines chez maman, je n'arrive plus à me lever, je suis épuisée. Je ne veux pas que papa ait des ennuis. Et je ne veux pas que maman le sache, sinon ils vont encore se disputer. »</blockquote>"""),
    ],
    groupes=[
        dict(nom="Le cadre", angle="Que dit la règle, et s'applique-t-elle ici ?",
             questions=["L'article 12 impose-t-il des retenues automatiques ? Que devient l'individualisation ?", "La procédure de l'article L131-8 concerne-t-elle Mila ? Que traite-t-elle exactement ?", "Que faire de la mention « à appliquer systématiquement » ?"],
             docs=[3, 4, 2]),
        dict(nom="Les signaux", angle="Que disent les données quand on les croise ?",
             questions=["Les retards suivent-ils la garde alternée ? Regardez semaine par semaine.", "Quels signaux le trajet n'explique-t-il pas ?", "Quelles hypothèses devez-vous garder ouvertes ?"],
             docs=[1, 5]),
        dict(nom="La famille", angle="Avec qui construire l'alliance ?",
             questions=["Que vous apprend chaque parent ? Où se contredisent-ils ?", "Pouvez-vous accepter la demande du père de ne pas informer la mère ?", "Comment répondre à une menace sans vous justifier ni céder ?"],
             docs=[6, 7]),
        dict(nom="L'entretien", angle="Comment permettre à Mila de parler ?",
             questions=["Que dire en ouvrant l'entretien ? Que surtout ne pas dire ?", "Que lui annoncer sur la confidentialité, et à quel moment ?", "En quoi l'entretien avec le père diffère-t-il de celui avec Mila ?"],
             docs=[8, 9]),
    ],
    phases=[
        dict(titre="Ma première réaction", duree=5, modalite="Individuel",
             consigne="Lisez la situation et le message du professeur principal. Que lui répondez-vous ? Convoquez-vous Mila, et pour lui dire quoi ? Écrivez-le.",
             docs=[2]),
        dict(titre="L'enquête en groupes experts", duree=20, modalite="4 groupes experts, puis groupes mixtes",
             consigne="Chaque groupe mène son enquête. Un texte du dossier ne s'applique pas à la situation : trouvez-le. Groupes mixtes au bout de 12 minutes.",
             dossier=True, mission=True),
        dict(titre="Les entretiens", duree=20, modalite="Triades : CPE, Mila ou le père, observateur",
             consigne="Avec les cartes du document 9, jouez d'abord l'entretien avec Mila, puis celui avec le père. Changez de rôle. Si Mila se met à parler des vestiaires, le formateur vous remet le document 10.",
             docs=[]),
        dict(titre="Le rebondissement", duree=10, modalite="Groupes mixtes",
             consigne="Lisez le document 10. Mila demande que ses parents ne le sachent pas. Que lui répondez-vous ? Qui alertez-vous, dans quel ordre ? Que devient la question des retenues ?",
             docs=[10]),
        dict(titre="Je produis", duree=15, modalite="Binômes",
             consigne="Rédigez le compte rendu factuel, le plan de suivi de Mila et le message adressé à ses deux parents.",
             production=True),
        dict(titre="Retour sur ma première réaction", duree=5, modalite="Individuel",
             consigne="Relisez votre première réaction. Si vous aviez convoqué Mila pour parler des retenues, qu'aurait-elle dit ?",
             rappel=True),
    ],
    cloture=[
        "À quel moment avez-vous été tenté de refermer le dossier ?",
        "Pourquoi les retards de Mila ne suivaient-ils pas seulement la garde alternée ?",
        "Que répondez-vous désormais à un parent qui vous demande d'exclure l'autre parent ?",
    ],
    approfondir="accompagnement",
    refs=["missions", "protection", "climat"],
    formateur=dict(
        materiel=["Dossier en quatre jeux", "Cartes du document 9 par triade", "Document 10 en plusieurs exemplaires, remis seulement aux triades où Mila a parlé"],
        deroule=[
            "Écrit individuel. Beaucoup convoquent Mila « pour les retenues » : le noter.",
            "Ne pas désigner le texte piège. Groupes mixtes à 15 minutes.",
            "Circuler. Ne remettre le document 10 qu'aux triades où le CPE a ouvert la parole. Les autres le recevront à la fin : c'est un enseignement en soi.",
            "Exiger un ordre d'action précis et la réponse exacte faite à Mila.",
            "Productions en binômes ; lire un message aux parents.",
            "Écrit individuel.",
        ],
        relances=[
            "« Le règlement a été voté. Si vous ne l'appliquez pas pour Mila, vous devrez l'expliquer aux trente autres. »",
            "« Quinze retards, c'est plus que quatre demi-journées. La procédure s'applique, non ? »",
            "« Le père a la garde cette semaine. C'est à lui que vous parlez, point. »",
            "« Mila vous demande de ne rien dire à sa mère. Si vous la prévenez, elle ne vous fera plus jamais confiance. »",
            "« Une adolescente qui garde son petit frère tous les jours, c'est de la maltraitance : il faut signaler tout de suite. »",
        ],
        attendus="""
<p><strong>Le cadre.</strong> Un règlement intérieur peut prévoir une punition après trois retards, mais une application automatique sans examen de la situation contredit l'individualisation et ne traite pas la cause. L'article L131-8 vise les absences (pas les retards) et la procédure française devant l'autorité académique ; à l'étranger, elle ne s'applique pas telle quelle : vérifier la procédure de l'établissement. La mention « à appliquer systématiquement » n'a aucune valeur.</p>
<p><strong>Les signaux.</strong> Les retards ne suivent pas seulement la garde : la dernière semaine, chez la mère, en compte cinq. Le trajet explique une partie des retards, pas la baisse des résultats, l'isolement, ni l'endormissement en EPS. La convergence de ces signaux justifie de chercher ce qui se passe hors du lycée, sans conclure.</p>
<p><strong>La famille.</strong> Les deux parents exercent l'autorité parentale : l'établissement informe les deux, et ne peut pas exclure la mère à la demande du père. Répondre à la menace par des faits et une proposition de rencontre.</p>
<p><strong>Rebondissement.</strong> Mila porte chaque matin la charge de son petit frère et elle est épuisée : c'est une difficulté familiale sérieuse, pas en soi un danger qui impose une alerte immédiate. À Mila : la remercier, ne pas promettre de taire ce qui doit être traité, lui dire que l'on va chercher une solution avec ses parents sans les mettre en faute. Ensuite : informer la direction, solliciter l'infirmière et, s'il existe, le service social ou son équivalent local ; rencontrer le père sans le culpabiliser (horaires, solution de garde) ; informer les deux parents de ce qui concerne la scolarité, sans entrer dans leur conflit. Les retenues sont suspendues : elles ne sont plus le sujet. Si la situation s'aggravait (enfant laissé seul, épuisement majeur, mise en danger), elle relèverait du circuit de protection.</p>""",
        vigilance=[
            "Toute difficulté familiale n'est pas un danger : l'atelier entraîne au discernement entre accompagnement et alerte, sans minimiser ni dramatiser.",
            "Le document 10 n'est remis qu'aux triades qui ont ouvert la parole : en tirer la leçon au bilan, sans culpabiliser ceux qui ne l'ont pas obtenu.",
            "Si un stagiaire est touché par le thème, le laisser se retirer du jeu de rôle.",
        ],
    ),
    slides=[
        dict(t="titre", titre="Ne pas refermer trop vite le dossier", sous="Bilan de l'atelier 5 · Accompagner un élève et sa famille"),
        dict(t="points", titre="Ce que vous avez dû trancher", points=["Appliquer un règlement ou traiter une situation", "Une procédure nationale qui ne s'appliquait pas", "Deux parents, deux versions, une demande d'exclure l'autre", "Une révélation qui n'appelle ni le silence ni le signalement automatique"]),
        dict(t="def", titre="Les signaux faibles", terme="C'est la convergence qui alerte", definition="Un retard, une note en baisse, un moment de solitude ne disent rien seuls. Leur coïncidence dans le temps (assiduité, résultats, relations, rapport au corps) constitue un signal. Le rôle du CPE est de la repérer et de la partager avec les bonnes personnes.", source="Référentiel de formation 2026, compétences 1.4 et 1.5"),
        dict(t="deux", titre="Retard et absence ne relèvent pas des mêmes règles", a=("Le retard", ["Traité par le règlement intérieur", "Punition possible, réponse éducative à privilégier", "Toujours examiner la cause"]), b=("L'absence", ["En France : quatre demi-journées non justifiées dans le mois entraînent une saisine de l'autorité académique", "À l'étranger : procédure de l'établissement, à vérifier", "Code de l'éducation, art. L131-8"])),
        dict(t="cle", texte="Une punition automatique répond au symptôme. Elle ne dit rien de ce qui le produit, et peut fermer la seule porte par laquelle l'élève aurait parlé."),
        dict(t="points", titre="Coéducation et autorité parentale", points=["La coopération avec les parents est un principe inscrit dans la loi de refondation de l'École (2013)", "En cas de séparation, les deux parents exercent en principe l'autorité parentale", "L'établissement informe les deux, sauf décision de justice contraire", "On ne choisit pas un parent contre l'autre"]),
        dict(t="etapes", titre="L'écoute active", etapes=[("Empathie", "Comprendre le point de vue de l'autre de l'intérieur"), ("Considération", "Ne pas juger la personne, même si on juge l'acte"), ("Authenticité", "Être cohérent entre ce que l'on dit et ce que l'on fait"), ("Reformulation", "Redire pour vérifier et pour faire sentir que l'on a entendu")], source="D'après Carl Rogers"),
        dict(t="def", titre="Les élèves aidants", terme="Une charge invisible", definition="Un élève qui apporte régulièrement une aide à un proche (petit frère ou petite sœur, parent malade ou absent) peut voir sa scolarité fragilisée : fatigue, retards, isolement. Le repérer permet d'adapter et d'orienter, sans culpabiliser la famille.", source="À articuler avec les ressources sociales et de santé disponibles localement"),
        dict(t="deux", titre="Accompagner ou alerter ?", a=("Accompagner", ["Une difficulté réelle, sans danger immédiat", "Un travail avec l'élève et les deux parents", "Infirmière, service social, aménagements"]), b=("Alerter", ["Un danger ou un risque de danger pour l'élève", "La direction informée sans délai", "Le circuit de protection de l'établissement"]), source="Éduscol, protection de l'enfance"),
        dict(t="points", titre="Écrire un compte rendu professionnel", points=["Date, lieu, personnes présentes, objet", "Des faits, et des paroles rapportées entre guillemets", "Les actions décidées, les responsables, l'échéance", "Diffusé aux seules personnes qui en ont besoin pour agir"]),
    ],
))

# ======================================================================
# ATELIER 6
# ======================================================================
ATELIERS.append(dict(
    n=6,
    titre="Gérer un incident et protéger les élèves",
    accroche="Une vidéo humiliante, des parents qui exigent une exclusion, une victime qui ne veut plus venir.",
    problematique="Une vidéo humiliante circule, des parents exigent une exclusion immédiate, la proviseure veut une réponse ferme avant vendredi et l'élève visée ne veut plus venir. Comment rendre une justice scolaire qui respecte le droit, sans jamais faire passer la sanction avant la protection ?",
    situation="""
<p>Lundi, 8 h 05. Une vidéo de quinze secondes circule depuis le week-end sur les téléphones des élèves de 2nde. On y voit Inès, élève de 2nde B, filmée à son insu à la cantine pendant qu'un groupe l'imite et rit. La vidéo est accompagnée de messages insultants, dont certains visent aussi un professeur.</p>
<p>Plusieurs élèves désignent Yanis comme « celui qui a filmé ». Les parents d'Inès sont au portail : ils exigent son exclusion « dès aujourd'hui ». Inès est restée chez elle. La proviseure vous demande un point à 10 h et « une réponse ferme avant vendredi ». Sur un réseau social, un parent évoque déjà l'affaire.</p>""",
    objectifs=[
        "Choisir entre punition et sanction, et préparer une décision qui appartient au chef d'établissement.",
        "Appliquer les principes généraux du droit disciplinaire à une situation sous pression.",
        "Reconnaître une situation de harcèlement et engager une prise en charge adaptée.",
        "Situer les procédures de protection françaises et leur transposition dans un établissement à l'étranger.",
        "Protéger tous les élèves concernés, y compris celui qui est mis en cause.",
    ],
    competences=["C2", "C1"],
    blocs=["1", "3"],
    blocs_detail="1.3 (règles de vie et de droit) ; 3.6 (protection de l'enfance)",
    production="Deux arbres de décision (incident, protection) et la proposition écrite que vous remettez à la proviseure.",
    criteres=[
        "Les deux arbres sont distincts et montrent le point où l'un bascule dans l'autre.",
        "La proposition respecte les principes : légalité, contradictoire, proportionnalité, individualisation.",
        "Elle prévoit la protection d'Inès avant toute décision disciplinaire.",
        "Elle tient compte de la situation particulière de Yanis.",
        "Elle prévoit la communication : qui parle, à qui, ce qui reste confidentiel.",
    ],
    docs=[
        dict(titre="Lundi, 8 h 05 : ce que vous savez", type="Situation", html="""
<ul>
<li>Une vidéo de 15 secondes montre Inès filmée à son insu à la cantine, imitée par un groupe qui rit.</li>
<li>Des messages l'accompagnent : « la pleureuse », « elle sert à rien », et des insultes visant M. Garnier.</li>
<li>Plusieurs élèves disent que Yanis a filmé. Personne ne sait qui a diffusé en premier.</li>
<li>Selon une amie d'Inès, « ça fait des semaines qu'on se moque d'elle ».</li>
</ul>"""),
        dict(titre="Les parents d'Inès, au portail", type="Messages", html="""
<blockquote>« Notre fille ne remettra pas les pieds ici tant que ce garçon sera là. Nous exigeons son exclusion aujourd'hui. Si rien n'est fait, nous porterons plainte et nous irons voir la presse. »</blockquote>"""),
        dict(titre="Punitions et sanctions", type="Texte officiel", groupe=1, html="""
<p><strong>Code de l'éducation, article R511-13</strong> et ressources Éduscol (synthèse reformulée).</p>
<table><thead><tr><th></th><th>Punitions scolaires</th><th>Sanctions disciplinaires</th></tr></thead><tbody>
<tr><td>Pour quoi ?</td><td>Manquements mineurs aux obligations des élèves</td><td>Atteintes aux personnes et aux biens, manquements graves</td></tr>
<tr><td>Qui décide ?</td><td>Les personnels, selon le règlement intérieur</td><td>Le chef d'établissement ou le conseil de discipline</td></tr>
<tr><td>Lesquelles ?</td><td>Inscription sur le carnet, excuse, devoir supplémentaire, retenue…</td><td>Avertissement ; blâme ; mesure de responsabilisation ; exclusion temporaire de la classe (8 jours au plus) ; exclusion temporaire de l'établissement (8 jours au plus) ; exclusion définitive</td></tr>
</tbody></table>
<p>Les sanctions peuvent être assorties d'un sursis. Des mesures de prévention, de réparation et d'accompagnement peuvent les compléter.</p>
<p class="note"><a href="https://eduscol.education.gouv.fr/5043/les-procedures-disciplinaires" target="_blank" rel="noopener">Éduscol, les procédures disciplinaires</a>.</p>"""),
        dict(titre="Les principes du droit disciplinaire", type="Texte officiel", groupe=1, html="""
<ol>
<li><strong>Légalité :</strong> seules les sanctions prévues par les textes et le règlement intérieur peuvent être prononcées.</li>
<li><strong>Contradictoire :</strong> l'élève et ses représentants légaux sont informés des faits et peuvent présenter leur défense, avec un délai, avant toute sanction.</li>
<li><strong>Proportionnalité :</strong> la sanction est graduée selon la gravité des faits.</li>
<li><strong>Individualisation :</strong> elle tient compte de la situation de chaque élève et de sa part dans les faits ; pas de sanction collective.</li>
<li><strong>Non bis in idem :</strong> on ne sanctionne pas deux fois les mêmes faits.</li>
<li><strong>Motivation :</strong> la décision est écrite et motivée.</li>
</ol>
<p>Lorsqu'une procédure est engagée, le chef d'établissement peut, à titre conservatoire et si la situation l'exige, interdire temporairement l'accès de l'élève à l'établissement. Ce n'est pas une sanction.</p>"""),
        dict(titre="Le harcèlement entre élèves", type="Texte officiel", groupe=2, html="""
<p><strong>Ressources nationales</strong> (synthèse reformulée).</p>
<ul>
<li>Le harcèlement se caractérise par <strong>la répétition</strong> de propos ou de comportements, <strong>un rapport de force</strong> déséquilibré et <strong>l'isolement</strong> de la victime. Le cyberharcèlement en prolonge les effets hors de l'établissement.</li>
<li>Depuis la loi du 2 mars 2022, le harcèlement scolaire est un délit pénal en France.</li>
<li>Le programme pHARe organise la prévention et la prise en charge : équipes ressources formées, entretiens avec les élèves concernés, méthode de la préoccupation partagée, suivi de la victime.</li>
<li>La médiation entre pairs et la confrontation entre la victime et les auteurs sont déconseillées en situation de harcèlement.</li>
</ul>
<p class="note"><a href="https://www.education.gouv.fr/non-au-harcelement/phare-un-dispositif-de-lutte-contre-le-harcelement-l-ecole-323435" target="_blank" rel="noopener">Programme pHARe</a>.</p>"""),
        dict(titre="Le témoignage de l'AED", type="Témoignages", groupe=2, html="""
<blockquote>Camille : « Depuis la rentrée, à la cantine, il y a toujours le même groupe qui s'assoit près d'Inès pour la faire rire jaune. Une fois elle est partie en pleurant. J'ai cru que c'était des histoires de classe, je n'ai rien écrit. »</blockquote>"""),
        dict(titre="La protection de l'enfance en France", type="Texte officiel", groupe=3, html="""
<p><strong>Ressources Éduscol</strong> (synthèse reformulée).</p>
<ul>
<li><strong>L'information préoccupante</strong> est transmise à la cellule départementale (CRIP) lorsqu'un enfant est en danger ou en risque de l'être.</li>
<li><strong>Le signalement</strong> est adressé directement au procureur de la République en cas de danger grave ou immédiat, ou de faits pouvant constituer une infraction.</li>
<li>L'article 40 du code de procédure pénale fait obligation à tout fonctionnaire qui acquiert la connaissance d'un crime ou d'un délit d'en aviser le procureur.</li>
</ul>
<p class="note">Fiche du classeur de Mme Martel. Le lycée Horizon est situé hors de France. <a href="https://eduscol.education.gouv.fr/4350/protection-de-l-enfance" target="_blank" rel="noopener">Éduscol, protection de l'enfance</a>.</p>"""),
        dict(titre="Le protocole de l'établissement", type="Établissement", groupe=3, html="""
<p><strong>Lycée Horizon · Protocole de protection</strong> (version 2024, validée par la direction).</p>
<ol>
<li>Tout personnel informé d'une situation de danger ou de harcèlement prévient immédiatement le CPE ou la direction.</li>
<li>La direction réunit sans délai la cellule de suivi (direction, CPE, infirmière, psychologue).</li>
<li>La cellule décide des mesures de protection, de l'information des familles et des signalements aux autorités compétentes du pays et au poste consulaire si nécessaire.</li>
<li>Seule la direction communique à l'extérieur.</li>
</ol>"""),
        dict(titre="Trois pressions de la matinée", type="Messages", groupe=4, html="""
<ul>
<li><strong>Mme Laurent :</strong> « Je veux une réponse ferme et visible avant vendredi. Les parents doivent voir qu'on agit. »</li>
<li><strong>M. Garnier :</strong> « J'exige une sanction exemplaire. Je suis insulté dans cette vidéo. »</li>
<li><strong>Publication d'un parent sur un réseau social :</strong> « Au lycée Horizon, on laisse filmer et humilier nos enfants. Le harceleur s'appelle Y., en 2nde. Partagez ! »</li>
</ul>"""),
        dict(titre="Mardi, 14 h : l'entretien avec Yanis", type="Rebondissement", html="""
<blockquote>« Oui, j'ai filmé. Mais c'est les terminales qui m'ont dit de le faire, sinon ils mettaient en ligne la vidéo de moi de l'an dernier, quand ils m'avaient enfermé dans les toilettes. Je n'ai pas mis la vidéo sur le groupe. C'est Sacha qui l'a envoyée. Je ne veux pas qu'ils sachent que j'ai parlé. »</blockquote>
<p class="note">Le dossier de Yanis mentionne, l'an dernier, un « conflit avec des élèves plus âgés, réglé par une discussion ».</p>"""),
        dict(titre="Douze cartes pour la première heure", type="Outil", html="""
<div class="cards nine">
<div class="card">1 · Appeler les parents d'Inès pour organiser sa protection et son retour</div>
<div class="card">2 · Conserver une preuve datée de la vidéo, sans la diffuser</div>
<div class="card">3 · Informer la proviseure</div>
<div class="card">4 · Convoquer Yanis devant sa classe</div>
<div class="card">5 · Recevoir séparément les élèves cités</div>
<div class="card">6 · Réunir la cellule de suivi</div>
<div class="card">7 · Annoncer aux parents d'Inès que Yanis sera exclu</div>
<div class="card">8 · Répondre sur le réseau social au nom du lycée</div>
<div class="card">9 · Prévenir M. Garnier qu'il est visé et lui proposer un soutien</div>
<div class="card">10 · Demander aux AED une vigilance à la cantine</div>
<div class="card">11 · Montrer la vidéo à la classe pour la faire réagir</div>
<div class="card">12 · Consigner les faits connus, avec l'heure</div>
</div>"""),
        dict(titre="Cartes de la commission éducative", type="Simulation", html="""
<p class="note">La commission éducative examine la situation d'un élève et recherche une réponse éducative ; elle ne prononce pas de sanction. Son existence et sa composition dépendent du règlement de l'établissement.</p>
<div class="cards">
<div class="card"><h4>La proviseure</h4><p>Vous présidez. Vous rappelez l'objet de la commission et vous veillez à ce que Yanis et son parent soient entendus.</p></div>
<div class="card"><h4>Le CPE</h4><p>Vous présentez les faits établis, ceux qui restent incertains, et la situation de Yanis.</p></div>
<div class="card"><h4>Le professeur principal</h4><p>Vous décrivez Yanis en classe. Vous êtes partagé : il a filmé, mais il est en souffrance.</p></div>
<div class="card"><h4>Yanis</h4><p>Vous reconnaissez avoir filmé. Vous avez peur des terminales et vous refusez de les nommer devant tout le monde.</p></div>
<div class="card"><h4>Le parent de Yanis</h4><p>Vous défendez votre fils. Vous découvrez ce qui lui est arrivé l'an dernier et vous êtes en colère contre le lycée.</p></div>
<div class="card"><h4>Les observateurs</h4><p>Vérifiez : contradictoire, individualisation, proportionnalité, protection de Yanis, mesure éducative proposée.</p></div>
</div>"""),
    ],
    groupes=[
        dict(nom="Le droit disciplinaire", angle="Peut-on exclure Yanis aujourd'hui ?",
             questions=["Qui peut décider d'une sanction ? Selon quelle procédure, et dans quels délais ?", "Une exclusion « dès aujourd'hui » est-elle possible ? Sous quelle forme exacte ?", "Comment les principes s'appliquent-ils si plusieurs élèves sont impliqués ?"],
             docs=[3, 4]),
        dict(nom="Le harcèlement", angle="Est-ce un incident ou un harcèlement ?",
             questions=["Les trois critères du harcèlement sont-ils réunis ? Appuyez-vous sur les faits.", "Que change ce que dit Camille ?", "Pourquoi la confrontation et la médiation sont-elles exclues ?"],
             docs=[5, 6, 1]),
        dict(nom="La protection", angle="Qui alerter, ici, à l'étranger ?",
             questions=["La fiche sur la protection de l'enfance s'applique-t-elle au lycée Horizon ? En partie ?", "Que prévoit le protocole de l'établissement ? Dans quel ordre ?", "Qui est en danger dans cette situation ?"],
             docs=[7, 8]),
        dict(nom="La communication", angle="Que dire, à qui, et que taire ?",
             questions=["Que pouvez-vous dire aux parents d'Inès ? Que ne pouvez-vous pas leur dire ?", "Que faire de la publication qui nomme un élève ?", "Que répondre à la proviseure qui veut une réponse « visible » ?"],
             docs=[9, 2, 8]),
    ],
    phases=[
        dict(titre="Ma première réaction", duree=5, modalite="Individuel",
             consigne="Lisez la situation, ce que vous savez et le message des parents. Il est 8 h 10. Écrivez vos cinq premières actions, dans l'ordre, et ce que vous dites aux parents au portail.",
             docs=[1, 2]),
        dict(titre="L'enquête en groupes experts", duree=30, modalite="4 groupes experts, puis groupes mixtes",
             consigne="Chaque groupe mène son enquête dans le dossier. Une fiche du dossier décrit des procédures qui ne s'appliquent pas directement au lycée Horizon : à vous de dire pourquoi. Groupes mixtes au bout de 18 minutes.",
             dossier=True, mission=True),
        dict(titre="Le rebondissement", duree=15, modalite="Groupes mixtes",
             consigne="Lisez le document 10. Yanis est-il auteur, victime, ou les deux ? Que change ce qu'il dit pour la sanction, pour sa protection, pour l'enquête ?",
             docs=[10]),
        dict(titre="Je produis", duree=20, modalite="Groupes mixtes",
             consigne="Dessinez les deux arbres de décision, puis rédigez la proposition que vous remettez à la proviseure mercredi matin.",
             production=True),
        dict(titre="La confrontation", duree=15, modalite="Simulation : CPE et direction face aux parents",
             consigne="Un groupe joue les parents d'Inès, un autre le CPE et la proviseure. Les parents exigent de savoir quelle sanction aura « le coupable ». Le CPE doit tenir le cadre et la confidentialité sans perdre leur confiance.",
             positions=[
                 ("Les parents d'Inès", "Vous exigez des noms, une sanction immédiate et des garanties. Vous menacez de la presse."),
                 ("Le CPE et la proviseure", "Vous protégez Inès, vous expliquez la procédure, vous ne citez aucun autre élève et vous ne promettez pas de sanction."),
             ]),
        dict(titre="Retour sur ma première réaction", duree=5, modalite="Individuel",
             consigne="Relisez vos cinq premières actions. Où était Inès dans votre liste ? Qu'auriez-vous dit aux parents ?",
             rappel=True),
    ],
    cloture=[
        "Dans votre première liste, la protection d'Inès venait-elle avant la sanction ?",
        "Qu'est-ce qui distingue une réponse ferme d'une réponse rapide ?",
        "Dans votre établissement, qui compose la cellule de suivi et qui communique à l'extérieur ?",
    ],
    approfondir="accompagnement",
    refs=["discipline", "phare", "protection", "climat"],
    formateur=dict(
        materiel=["Dossier en quatre jeux", "Document 10 imprimé à part", "Grandes feuilles pour les arbres de décision"],
        deroule=[
            "Écrit individuel. Compter combien de listes commencent par Yanis et combien par Inès.",
            "Ne pas désigner la fiche piège. Exiger des réponses appuyées sur les documents. Groupes mixtes à 20 minutes.",
            "Le document 10 brouille la distinction entre auteur et victime. Laisser le malaise s'installer.",
            "Arbres affichés et comparés ; propositions lues.",
            "Le groupe des parents doit être pressant. Arrêter si la tension devient personnelle.",
            "Écrit individuel.",
        ],
        relances=[
            "« Les parents ont raison : si on ne l'exclut pas aujourd'hui, Inès ne reviendra pas. »",
            "« Vous êtes fonctionnaire : l'article 40 vous oblige à saisir le procureur. Qu'attendez-vous ? »",
            "« Une médiation entre Inès et Yanis réglerait tout en une heure. »",
            "« Yanis a filmé : peu importe pourquoi, il est coupable. »",
            "« La publication sur le réseau social n'est pas notre affaire, c'est hors de l'établissement. »",
        ],
        attendus="""
<p><strong>Les douze cartes.</strong> Ordre attendu : 3, 2 et 12 dans les premières minutes, puis 1, 6, 5, 9 et 10. Cartes à rejeter : 4 (humiliation publique), 7 (promesse d'une sanction qui ne relève pas du CPE), 8 (seule la direction communique), 11 (nouvelle diffusion de l'humiliation).</p>
<p><strong>Commission éducative.</strong> Une issue réussie : la responsabilité de Yanis est reconnue, une mesure de responsabilisation ou de réparation est proposée, sa protection devient une priorité, et l'enquête sur les commanditaires est confiée à la direction. Une issue ratée : Yanis est sommé de nommer les terminales en séance.</p>
<p><strong>Ordre attendu.</strong> 1) Inès : contacter la famille pour sa sécurité et son retour, proposer un accueil protégé. 2) Préserver les preuves (sans diffuser la vidéo). 3) Informer la direction et réunir la cellule. 4) Établir les faits. 5) Seulement ensuite, la question disciplinaire.</p>
<p><strong>Le droit disciplinaire.</strong> Seul le chef d'établissement (ou le conseil de discipline) prononce une sanction, après une procédure contradictoire. Une exclusion « dès aujourd'hui » n'est possible que sous la forme d'une mesure conservatoire, dans le cadre d'une procédure engagée ; ce n'est pas une sanction. Individualisation : la part de chaque élève (filmer, diffuser, commanditer, commenter) est distincte.</p>
<p><strong>Le harcèlement.</strong> Répétition (depuis la rentrée), rapport de force (un groupe contre une élève), isolement : les critères sont réunis. Camille aurait dû écrire : c'est un enseignement pour l'équipe. Pas de confrontation ni de médiation.</p>
<p><strong>La protection.</strong> La fiche française décrit les procédures (CRIP, procureur, article 40) valables en France. Le lycée Horizon applique son protocole : cellule de suivi, autorités compétentes du pays, poste consulaire si nécessaire. Le CPE ne décide pas seul d'un signalement. Les personnes en danger : Inès, mais aussi Yanis, sous la menace d'élèves plus âgés.</p>
<p><strong>Rebondissement.</strong> Yanis est à la fois auteur et victime. Il reste responsable de ce qu'il a fait, mais l'individualisation impose d'en tenir compte, et sa protection devient elle aussi prioritaire. Son « conflit réglé par une discussion » l'an dernier ressemble à un harcèlement non traité.</p>
<p><strong>Communication.</strong> Aux parents d'Inès : ce qui est fait pour protéger leur fille, la procédure en cours, sans aucun nom ni sanction annoncée. La publication qui nomme un mineur : à signaler, la direction s'en charge.</p>""",
        vigilance=[
            "C'est l'atelier le plus exposé émotionnellement. Annoncer en début de séance que l'on peut se retirer d'un jeu de rôle.",
            "Ne jamais projeter ni décrire une vidéo réelle.",
            "Ne pas laisser croire que le CPE décide d'un signalement : il alerte, la direction et la cellule décident.",
        ],
    ),
    slides=[
        dict(t="titre", titre="La protection avant la sanction", sous="Bilan de l'atelier 6 · Gérer un incident et protéger les élèves"),
        dict(t="points", titre="Ce que vous avez dû trancher", points=["Des parents qui exigent une exclusion le jour même", "Une direction qui veut une réponse « visible »", "Une fiche de procédures… françaises", "Un auteur présumé qui est aussi une victime"]),
        dict(t="etapes", titre="Trois raisonnements à mener dans l'ordre", etapes=[("1. Protéger", "Qui est en danger ? Que faire dans l'heure ?"), ("2. Établir les faits", "Qui a fait quoi ? Avec quelles preuves ?"), ("3. Décider", "Quelles suites éducatives, quelle procédure disciplinaire, par qui ?")]),
        dict(t="deux", titre="Punition ou sanction ?", a=("Punition scolaire", ["Manquement mineur", "Décidée par les personnels", "Retenue, devoir, excuse…"]), b=("Sanction disciplinaire", ["Atteinte aux personnes, faits graves", "Décidée par le chef d'établissement ou le conseil de discipline", "Six sanctions, de l'avertissement à l'exclusion définitive"]), source="Code de l'éducation, art. R511-13"),
        dict(t="etapes", titre="Les principes du droit disciplinaire", etapes=[("Légalité", "Seules les sanctions prévues"), ("Contradictoire", "L'élève est entendu avant"), ("Proportionnalité", "Graduée selon la gravité"), ("Individualisation", "La part de chacun, sa situation"), ("Non bis in idem", "Pas deux sanctions pour les mêmes faits"), ("Motivation", "Une décision écrite et motivée")], source="Éduscol, les procédures disciplinaires"),
        dict(t="cle", texte="Une réponse ferme n'est pas une réponse rapide. C'est une réponse juste, fondée sur des faits établis, prononcée par l'autorité compétente, et accompagnée de la protection des victimes."),
        dict(t="def", titre="Le harcèlement", terme="Répétition · rapport de force · isolement", definition="Le harcèlement entre pairs se distingue du conflit par la répétition des atteintes, un rapport de force déséquilibré et l'isolement de la victime. Cette définition, issue des travaux du psychologue Dan Olweus, fonde les dispositifs actuels. En France, le harcèlement scolaire est un délit depuis la loi du 2 mars 2022.", source="Programme pHARe"),
        dict(t="points", titre="Prendre en charge un harcèlement", points=["Protéger et écouter la victime, organiser son retour", "Recevoir séparément les élèves impliqués : la méthode de la préoccupation partagée", "Jamais de confrontation, pas de médiation", "Suivre dans la durée et vérifier que cela a cessé"], source="Programme pHARe ; méthode d'Anatol Pikas"),
        dict(t="deux", titre="Protection : en France et à l'étranger", a=("En France", ["Information préoccupante à la CRIP", "Signalement au procureur en cas de danger grave", "Article 40 du code de procédure pénale"]), b=("Au lycée Horizon", ["Protocole de l'établissement", "Cellule de suivi réunie par la direction", "Autorités du pays, poste consulaire si nécessaire"]), source="À vérifier dans chaque établissement du réseau"),
        dict(t="points", titre="Communiquer en situation de crise", points=["Une seule voix vers l'extérieur : la direction", "Aux familles : ce qui est fait pour leur enfant, jamais les noms des autres", "Ne promettre aucune sanction avant la fin de la procédure", "Signaler les publications qui exposent un mineur"]),
    ],
))

# ======================================================================
# ATELIER 7
# ======================================================================
ATELIERS.append(dict(
    n=7,
    titre="Faire vivre la démocratie scolaire",
    accroche="Les élus veulent un projet, la direction des garanties, les élèves n'y croient plus.",
    problematique="Les élus du CVL veulent porter un projet, la direction pose des conditions, un élu parle de bloquer le lycée et la plupart des élèves ne croient plus aux instances. Comment accompagner une participation réelle, sans la confisquer ni la laisser déraper ?",
    situation="""
<p>Octobre. Le nouveau CVL vient d'être élu avec 18 % de participation. Les élus veulent créer un espace calme. Ils ont lancé seuls un questionnaire et en présentent fièrement les résultats.</p>
<p>L'an dernier, le CVL avait obtenu la promesse de casiers. Ils n'ont jamais été installés, et beaucoup d'élèves en parlent encore. Cette semaine, un élu propose, si la direction refuse, de « bloquer l'entrée du lycée lundi pour se faire entendre ». Au collège, une élue du CVC demande que les collégiens soient associés. Un professeur vous glisse : « Les délégués, c'est pour faire joli. »</p>
<p>La réunion du CVL avec la direction a lieu dans dix jours.</p>""",
    objectifs=[
        "Situer les droits d'expression, de réunion, d'association et de publication des lycéens, et leurs limites.",
        "Lire une consultation avec rigueur : formulation, taux de réponse, représentativité.",
        "Comprendre ce qui fait perdre confiance dans les instances et comment la restaurer.",
        "Distinguer propositions des élèves et décisions des instances compétentes.",
        "Accompagner les élus sans décider à leur place.",
    ],
    competences=["C6", "C3"],
    blocs=["1", "3"],
    blocs_detail="1.6 (citoyenneté participative, engagement des élèves) ; 3.1 (principes et valeurs de la République)",
    production="Le questionnaire réécrit et testé, et la feuille de route des élus jusqu'à la réunion avec la direction.",
    criteres=[
        "Le questionnaire réécrit pose une question neutre, ouverte à tous les niveaux, et a résisté au crash-test d'un autre groupe.",
        "Elle associe les collégiens par leurs propres instances.",
        "Elle distingue ce que les élus proposent et ce que l'instance compétente décide.",
        "Elle prévoit un retour aux élèves, quelle que soit la réponse de la direction.",
        "Elle propose aux élus une forme d'action légitime à la place du blocage.",
    ],
    docs=[
        dict(titre="La demande des élus", type="Messages", html="""
<blockquote>« Bonjour, nous voulons créer un espace calme pour les lycéens. Le questionnaire montre que c'est ce que veulent les élèves. Pouvez-vous nous aider à le présenter à la direction ? »</blockquote>"""),
        dict(titre="Le message de Tom, élu de 1re", type="Messages", html="""
<blockquote>« Si la direction dit non comme l'an dernier pour les casiers, on bloque l'entrée lundi. On a déjà 40 élèves d'accord sur le groupe. C'est notre droit de manifester. »</blockquote>"""),
        dict(titre="Les droits des lycéens", type="Texte officiel", groupe=1, html="""
<p><strong>Code de l'éducation</strong> (synthèse reformulée). Les lycéens disposent, dans le respect du pluralisme et du principe de neutralité, de la liberté d'information et d'expression. Ils exercent des droits de réunion, d'association et de publication.</p>
<ul>
<li>Les réunions se tiennent en dehors des heures de cours, avec l'accord du chef d'établissement sur les conditions.</li>
<li>Les publications lycéennes peuvent être diffusées librement ; leurs auteurs en sont responsables. Elles ne doivent pas porter atteinte aux droits d'autrui ni à l'ordre public, ni être injurieuses ou diffamatoires.</li>
<li>L'exercice de ces droits ne peut porter atteinte aux activités d'enseignement, à la sécurité ni à la liberté d'autrui.</li>
</ul>"""),
        dict(titre="Le rôle des instances", type="Établissement", groupe=1, html="""
<p><strong>Lycée Horizon · Instances</strong> (extrait du règlement, fictif).</p>
<ul>
<li>Le <strong>CVL</strong> formule des avis et des propositions sur la vie lycéenne. Il est présidé par la proviseure ; le CPE accompagne les élus.</li>
<li>Le <strong>CVC</strong> joue le même rôle pour les collégiens.</li>
<li>Le <strong>conseil d'établissement</strong> délibère sur le règlement intérieur, l'organisation et les questions budgétaires, selon les règles fixées par l'AEFE.</li>
</ul>
<p class="note"><a href="https://www.aefe.gouv.fr/fr/ressources-documentaires/circulaire-relative-lorganisation-et-au-fonctionnement-des-instances-des" target="_blank" rel="noopener">Circulaire AEFE relative aux instances</a> : à vérifier selon le statut de l'établissement.</p>"""),
        dict(titre="Le questionnaire des élus", type="Données", groupe=2, html="""
<p><strong>Question posée :</strong> « Êtes-vous d'accord pour qu'on ait ENFIN un espace calme au lycée, comme dans tous les bons lycées ? »</p>
<table class="center"><thead><tr><th>Réponse</th><th>Nombre</th></tr></thead><tbody>
<tr><td>Oui</td><td>87</td></tr><tr><td>Non</td><td>9</td></tr><tr><td>Sans avis</td><td>4</td></tr>
</tbody></table>
<p>Diffusé sur le groupe de messagerie des élus de terminale. 100 réponses sur 300 lycéens. Les élus concluent : « 87 % des lycéens veulent un espace calme. »</p>"""),
        dict(titre="La participation aux élections", type="Données", groupe=2, html="""
<table class="center"><thead><tr><th>Élection</th><th>Inscrits</th><th>Votants</th><th>Participation</th></tr></thead><tbody>
<tr><td>CVL, l'an dernier</td><td>290</td><td>110</td><td>38 %</td></tr>
<tr><td>CVL, cette année</td><td>300</td><td>54</td><td>18 %</td></tr>
</tbody></table>"""),
        dict(titre="Le dernier compte rendu du CVL", type="Établissement", groupe=3, html="""
<p><strong>CVL du 12 mai</strong> (extrait).</p>
<blockquote>« Les élus demandent l'installation de casiers. La direction indique que le projet est intéressant et qu'il sera étudié. »</blockquote>
<p class="note">Aucune suite écrite. Le projet n'apparaît dans aucun compte rendu du conseil d'établissement.</p>"""),
        dict(titre="Ce que disent les élèves", type="Témoignages", groupe=3, html="""
<ul>
<li>« Le CVL, ça sert à rien, ils promettent et rien ne se passe. »</li>
<li>« On n'a jamais su ce qu'ils avaient dit à la direction. »</li>
<li>« Je n'ai pas voté, je ne savais même pas qui se présentait. »</li>
<li>Une élue du CVC : « Les collégiens aussi ont besoin d'un endroit calme. Pourquoi c'est toujours les lycéens qui décident ? »</li>
</ul>"""),
        dict(titre="Le message de la direction", type="Messages", groupe=4, html="""
<blockquote>M. Vidal : « Un espace calme, pourquoi pas, mais je n'ai pas de salle libre, pas de budget voté et des contraintes de surveillance. Je ne veux pas d'une nouvelle déception comme les casiers. Qu'ils viennent avec un projet sérieux. »</blockquote>
<p class="note">Le conseil d'établissement qui vote le budget se réunit le 20 novembre.</p>"""),
        dict(titre="Cartes de la répétition", type="Simulation", groupe=4, html="""
<div class="cards">
<div class="card"><h4>L'élu ou l'élue</h4><p>Vous présentez le projet d'espace calme en deux minutes : le besoin, ce que disent les élèves, ce que vous demandez exactement.</p></div>
<div class="card"><h4>M. Vidal</h4><p>Vous interrompez une fois avec une objection : salle, budget, surveillance ou « comme les casiers ». Vous ne promettez rien.</p></div>
<div class="card"><h4>Le CPE coach</h4><p>Vous ne parlez pas pendant la présentation. Après : deux points forts, une question, une suggestion. Vous ne réécrivez pas le discours à la place de l'élu.</p></div>
</div>"""),
        dict(titre="Vendredi : le journal lycéen", type="Rebondissement", html="""
<p>Le journal lycéen, animé par deux élus, publie un article intitulé « Cantine : on nous empoisonne ? ». Il cite nommément le cuisinier, affirme sans preuve que « des produits périmés sont servis » et appelle à « boycotter la cantine lundi ».</p>
<p>Le gestionnaire exige que le CPE « fasse retirer le journal ». Le cuisinier est en arrêt depuis la parution.</p>"""),
    ],
    groupes=[
        dict(nom="Le cadre", angle="Que peuvent faire les élus, et où est la limite ?",
             questions=["Le blocage de l'entrée est-il un droit des lycéens ? Justifiez avec le document 3.", "Que peuvent faire les élus pour se faire entendre ?", "Qui décide de l'espace calme ? Qui donne un avis ?"],
             docs=[3, 4, 2]),
        dict(nom="Les chiffres", angle="Que vaut le questionnaire ?",
             questions=["Relevez tous les biais du questionnaire : formulation, diffusion, taux de réponse.", "Les élus peuvent-ils dire « 87 % des lycéens » ? Que peuvent-ils dire ?", "Que dit la participation aux élections ?"],
             docs=[5, 6]),
        dict(nom="La confiance", angle="Pourquoi les élèves n'y croient-ils plus ?",
             questions=["Qu'est-ce qui a manqué après le CVL de mai ?", "Que demandent, au fond, les élèves interrogés ?", "Que faire pour les collégiens ?"],
             docs=[7, 8]),
        dict(nom="Les contraintes", angle="Que faut-il savoir avant la réunion ?",
             questions=["Quelles informations les élus doivent-ils obtenir, et de qui ?", "Le calendrier du conseil d'établissement change-t-il la stratégie ?", "Comment éviter « une nouvelle déception » ?"],
             docs=[9, 4]),
    ],
    phases=[
        dict(titre="Ma première réaction", duree=10, modalite="Individuel",
             consigne="Lisez la situation, la demande des élus et le message de Tom. Que répondez-vous aux élus ? Et à Tom ? Écrivez-le.",
             docs=[1, 2]),
        dict(titre="L'enquête en groupes experts", duree=15, modalite="4 groupes experts, puis groupes mixtes",
             consigne="Chaque groupe mène son enquête. Ne reprenez aucune conclusion des élus sans l'avoir vérifiée. Groupes mixtes au bout de 10 minutes.",
             dossier=True, mission=True),
        dict(titre="La réunion avec la direction", duree=15, modalite="Simulation : élus, M. Vidal, CPE, observateur",
             consigne="Chaque joueur reçoit une carte du document 10. La réunion dure 10 minutes. L'observateur rend compte : qui a parlé, qui a décidé, qu'est-ce qui a été promis ?",
             docs=[]),
        dict(titre="Le rebondissement", duree=10, modalite="Groupes mixtes",
             consigne="Lisez le document 11. Faut-il retirer le journal ? Qui peut le décider ? Que faites-vous avec les rédacteurs, avec le cuisinier, avec les élèves ?",
             docs=[11]),
        dict(titre="Je produis", duree=5, modalite="Groupes mixtes",
             consigne="Rédigez la feuille de route des élus et le plan de retour aux élèves.",
             production=True),
        dict(titre="Retour sur ma première réaction", duree=5, modalite="Individuel",
             consigne="Relisez ce que vous aviez répondu aux élus et à Tom. Leur aviez-vous laissé une place, ou aviez-vous décidé pour eux ?",
             rappel=True),
    ],
    cloture=[
        "Qu'avez-vous failli décider à la place des élus ?",
        "Que pouvez-vous dire, et ne pas dire, à partir de 100 réponses volontaires ?",
        "Dans votre établissement, que sont devenues les dernières propositions des élus ?",
    ],
    approfondir=None,
    refs=["democratie", "aefe_instances", "missions"],
    formateur=dict(
        materiel=["Dossier en quatre jeux", "Cartes du document 10", "Document 11 imprimé à part"],
        deroule=[
            "Écrit individuel. Repérer ceux qui interdisent le blocage sans proposer d'alternative.",
            "Groupes mixtes à 10 minutes. Exiger le calcul des biais du questionnaire.",
            "Réunion jouée devant le groupe. Arrêter à 10 minutes.",
            "Le document 11 oppose liberté de publication et atteinte à une personne : faire nommer les deux.",
            "Production rapide ; elle sera reprise dans le carnet.",
            "Écrit individuel.",
        ],
        relances=[
            "« Le blocage est une manifestation. Le droit de manifester est constitutionnel. Vous allez l'interdire ? »",
            "« 87 %, c'est massif. Pourquoi chipoter ? »",
            "« Les collégiens compliquent tout. Le projet est porté par le CVL, point. »",
            "« La direction n'a pas d'argent. Autant dire tout de suite aux élus que c'est impossible. »",
            "« Le journal est diffamatoire : le CPE doit le confisquer immédiatement. »",
        ],
        attendus="""
<p><strong>Crash-test.</strong> Une question recevable : « Parmi ces projets, lequel vous semble le plus utile pour la vie au lycée ? Espace calme · Accueil des nouveaux élèves · Cantine · Autre (précisez) », diffusée à tous les niveaux et au collège par le CVC, avec le nombre de réponses affiché.</p>
<p><strong>Le cadre.</strong> Les droits des lycéens ne permettent pas d'empêcher l'accès au lycée : l'exercice de ces droits ne doit porter atteinte ni aux enseignements, ni à la sécurité, ni à la liberté d'autrui. Le CPE n'interdit pas seulement : il propose des formes légitimes (pétition, motion au CVL, publication, réunion d'information, présentation au conseil d'établissement).</p>
<p><strong>Les chiffres.</strong> Question orientée (« ENFIN », « comme dans tous les bons lycées »), diffusion limitée aux terminales, réponses volontaires, 100 sur 300 : rien ne permet de parler au nom des lycéens. On peut dire que 87 des 100 répondants, majoritairement en terminale, sont favorables. Une consultation neutre, ouverte à tous les niveaux et au collège via le CVC, est nécessaire.</p>
<p><strong>La confiance.</strong> Le projet de casiers est mort faute de suite écrite et de retour aux élèves. La participation s'effondre quand la parole ne produit rien de visible. Il faut une boucle de retour : ce qui a été demandé, ce qui a été répondu, pourquoi.</p>
<p><strong>Les contraintes.</strong> Obtenir avant la réunion : salle possible, coût, surveillance, calendrier du conseil d'établissement du 20 novembre. Viser une proposition présentable à cette date.</p>
<p><strong>Rebondissement.</strong> La liberté de publication engage la responsabilité des auteurs ; les propos sans preuve visant nommément une personne peuvent être diffamatoires. Le chef d'établissement peut suspendre ou interdire la diffusion d'une publication qui porte gravement atteinte aux droits d'autrui ; ce n'est pas au CPE de « confisquer ». Le CPE reçoit les rédacteurs pour travailler la vérification des faits et le droit de réponse, et alerte la direction sur la situation du cuisinier.</p>""",
        vigilance=[
            "Les stagiaires oscillent entre « tout interdire » et « laisser faire » : la posture attendue est l'accompagnement exigeant.",
            "Les règles précises sur les publications et les instances dépendent du statut de l'établissement AEFE : à vérifier.",
        ],
    ),
    slides=[
        dict(t="titre", titre="Une participation qui ne soit pas décorative", sous="Bilan de l'atelier 7 · Faire vivre la démocratie scolaire"),
        dict(t="points", titre="Ce que vous avez dû trancher", points=["Un projet porté par un questionnaire biaisé", "Une menace de blocage au nom du droit de manifester", "Une instance discréditée par une promesse non tenue", "Une publication qui met en cause nommément une personne"]),
        dict(t="etapes", titre="L'échelle de la participation", etapes=[("Manipulation", "Les adultes utilisent la parole des élèves"), ("Décoration", "Les élèves sont présents, sans pouvoir réel"), ("Consultation", "On demande leur avis, sans retour"), ("Partenariat", "Les élèves proposent, les adultes répondent et expliquent"), ("Initiative", "Les élèves portent un projet de bout en bout")], source="D'après Sherry Arnstein (1969) et Roger Hart (1992)"),
        dict(t="cle", texte="Ce qui tue la participation, ce n'est pas le refus : c'est le silence. Une réponse négative expliquée vaut mieux qu'une promesse sans suite."),
        dict(t="def", titre="Les droits des lycéens", terme="Expression · réunion · association · publication", definition="Les lycéens disposent de la liberté d'information et d'expression, dans le respect du pluralisme et de la neutralité. Ces droits ne peuvent porter atteinte ni aux enseignements, ni à la sécurité, ni aux droits d'autrui. Bloquer l'accès au lycée n'en fait pas partie.", source="Code de l'éducation"),
        dict(t="points", titre="Lire une consultation", points=["La question est-elle neutre ?", "Qui a pu répondre ? Qui n'a pas pu ?", "Combien ont répondu, sur combien ?", "Les réponses volontaires surreprésentent les plus motivés"]),
        dict(t="deux", titre="Proposer et décider", a=("Les élus du CVL et du CVC", ["Consultent leurs camarades", "Formulent des avis et des propositions", "Rendent compte aux élèves"]), b=("Les instances compétentes", ["Le conseil d'établissement délibère", "La direction met en œuvre", "Selon les règles de l'AEFE et du statut de l'établissement"]), source="Circulaire AEFE relative aux instances"),
        dict(t="points", titre="Le CPE accompagne sans confisquer", points=["Il forme les élus : consulter, argumenter, rendre compte", "Il fait préciser qui décide de quoi, et quand", "Il ne porte pas le projet à leur place", "Il propose des formes d'action légitimes plutôt que d'interdire seulement"]),
        dict(t="points", titre="Une publication lycéenne responsable", points=["Les auteurs sont responsables de ce qu'ils publient", "Pas d'injure, pas de diffamation, pas d'atteinte aux droits d'autrui", "Le chef d'établissement peut en suspendre la diffusion en cas d'atteinte grave", "Le CPE accompagne : vérifier les faits, offrir un droit de réponse"]),
    ],
))

# ======================================================================
# ATELIER 8
# ======================================================================
ATELIERS.append(dict(
    n=8,
    titre="Une matinée dans la peau du CPE",
    accroche="Tout arrive en même temps : sur quels critères je décide, et comment j'en rends compte ?",
    problematique="Six événements se télescopent en une matinée, avec des informations incomplètes et des demandes contradictoires. Sur quels critères décider, que déléguer, que refuser, et comment rendre compte de mes choix ?",
    situation="""
<p>Un jeudi d'octobre. Vous êtes seul à la vie scolaire jusqu'à 11 h : M. Vidal est en réunion à l'extérieur et la proviseure reçoit des inspecteurs. Votre équipe d'AED est celle que vous connaissez.</p>
<p>Les événements vont arriver un par un, au signal du formateur. Vous n'aurez pas le temps de tout traiter. Vous aurez à rendre compte de vos choix.</p>""",
    objectifs=[
        "Prioriser des événements simultanés selon des critères explicites.",
        "Repérer une demande qui excède ses droits, même venant d'un collègue.",
        "Décider dans l'incertitude et tracer ses décisions.",
        "Rendre compte à la direction de façon factuelle et confidentielle.",
        "Analyser sa pratique avec des pairs et préparer ses trente premiers jours.",
    ],
    competences=["C1", "C2", "C4", "C5", "C8"],
    blocs=["4", "2"],
    blocs_detail="4.2 (collectif professionnel, analyse de pratique) ; 2.1 (évaluation) ; 3.6 (protection)",
    production="Mon journal des décisions, le point écrit à la direction et mon plan des trente premiers jours.",
    criteres=[
        "Chaque décision du journal indique le critère qui l'a guidée.",
        "La situation de protection est traitée dès qu'elle est connue.",
        "Aucune demande hors cadre n'est exécutée.",
        "Le point écrit est factuel et ne contient aucune information confidentielle inutile.",
        "Le plan des trente jours fixe deux priorités avec une preuve attendue.",
    ],
    docs=[
        dict(titre="Le journal des décisions", type="Outil", html="""
<table class="blank"><thead><tr><th>Heure</th><th>Événement</th><th>Critère de priorité</th><th>Décision</th><th>Qui agit ?</th><th>Trace, suivi</th></tr></thead>
<tbody><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>"""),
        dict(titre="Le tableau des postes de ce jeudi", type="Établissement", html="""
<table class="center"><thead><tr><th>Créneau</th><th>Postes prévus</th><th>AED disponibles ce jour</th></tr></thead><tbody>
<tr><td>T1 · 08:00</td><td>Portail Antoine + Bérénice<br>Cour Camille<br>Accueil David</td><td>A, B, C, D, F</td></tr>
<tr><td>T2 · 10:00</td><td>Cour Fabien<br>Étude Elsa<br>Accueil Bérénice</td><td>A, B, C, E, F</td></tr>
<tr><td>T3 · 12:00</td><td>Cantine David<br>Cour Fabien<br>Accueil Antoine</td><td>A, B, D, E, F</td></tr>
</tbody></table>"""),
        dict(titre="Grille d'analyse de pratique", type="Outil", html="""
<ol>
<li><strong>L'exposant</strong> (2 min) raconte une décision de la matinée qui l'a fait hésiter.</li>
<li><strong>Questions de clarification</strong> (3 min) : le groupe ne pose que des questions factuelles, sans conseil.</li>
<li><strong>Hypothèses</strong> (4 min) : chacun propose une lecture de la situation, en commençant par « Si j'étais toi… » ou « Je me demande si… ». L'exposant écoute sans répondre.</li>
<li><strong>Retour de l'exposant</strong> (2 min) : ce qu'il retient, ce qu'il ferait autrement.</li>
</ol>"""),
        dict(titre="Mon plan des trente premiers jours", type="Outil", html="""
<table class="blank"><thead><tr><th>Semaine</th><th>Intention</th><th>Action</th><th>Partenaire</th><th>Preuve attendue</th></tr></thead><tbody>
<tr><td>1</td><td>Rencontrer, observer, vérifier le cadre</td><td></td><td></td><td></td></tr>
<tr><td>2</td><td>Sécuriser l'organisation et les transmissions</td><td></td><td></td><td></td></tr>
<tr><td>3</td><td>Structurer les suivis et les partenariats</td><td></td><td></td><td></td></tr>
<tr><td>4</td><td>Bilan avec la direction, deux ou trois priorités</td><td></td><td></td><td></td></tr>
</tbody></table>"""),
        dict(titre="9 h 20 : deux appels", type="Rebondissement", html="""
<ul>
<li>Le père de l'élève de 6e (événement de 8 h 05) appelle de l'étranger : « Pourquoi avez-vous appelé ma sœur ? Mon fils est grand, il sait se débrouiller trois jours. Ce n'est pas votre affaire. »</li>
<li>La proviseure, entre deux rendez-vous : « Pour le point de 11 h, mettez-moi les noms des élèves concernés, le détail de ce qu'a dit le petit de 6e et ce que l'infirmière a constaté pour l'élève de 1re. Les inspecteurs pourraient demander. »</li>
</ul>"""),
    ],
    groupes=[],
    phases=[
        dict(titre="Je prends mon poste", duree=5, modalite="Groupes de quatre : un CPE, trois observateurs",
             consigne="Répartissez les rôles. Avant le premier événement, écrivez dans votre carnet les trois critères que vous utiliserez pour décider de vos priorités.",
             docs=[1, 2]),
        dict(titre="Les événements", duree=30, modalite="Groupes",
             consigne="Révélez les événements au signal du formateur, pas avant. Consignez chaque décision et son critère dans le journal. Vous ne pourrez pas tout traiter : choisissez.",
             sequence=[
                 ("07:52", "Bérénice prévient par message qu'elle sera absente toute la journée. Elle tenait le portail en binôme à T1 et l'accueil à T2."),
                 ("08:10", "Un professeur principal de 4e signale qu'un élève cumule six demi-journées d'absence non justifiées en trois semaines. Personne n'a joint la famille."),
                 ("08:25", "Elsa rapporte qu'une élève de 5e lui a confié recevoir depuis un mois des messages humiliants et ne plus vouloir aller en EPS. L'élève est en cours en ce moment."),
                 ("08:30", "Un père se présente sans rendez-vous et exige d'être reçu immédiatement au sujet d'une punition donnée à son fils il y a deux semaines. Il élève la voix dans le hall."),
                 ("08:45", "M. Garnier vous amène un élève : « Il a un téléphone volé dans son sac, j'en suis sûr. Fouillez-le, c'est votre rôle. »"),
                 ("09:00", "La proviseure demande pour 11 h un point écrit et factuel sur la matinée."),
             ], docs=[]),
        dict(titre="Le rebondissement", duree=10, modalite="Groupes",
             consigne="Lisez le document 5. Que répondez-vous à la mère ? Et à la proviseure ? Rédigez le point écrit de 11 h.",
             docs=[5]),
        dict(titre="L'analyse de pratique", duree=15, modalite="Groupes de quatre",
             consigne="Avec la grille du document 3, un membre du groupe expose la décision qui l'a le plus fait hésiter. Respectez strictement les étapes et les temps.",
             docs=[3]),
        dict(titre="Je me projette", duree=10, modalite="Individuel",
             consigne="Établissez votre plan des trente premiers jours avec le document 4, puis faites votre positionnement de fin de formation.",
             docs=[4], production=True),
        dict(titre="Retour sur mes critères", duree=5, modalite="Individuel",
             consigne="Relisez les trois critères que vous aviez écrits en prenant votre poste. Les avez-vous vraiment appliqués ? Lequel a cédé sous la pression ?",
             rappel=True),
    ],
    cloture=[
        "Quel événement avez-vous traité trop tard, et pourquoi ?",
        "Qu'avez-vous refusé de faire, et à qui ?",
        "Quelles sont vos deux priorités pour votre première semaine ?",
    ],
    approfondir="integration",
    refs=["formation", "competences", "missions", "phare"],
    formateur=dict(
        materiel=["Les six événements imprimés séparément, ou révélés à l'écran", "Document 5 imprimé à part", "Chronomètre", "Grille d'observation par observateur"],
        deroule=[
            "Exiger les trois critères écrits avant le premier événement.",
            "Révéler un événement toutes les quatre à cinq minutes, sans attendre que le précédent soit traité. L'événement de 8 h 45 arrive volontairement pendant le traitement de la confidence.",
            "Le document 5 met le CPE face à sa propre hiérarchie : exiger une réponse écrite à la proviseure.",
            "Respecter strictement les temps de la grille. Le formateur peut jouer le rôle de garant du cadre.",
            "Écrit individuel, puis positionnement final sur le site.",
            "Écrit individuel ; inviter deux volontaires à lire leur critère qui a cédé.",
        ],
        relances=[
            "« Le car attend : laissez partir l'élève, sa mère a dit oui au téléphone. »",
            "« Fouiller un sac, c'est cinq secondes. Le professeur est sûr de lui. »",
            "« La proviseure est votre supérieure. Si elle veut les noms, vous les donnez. »",
            "« L'élève de 6e est en classe, il est en sécurité : ça peut attendre ce soir. »",
            "« L'élève de 1re sent l'alcool : c'est une sanction, appelez ses parents pour qu'ils viennent le chercher. »",
        ],
        attendus="""
<p><strong>Critères attendus.</strong> Protection de l'élève, sécurité des personnes, continuité du service, puis relation et administratif. Les décisions irréversibles se prennent avec la direction ; les décisions réversibles se prennent et se tracent.</p>
<p><strong>07:50, la sortie.</strong> Sans l'autorisation écrite prévue, l'élève ne part pas : l'accord oral d'un parent ne suffit pas. Il est accueilli en étude ou dans une autre classe, et la famille est rappelée. Le professeur part avec le reste du groupe.</p>
<p><strong>08:05, l'enfant seul (prioritaire).</strong> Un enfant de 11 ans seul chez lui depuis deux jours est une situation de danger : informer la direction sans attendre, joindre les parents et l'adulte de référence, activer le circuit de protection de l'établissement. On ne laisse pas l'élève repartir seul ce soir sans solution.</p>
<p><strong>08:20, l'élève de 1re.</strong> D'abord la santé et la sécurité : accompagnement à l'infirmerie, jamais seul. Puis la famille et la direction. La question disciplinaire viendra après, si elle se pose.</p>
<p><strong>08:40, la photo.</strong> Écouter, vérifier l'autorisation de droit à l'image, faire retirer la photo si elle manque, et renvoyer vers la direction, qui répond pour l'établissement. Ne pas promettre de sanction ni d'indemnité.</p>
<p><strong>08:45, la fouille.</strong> Refuser : un CPE ne fouille pas un élève ni son sac. On peut lui demander de montrer volontairement le contenu ; en cas de refus et de soupçon sérieux, la direction décide de la suite. Recevoir l'élève, garder le calme.</p>
<p><strong>Rebondissement.</strong> Au père : rester calme, expliquer que la sécurité de son fils est la priorité de l'établissement et que la direction le rappellera. À la proviseure : l'informer oralement de l'essentiel ; dans l'écrit de 11 h, ne mettre ni les noms, ni le récit de l'enfant, ni les constats de l'infirmière, qui relèvent du circuit de protection et du secret ; le lui expliquer.</p>""",
        vigilance=[
            "Évaluer le raisonnement et l'ordre des priorités, pas une réponse unique.",
            "Le refus de la fouille et le refus de transmettre des détails à la proviseure sont des moments clés : les stagiaires ont besoin de savoir qu'ils ont le droit de dire non, et comment le dire.",
            "Le positionnement final se fait à la fin de l'atelier, avant l'évaluation de la formation.",
        ],
    ),
    slides=[
        dict(t="titre", titre="Décider quand tout arrive en même temps", sous="Bilan de l'atelier 8 · Une matinée dans la peau du CPE"),
        dict(t="points", titre="Ce que vous avez dû trancher", points=["Un enfant de 11 ans seul chez lui depuis deux jours", "Un élève qui sent l'alcool à 8 h 20", "Un collègue qui exige une fouille", "Une proviseure qui veut tout savoir"]),
        dict(t="etapes", titre="Une hiérarchie de critères", etapes=[("1. Protection", "Un élève en danger passe avant tout"), ("2. Sécurité", "Des personnes, des lieux, de l'ordre"), ("3. Continuité", "Le service qui permet d'accueillir"), ("4. Relation", "Les familles, les collègues"), ("5. Administratif", "Ce qui peut attendre une heure")]),
        dict(t="deux", titre="Urgent n'est pas important", a=("Ce qui crie", ["Le parent au téléphone", "Le collègue qui insiste", "Le car qui attend"]), b=("Ce qui compte", ["L'enfant seul chez lui", "L'élève qui a bu, à mettre en sécurité", "Les droits de l'élève accusé de vol"]), source="D'après la matrice d'Eisenhower"),
        dict(t="def", titre="Décider dans l'incertitude", terme="Réversible ou irréversible ?", definition="Une décision réversible (déplacer un AED, différer un rendez-vous) se prend tout de suite et se trace. Une décision irréversible ou qui engage les droits d'une personne (sanction, signalement, communication de données) se prend avec l'autorité compétente.", source=""),
        dict(t="points", titre="Ce que le CPE ne fait pas", points=["Fouiller un élève ou son sac", "Laisser partir un élève sans l'autorisation requise", "Transmettre des informations de santé ou de protection hors du circuit prévu", "Mais il le dit, il l'explique, et il propose ce qui est possible"]),
        dict(t="def", titre="Le praticien réflexif", terme="Réfléchir dans l'action, réfléchir sur l'action", definition="Pour Donald Schön, le professionnel compétent n'applique pas seulement des savoirs : il ajuste en situation, puis revient sur ce qu'il a fait pour en tirer des enseignements. L'analyse de pratique entre pairs est le lieu de cette seconde réflexion.", source="Donald Schön, The Reflective Practitioner, 1983"),
        dict(t="etapes", titre="Analyser sa pratique entre pairs", etapes=[("Exposer", "Une situation vécue, sans se justifier"), ("Clarifier", "Questions factuelles seulement"), ("Faire des hypothèses", "Plusieurs lectures, aucun conseil imposé"), ("Retenir", "Ce que l'exposant garde pour lui")], source="D'après les groupes d'analyse de pratique professionnelle"),
        dict(t="etapes", titre="Mes trente premiers jours", etapes=[("Semaine 1", "Rencontrer, observer, vérifier le cadre et les circuits d'alerte"), ("Semaine 2", "Sécuriser l'organisation et les transmissions"), ("Semaine 3", "Structurer les suivis et les partenariats"), ("Semaine 4", "Faire le bilan avec la direction, fixer deux ou trois priorités")]),
        dict(t="cle", texte="Vous ne saurez pas tout dans trente jours. Mais vous saurez qui décide, à qui alerter, et ce que vous ne faites jamais seul."),
    ],
))


# ----------------------------------------------------------------------
# Atelier « Construire mon année de CPE », inséré en 2e position, puis
# numérotation automatique de tous les ateliers.
# ----------------------------------------------------------------------
from atelier_annee import ATELIER_ANNEE  # noqa: E402

ATELIERS.insert(1, ATELIER_ANNEE)
for _i, _a in enumerate(ATELIERS, 1):
    _a["n"] = _i

# ----------------------------------------------------------------------
# Scénarisation : un moteur pédagogique différent pour chaque atelier
# ----------------------------------------------------------------------
from scenarios import appliquer  # noqa: E402

appliquer(ATELIERS)
