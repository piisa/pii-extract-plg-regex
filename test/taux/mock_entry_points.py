"""
A function to mock the importlib.metadata.entry_points call
"""

from unittest.mock import Mock

from pii_extract.gather.collector.defs import PII_EXTRACT_PLUGIN_ID
import pii_extract.gather.collector.plugin as mod

from pii_extract_plg_regex.plugin_loader import PiiExtractPluginLoader

# ---------------------------------------------------------------------


def mock_entry_points(monkeypatch):
    """
    Monkey-patch the entry_points call to return our plugin entry point
    """
    mock_entry = Mock()
    mock_entry.name = "plugin loader for unit testing"
    mock_entry.load = Mock(return_value=PiiExtractPluginLoader)

    mock_ep = Mock(return_value={PII_EXTRACT_PLUGIN_ID: [mock_entry]})

    monkeypatch.setattr(mod, 'entry_points', mock_ep)
