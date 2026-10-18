# Azentrius for Home Assistant

A Home Assistant theme in the colours and type of the Azentrius Design System: ink, paper and gold,
set in DM Sans. Light and dark mode follow the setting in your Home Assistant profile.

## What it changes

- **Action colour:** ink in light mode, gold in dark mode. Buttons, switches, sliders, tabs and the
  selected sidebar entry use it, with white text on ink and ink text on gold.
- **Surfaces:** header and sidebar sit on the page ground (paper in light mode, ink in dark mode).
  Cards are flat with a thin border and a 16 px radius; dialogs have a 24 px radius.
- **Text, lines and focus:** warm greys for secondary text and borders, a bronze or gold focus ring
  and links.
- **Status:** success, warning, error and information in the design system's colours. The badge and
  dot in the sidebar that point to new notifications use the information colour; gold is never a
  status.
- **Type:** DM Sans for the interface, Red Hat Mono for code, once you add the fonts (see
  [Fonts](#fonts)). Titles use weight 600.

What stays Home Assistant's: the colours of device states (amber for a light that is on, orange for
heating, blue for cooling, and so on), sizes and spacing, icons and texts. The theme only sets
values; it adds no content.

## Install with HACS

1. In HACS, open the menu, choose **Custom repositories** and add
   `https://github.com/Azentrius/home-assistant-theme` with the type **Theme**.
2. Download **Azentrius**. HACS puts the files of the release into `/config/themes/azentrius/`;
   Home Assistant reads `azentrius.yaml` from there and ignores the rest.
3. Make sure `configuration.yaml` loads the themes folder:

   ```yaml
   frontend:
     themes: !include_dir_merge_named themes
   ```

4. Run the action **Home Assistant Frontend: Reload themes**, or restart Home Assistant if you just
   added the line above.
5. Pick **Azentrius** under **Profile › Theme**. To make it the default for everyone, run the action
   `frontend.set_theme` with `name: Azentrius`. A choice in a profile wins over the default.

## Install by hand

1. Download `azentrius-home-assistant-theme-VERSION.zip` and `SHA256SUMS` from the
   [latest release](https://github.com/Azentrius/home-assistant-theme/releases/latest) and check
   them (see [Check a download](#check-a-download)).
2. Unpack the archive into your Home Assistant configuration folder (`/config`). It contains
   `themes/azentrius.yaml` and the folder `www/azentrius/` with the fonts.
3. Continue with steps 3 to 5 above, and add the fonts as described below.

## Fonts

HACS installs only the theme file. Without the fonts, Home Assistant shows the theme in your
system's sans-serif, which works but is not DM Sans. To add them:

1. Copy the folder `www/azentrius/` from the release archive to `/config/www/azentrius/`.
2. Load its script on every page, in `configuration.yaml`:

   ```yaml
   frontend:
     extra_module_url:
       - /local/azentrius/azentrius.js
   ```

3. Restart Home Assistant.

Your own Home Assistant serves the fonts; nothing is loaded from anywhere else. Home Assistant makes
everything in `/config/www` available under `/local/` without signing in, so that folder holds only
the script, the fonts and their licences.

## Compatibility

Tested with Home Assistant 2026.10 (frontend 20260930.4). Home Assistant promises only
`primary-color`, `accent-color` and the state colours as the interface for themes. This theme also
sets newer variables such as `ha-color-…` and `ha-switch-…`, which can change with a frontend
update. If something looks wrong after an update, please
[open an issue](https://github.com/Azentrius/home-assistant-theme/issues).

## Check a download

Every release has a `SHA256SUMS` file and a signed build provenance from this repository's release
workflow:

```sh
sha256sum --ignore-missing -c SHA256SUMS
gh attestation verify azentrius-home-assistant-theme-VERSION.zip --repo Azentrius/home-assistant-theme
```

`SHA256SUMS` also lists every file inside the archive, so you can check the unpacked files in
`/config` the same way, and `azentrius.yaml`, the theme file a release also carries on its own for
HACS.

## How it is made

The theme is generated from the tokens of the Azentrius Design System, which also styles the
Azentrius Cockpit add-ons. Colour pairs are checked for contrast in both modes when the theme is
generated: text at least 4.5:1, borders, focus ring and controls at least 3:1. Changes to colours
start in the design system and come here as a new release.

## License

The theme and the font script are licensed under the [Apache License 2.0](LICENSE). The fonts DM Sans
and Red Hat Mono are licensed under the SIL Open Font License 1.1; their licence texts are in
`www/azentrius/`. The Apache License grants no rights to the name Azentrius or its marks; see
[NOTICE](NOTICE).
