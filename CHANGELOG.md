# Changelog

## 1.0.2 – 2026-10-18

Fixes the download with HACS, this time for good.

- **HACS:** for a theme, HACS builds the address of a zip release with `tags/` in it, which GitHub
  answers with "not found", so 1.0.1 could not be installed either. Releases now carry
  `azentrius.yaml` itself, next to the archive and `SHA256SUMS`; HACS downloads these files into
  `/config/themes/azentrius/`, and Home Assistant reads the YAML file among them. `hacs.json` no
  longer asks for a zip release, and `azentrius-hacs.zip` is gone.

## 1.0.1 – 2026-10-18

Fixes the download with HACS.

- **HACS:** HACS downloads every file of a theme's release, so 1.0.0 put the archives into
  `/config/themes/azentrius/` instead of the theme. Releases now carry `azentrius-hacs.zip` with only
  `azentrius.yaml`, and `hacs.json` points HACS to it (`zip_release`). The theme lands in
  `/config/themes/azentrius/azentrius.yaml`.

## 1.0.0 – 2026-10-18

First release: the Azentrius theme for Home Assistant, with light and dark mode and the fonts as an
optional download.

- **Theme:** `themes/azentrius.yaml`, one theme with `light` and `dark` modes, generated from the
  Azentrius Design System and tested with Home Assistant 2026.10.
- **Fonts:** `www/azentrius/azentrius.js` loads DM Sans and Red Hat Mono from `/local/azentrius/`
  when added with `extra_module_url`.
- **Release archive:** `azentrius-home-assistant-theme-VERSION.zip` with the theme, the fonts and
  their licences, ready to unpack into `/config`, with `SHA256SUMS` and a signed build provenance.
