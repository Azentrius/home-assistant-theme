# Changelog

## 1.0.6 – 2026-10-25

The product name in the files and the release title; the theme itself is unchanged.

- **Name:** `NOTICE`, the first line of `themes/azentrius.yaml` and of `www/azentrius/azentrius.js`
  and the release title say Azentrius Theme, as the README does, instead of "Azentrius for Home
  Assistant". In HACS and in the profile's theme list it stays Azentrius, so installed themes and
  `frontend.set_theme` keep working.
- **README:** "Made by Azentrius" links to azentrius.com.

## 1.0.5 – 2026-10-18

The theme gets its product name; the theme itself is unchanged.

- **README:** the heading names it Azentrius Theme, as the Azentrius design system does. In HACS
  and in the profile's theme list it stays Azentrius, so installed themes and `frontend.set_theme`
  keep working.
- **README:** ends with "Made by Azentrius", like the other Azentrius repositories.

## 1.0.4 – 2026-10-18

Two fixes for dark mode.

- **Avatar:** the initials in the user avatar at the bottom of the sidebar were barely visible in
  dark mode, dark grey on dark grey. The theme now sets `text-light-primary-color`, so they show in
  the text colour in both modes.
- **Input fields:** in dark mode, text fields in dialogs had the same colour as the dialog and showed
  only their bottom line. They now sit a step darker, on the page ground, and turn lighter on hover.
  Light mode is unchanged.
- **README:** new screenshots with both fixes.

## 1.0.3 – 2026-10-18

Screenshots for the HACS store; the theme is unchanged.

- **README:** screenshots of a settings page with switches and of a dialog, in light and dark mode,
  taken in the Home Assistant demo.
- **HACS:** the validation in CI now runs every check, including the one for images in the README, as
  the HACS default repositories require.

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
