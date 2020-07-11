---
title: Build and publish the course material
parent: manual.md
---

### Convert to html, slideshow and pdf

Use [nbcourse](https://gitlab.math.unistra.fr/boileau/nbcourse):

```bash
nbcourse list
build_book          Build pdf book
build_pages         Build html pages
convert_to_html     Convert executed notebook to html page
convert_to_slides   Convert executed notebook to reveal slides
copy_material       Copy notebook and theme material to output directory
copy_reveal         Copy reveal.js to output directory
execute_notebooks   Write executed notebooks to output directory
output_dir          Create empty output directory
zip_archive         Build a single zip archive for all material
zip_chapters        Build zip archives for single chapter downloads
```

Edit the `nbcourse.yml` file and run:

```bash
nbcourse [-n 4] [target]  # [to run on 4 parallel threads]
```

The result will be located in `build/` directory.

### Publish with GitLab Pages

Publishing with [GitLab Pages](https://docs.gitlab.com/ee/user/project/pages/) is as simple as adding a `.gitlab-ci.yml` such as:

```yaml
pages:
  image: boileaum/jupyter
  script:
    - pip install nbcourse
    - nbcourse -n 5
    - mv build public
  artifacts:
    paths:
      - public
```
