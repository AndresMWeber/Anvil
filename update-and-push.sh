#!/usr/bin/env bash

if [ -n "${version+set}" ]; then
    echo "Updating project to $version"

    sed -i "/^__version__/c\__version__ = '$version'" ./anvil/version.py
    echo "Updated version.py"

    git add -A
    git commit -m "versioned up to $version"
    echo "Committed."

    git tag $version --force
    echo "Tagged."

    git push origin master --tags --force
    echo "Pushed!"
fi
