"""
Several functions that can be used to patch module objects, so as to enable
normalized tests.
They all use the "monkeypatch" pytest fixture
"""

import datetime

from unittest.mock import Mock

from pii_data.types.piicollection import collection
from pii_data.types.doc import document

from pii_extract.gather.collection.sources.defs import PII_EXTRACT_PLUGIN_ID
import pii_extract.gather.collection.sources.plugin as plugin_mod

from pii_extract_plg_regex.plugin_loader import PiiExtractPluginLoader


def patch_timestamp(monkeypatch):
    """
    Monkey-patch the piicollection module to ensure the timestamps it produces
    have always the same value
    """
    mock_datetime = Mock()
    mock_datetime.utcnow.return_value = datetime.datetime(2000, 1, 1)
    mock_datetime.side_effect = lambda *a, **kw: datetime.datetime(*a, **kw)
    monkeypatch.setattr(collection, 'datetime', mock_datetime)


def patch_uuid(monkeypatch):
    """
    Monkey-patch the document module to ensure a fixed uuid
    """
    mock_uuid = Mock()
    mock_uuid.uuid4 = Mock(return_value="00000-11111")
    monkeypatch.setattr(document, 'uuid', mock_uuid)


def patch_entry_points(monkeypatch):
    """
    Monkey-patch the the importlib.metadata.entry_points call to return
    our plugin entry point
    """
    mock_entry = Mock()
    mock_entry.name = "plugin loader for unit testing"
    mock_entry.load = Mock(return_value=PiiExtractPluginLoader)

    mock_ep = Mock(return_value={PII_EXTRACT_PLUGIN_ID: [mock_entry]})

    monkeypatch.setattr(plugin_mod, 'entry_points', mock_ep)
