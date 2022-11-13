"""
The plugin entry point
"""

from pathlib import Path

from typing import Dict, Iterable

from pii_extract.gather.collector import FolderTaskCollector
from . import VERSION, defs

DESCRIPTION = "Regex-based PII tasks (plus context-based validation) for some languages and countries"


# Define the folder holding the detection modules
_MODPATH = Path(__file__).parent / "modules"


class RegexTaskCollector(FolderTaskCollector):
    """
    Define a task collector to be executed over the "modules" folder
    """
    def __init__(self, debug: bool = False, **kwargs):
        super().__init__("pii_extract_plg_regex.modules", _MODPATH,
                         "piisa:pii_extract_plg_regex",
                         version=VERSION, debug=debug, **kwargs)


class PiiExtractPluginLoader:
    """
    The class acting as entry point for the package (the plugin loader)
    """
    source = "piisa:pii-extract-plg-regex"
    version = VERSION
    description = DESCRIPTION

    def __init__(self, config: Dict = None, debug: bool = False):
        self.cfg = config.get(defs.FMT_CONFIG, {}) if config else {}
        self.tasks = RegexTaskCollector(debug=debug,
                                        pii_filter=self.cfg.get("pii_filter"))


    def __repr__(self) -> str:
        return '<PiiExtractPluginLoader: regex>'


    def get_plugin_tasks(self, lang: str = None) -> Iterable[Dict]:
        """
        Return an iterable of task definitions
        """
        return self.tasks.gather_tasks(lang)
