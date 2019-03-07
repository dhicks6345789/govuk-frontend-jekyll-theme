#!/usr/bin/python3
versionHandle = open("../govuk-frontend/package/dist/VERSION.txt")
govukFrontendVersion = versionHandle.read().strip()
versionHandle.close()
print(govukFrontendVersion)
