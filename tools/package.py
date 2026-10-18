#!/usr/bin/env python3
"""Builds the release archive and SHA256SUMS.

azentrius-home-assistant-theme-VERSION.zip unpacks into the Home Assistant configuration folder:
themes/azentrius.yaml and www/azentrius/ with the font script, the fonts, their licences, LICENSE
and NOTICE. It has the same bytes on every build (fixed times and modes, sorted entries).

A release also carries themes/azentrius.yaml on its own: HACS downloads every file of a theme's
release into /config/themes/azentrius/ and uses the YAML file among them. SHA256SUMS lists the
archive, that file and every file in the archive. Run with `make package`.
"""
# SPDX-License-Identifier: Apache-2.0
import hashlib
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
THEME = ROOT / "themes" / "azentrius.yaml"


def entries():
    """Pairs of (path in the archive, file in the repository)."""
    files = [("themes/azentrius.yaml", THEME)]
    for path in sorted((ROOT / "www" / "azentrius").iterdir()):
        if path.is_file():
            files.append((f"www/azentrius/{path.name}", path))
    files += [("www/azentrius/LICENSE", ROOT / "LICENSE"), ("www/azentrius/NOTICE", ROOT / "NOTICE")]
    return sorted(files)


def main():
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    archive = ROOT / f"azentrius-home-assistant-theme-{version}.zip"
    inner = []
    with zipfile.ZipFile(archive, "w") as z:
        for name, path in entries():
            data = path.read_bytes()
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data, compresslevel=9)
            inner.append(f"{hashlib.sha256(data).hexdigest()}  {name}")
    lines = [
        f"{hashlib.sha256(archive.read_bytes()).hexdigest()}  {archive.name}",
        f"{hashlib.sha256(THEME.read_bytes()).hexdigest()}  {THEME.name}",
    ] + inner
    (ROOT / "SHA256SUMS").write_bytes(("\n".join(lines) + "\n").encode("ascii"))
    print(f"{archive.name} and SHA256SUMS")


if __name__ == "__main__":
    main()
