#!/usr/bin/env python
from pathlib import Path

from setuptools import find_packages, setup

packages = find_packages(where="asdf_chunked")
packages.append("asdf_chunked.resources")

package_dir = {
    "": "asdf_chunked",
    "asdf_chunked.resources": "resources",
}


def package_yaml_files(directory):
    paths = sorted(Path(directory).rglob("*.yaml"))
    return [str(p.relative_to(directory)) for p in paths]


package_data = {"asdf_chunked.resources": package_yaml_files("resources")}

setup(
    use_scm_version=True,
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
)
