# Development Instructions

## Prereqs

You need pipenv to use this package.  Install it with `pip install pipenv`

## Pushing a new version

In order to push a new version, you need to create a `~/.pypirc` file with the following contents:

```
[distutils]
index-servers =
	metify-internal

[metify-internal]
repository=https://download.metify.io/repository/pypi-internal/
username=USER
password=PASS
```

After creating the file, run:

```
chmod 600 ~/.pypirc
```

Make sure to bump the version number in `setup.cfg`.

Then run `make publish`