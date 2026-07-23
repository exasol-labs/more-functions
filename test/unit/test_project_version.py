import tomllib
from pathlib import Path

PROJECT_ROOT = Path(__file__).parents[2]


def test_project_version_is_consistent_across_package_metadata() -> None:
    with (PROJECT_ROOT / "pyproject.toml").open("rb") as pyproject_file:
        project = tomllib.load(pyproject_file)["project"]

    project_name = project["name"]
    project_version = project["version"]
    rockspec = PROJECT_ROOT / f"{project_name}-{project_version}-1.rockspec"

    assert rockspec.is_file()
    assert f'package = "{project_name}"' in rockspec.read_text()
    assert f'version = "{project_version}-1"' in rockspec.read_text()
