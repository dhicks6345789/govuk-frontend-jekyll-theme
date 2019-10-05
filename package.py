#!/usr/bin/python3

import os
import sys
import shutil
import zipfile
import urllib.request

def copyFiles(src, dest, filetypes):
  for item in os.listdir(src):
    if os.path.isdir(src + os.sep + item):
      copyFiles(src + os.sep + item, dest + os.sep + item, filetypes)
    else:
      if item.split(".")[-1].lower() in filetypes:
        os.makedirs(dest, exist_ok=True)
        shutil.copy(src + os.sep + item, dest + os.sep + item)

if len(sys.argv) < 3:
  print("Generates a Jekyll-compatible template from the GOV.UK Design System frontend.")
  print("See the GOV.UK frontend documentation on Github for more details of the Design System frontend itself:")
  print("https://github.com/alphagov/govuk-frontend")
  print("")
  print("Usage: python3 package.py outputFolder")
        
zipArchive = open("master.zip", "wb")
zipArchive.write(urllib.request.urlopen("https://github.com/alphagov/govuk-frontend/archive/master.zip").read())
zipArchive.close()
zipfile.ZipFile("master.zip", "r").extractall("master")

versionHandle = open("master/govuk-frontend-master/dist/VERSION.txt")
govukFrontendVersion = versionHandle.read().strip()
versionHandle.close()

exit(0)

# Copy over the SCSS files from govuk-frontend
copyFiles("../govuk-frontend/package", "_sass", ["scss"])
for folder in ["components","core","helpers","objects","overrides","settings","tools","utilities","vendor"]:
  copyFiles("../govuk-frontend/package/" + folder, "_sass/" + folder, ["scss"])

# Copy over compiled / minified Javascript files.
copyFiles("../govuk-frontend/dist", govukFrontendFolder + "/javascript", ["js"])

copyFiles("../govuk-frontend/dist/assets/fonts", govukFrontendFolder + "/assets/fonts", ["woff","woff2","eot"])
copyFiles("../govuk-frontend/dist/assets/images", govukFrontendFolder + "/assets/images", ["ico","png","svg"])
