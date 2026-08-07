from pathlib import Path
import sys


class FileSystem:

    @staticmethod
    def root() -> Path:
        """
        Returns the project root.

        Development:
            project/

        Executable:
            folder_where_the_exe_is/
        """

        if getattr(sys, "frozen", False):
            return Path(sys.executable).parent

        return Path(__file__).resolve().parent.parent.parent


    @staticmethod
    def path(*parts) -> Path:
        """
        Returns a path relative to the project root.
        """

        return FileSystem.root().joinpath(*parts)

    @staticmethod
    def assets(*parts) -> Path:
        return FileSystem.path("assets", *parts)


    @staticmethod
    def data(*parts) -> Path:
        return FileSystem.path("data", *parts)