[![](https://images.microbadger.com/badges/image/daemonecles/anvil.svg)](https://coveralls.io/github/AndresMWeber/Anvil?branch=master)

[![](https://images.microbadger.com/badges/version/daemonecles/anvil.svg)](https://coveralls.io/github/AndresMWeber/Anvil?branch=master)

[![](https://images.microbadger.com/badges/version/daemonecles/anvil:maya2017.svg)](https://coveralls.io/github/AndresMWeber/Anvil?branch=master)

[![](https://images.microbadger.com/badges/version/daemonecles/anvil:maya2016.svg)](https://coveralls.io/github/AndresMWeber/Anvil?branch=master)

[![](https://images.microbadger.com/badges/version/daemonecles/anvil:maya2015.svg)](https://coveralls.io/github/AndresMWeber/Anvil?branch=master)

____

## Docker Image Details

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
`$MAYA_VERSION=####`
:    for getting the installed maya version quickly in the format #### - e.g. - 2017.

`$PYTHON_PATH=$HOME/nvenv/lib/python2.7/site-packages`
:    Placeholder for your test runner virtualenv named "nvenv" so maya can access the installed packages.

`$TEST_PATH=$HOME/test-results`
:    A default directory where the user can place test resulting xml files etc.

## Feedback

### Issues/Contributing

If you have any problems with or questions about contributing to this image, please contact Marcus Ottosson through a [GitHub issue][3] (since the image is basically his with minor additions)

[3]: https://github.com/mottosso/docker-maya/issues
