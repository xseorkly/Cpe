# -*- coding: utf-8 -*-
"""Atelier « Construire mon année de CPE » (planning annuel).

Construit à partir des ressources du Drive du formateur : « Calendrier annuel
du CPE », « Une année de CPE », cartes Joker, activité « timeline du CPE »,
recensement des missions des AED, présentation des instances lycéennes.
"""

ATELIER_ANNEE = dict(
    n=2,
    titre="Construire mon année de CPE",
    accroche="Élections, AED, conseils, orientation, prévention : anticiper l'année plutôt que la subir.",
    problematique="Fin août, la proviseure me demande le calendrier annuel de la vie scolaire. Comment anticiper toute une année (élections, instances, recrutement et suivi des AED, conseils de classe, orientation, prévention) avec un agenda hérité plein d'erreurs et un calendrier local qui n'est pas celui de la France ?",
    situation="""
<p>Vendredi 28 août, 16 h. La pré-rentrée a lieu lundi. Mme Laurent vous arrête dans le couloir : « Lundi, je veux le calendrier annuel de la vie scolaire, sur une page. Je veux savoir qui fait quoi, et quand. L'an dernier, on a couru après tout. »</p>
<p>Dans le bureau, l'agenda de Mme Martel tient en une feuille couverte de post-it. Les élections des délégués y sont notées « en novembre ». Le recrutement des AED, « après la rentrée ». La formation des délégués, « si on a le temps ». Le bilan de la vie scolaire n'apparaît nulle part.</p>
<p>Vous avez aussi reçu le calendrier de l'établissement, la liste des journées nationales et les attentes des collègues. Rien n'est encore assemblé.</p>""",
    objectifs=[
        "Situer les grands rendez-vous de l'année dans les trois domaines de missions du CPE.",
        "Ordonner le cycle de la démocratie scolaire : engagement, élections, formation des délégués, projets, bilan.",
        "Planifier le cycle de vie d'un AED : recrutement, fiche de poste, accueil, période d'essai, entretiens.",
        "Repérer les périodes de surcharge et arbitrer entre des rendez-vous concurrents.",
        "Adapter un calendrier national au calendrier de l'établissement et du pays d'accueil.",
    ],
    competences=["C1", "C3", "C4", "C6"],
    blocs=["1", "2"],
    blocs_detail="1.1 (organiser et animer l'équipe), 1.5 et 1.6 (parcours, citoyenneté) ; 2.3 (contextes d'exercice)",
    production="Le calendrier annuel de la vie scolaire sur une page, avec qui fait quoi et quand, et les trois périodes de vigilance de l'année.",
    criteres=[
        "Le calendrier couvre septembre à juillet et distingue au moins quatre domaines : démocratie scolaire, équipe AED, suivi des élèves, prévention et pilotage.",
        "Les élections et la formation des délégués précèdent la première réunion des instances.",
        "Le cycle de l'AED est complet : recrutement, fiche de poste, accueil, période d'essai, entretien intermédiaire, entretien de fin d'année.",
        "Trois périodes de surcharge sont repérées, avec l'arbitrage proposé.",
        "Chaque rendez-vous nomme un responsable et les partenaires associés.",
        "Les dates nationales sont adaptées au calendrier de l'établissement et du pays.",
    ],
    docs=[
        dict(titre="Le message de la proviseure", type="Messages", html="""
<blockquote>« Pour lundi : le calendrier annuel de la vie scolaire sur une page. Je veux voir les élections, les instances, les conseils de classe, l'orientation, les actions de prévention et tout ce qui concerne les AED. Pour chaque moment : qui pilote, avec qui, et à quelle date au plus tard. Signalez-moi aussi les semaines où ça risque de coincer. »</blockquote>"""),
        dict(titre="L'agenda hérité de Mme Martel", type="Établissement", html="""
<table><thead><tr><th>Post-it</th><th>Ce qui est écrit</th></tr></thead><tbody>
<tr><td>Élections</td><td>« Délégués : novembre, après les vacances. CVL : on verra. »</td></tr>
<tr><td>AED</td><td>« Recruter après la rentrée, quand on connaîtra les besoins. »</td></tr>
<tr><td>Fiche de poste AED</td><td>« Pas besoin, ils savent ce qu'ils ont à faire. »</td></tr>
<tr><td>Formation délégués</td><td>« Si on a le temps. »</td></tr>
<tr><td>Réunion vie scolaire</td><td>« Quand on peut. »</td></tr>
<tr><td>Conseils de classe</td><td>« Voir avec le secrétariat. »</td></tr>
<tr><td>Harcèlement</td><td>« Affiche en novembre. »</td></tr>
<tr><td>Entretiens AED</td><td>« Juin : on renouvelle tout le monde, c'est plus simple. »</td></tr>
</tbody></table>
<p class="note">Aucune mention du bilan de la vie scolaire, de l'orientation, des exercices de sécurité ni de la liaison avec le primaire.</p>"""),
        dict(titre="Les repères nationaux de l'année", type="Texte officiel", groupe=1, html="""
<p>Repères du calendrier national (synthèse). Dans un établissement du réseau AEFE, ces dates se transposent au calendrier de l'établissement.</p>
<table><thead><tr><th>Période</th><th>Repère</th></tr></thead><tbody>
<tr><td>Septembre</td><td>Semaine de l'engagement lycéen : susciter les candidatures</td></tr>
<tr><td>Septembre–octobre</td><td>Élections des délégués de classe ; en France, au plus tard avant la fin de la septième semaine de l'année scolaire</td></tr>
<tr><td>Octobre</td><td>Semaine de la démocratie scolaire ; élections au CVL et au CVC</td></tr>
<tr><td>Début novembre</td><td>Journée « Non au harcèlement » (premier jeudi qui suit les vacances d'automne)</td></tr>
<tr><td>9 et 10 décembre</td><td>Journée de la laïcité ; journée des droits de l'homme</td></tr>
<tr><td>Mars</td><td>Semaine d'éducation contre le racisme et l'antisémitisme ; semaine de la persévérance scolaire</td></tr>
<tr><td>7 avril</td><td>Journée mondiale de la santé</td></tr>
<tr><td>17 mai</td><td>Journée de lutte contre l'homophobie et la transphobie</td></tr>
</tbody></table>
<p class="note">Les dates exactes changent chaque année : à vérifier au calendrier officiel et à adapter au pays d'accueil.</p>"""),
        dict(titre="Le calendrier 2026-2027 du lycée Horizon", type="Établissement", groupe=3, html="""
<table><thead><tr><th>Date</th><th>Événement</th></tr></thead><tbody>
<tr><td>31 août</td><td>Pré-rentrée des personnels</td></tr>
<tr><td>1er septembre</td><td>Rentrée des élèves</td></tr>
<tr><td>8 septembre</td><td>Réunion parents-professeurs</td></tr>
<tr><td>Du 24 octobre au 2 novembre</td><td>Vacances d'automne</td></tr>
<tr><td>12 novembre</td><td>Premier conseil d'établissement de l'année (il doit compter des représentants élus des élèves)</td></tr>
<tr><td>Du 7 au 11 décembre</td><td>Conseils de classe du premier trimestre</td></tr>
<tr><td>Du 19 décembre au 3 janvier</td><td>Vacances d'hiver</td></tr>
<tr><td>Février</td><td>Examens blancs ; ouverture des réinscriptions pour l'année suivante</td></tr>
<tr><td>Du 15 au 18 mars</td><td>Regroupement inter-CVL de la zone (deux élus et leur CPE)</td></tr>
<tr><td>Du 22 au 26 mars</td><td>Conseils de classe du deuxième trimestre</td></tr>
<tr><td>Avril</td><td>Fête nationale du pays d'accueil (jour férié) ; vacances de printemps</td></tr>
<tr><td>Juin</td><td>Conseils de classe du troisième trimestre ; examens ; commissions d'appel ; dernier conseil d'établissement</td></tr>
<tr><td>3 juillet</td><td>Fin des cours</td></tr>
</tbody></table>"""),
        dict(titre="Le cycle de vie d'un AED", type="Établissement", groupe=2, html="""
<p>Pratique du lycée Horizon, fixée par la direction (AED recrutés en contrat de droit local).</p>
<table><thead><tr><th>Étape</th><th>Ce qui se passe</th><th>Qui</th></tr></thead><tbody>
<tr><td>Anticiper les besoins</td><td>Postes à pourvoir, profils, emploi du temps de l'année suivante</td><td>CPE, direction</td></tr>
<tr><td>Recruter</td><td>Annonce, entretiens, choix ; derniers ajustements à la rentrée</td><td>Direction, avec le CPE</td></tr>
<tr><td>Rédiger la fiche de poste</td><td>Missions, lieux, horaires, référent, règles de transmission, formation</td><td>CPE, validée par la direction</td></tr>
<tr><td>Accueillir et former</td><td>Visite, livret d'accueil, binôme, protocoles, règlement intérieur</td><td>CPE, AED référent</td></tr>
<tr><td>Période d'essai</td><td>Point à mi-parcours, puis terme ou prolongation</td><td>Direction, sur avis du CPE</td></tr>
<tr><td>Entretien intermédiaire</td><td>Bilan, besoins de formation, ajustements</td><td>CPE</td></tr>
<tr><td>Entretien de fin d'année</td><td>Bilan, souhaits, avis sur le renouvellement</td><td>CPE ; décision par la direction</td></tr>
</tbody></table>
<p class="note">Les dates de ces étapes ne sont pas indiquées : c'est à vous de les placer.</p>"""),
        dict(titre="Les instances des élèves", type="Ressource", groupe=1, html="""
<ul>
<li><strong>Délégués de classe :</strong> deux titulaires et deux suppléants par classe, élus pour l'année ; tous les élèves sont électeurs et éligibles. Ils représentent leurs camarades au conseil de classe et au quotidien.</li>
<li><strong>Éco-délégués :</strong> élus dans chaque classe pour porter des actions de développement durable.</li>
<li><strong>CVL :</strong> dix lycéens élus pour deux ans, renouvelés par moitié chaque année. Il est consulté sur la vie lycéenne et les conditions de travail des élèves.</li>
<li><strong>CVC :</strong> le conseil de la vie collégienne, pour les collégiens.</li>
<li><strong>Représentants des élèves au conseil d'établissement :</strong> élus selon les règles de l'établissement et de l'AEFE.</li>
</ul>
<p class="note">La formation des délégués se pense en plusieurs temps : après l'élection, à mi-année, puis un bilan en fin d'année.</p>"""),
        dict(titre="Ce que disent les collègues", type="Témoignages", groupe=3, html="""
<ul>
<li><strong>Un professeur principal :</strong> « Pas d'heure de vie de classe avant la troisième semaine, mon emploi du temps n'est pas stabilisé. »</li>
<li><strong>La psychologue :</strong> « J'ai besoin de connaître tôt les élèves à repérer pour les conseils du premier trimestre. »</li>
<li><strong>L'infirmière :</strong> « Chaque année, la semaine santé tombe en même temps que les examens blancs. »</li>
<li><strong>Antoine, AED :</strong> « On voudrait savoir à l'avance les semaines chargées, pour poser nos absences ailleurs. »</li>
<li><strong>Un parent élu :</strong> « Les familles veulent l'information sur l'orientation dès janvier, pas en avril. »</li>
<li><strong>Le directeur de l'école primaire voisine :</strong> « Pour les futurs 6e, nous aimerions une visite en mai. »</li>
</ul>"""),
        dict(titre="Douze moments forts d'une année de CPE", type="Outil", groupe=4, html="""
<table><thead><tr><th>Moment</th><th>Période</th><th>Traces et indicateurs</th></tr></thead><tbody>
<tr><td>Rentrée et accueil</td><td>Septembre</td><td>Absences des quinze premiers jours, diffusion du règlement, plannings AED</td></tr>
<tr><td>Élections des délégués, CVC et CVL</td><td>Septembre–octobre</td><td>Taux de participation, procès-verbaux, affichage</td></tr>
<tr><td>Formation des délégués</td><td>Octobre, puis à mi-année</td><td>Programme, émargements, évaluation</td></tr>
<tr><td>Semaine de la démocratie scolaire</td><td>Octobre</td><td>Ateliers, fréquentation, productions</td></tr>
<tr><td>Prévention et pHARe</td><td>Novembre, puis toute l'année</td><td>Signalements, délais de traitement, actions</td></tr>
<tr><td>Exercices de sécurité</td><td>Septembre–novembre, puis rappels</td><td>Temps d'évacuation, rapports, ajustements</td></tr>
<tr><td>Conseils de classe et suivis</td><td>Fin de chaque trimestre</td><td>Décisions, dispositifs d'aide, assiduité</td></tr>
<tr><td>Parcours Avenir et orientation</td><td>Janvier–avril</td><td>Stages, entretiens, vœux</td></tr>
<tr><td>Santé et prévention des conduites à risque</td><td>Novembre–mars</td><td>Séances, incidents, récidives</td></tr>
<tr><td>Bilans de la vie scolaire</td><td>Chaque mois ou trimestre</td><td>Tableaux de bord, décisions prises</td></tr>
<tr><td>Organisation et management des AED</td><td>Septembre, puis régulations</td><td>Plannings, fiches de poste, réunions, formations</td></tr>
<tr><td>Portes ouvertes, inscriptions, examens</td><td>Avril–juin</td><td>Dossiers, incidents, retours des familles</td></tr>
</tbody></table>
<p class="note">D'après les cartes « Une année de CPE ».</p>"""),
        dict(titre="Le calendrier à compléter", type="Outil", groupe=4, html="""
<table class="blank"><thead><tr><th>Mois</th><th>Démocratie scolaire</th><th>Équipe AED</th><th>Suivi des élèves</th><th>Prévention et pilotage</th></tr></thead><tbody>
<tr><td>Septembre</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Octobre</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Novembre</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Décembre</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Janvier</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Février</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Mars</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Avril</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Mai</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Juin</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Juillet</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Toute l'année</td><td></td><td></td><td></td><td></td></tr>
</tbody></table>"""),
        dict(titre="Mi-octobre : trois nouvelles", type="Rebondissement", html="""
<ul>
<li>Le pays d'accueil organise des élections nationales : les autorités ferment les écoles du 9 au 13 novembre. Le premier conseil d'établissement est reporté au 23 novembre.</li>
<li>Deux AED démissionnent pendant les vacances d'automne. Leurs remplaçants ne pourront arriver qu'à la fin novembre.</li>
<li>L'AEFE annonce une visite d'inspection de la vie scolaire en février. L'inspecteur souhaite consulter le bilan du premier trimestre et le projet de la vie scolaire.</li>
</ul>
<p>Que déplacez-vous ? Que maintenez-vous coûte que coûte ? Que produisez-vous, et pour quand ?</p>"""),
    ],
    groupes=[
        dict(nom="La démocratie scolaire", angle="Dans quel ordre faire vivre les instances ?",
             questions=["Placez dans l'ordre : engagement, candidatures, élections des délégués, CVL et CVC, formation des délégués, premières réunions, bilan.", "Les élections de Mme Martel « en novembre » posent quel problème avec le calendrier de l'établissement ?", "Où placer les trois temps de formation des délégués et le regroupement inter-CVL ?"],
             docs=[3, 6, 4]),
        dict(nom="L'équipe AED", angle="Quand recruter, accueillir, évaluer ?",
             questions=["Placez chaque étape du cycle de vie d'un AED sur l'année. Laquelle se prépare l'année précédente ?", "Que contient une fiche de poste ? Quand la remettre ? Que répondre au post-it « pas besoin » ?", "Quand placer la réunion d'équipe, les formations et les entretiens ?"],
             docs=[5, 2]),
        dict(nom="Le suivi des élèves", angle="Comment le suivi suit-il le rythme des trimestres ?",
             questions=["Que faire avant, pendant et après chaque conseil de classe ?", "Quand placer l'orientation, les réunions avec les familles, la liaison avec le primaire ?", "Quelles demandes des collègues pouvez-vous satisfaire, et comment ?"],
             docs=[4, 7]),
        dict(nom="Prévention et pilotage", angle="Comment ne pas transformer les journées nationales en décor ?",
             questions=["Quelles journées nationales retenez-vous, et pour quelle action concrète ?", "Où placer les exercices de sécurité et les bilans de la vie scolaire ?", "Quand produire le rapport d'activité, et à partir de quelles données ?"],
             docs=[3, 8]),
    ],
    phases=[
        dict(titre="Ma première réaction", duree=5, modalite="Individuel, sans document",
             consigne="Sans rien consulter, notez dix moments forts de votre année de CPE et placez-les sur les mois, de septembre à juillet. Entourez celui qui vous inquiète le plus.",
             docs=[1, 2]),
        dict(titre="L'enquête en groupes experts", duree=20, modalite="4 groupes experts",
             consigne="Chaque groupe construit la « ligne » de l'année pour son domaine, mois par mois, et relève les erreurs de l'agenda de Mme Martel. Pour chaque moment : qui pilote, avec qui, à quelle date au plus tard.",
             dossier=True, mission=True),
        dict(titre="J'assemble l'année", duree=20, modalite="Groupes mixtes : un membre de chaque groupe expert",
             consigne="Assemblez les quatre lignes dans le calendrier ci-dessous (ou sur la frise murale). Repérez les semaines où tout se télescope et proposez pour chacune un arbitrage : ce qui avance, ce qui recule, ce qui se délègue.",
             docs=[], planner=True),
        dict(titre="Le rebondissement", duree=10, modalite="Groupes mixtes",
             consigne="Lisez le document 10. Reprenez votre calendrier : que déplacez-vous, que maintenez-vous coûte que coûte, que produisez-vous pour l'inspection ?",
             docs=[10]),
        dict(titre="Je produis", duree=15, modalite="Groupes mixtes, puis affichage",
             consigne="Mettez au propre le calendrier annuel sur une page pour la proviseure, avec qui fait quoi et quand, et vos trois périodes de vigilance. Affichez-le : les groupes comparent leurs choix.",
             production=True),
        dict(titre="Retour sur ma première réaction", duree=5, modalite="Individuel",
             consigne="Relisez vos dix moments forts. Lesquels aviez-vous oubliés ? Lequel aviez-vous placé trop tard ?",
             rappel=True),
    ],
    cloture=[
        "Quel rendez-vous de l'année aviez-vous complètement oublié ?",
        "Qu'est-ce qui, dans le cycle d'un AED, se prépare l'année d'avant ?",
        "Quelle date de votre établissement devez-vous vérifier dès lundi ?",
    ],
    approfondir="organisation",
    refs=["missions", "democratie", "aed", "aefe_instances", "phare"],
    formateur=dict(
        materiel=["Dossier en quatre jeux", "Une grande frise murale septembre–juillet (ou tableau partagé) à quatre lignes de couleur", "Post-it de quatre couleurs", "Document 10 imprimé à part"],
        deroule=[
            "Écrit individuel et silencieux. Recueillir le moment qui inquiète le plus : souvent les élections ou les conseils.",
            "Chaque groupe expert remplit sa ligne avec des post-it de sa couleur. Relancer avec les questions dérangeantes.",
            "Les groupes mixtes collent les quatre couleurs sur la frise. Faire nommer les collisions à voix haute.",
            "Distribuer le document 10 sans délai supplémentaire. Exiger une liste « ce qui bouge / ce qui ne bouge pas ».",
            "Photographier chaque calendrier ; comparer deux choix opposés devant le groupe.",
            "Écrit individuel.",
        ],
        relances=[
            "« Mme Martel faisait les élections en novembre depuis onze ans et tout se passait bien. Pourquoi changer ? »",
            "« Recruter en juin, c'est payer des gens pendant l'été pour rien. Attendez la rentrée. »",
            "« Une fiche de poste pour un AED, c'est de la paperasse. Ils apprennent sur le terrain. »",
            "« Renouveler tout le monde en juin, c'est plus simple et ça évite les conflits. »",
            "« Les journées nationales, il suffit de mettre une affiche. »",
            "« Le premier conseil d'établissement est reporté : vous pouvez donc décaler les élections et la formation des délégués. »",
        ],
        attendus="""
<p><strong>Démocratie scolaire.</strong> Semaine de l'engagement en septembre, élections des délégués de classe au plus tard début octobre, puis CVL et CVC pendant la semaine de la démocratie scolaire, avant les vacances d'automne. Les élus doivent être en place et formés avant le premier conseil d'établissement du 12 novembre : les élections « en novembre » de Mme Martel le rendaient impossible. Formation des délégués en trois temps : octobre, janvier-février, bilan en mai. Le regroupement inter-CVL de mars se prépare dès janvier (choix des deux élus, projet à présenter).</p>
<p><strong>Équipe AED.</strong> Anticipation des besoins et recrutement en mai-juin pour une prise de poste à la pré-rentrée ; derniers ajustements en septembre. Fiche de poste remise à la prise de fonction et revue chaque année : elle protège l'AED autant que le service. Accueil et formation à la pré-rentrée ; point de mi-période d'essai fin septembre et terme ou prolongation en octobre ; formation en octobre-novembre ; entretien intermédiaire en janvier-février ; entretien de fin d'année en juin, avec des critères explicites, la décision appartenant à la direction. Réunion d'équipe à jour fixe (hebdomadaire ou bimensuelle).</p>
<p><strong>Suivi des élèves.</strong> Commission de suivi dès octobre pour repérer ; préparation des conseils avec les professeurs principaux et la psychologue la semaine précédente ; entretiens et dispositifs après chaque conseil. Orientation : information des familles dès janvier, conseils du deuxième trimestre avec intentions, vœux et affectation au troisième. Liaison avec le primaire en mai.</p>
<p><strong>Prévention et pilotage.</strong> Chaque journée retenue porte une action préparée avec les élus ou l'équipe pHARe, pas une affiche. Exercices de sécurité dès septembre. Bilan de la vie scolaire à chaque fin de trimestre, rapport d'activité en juin pour le dernier conseil d'établissement.</p>
<p><strong>Périodes de vigilance attendues.</strong> La première quinzaine de septembre (accueil, recrutements, plannings) ; la fin novembre et le début décembre (conseil d'établissement, formation des délégués, conseils du premier trimestre) ; la fin mars (inter-CVL et conseils du deuxième trimestre la même semaine ou presque) ; juin (conseils, examens, entretiens AED, rapport d'activité).</p>
<p><strong>Rebondissement.</strong> On ne décale pas les élections : elles sont faites, et la formation des délégués peut se tenir avant le 23 novembre. Les remplacements d'AED imposent un planning dégradé jusqu'à fin novembre, à présenter à la direction. Pour l'inspection : le bilan du premier trimestre (données d'assiduité et d'incidents, actions menées) et le projet de vie scolaire, à finaliser en janvier.</p>""",
        vigilance=[
            "Les dates nationales sont des repères : dans le réseau AEFE, le calendrier de l'établissement, les jours fériés du pays et les règles des instances AEFE priment. Faire vérifier chaque date localement.",
            "Ne pas laisser l'atelier devenir un exercice de remplissage de tableau : exiger pour chaque moment le responsable, les partenaires et la date limite.",
            "La décision de renouveler ou non un AED appartient à la direction ; le CPE donne un avis fondé sur des critères connus à l'avance.",
        ],
    ),
    slides=[
        dict(t="titre", titre="Anticiper l'année plutôt que la subir", sous=""),
        dict(t="points", titre="Ce que vous avez dû trancher", points=["Des élections « en novembre » incompatibles avec la première instance", "Des AED recrutés trop tard et sans fiche de poste", "Des semaines où tout se télescope", "Un calendrier bousculé par le pays d'accueil et une inspection"]),
        dict(t="etapes", titre="L'année du CPE en quatre temps", etapes=[("Septembre–octobre", "Installer : accueil, équipe, règles, élections, premiers repérages"), ("Novembre–décembre", "Faire vivre : instances, formation des délégués, prévention, premiers conseils"), ("Janvier–avril", "Accompagner les parcours : orientation, persévérance, bilans intermédiaires"), ("Mai–juillet", "Faire le bilan et anticiper : conseils, entretiens AED, rapport, rentrée suivante")], source="D'après « Une année de CPE » et le calendrier annuel du CPE"),
        dict(t="etapes", titre="Le cycle de la démocratie scolaire", etapes=[("Septembre", "Semaine de l'engagement : susciter les candidatures"), ("Septembre–octobre", "Élections des délégués de classe, puis CVL et CVC"), ("Octobre", "Première formation des délégués ; semaine de la démocratie scolaire"), ("Novembre", "Premières réunions ; élus présents au conseil d'établissement"), ("Janvier–mars", "Deuxième formation ; projets ; regroupement inter-CVL"), ("Mai", "Bilan des instances et de la formation des délégués")], source="Éduscol, guide de la démocratie scolaire ; à adapter au calendrier AEFE"),
        dict(t="etapes", titre="Le cycle de vie d'un AED", etapes=[("Mai–juin (N-1)", "Anticiper les besoins, recruter"), ("Pré-rentrée", "Accueillir, remettre la fiche de poste, former"), ("Septembre–octobre", "Point de mi-période d'essai, puis terme ou prolongation"), ("Octobre–novembre", "Formation : posture, protocoles, harcèlement"), ("Janvier–février", "Entretien intermédiaire"), ("Juin", "Entretien de fin d'année, avis sur le renouvellement")], source="D'après « Une année de CPE » ; contrats de droit local : calendrier RH fixé par la direction"),
        dict(t="def", titre="La fiche de poste de l'AED", terme="Un outil qui protège autant qu'il cadre", definition="Rédigée par le CPE et validée par la direction, elle précise les missions, les lieux, les horaires, le référent, les règles de transmission et les formations prévues. Remise à la prise de fonction et revue chaque année, elle sert de base aux entretiens et évite les malentendus.", source="Circulaire du 17 septembre 2025 (AED de droit français) ; à transposer aux contrats locaux"),
        dict(t="deux", titre="Le suivi des élèves au rythme des conseils", a=("Avant le conseil", ["Croiser assiduité, incidents, observations", "Préparer avec le professeur principal et la psychologue", "Repérer les élèves à évoquer"]), b=("Après le conseil", ["Entretiens avec les élèves et les familles", "Mise en place des dispositifs décidés", "Date de suivi fixée"])),
        dict(t="points", titre="Les journées nationales : des leviers, pas des décors", points=["Début novembre : « Non au harcèlement », préparée avec l'équipe pHARe et les élus", "9 décembre : laïcité, avec un projet porté par les élèves", "Mars : persévérance scolaire, racisme et antisémitisme", "Une journée retenue = une action, un responsable, une trace"]),
        dict(t="def", titre="Planifier à rebours", terme="Le rétroplanning", definition="On part de la date qui ne bouge pas (le premier conseil d'établissement, les conseils de classe) et l'on remonte : ce qui doit être prêt la veille, la semaine d'avant, le mois d'avant. Les jalons rendent visibles les collisions et permettent d'arbitrer à temps.", source=""),
        dict(t="points", titre="Le calendrier dans un établissement AEFE", points=["Le calendrier et les jours fériés du pays d'accueil", "Les règles des instances fixées par l'AEFE et le statut de l'établissement", "Le calendrier RH des personnels recrutés localement", "Les temps forts de la zone : regroupements, inter-CVL, formations"]),
        dict(t="cle", texte="Un CPE qui subit l'année court après les urgences. Un CPE qui l'anticipe garde du temps pour les élèves."),
    ],
)
