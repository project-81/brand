"""
A module for project-specific task registration.
"""

# built-in
from pathlib import Path
from typing import Dict

# third-party
from vcorelib.paths.context import in_dir
from vcorelib.task import Inbox, Outbox
from vcorelib.task.manager import TaskManager
from vcorelib.task.subprocess.run import SubprocessLogMixin


class RunSvgen(SubprocessLogMixin):
    """A simple task for running 'svgen' commands."""

    default_requirements = {"vmklib.init", "venv"}

    async def run(self, inbox: Inbox, outbox: Outbox, *args, **kwargs) -> bool:
        """Run svgen."""

        cwd: Path = args[0]
        name: str = kwargs["script"]
        target = cwd.joinpath("svg_scripts", name)

        # Locate some project directories.
        venv_bin = inbox["venv"]["venv{python_version}"]["bin"]
        build = inbox["vmklib.init"]["__dirs__"]["build"]

        build = build.joinpath("svg")
        build.mkdir(parents=True, exist_ok=True)

        return await self.exec(
            str(venv_bin.joinpath("svgen")),
            *args[1:],
            "-c",
            str(target.with_suffix(".json")),
            "-o",
            build.joinpath(f"{name}.svg"),
            target.with_suffix(".py"),
        )


class HostSvg(SubprocessLogMixin):
    """A taskf or hosting generated SVG files via HTTP."""

    default_requirements = {"vmklib.init", "venv"}

    async def run(self, inbox: Inbox, outbox: Outbox, *args, **kwargs) -> bool:
        """Host SVG via HTTP."""

        # Locate some project directories.
        venv_bin = inbox["venv"]["venv{python_version}"]["bin"]
        build = inbox["vmklib.init"]["__dirs__"]["build"]

        with in_dir(build, "svg"):
            return await self.exec(
                str(venv_bin.joinpath("python")), "-m", "http.server", "0"
            )


def register(
    manager: TaskManager,
    project: str,
    cwd: Path,
    substitutions: Dict[str, str],
) -> bool:
    """Register project tasks to the manager."""

    manager.register(RunSvgen("svg-{script}", cwd))
    manager.register(RunSvgen("images-{script}", cwd, "--images"))
    manager.register(HostSvg("host-svg"))

    del project
    del substitutions
    return True
