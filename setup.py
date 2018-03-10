import codecs
from os.path import abspath, dirname, join
from setuptools import setup, find_packages

__author__ = 'Andres Weber'
__author_email__ = 'andresmweber@gmail.com'
__package__ = 'anvil'
__url__ = 'https://github.com/andresmweber/anvil'
__version__ = '0.0.0'

with codecs.open(abspath(join(__package__, 'version.py'))) as ver_file:
    exec (ver_file.read())

with codecs.open(join(abspath(dirname(__file__)), 'README.md'), encoding='utf-8') as readme_file:
    long_description = readme_file.read()

description = 'Yet another auto-rigger.'

install_requires = [
    'python-dateutil',
    'PyYAML',
    'six',
    'jsonschema',
    'nomenclate',
    'colorama',
    'deepdiff',
    'structlog'
]

tests_requires = [
    'coverage',
    'unittest2',
    'nose',
]

dev_requires = ['Sphinx', 'docutils', 'docopt']

setup(
    name=__package__,
    version=__version__,
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*']),
    package_data={'curve_shapes.yml': ['anvil/objects/curve_shapes.yml']},
    include_package_data=True,
    url=__url__,
    license='MIT',
    author=__author__,
    author_email=__author_email__,
    description=description,
    long_description=long_description,
    keywords='auto-rig, rig, maya, auto, auto-rigger, python, circleci, pymel',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Multimedia :: Graphics :: 3D Modeling',
    ],
    install_requires=install_requires,
    extras_require={
        'tests': tests_requires,
        'dev': dev_requires
    }
)
