# Legal document generator

This folder keeps legal pages for every Doo Games Studio app in one place.

## Structure

- `templates/` contains the HTML templates for Terms and Privacy with placeholders.
- `apps.json` holds the metadata for each app (name, slug, contact, effective date, etc.).
- `build_legals.py` fills the templates with the metadata and writes:
  - `legal/apps/<slug>/terms.html` and `privacy-policy.html` for every app.
  - `legal/terms.html` and `legal/privacy-policy.html` for whichever app is listed as `default_app`.

The generated pages share the same styles and wording so you only need to maintain one source of truth.

## Adding or updating an app

1. Update `apps.json`: add or edit an app entry and make sure the `slug` value matches the directory name you want under `apps/`. Adjust `effective_date`, `name`, or `contact_email` as needed.
2. If you want a different app to be the default root document, change `default_app` to its slug.
3. Run `python legal/build_legals.py` from the repo root. This regenerates every legal page.
4. Publish the appropriate URLs inside the App Store and Google Play (e.g., use `legal/apps/chrono-merge/terms.html` for Chrono Merge).

## Notes

- The templates contain shared copy about App Store and Google Play requirements. Edit them only when you want to change the overall tone or obligations across all apps.
- `build_legals.py` requires Python 3 (3.8+) to render the templates; you can also duplicate one of the generated files and tweak the placeholders manually if Python is unavailable.
- You can extend the metadata or add new placeholders if a specific app needs unique sections.
