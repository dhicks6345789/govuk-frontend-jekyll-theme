# govuk-frontend-jekyll-theme
A Python script to construct a Jekyll theme based on the GOV.UK Design System minimum page template.

This script downloads the latest GOV.UK Design System archive directly from Github at:
https://github.com/alphagov/govuk-frontend/archive/master.zip

It then extracts the static asset files and compiled/minified Javascript files and places them in a Jeykll-compatible folder structure. It also copies accross SCSS files (not the compiled CSS files), ready for Jekyll to compile into CSS files, as well as adding a couple of SCSS files of its own.

## Installation:

Simply clone the Git repository:

```
git clone https://github.com/dhicks6345789/govuk-frontend-jekyll-theme.git
```

## Usage:

```
python3 package.py outputFolder
```

outputFolder can be an existing folder, one already with files in (i.e. your existing Jekyll project folder), this script will create a set of sub-folders if they don't already exist ("_sass", "_includes", "_layouts", "_plugins", "assets", "javascript") and populate them with appropriate files. Existing files in the destination folder will be left alone, other than if their filename happens to match a file being copied over, in which case files will be overwritten.

## More Details

See the GOV.UK Frontend page for more details:
https://github.com/alphagov/govuk-frontend

In particular, the "Installing GOV.UK Frontend from dist" section is probably most relevant:
https://github.com/alphagov/govuk-frontend/blob/master/docs/installation/installing-from-dist.md
