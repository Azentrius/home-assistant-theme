# SPDX-License-Identifier: Apache-2.0
.PHONY: check package

# Theme, font script, fonts, licences and changelog (needs tools/requirements.txt)
check:
	python3 tools/check.py

# azentrius-home-assistant-theme-VERSION.zip and SHA256SUMS, the same bytes every time
package:
	python3 tools/package.py
