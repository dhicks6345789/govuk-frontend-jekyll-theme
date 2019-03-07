#!/usr/bin/python3

import os

def copyFiles(src, dest, filetypes):
  for item in os.listdir(src):
    if os.path.isdir(src + os.sep + item):
      copyFiles(src + os.sep + item, dest + os.sep + item, fileTypes)
    else:
      if item.split["."][:-1].lower() in filetypes:
        print item

versionHandle = open("../govuk-frontend/dist/VERSION.txt")
govukFrontendVersion = versionHandle.read().strip()
versionHandle.close()

#os.makedirs("govuk-frontend", exist_ok=True)
#os.makedirs("govuk-frontend/assets", exist_ok=True)
#os.makedirs("govuk-frontend/javascript", exist_ok=True)
#os.makedirs("govuk-frontend/stylesheets", exist_ok=True)

#os.system("cp ../govuk-frontend/package/settings/*.scss ")
copyFiles("../govuk-frontend/package/settings", "_sass/settings", ["scss"])
