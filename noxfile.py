from pathlib import Path

import nox

# imports all nox task provided by the toolbox
from exasol.toolbox.nox.tasks import *

ROOT = Path(__file__).parent
LUA_TEST_ENVIRONMENT = ROOT / ".lua-test"

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


def run_oft_for_udf_client(session: nox.Session, *args) -> None:
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


@nox.session(name="test:lua", python=False)
def run_lua_unit_tests(session: nox.Session):
    """Install the project-local Lua test tools and run the Lua unit tests."""
    lua_bin_dir = LUA_TEST_ENVIRONMENT / "bin"
    luarocks = lua_bin_dir / "luarocks"
    busted = lua_bin_dir / "busted"

    if not luarocks.exists():
        session.run(
            "poetry",
            "run",
            "hererocks",
            str(LUA_TEST_ENVIRONMENT),
            "--lua",
            "5.4",
            "--luarocks",
            "latest",
        )
    if not busted.exists():
        session.run(str(luarocks), "install", "busted", "2.3.0-1")
    session.run(str(busted), "test/unit/lua")


@nox.session(name="oft:trace", python=False)
def run_oft_udf_client_plaintext(session: nox.Session):
    """
    Downloads (if needed) OFT and executes it for the udf client for tag "V2,_" printing the output to stdout.
    """
    run_oft_for_udf_client(session)


@nox.session(name="oft:trace-html", python=False)
def run_oft_udf_client_html(session: nox.Session):
    """
    Downloads (if needed) OFT and executes it for the udf client for tag "V2,_" creating a html page as output.
    """
    html_file = session.posargs[0] if session.posargs else "report.html"
    run_oft_for_udf_client(session, "-o", "html", "-f", html_file)
