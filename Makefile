update-and-push:
	sh ./update-and-push.sh version

nvenv: make-venv

make-venv:
	pip2.6 install virtualenv
	python -m virtualenv ~/nvenv

install-deps: make-venv
	~/nvenv/bin/pip install -Ur requirements.txt
	~/nvenv/bin/pip install coveralls nose

test-unit:
	. ~/nvenv/bin/activate
	mayapy -m nose -c tests/.noserc --xunit-file=$(TEST_PATH)/noselog$(PYTHON_VERSION).xml

upload-coverage:
	. ~/nvenv/bin/activate
	~/nvenv/bin/coveralls

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

update-git:
	yum remove -y git
	yum install -y epel-release
	yum install -y https://centos6.iuscommunity.org/ius-release.rpm
	yum install -y git2u
	mkdir ~/test-results

mayapy-install-deps-and-pip:
	wget https://bootstrap.pypa.io/get-pip.py
	mayapy get-pip.py
	chmod -x $(find tests/ -name '*.py')
	mayapy -m pip install -r requirements.txt
	mayapy -m pip install coveralls