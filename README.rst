Anvil: Just another autorigger
###################################################################################################
`Online Documentation (ReadTheDocs) <http://riganvil.readthedocs.io/en/latest/>`_

.. image:: https://badge.fury.io/py/Anvil.svg
    :target: https://badge.fury.io/py/Anvil

.. image:: https://circleci.com/gh/AndresMWeber/Anvil.svg?style=shield&circle-token=:circle-token
    :target: https://circleci.com/gh/AndresMWeber/Anvil/

.. image:: https://coveralls.io/repos/github/AndresMWeber/Anvil/badge.svg?branch=master
    :target: https://coveralls.io/github/AndresMWeber/Anvil?branch=master

.. image:: https://landscape.io/github/AndresMWeber/Anvil/master/landscape.svg?style=flat
    :target: https://landscape.io/github/AndresMWeber/Anvil/master
    :alt: Code Health

.. image:: https://images.microbadger.com/badges/image/daemonecles/anvil.svg
    :target: https://coveralls.io/github/AndresMWeber/Anvil?branch=master

.. image:: https://images.microbadger.com/badges/version/daemonecles/anvil.svg
    :target: https://coveralls.io/github/AndresMWeber/Anvil?branch=master

.. image:: https://images.microbadger.com/badges/version/daemonecles/anvil:maya2017.svg
    :target: https://coveralls.io/github/AndresMWeber/Anvil?branch=master

.. image:: https://images.microbadger.com/badges/image/daemonecles/anvil:maya2016.svg
    :target: https://coveralls.io/github/AndresMWeber/Anvil?branch=master

.. image:: https://images.microbadger.com/badges/image/daemonecles/anvil:maya2015.svg
    :target: https://coveralls.io/github/AndresMWeber/Anvil?branch=master

.. contents::

.. section-numbering::

Synopsis
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
Windows, etc.
-------------
A universal installation method (that works on Windows, Mac OS X, Linux, …, and always provides the latest version) is to use `pip`:

.. code-block:: bash

    # Make sure we have an up-to-date version of pip and setuptools:
    $ pip install --upgrade pip setuptools
    $ pip install Anvil


(If ``pip`` installation fails for some reason, you can try ``easy_install anvil`` as a fallback.)

Usage
=============

Python Package Usage
---------------------
Use this tool via package level functions

.. code-block:: python

    import anvil
    anvil.lorem_ipsum()

Docker Image Details
====================

# Supported tags

- `maya2015`, `maya2016`, `maya2017`

For more information about this image and its history, please see its the `GitHub repository <https://github.com/andresmweber/anvil/wiki>`_.

Usage
-----

To use this image and any of it's supported tags, use `docker run`.

.. code-block:: bash

     $ docker run -ti --rm daemonecles/anvil

Without a "tag", this would download the latest available image of Maya. You can explicitly specify a version with a tag.

.. code-block:: bash

     $ docker run -ti --rm daemonecles/anvil:2017

Images occupy around **5 gb** of virtual disk space once installed, and about **1.5 gb** of bandwidth to download.

**Example**

This example will run the latest available version of Maya, create a new scene and save it in your current working directory.


.. code-block:: bash

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


What's in this image?
---------------------

This image builds on `mottosso/maya`__ which has the following software installed.

- `Centos6 <https://www.centos.org/download/>`_
- `git <https://git-scm.com/>`_ - old version
- `pip2.6 <https://pip.pypa.io/en/stable/>`_
- `python2.6 <https://www.python.org/download/releases/2.6.6/>`_

Additional installations include.

- `python2.7 <https://www.python.org/download/releases/2.7.4/>`_
- `pip2.7 <https://pip.pypa.io/en/stable/>`_

Environment variables
---------------------
`$MAYA_VERSION=####`
     for getting the installed maya version quickly in the format #### - e.g. - 2017.

`$PYTHON_PATH=$HOME/nvenv/lib/python2.7/site-packages`
     Placeholder for your test runner virtualenv named "nvenv" so maya can access the installed packages.

`$TEST_PATH=$HOME/test-results`
     A default directory where the user can place test resulting xml files etc.

Each tag represents a particular version of Maya, such as maya2016. In this image, `python` is an alias to `maya/bin/mayapy` which has the following Python packages installed via `pip`.

.. _mottossomaya: https://registry.hub.docker.com/u/mottosso/maya/
__ mottossomaya_

Version Support
===============
This package supports only Maya 2015, 2016 and 2017 so far so please be aware...plans for 2018 are in the works.

Acknowledgments
===============
-  Marcus Ottosson - Without him I would not have been able to complete the docker side of things.
