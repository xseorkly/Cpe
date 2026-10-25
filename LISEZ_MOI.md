# Entrer dans le métier de CPE

Formation des CPE débutants du réseau AEFE : neuf ateliers progressifs, environ 22 h 30 de travail en temps indicatifs, sans découpage en journées (sessions en présence ou à distance).
Site statique publié avec GitHub Pages : https://xseorkly.github.io/Cpe/

## Ce que contient le site

| Page | Public | Rôle |
| --- | --- | --- |
| `index.html` | Stagiaires | Accueil, public, finalité, les 9 ateliers |
| `positionnement.html` | Stagiaires | Autopositionnement avant l'atelier 1 et après le dernier atelier |
| `atelier-1.html` à `atelier-9.html` | Stagiaires | Situations-problèmes, chacune avec son propre moteur (débat mouvant, forum-théâtre, tables tournantes, commission simulée, crash-test…), dossier documentaire, rebondissement, production, bilan et propositions de réponse protégés |
| `carnet.html` | Stagiaires | Toutes les notes réunies ; export Markdown, sauvegarde JSON, import, effacement |
| `mallette.html` | Stagiaires | Neuf fiches réflexes à construire au fil des ateliers |
| `ressources.html` | Stagiaires | PDF, approfondissements, textes de référence, compétences C1 à C8 et blocs 2026 |
| `approfondir/` | Stagiaires | Six pages de savoirs développés, liées aux ateliers |
| `formateur/` | Formateur | Programme minuté, fiches par atelier : déroulé, questions pour mettre en difficulté, attendus, vigilance, dossier imprimable, diaporama |
| `quiz.html` | Tous | Quiz de réactivation, à chaque reprise après une pause |
| `lexique.html` | Stagiaires | Lexique du CPE débutant (définitions aussi en infobulle dans les ateliers) et fonctionnement des formats |
| `ressources/` | Tous | Guide formateur, carnet, banque de prompts IA, mallette réflexe (PDF) |
| `ressources/kits/` | Tous | Dossier de chaque atelier, un document par page : `atelier-N-dossier.pdf` (stagiaires, intégré à la page de l'atelier) et `atelier-N-complet.pdf` (formateur, rebondissements compris) |

Les fiches formateur, les bilans, les propositions de réponse, le guide PDF et les dossiers complets (rebondissements et cartes secrètes des jeux de rôle) sont chiffrés avec le mot de passe de la formation. Le dossier `_build/` n'est plus publié sur GitHub Pages (voir `.github/workflows/static.yml`) ; il reste lisible dans le dépôt GitHub tant que celui-ci est public.

## Mot de passe de la formation

Il n'est écrit nulle part dans le dépôt. Pour régénérer le site, créez le fichier `_build/.mot_de_passe` (exclu par `.gitignore`) contenant le mot de passe, ou définissez la variable d'environnement `CPE_MDP`.

## Modifier le contenu

Les neuf ateliers sont dans **`_build/ateliers.py`** (l’atelier 2, « Construire mon année de CPE », est dans `_build/atelier_annee.py`) : problématique, situation, dossier documentaire (avec ses documents pièges), missions des groupes, étapes, rebondissements, controverses, critères de réussite, attendus, questions pour mettre en difficulté et diaporamas de bilan. La scénarisation (étapes, formats, durées, consignes et conduite du formateur) est dans `_build/scenarios.py`. Les éléments communs (références, compétences, programme) sont dans `_build/content.py`. Les pages HTML et les deux PDF (guide formateur, carnet) sont générés à partir de ces fichiers.

```bash
python3 _build/pdfs.py    # régénère le guide, le carnet et les dossiers d'atelier (nécessite reportlab)
python3 _build/build.py   # régénère toutes les pages HTML (après pdfs.py : les liens vers les pages des PDF en dépendent)
```

Ne modifiez pas directement les fichiers HTML générés : ils seraient écrasés à la génération suivante. Le style est dans `assets/site.css`, les comportements dans `assets/site.js`.

## Données personnelles

Les notes, la progression et le positionnement sont enregistrés uniquement dans le navigateur (`localStorage`, préfixe `cpe3:`). Rien n'est transmis à un serveur. Le lycée Horizon et toutes les situations sont fictifs : ne saisir aucune donnée réelle d'élève.

## Références

Textes vérifiés le 17 octobre 2026 : circulaire n° 2015-139 (missions des CPE), arrêté du 1er juillet 2013 (compétences), référentiel de formation des CPE 2026 (annexe 32, quatre blocs), circulaire du 17 septembre 2025 (cadre de gestion des AED), ressources Éduscol (procédures disciplinaires, protection de l'enfance, démocratie scolaire), programme pHARe, circulaire AEFE sur les instances.
