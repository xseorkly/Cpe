# Entrer dans le métier de CPE

Formation des CPE débutants du réseau AEFE : neuf ateliers progressifs, 13 h 30 sur 2 jours.
Site statique publié avec GitHub Pages : https://xseorkly.github.io/Cpe/

## Ce que contient le site

| Page | Public | Rôle |
| --- | --- | --- |
| `index.html` | Stagiaires | Accueil, public, finalité, les 9 ateliers |
| `positionnement.html` | Stagiaires | Autopositionnement avant l'atelier 1 et après l'atelier 8 |
| `atelier-1.html` à `atelier-9.html` | Stagiaires | Situations-problèmes : réaction spontanée, enquête en groupes experts dans un dossier documentaire, rebondissement, controverse, production, retour réflexif, bilan projetable |
| `carnet.html` | Stagiaires | Toutes les notes réunies ; export Markdown, sauvegarde JSON, import, effacement |
| `mallette.html` | Stagiaires | Neuf fiches réflexes à construire au fil des ateliers |
| `ressources.html` | Stagiaires | PDF, approfondissements, textes de référence, compétences C1 à C8 et blocs 2026 |
| `approfondir/` | Stagiaires | Six pages de savoirs développés, liées aux ateliers |
| `formateur/` | Formateur | Programme minuté, fiches par atelier : déroulé, questions pour mettre en difficulté, attendus, vigilance, dossier imprimable, diaporama |
| `ressources/` | Tous | Guide formateur, carnet, banque de prompts IA, mallette réflexe (PDF) |

L'espace `formateur/` n'est lié depuis aucune page stagiaire et il est exclu des moteurs de recherche (`robots.txt`, `noindex`). Ce n'est pas une protection : toute page publiée sur GitHub Pages est accessible à qui connaît son adresse.

## Modifier le contenu

Les neuf ateliers sont dans **`_build/ateliers.py`** (l’atelier 2, « Construire mon année de CPE », est dans `_build/atelier_annee.py`) : problématique, situation, dossier documentaire (avec ses documents pièges), missions des groupes, étapes, rebondissements, controverses, critères de réussite, attendus, questions pour mettre en difficulté et diaporamas de bilan. Les éléments communs (références, compétences, programme) sont dans `_build/content.py`. Les pages HTML et les deux PDF (guide formateur, carnet) sont générés à partir de ces fichiers.

```bash
python3 _build/build.py   # régénère toutes les pages HTML
python3 _build/pdfs.py    # régénère le guide formateur et le carnet (nécessite reportlab)
```

Ne modifiez pas directement les fichiers HTML générés : ils seraient écrasés à la génération suivante. Le style est dans `assets/site.css`, les comportements dans `assets/site.js`.

## Données personnelles

Les notes, la progression et le positionnement sont enregistrés uniquement dans le navigateur (`localStorage`, préfixe `cpe3:`). Rien n'est transmis à un serveur. Le lycée Horizon et toutes les situations sont fictifs : ne saisir aucune donnée réelle d'élève.

## Références

Textes vérifiés le 17 octobre 2026 : circulaire n° 2015-139 (missions des CPE), arrêté du 1er juillet 2013 (compétences), référentiel de formation des CPE 2026 (annexe 32, quatre blocs), circulaire du 17 septembre 2025 (cadre de gestion des AED), ressources Éduscol (procédures disciplinaires, protection de l'enfance, démocratie scolaire), programme pHARe, circulaire AEFE sur les instances.
