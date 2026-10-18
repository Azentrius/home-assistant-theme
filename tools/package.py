#!/usr/bin/env python3
"""Builds the release archives and SHA256SUMS.

- azentrius-home-assistant-theme-VERSION.zip unpacks into the Home Assistant configuration folder:
  themes/azentrius.yaml and www/azentrius/ with the font script, the fonts, their licences,
  LICENSE and NOTICE.
- azentrius-hacs.zip holds only azentrius.yaml. HACS downloads it (hacs.json: zip_release) and
  unpacks it into /config/themes/azentrius/; without it, HACS would fetch every file of the release.

Both have the same bytes on every build (fixed times and modes, sorted entries). SHA256SUMS lists
the archives and every file in the full archive. Run with `make package`.
"""
# SPDX-License-Identifier: Apache-2.0
import hashlib
import json
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
THEME = ROOT / "themes" / "azentrius.yaml"


def full_entries():
    """Pairs of (path in the archive, file in the repository) for the full archive."""
    files = [("themes/azentrius.yaml", THEME)]
    for path in sorted((ROOT / "www" / "azentrius").iterdir()):
        if path.is_file():
            files.append((f"www/azentrius/{path.name}", path))
    files += [("www/azentrius/LICENSE", ROOT / "LICENSE"), ("www/azentrius/NOTICE", ROOT / "NOTICE")]
    return sorted(files)


def write_zip(archive, entries):
    """Writes the archive reproducibly; returns (path in the archive, sha256) per entry."""
    sums = []
    with zipfile.ZipFile(archive, "w") as z:
        for name, path in entries:
            data = path.read_bytes()
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data, compresslevel=9)
            sums.append((name, hashlib.sha256(data).hexdigest()))
    return sums


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    full = ROOT / f"azentrius-home-assistant-theme-{version}.zip"
    hacs = ROOT / json.loads((ROOT / "hacs.json").read_text(encoding="utf-8"))["filename"]
    inner = write_zip(full, full_entries())
    write_zip(hacs, [("azentrius.yaml", THEME)])
    lines = [f"{digest(full)}  {full.name}", f"{digest(hacs)}  {hacs.name}"]
    lines += [f"{sha}  {name}" for name, sha in inner]
    (ROOT / "SHA256SUMS").write_bytes(("\n".join(lines) + "\n").encode("ascii"))
    print(f"{full.name}, {hacs.name} and SHA256SUMS")


if __name__ == "__main__":
    main()
