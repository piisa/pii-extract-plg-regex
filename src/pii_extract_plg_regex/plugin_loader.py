"""
The plugin entry point
"""

from pathlib import Path

from typing import Dict, Iterable

from pii_extract.gather.collection.sources import FolderTaskCollector
from pii_extract.helper.logger import PiiLogger

from . import VERSION, defs


# Define the folder holding the detection modules
_MODPATH = Path(__file__).parent / "modules"


class RegexTaskCollector(FolderTaskCollector):
    """
    Define a task collector to be executed over the "modules" folder
    """
    def __init__(self, debug: bool = False, **kwargs):
        super().__init__("pii_extract_plg_regex.modules", _MODPATH,
                         defs.TASK_SOURCE, version=VERSION, debug=debug,
                         **kwargs)


class PiiExtractPluginLoader:
    """
    The class acting as entry point for the package (the plugin loader)
    """
    source = defs.TASK_SOURCE
    version = VERSION
    description = defs.TASK_DESCRIPTION

    def __init__(self, config: Dict = None, debug: bool = False,
                 languages: Iterable[str] = None, **kwargs):
        """
          :param config: either a configuration for the plugin, or a filename
            containing that configuration
          :param debug: activate debug mode
          :param languages: restrict the plugin to those languages
        """
        self.cfg = config.get(defs.FMT_CONFIG, {}) if config else {}
        self._log = PiiLogger(__name__, debug)
        self._log(".. plg-regex version: %s", VERSION)
        self.tasks = RegexTaskCollector(debug=debug, languages=languages,
                                        pii_filter=self.cfg.get("pii_list"))


    def __repr__(self) -> str:
        return f'<PiiExtractPluginLoader: regex {VERSION}>'


    def get_plugin_tasks(self, lang: str = None) -> Iterable[Dict]:
        """
        Return an iterable of task definitions
        """
        return self.tasks.gather_tasks(lang)
