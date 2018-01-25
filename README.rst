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

.. contents::

.. section-numbering::

Synopsis
=============

My Autorigger.  Ain't yo business..yet!

Features
--------
-  Caching
-  Uses automated naming conventions as read in config.yml
-  Up to date with online help docs
-  Temp file generator
-  JSON file output
-  CLI access
-  Dict output

Installation
============
Windows, etc.
-------------
A universal installation method (that works on Windows, Mac OS X, Linux, …, and always provides the latest version) is to use `pip`:

.. code-block:: bash

    # Make sure we have an up-to-date version of pip and setuptools:
    $ pip install --upgrade pip setuptools
    $ pip install Anvil


(If ``pip`` installation fails for some reason, you can try
``easy_install anvil`` as a fallback.)

Usage
=============

Python Package Usage
---------------------
Use this tool via package level functions

.. code-block:: python

    import anvil
    anvil.lorem_ipsum()


Version Support
===============
This package supports the Maya 2015, 2016 and 2017 so far so please be aware.
