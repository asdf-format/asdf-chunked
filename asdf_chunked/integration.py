import sys
from pathlib import Path

if sys.version_info < (3, 9):
    import importlib_resources
else:
    import importlib.resources as importlib_resources

from asdf import DirectoryResourceMapping

import asdf_chunked


def get_resource_mappings():
    resources_root = importlib_resources.files(asdf_chunked) / "resources"
    if not resources_root.is_dir():
        # In an editable install, the resources directory will exist off the
        # repository root:
        resources_root = Path(__file__).absolute().parent.parent.parent / "resources"
        if not resources_root.is_dir():
            raise RuntimeError("Missing resources directory")

    return [
        DirectoryResourceMapping(
            resources_root / "stsci.edu" / "schemas",
            "http://stsci.edu/schemas/asdf/chunked/",
            recursive=True,
        ),
        DirectoryResourceMapping(
            resources_root / "asdf-format.org" / "manifests",
            "asdf://asdf-format.org/transform/manifests/",
        ),
    ]
