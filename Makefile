update-and-push:
	sh ./update-and-push.sh version

nvenv: make-venv

make-venv:
	wget https://bootstrap.pypa.io/get-pip.py
	python2.7 get-pip.py
	pip2.7 install --upgrade pip
	pip2.7 install virtualenv
	python2.7 -m virtualenv ~/nvenv --python=python2.7 --no-site-packages

install-deps: make-venv
	~/nvenv/bin/pip install -Ur requirements.txt
	~/nvenv/bin/pip install coverage nose codacy-coverage

test-unit:
	. ~/nvenv/bin/activate
	mayapy -m nose -c tests/.noserc --xunit-file=$(TEST_PATH)/noselog$(MAYA_VERSION).xml

upload-coverage:
	. ~/nvenv/bin/activate
	~/nvenv/bin/coverage xml
	~/nvenv/bin/python-codacy-coverage -r coverage.xml


verify-git-tag: make-venv
	. ~/nvenv/bin/activate
	~/nvenv/bin/python setup.py verify

dist:
	# create a source distribution
	~/nvenv/bin/python setup.py sdist

	# create a wheel
	~/nvenv/bin/python setup.py bdist_wheel

upload-to-pypi:
	. ~/nvenv/bin/activate
	~/nvenv/bin/twine upload dist/*
