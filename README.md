# pytest-pattern
Plugin for pytest to add fuzzy string matching.

## Installation

Currently, this is hosted on the [Springload index](https://springload.github.io/python-package-index/) - 
to install, use pip like usual, but add the extra index url:

```
pip install pytest-pattern --extra-index-url=https://springload.github.io/python-package-index/
```

or in a requirements.txt file like:

```
--extra-index-url=https://springload.github.io/python-package-index/
pytest-pattern==0.0
```

## Release process

To release a new version, 
1. Update the version in the setup.cfg file.
2. Tag the commit once on the main branch with `vM.m` format tag. 
3. Create a release in github.
4. Add another link to [the SL index pytest-pattern](https://springload.github.io/python-package-index/pytest-pattern) page in the [repo](https://github.com/springload/python-package-index/edit/main/pytest-pattern/index.html).
