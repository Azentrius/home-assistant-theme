# Security Policy

## Reporting a vulnerability

Please do **not** open a public issue for security problems.

Report them privately through GitHub instead:
[Report a vulnerability](https://github.com/Azentrius/home-assistant-theme/security/advisories/new)
(tab **Security → Report a vulnerability** in this repository).

Please include:

- what is affected (theme file, font script, release archive; version or commit),
- steps to reproduce,
- the impact you expect.

We aim to acknowledge reports within 7 days. This is a small project, so a fix
may take longer; we will keep you informed and credit you in the advisory
unless you prefer to stay anonymous.

## Supported versions

Only the latest release and the latest state of the `main` branch receive
security fixes.

## Especially relevant

The theme only sets CSS custom properties. The font script runs on every page
of Home Assistant once it is added with `extra_module_url`. Reports are
particularly welcome for:

- the font script loading anything other than the files next to it, or
  running anything other than adding the font faces,
- the release archive placing files outside `themes/` and `www/azentrius/`,
- release archives or `SHA256SUMS` that do not match the tagged source.
