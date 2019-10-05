#!/usr/bin/python3

import os
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

zipArchive = open("master.zip", "wb")
zipArchive.write(urllib.request.urlopen("https://github.com/alphagov/govuk-frontend/archive/master.zip").read())
zipArchive.close()

zipRef = zipfile.ZipFile("master.zip", "r")
zipRef.extractall("master")

print("https://github.com/alphagov/govuk-frontend/archive/master.zip")
        
exit(0)
        
versionHandle = open("../govuk-frontend/dist/VERSION.txt")
govukFrontendVersion = versionHandle.read().strip()
versionHandle.close()
govukFrontendFolder = "govuk-frontend-" + govukFrontendVersion

# Copy over the SCSS files from govuk-frontend
copyFiles("../govuk-frontend/package", "_sass", ["scss"])
for folder in ["components","core","helpers","objects","overrides","settings","tools","utilities","vendor"]:
  copyFiles("../govuk-frontend/package/" + folder, "_sass/" + folder, ["scss"])

# Copy over compiled / minified Javascript files.
copyFiles("../govuk-frontend/dist", govukFrontendFolder + "/javascript", ["js"])

copyFiles("../govuk-frontend/dist/assets/fonts", govukFrontendFolder + "/assets/fonts", ["woff","woff2","eot"])
copyFiles("../govuk-frontend/dist/assets/images", govukFrontendFolder + "/assets/images", ["ico","png","svg"])
