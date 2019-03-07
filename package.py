#!/usr/bin/python3

import os
import shutil

def copyFiles(src, dest, filetypes):
  for item in os.listdir(src):
    if os.path.isdir(src + os.sep + item):
      copyFiles(src + os.sep + item, dest + os.sep + item, filetypes)
    else:
      if item.split(".")[-1].lower() in filetypes:
        os.makedirs(dest, exist_ok=True)
        shutil.copy(src + os.sep + item, dest + os.sep + item)

versionHandle = open("../govuk-frontend/dist/VERSION.txt")
govukFrontendVersion = versionHandle.read().strip()
versionHandle.close()

for folder in ["components","core","helpers","objects","overrides","settings","tools","utilities","vendor"]:
  copyFiles("../govuk-frontend/package/" + folder, "_sass/" + folder, ["scss"])
