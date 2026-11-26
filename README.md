# Elwahizy

Source for the Elwahizy website: a small, plain static site (HTML + CSS, no build step, no framework).

## Pages

| File | Page |
| --- | --- |
| `index.html` | Home |
| `about.html` | About |
| `jobs.html` | Opportunities |
| `contact.html` | Contact |

Shared styles live in `style.css`; images in `images/img/`.

## Local preview

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000>.

## Checks

```bash
python3 scripts/validate.py
```

Verifies pages exist, local `href`/`src` targets resolve, each page has a title, viewport, `lang`, and alt text on images, and no placeholder text remains.

## Deployment

GitHub Pages, **Deploy from a branch**: branch `main`, folder `/ (root)`. `.nojekyll` disables Jekyll processing so files are served as-is.

No custom domain is configured.

## Notes

- Never commit secrets, API keys, or private contact details to this repository.
- Contact details and openings are intentionally not published yet.
