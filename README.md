<h1 align="center"> Anvil </h1> <br>

<p align="center">
  Just another autorigger
  <a href="http://riganvil.readthedocs.io/en/latest/">Online Documentation (ReadTheDocs)</a>
</p>


<div align="center">
  <!-- PyPi Package Info -->
  <a href="https://badge.fury.io/py/Anvil">
    <img src="https://badge.fury.io/py/Anvil.svg"
      alt="PyPi Package" />
  </a>
  <!-- CircleCI Build Status -->
  <a href="https://circleci.com/gh/AndresMWeber/Anvil/">
    <img src="https://circleci.com/gh/AndresMWeber/Anvil.svg?style=shield&circle-token=:circle-token"
      alt="Build Status" />
  </a>
  <!-- Coverage Stats -->
  <a href="https://coveralls.io/github/AndresMWeber/Anvil?branch=master/">
    <img src="https://coveralls.io/repos/github/AndresMWeber/Anvil/badge.svg?branch=master"
      alt="Coveralls Stats" />
  </a>
  <!-- LandscapeIO  -->
  <a href="https://landscape.io/github/AndresMWeber/Anvil/master">
    <img src="https://landscape.io/github/AndresMWeber/Anvil/master/landscape.svg?style=flat"
      alt="LandscapeIO" />
  </a>
  <!-- Codacy Rating -->
  <a href="https://www.codacy.com/app/AndresMWeber/Anvil?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=AndresMWeber/Anvil&amp;utm_campaign=Badge_Grade">
    <img src="https://api.codacy.com/project/badge/Grade/ef864a0c79984322b7809d64e3f036c8"
      alt="Codacy Rating" />
  </a>
</div>

Introduction
=============

My Autorigger.  Ain't yo business..yet!

Features
--------
-  Caching
-  Automated naming conventions
-  YAML Config
-  Online Documentation
-  Temp file generator
-  JSON file output
-  CLI access
-  Dict output
-  Automated Custom Docker Image Builds
-  Test suite automation using CircleCI
-  Automated testing in Maya versions 2015, 2016, 2017

Prerequisites
=============
To run Anvil locally you must have these installed:

- Maya (2015-2017)
- Python2.7 (or sudo access to pip install via mayapy)


Installation
============
#### Windows, etc.

A universal installation method (that works on Windows, Mac OS X, Linux, …, and always provides the latest version) is to use `pip`:

.. code-block:: bash

    # Make sure we have an up-to-date version of pip and setuptools:
    $ pip install --upgrade pip setuptools
    $ pip install Anvil


(If ``pip`` installation fails for some reason, you can try ``easy_install anvil`` as a fallback.)

Usage
=====
#### Python Package Usage

Use this tool via package level functions

.. code-block:: python

    import anvil
    anvil.lorem_ipsum()

Version Support
===============
This package supports only Maya 2015, 2016 and 2017 so far so please be aware...plans for 2018 are in the works.

Acknowledgments
===============
-  Marcus Ottosson - Without him I would not have been able to complete the docker side of things.



<h1 align="center"> Docker Image Documentation </h1> <br>

<p align="center">
  Adapted README from <a href="https://github.com/mottosso/docker-maya">Marcus Ottosson</a>
</p>

<div align="center">
  <!-- Docker Cloud and Layer-->
  <a href="https://cloud.docker.com/app/daemonecles/repository/docker/daemonecles/anvil/general">
    <img src="https://images.microbadger.com/badges/image/daemonecles/anvil.svg"
      alt="Docker Cloud" />
  </a>
  <!-- Latest Tag -->
  <a href="https://hub.docker.com/r/daemonecles/anvil/">
    <img src="https://images.microbadger.com/badges/version/daemonecles/anvil.svg"
      alt="LatestTag" />
  </a>
  <!-- Maya2017 Tag -->
  <a href="https://hub.docker.com/r/daemonecles/anvil/">
    <img src="https://images.microbadger.com/badges/version/daemonecles/anvil:maya2017.svg"
      alt="Maya2017Tag" />
  </a>
  <!-- Maya2016 Tag -->
  <a href="https://hub.docker.com/r/daemonecles/anvil/">
    <img src="https://images.microbadger.com/badges/version/daemonecles/anvil:maya2016.svg"
      alt="Maya2016Tag" />
  </a>
  <!-- Maya2015 Tag -->
  <a href="https://hub.docker.com/r/daemonecles/anvil/">
    <img src="https://images.microbadger.com/badges/version/daemonecles/anvil:maya2015.svg"
      alt="Maya2015Tag" />
  </a>
</div>

### Supported tags

- `maya2015`, `maya2016`, `maya2017`

Each tag represents a particular version of Maya, such as maya2016. In this image, `python` is an alias to `maya/bin/mayapy` which has the following Python packages installed via `pip`.
For more information about this image and its history, please see its the [GitHub repository][1]

[1]: https://github.com/andresmweber/anvil/wiki

### Usage

To use this image and any of it's supported tags, use `docker run`.

```bash
$ docker run -ti --rm daemonecles/anvil
```

Without a "tag", this would download the latest available image of Maya. You can explicitly specify a version with a tag.

```bash
$ docker run -ti --rm daemonecles/anvil:2017
```

Images occupy around **5 gb** of virtual disk space once installed, and about **1.5 gb** of bandwidth to download.

### Example

This example will run the latest available version of Maya, create a new scene and save it in your current working directory.

```bash
$ docker run -ti -v $(pwd):/root/workdir --rm daemonecles/maya2016
$ mayapy
>>> from maya import standalone, cmds
>>> standalone.initialize()
>>> cmds.file(new=True)
>>> cmds.polySphere(radius=2)
>>> cmds.file(rename="my_scene.ma")
>>> cmds.file(save=True, type="mayaAscii")
>>> exit()
$ cp /root/maya/projects/default/scenes/my_scene.ma workdir/my_scene.ma
$ exit
$ cat my_scene.ma
```

### What's in this image?

This image builds on [daemonecles/anvil][2] which has the following software installed.

- [Centos6](https://www.centos.org/download/)
- [git](https://git-scm.com/) - old version
- [pip2.6](https://pip.pypa.io/en/stable/)
- [python2.6](https://www.python.org/download/releases/2.6.6/)

Additional installations include.

- [python2.7](https://www.python.org/download/releases/2.7.4/)
- [pip2.7](https://pip.pypa.io/en/stable/)
- [git](https://git-scm.com/) - up to date (for CircleCI checkout)

[2]: (https://registry.hub.docker.com/u/daemonecles/anvil/)

## Environment variables
* `$MAYA_VERSION=####`: for getting the installed maya version quickly in the format #### - e.g. - 2017.
* `$PYTHON_PATH=$HOME/nvenv/lib/python2.7/site-packages`: Placeholder for your test runner virtualenv named "nvenv" so maya can access the installed packages.
* `$TEST_PATH=$HOME/test-results`: A default directory where the user can place test resulting xml files etc.

## Feedback
### Issues/Contributing

If you have any problems with or questions about contributing to this image, please contact Marcus Ottosson through a [GitHub issue][3] (since the image is basically his with minor additions)

[3]: https://github.com/mottosso/docker-maya/issues
