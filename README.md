# elwahizy.website

A small static website built with HTML and CSS. The current home page is a responsive image-grid layout demo.

## Project structure

- `website/index.html` — home page and image grid
- `website/about.html`, `website/jobs.html`, `website/contact.html` — placeholder pages
- `website/style.css` — shared layout, grid, navigation, and color styles
- `website/script.js` — currently empty
- `website/images/` — images used by the site

## Preview locally

From the repository root, start a static web server:

```sh
python3 -m http.server 8000 --directory website
```

Then open <http://localhost:8000> in a browser. No build step or package installation is required.

## Current design review

- The home page displays the image grid, but its navigation links all point to `#`; they do not lead to the other pages.
- About, Jobs, and Contact currently contain placeholder text and do not load the shared stylesheet.
- The home page's navigation list markup is malformed, and its images do not have alternative text.
- The grid's fixed minimum column width and large box padding may cause horizontal overflow on narrow screens.

These pages and responsive/accessibility details should be completed before treating the site as a finished multi-page website.
