#!/usr/bin/python3

import os
import shutil

def copyFiles(src, dest, filetypes):
  for item in os.listdir(src):
    if os.path.isdir(src + os.sep + item):
      copyFiles(src + os.sep + item, dest + os.sep + item, fileTypes)
    else:
      if item.split(".")[-1].lower() in filetypes:
        os.makedirs(dest, exist_ok=True)
        shutil.copy(src + os.sep + item, dest + os.sep + item)

versionHandle = open("../govuk-frontend/dist/VERSION.txt")
govukFrontendVersion = versionHandle.read().strip()
versionHandle.close()

#os.system("cp ../govuk-frontend/package/settings/*.scss ")
copyFiles("../govuk-frontend/package/settings", "_sass/settings", ["scss"])
