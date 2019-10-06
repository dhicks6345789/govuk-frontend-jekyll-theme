# govuk-frontend-jekyll-theme
A Python script to construct a Jekyll theme based on the GOV.UK Design System minimum page template.

This script downloads the latest GOV.UK Design System archive directly from Github at:
https://github.com/alphagov/govuk-frontend/archive/master.zip

It then extracts the static asset files and compiled/minified Javascript files and places them in a Jeykll-compatible folder structure. It also copies accross SCSS files (not the compiled CSS files), ready for Jekyll to compile into CSS files, as well as adding a couple of SCSS files of its own.

Usage:

python3 package.py outputFolder

outputFolder can be an existing folder, one already with files in, this script will create a set of sub-folders if they don't already exist ("_sass", "_includes", "_layouts", "_plugins", "assets", "javascript") and populate them with appropriate files.

See the GOV.UK Frontend page for more details:
https://github.com/alphagov/govuk-frontend

In particular, the "Installing GOV.UK Frontend from dist" section is probably most relevant:
https://github.com/alphagov/govuk-frontend/blob/master/docs/installation/installing-from-dist.md
