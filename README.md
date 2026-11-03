# jqshang.github.io

Personal academic website, built with [Astro](https://astro.build) and deployed to GitHub Pages by
`.github/workflows/deploy.yml` on every push to `master`.

## Editing content

All content lives in `src/data/`. Edit the YAML, nothing else:

| File | What |
| --- | --- |
| `profile.yaml` | Name, affiliation, links, bio |
| `publications.yaml` | Papers (title, authors, venue, links, BibTeX) |
| `projects.yaml` | Projects |
| `cv.yaml` | Experience, education, awards |

The CV PDF is `public/cv.pdf`; the photo is `public/images/profile.jpg`.

## Local preview

```sh
npm install
npm run dev        # http://localhost:4321, live reload
npm run build && npm run preview   # exactly what gets published
```

The previous AcademicPages site is preserved in git under the tag `v1-academicpages`
(`git checkout v1-academicpages` to look at it).
