#!/usr/bin/python3

import os
import sys
import shutil
import zipfile
import urllib.request

def mkdir(thePath):
  if not os.path.exists(thePath):
    os.mkdir(thePath)

def copyFiles(src, dest, filetypes):
  for item in os.listdir(src):
    if os.path.isdir(src + os.sep + item):
      copyFiles(src + os.sep + item, dest + os.sep + item, filetypes)
    else:
      if item.split(".")[-1].lower() in filetypes:
        os.makedirs(dest, exist_ok=True)
        shutil.copy(src + os.sep + item, dest + os.sep + item)

outputFolder = ""
if len(sys.argv) < 2:
  print("Generates a Jekyll-compatible template from the GOV.UK Design System frontend.")
  print("Usage: python3 package.py outputFolder")
  sys.exit(0)
  
outputFolder = sys.argv[1]
        
zipArchive = open("master.zip", "wb")
zipArchive.write(urllib.request.urlopen("https://github.com/alphagov/govuk-frontend/archive/master.zip").read())
zipArchive.close()
zipfile.ZipFile("master.zip", "r").extractall("master")

versionHandle = open("master/govuk-frontend-master/dist/VERSION.txt")
govukFrontendVersion = versionHandle.read().strip()
versionHandle.close()

mkdir(outputFolder)
mkdir(outputFolder + os.sep + "_sass")
mkdir(outputFolder + os.sep + "_includes")
mkdir(outputFolder + os.sep + "_layouts")
mkdir(outputFolder + os.sep + "_plugins")
mkdir(outputFolder + os.sep + "assets")
mkdir(outputFolder + os.sep + "javascript")

# Copy over the SCSS files from govuk-frontend
copyFiles("master" + os.sep + "govuk-frontend-master" + os.sep + "package" + os.sep + "govuk", outputFolder + os.sep + "_sass", ["scss"])

# Copy over our includes folder.
copyFiles("_includes", outputFolder + os.sep + "_includes", ["html"])

# Copy over our layouts folder.
copyFiles("_layouts", outputFolder + os.sep + "_layouts", ["html"])

# Copy over our plugins folder.
copyFiles("_plugins", outputFolder + os.sep + "_plugins", ["rb"])

# Copy over compiled / minified Javascript files.
copyFiles("master" + os.sep + "govuk-frontend-master" + os.sep + "dist", outputFolder + os.sep + "javascript", ["js"])

# Copy over the govuk-frontend static assets (fonts, icons, images).
copyFiles("master" + os.sep + "govuk-frontend-master" + os.sep + "dist" + os.sep + "assets", outputFolder + os.sep + "assets", ["woff","woff2","eot","ico","png","svg"])
