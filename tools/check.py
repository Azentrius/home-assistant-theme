#!/usr/bin/env python3
"""Checks the theme, the font script, the fonts and the files around them.

Run with `make check`. Needs PyYAML (tools/requirements.txt).
"""
# SPDX-License-Identifier: Apache-2.0
import json
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
THEME = ROOT / "themes" / "azentrius.yaml"
FONT_DIR = ROOT / "www" / "azentrius"
SCRIPT = FONT_DIR / "azentrius.js"
NAME = "Azentrius"

HEX = re.compile(r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})")
KEY = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
SEMVER = re.compile(r"[0-9]+\.[0-9]+\.[0-9]+(?:-[0-9A-Za-z.]+)?")
SPDX = "SPDX-License-Identifier: Apache-2.0"

errors = []


def fail(message):
    errors.append(message)


def check_theme():
    text = THEME.read_text(encoding="utf-8")
    if SPDX not in "\n".join(text.splitlines()[:10]):
        fail(f"{THEME.name}: no SPDX header")
    data = yaml.safe_load(text)
    if not isinstance(data, dict) or list(data) != [NAME]:
        fail(f"{THEME.name}: must define exactly one theme, {NAME}")
        return
    theme = data[NAME]
    modes = theme.get("modes")
    if not isinstance(modes, dict) or set(modes) != {"light", "dark"}:
        fail(f"{THEME.name}: needs modes light and dark")
        return
    shared = {k: v for k, v in theme.items() if k != "modes"}
    light, dark = modes["light"], modes["dark"]
    if set(light) != set(dark):
        fail(f"{THEME.name}: light and dark set different variables: {sorted(set(light) ^ set(dark))}")
    both = set(shared) & set(light)
    if both:
        fail(f"{THEME.name}: set at the top and in the modes: {sorted(both)}")
    for scope, values in (("top", shared), ("light", light), ("dark", dark)):
        for key, value in values.items():
            if not KEY.fullmatch(str(key)):
                fail(f"{THEME.name} ({scope}): {key!r} is not a CSS variable name")
            if not isinstance(value, str) or not value.strip():
                fail(f"{THEME.name} ({scope}): {key} must be a non-empty string")
            elif value.startswith("#") and not HEX.fullmatch(value):
                fail(f"{THEME.name} ({scope}): {key} has an invalid colour {value!r}")
    return shared


def check_fonts(shared):
    script = SCRIPT.read_text(encoding="utf-8")
    if SPDX not in script:
        fail(f"{SCRIPT.name}: no SPDX header")
    if re.search(r"https?://|//[a-z0-9.-]+\.[a-z]{2,}/", script, re.IGNORECASE):
        fail(f"{SCRIPT.name}: must not load anything from another host")
    referenced = set(re.findall(r"\$\{base\}([A-Za-z0-9._-]+)", script))
    present = {p.name for p in FONT_DIR.glob("*.woff2")}
    if referenced != present:
        fail(f"{SCRIPT.name}: references {sorted(referenced)}, folder has {sorted(present)}")
    for name in sorted(present):
        if (FONT_DIR / name).read_bytes()[:4] != b"wOF2":
            fail(f"{name}: not a WOFF2 file")
    declared = set(re.findall(r'font-family: "([^"]+)"', script))
    if shared:
        for key in ("ha-font-family-body", "ha-font-family-code"):
            first = re.match(r'\s*"?([^",]+)"?', shared.get(key, ""))
            if not first or first.group(1) not in declared:
                fail(f"{SCRIPT.name}: does not declare the font of {key}")
    notice = (ROOT / "NOTICE").read_text(encoding="utf-8")
    for name in sorted(present):
        if f"www/azentrius/{name}" not in notice:
            fail(f"NOTICE: {name} is not listed")
    for licence in re.findall(r"see (www/azentrius/\S+)", notice):
        if not (ROOT / licence).is_file():
            fail(f"NOTICE: {licence} does not exist")


def check_repository():
    hacs = json.loads((ROOT / "hacs.json").read_text(encoding="utf-8"))
    if hacs.get("name") != NAME:
        fail(f"hacs.json: name must be {NAME}")
    # Without zip_release, HACS downloads every file of a release into the theme folder.
    if hacs.get("zip_release") is not True or not str(hacs.get("filename", "")).endswith(".zip"):
        fail("hacs.json: needs zip_release and the filename of the HACS archive")
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not SEMVER.fullmatch(version):
        fail(f"VERSION: {version!r} is not a version like 1.0.0")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    if not re.search(rf"^## {re.escape(version)}( |$)", changelog, re.MULTILINE):
        fail(f"CHANGELOG.md: no section for {version}")
    for path in sorted((ROOT / "tools").glob("*")):
        if path.suffix in (".py", ".sh") and SPDX not in path.read_text(encoding="utf-8"):
            fail(f"{path.relative_to(ROOT)}: no SPDX header")


def main():
    shared = check_theme()
    check_fonts(shared)
    check_repository()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    print("theme, font script, fonts, licences and changelog: ok")


if __name__ == "__main__":
    main()
