import nox
import os

locations = "src", "tests"

# nox.options.sessions = "lint", "tests"

@nox.session()
def tests(session):
    args = session.posargs or locations
    session.install("pytest", "pytest-cov")
    session.run("pytest", "--cov", *args)


@nox.session()
def lint(session):
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-black",
        "flake8-import-order",
    )
    session.run("flake8", *args)


@nox.session()
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", "--check", *args)


@nox.session()
def mypy(session):
    os.environ['MYPYPATH']=os.environ['PYTHONPATH']
    print(os.environ['MYPYPATH'])
    session.install("mypy")
    session.install("-r", "requirements.txt")
    session.run("mypy", "src")
