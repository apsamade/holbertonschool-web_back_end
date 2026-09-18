# i18n

A learning project on internationalization (i18n) and localization (l10n)
of a Flask application using Flask-Babel and pytz.

## Topics

- Parametrizing Flask templates to display different languages.
- Inferring the correct locale from URL parameters, user settings or
  request headers.
- Localizing timestamps by inferring the appropriate time zone.

## Files

Each `N-app.py` builds on the previous one:

- `0-app.py` — basic Flask app with a single `/` route.
- `1-app.py` — Babel setup with a `Config` class and supported languages.
- `2-app.py` — locale selected from the request `Accept-Language` header.
- `3-app.py` — templates parametrized with `gettext` message IDs.
- `4-app.py` — locale forced via a `locale` URL parameter.
- `5-app.py` — mock login via a `login_as` URL parameter.
- `6-app.py` — locale prioritized: URL, user settings, headers, default.
- `7-app.py` — time zone inferred and validated with `pytz`.

## Translations

Message catalogs live under `translations/[en|fr]/LC_MESSAGES/`. Regenerate
them with `pybabel extract`, `init`, and `compile` using `babel.cfg`.
