#!/usr/bin/python3

import os

versionHandle = open("../govuk-frontend/dist/VERSION.txt")
govukFrontendVersion = versionHandle.read().strip()
versionHandle.close()

govukPackageFolder = "govuk-frontend-" + govukFrontendVersion
if not os.path.exists(govukPackageFolder):
  os.mkdir(govukPackageFolder)
