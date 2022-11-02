"""
The plugin entry point
"""

from pathlib import Path

from typing import Dict, Iterable

from pii_extract.build.collector import FolderTaskCollector
from . import VERSION

DESCRIPTION = "Regex-based PII tasks (plus context-nased validation) for some languages and countries"


# Define the folder holding the detection modules
_MODPATH = Path(__file__).parent / "modules"


class MyTaskCollector(FolderTaskCollector):
    """
    Define a task collector to be executed over the "modules" folder
    """
    def __init__(self, debug: bool = False):
        super().__init__("pii_extract_plg_regex.modules", _MODPATH,
                         "piisa:pii_extract_plg_regex",
                         version=VERSION, debug=debug)


class PiiExtractPluginLoader:
    """
    The class acting as entry point for the package (the plugin loader)
    """
    source = "piisa:pii_extract_plg_regex"
    version = VERSION
    description = DESCRIPTION

    def __init__(self, debug: bool = False):
        self.tasks = MyTaskCollector(debug=debug)

    def __repr__(self) -> str:
        return '<PiiExtractPluginLoader: regex>'

    def get_tasks(self, lang: str = None) -> Iterable[Dict]:
        """
        Return an iterable of task definitions
        """
        return self.tasks.gather_all_tasks(lang)
