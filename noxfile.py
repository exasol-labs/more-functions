from pathlib import Path

import nox

# imports all nox task provided by the toolbox
from exasol.toolbox.nox.tasks import *

ROOT = Path(__file__).parent

# default actions to be run if nothing is explicitly specified with the -s option
nox.options.sessions = ["format:check"]


def get_oft_jar(session: nox.Session) -> Path:
    oft_version = "4.6.0"
    oft_jar = (
        Path.home()
        / ".m2"
        / "repository"
        / "org"
        / "itsallcode"
        / "openfasttrace"
        / "openfasttrace"
        / oft_version
        / f"openfasttrace-{oft_version}.jar"
    )
    if not oft_jar.exists():
        print(f"Downloading OpenFastTrace {oft_version}")
        session.run(
            "mvn",
            "--batch-mode",
            "org.apache.maven.plugins:maven-dependency-plugin:3.3.0:get",
            f"-Dartifact=org.itsallcode.openfasttrace:openfasttrace:{oft_version}",
        )
    return oft_jar


def run_oft(session: nox.Session, *args) -> None:
    oft_jar = get_oft_jar(session)
    doc_dir = Path(__file__).parent / "doc"
    src_dir = ROOT / "exasol"
    test_dir = ROOT / "test"

    with session.chdir(ROOT):
        session.run(
            "java",
            "-jar",
            oft_jar,
            "trace",
            "-a",
            "feat,req,dsn",
            f"{doc_dir}",
            f"{src_dir}",
            f"{test_dir}",
            *args,
        )


@nox.session(name="oft:trace", python=False)
def run_oft_udf_client_plaintext(session: nox.Session):
    """
    Downloads (if needed) OFT and executes it for the udf client for tag "V2,_" printing the output to stdout.
    """
    run_oft(session)


@nox.session(name="oft:trace-html", python=False)
def run_oft_udf_client_html(session: nox.Session):
    """
    Downloads (if needed) OFT and executes it for the udf client for tag "V2,_" creating an HTML page as output.
    """
    html_file = session.posargs[0] if session.posargs else "report.html"
    run_oft(session, "-o", "html", "-f", html_file)


@nox.session(name="lua:lint", python=False)
def lint_lua(session: nox.Session) -> None:
    """Check the Lua function sources with the installed linter."""
    session.run(
        "bash",
        "-c",
        'eval "$(luarocks --local path)" && '
        "luacheck exasol/more_functions/lua "
        "--globals decimal exa null run",
    )


@nox.session(name="lua:install-dependencies", python=False)
def install_lua_dependencies(session: nox.Session) -> None:
    """Install the Lua dependencies declared by this project."""
    session.run(
        "luarocks",
        "--lua-version=5.4",
        "--local",
        "install",
        "--only-deps",
        "more-functions-0.1.0-1.rockspec",
    )
