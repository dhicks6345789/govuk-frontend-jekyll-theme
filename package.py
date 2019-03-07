#!/usr/bin/python3
versionHandle = open("../govuk-frontend/dist/VERSION.txt")
govukFrontendVersion = versionHandle.read().strip()
versionHandle.close()
print(govukFrontendVersion)
