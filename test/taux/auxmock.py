import datetime

from unittest.mock import Mock
import pytest


from pii_data.types import document
from pii_data.types import piicollection


@pytest.fixture
def mock_timestamp(monkeypatch):
    """
    Monkey-patch the piicollection module to ensure the timestamps it produces
    have always the same value
    """
    mock_datetime = Mock()
    mock_datetime.utcnow.return_value = datetime.datetime(2000, 1, 1)
    mock_datetime.side_effect = lambda *a, **kw: datetime.datetime(*a, **kw)
    monkeypatch.setattr(piicollection, 'datetime', mock_datetime)


@pytest.fixture
def mock_uuid(monkeypatch):
    """
    Monkey-patch the document module to ensure a fixed uuid
    """
    mock_uuid = Mock()
    mock_uuid.uuid4 = Mock(return_value="00000-11111")
    monkeypatch.setattr(document, 'uuid', mock_uuid)
