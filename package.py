#!/usr/bin/python3

import os

versionHandle = open("../govuk-frontend/dist/VERSION.txt")
govukFrontendVersion = versionHandle.read().strip()
versionHandle.close()

os.makedirs("govuk-frontend", exist_ok=True)
os.makedirs("govuk-frontend/assets", exist_ok=True)
os.makedirs("govuk-frontend/javascript", exist_ok=True)
os.makedirs("govuk-frontend/stylesheets", exist_ok=True)
