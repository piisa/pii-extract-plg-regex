"""
Test credit card numbers
"""

import pytest

from pii_data.types import PiiEnum
from pii_data.types.doc.localdoc import SequenceLocalSrcDocument
from pii_extract.api import PiiProcessor

from taux.auxpatch import patch_uuid, patch_entry_points
from taux.taskproc import check_tasks

# Import the task descriptor
from pii_extract_plg_regex.modules.any.credit_card import PII_TASKS


TESTCASES = [
    # A valid credit card number
    (
        "El número de la tarjeta de crédito es 4273 9666 4581 5642",
        "El número de la tarjeta de crédito es <CREDIT_CARD:4273 9666 4581 5642>",
        {"type": "CREDIT_CARD", "value": "4273 9666 4581 5642",
         "chunkid": "1", "start": 38, "end": 57, "docid": "00000-11111"}
    ),
    # Number without spaces
    (
        "La tarjeta es 4273966645815642",
        "La tarjeta es <CREDIT_CARD:4273966645815642>",
        {"type": "CREDIT_CARD", "value": "4273966645815642",
         "chunkid": "2", "start": 14}
    ),
    # With text afterwards
    (
        "El número de la tarjeta es 4273 9666 4581 5642 probablemente",
        "El número de la tarjeta es <CREDIT_CARD:4273 9666 4581 5642> probablemente",
        {"type": "CREDIT_CARD", "value": "4273 9666 4581 5642",
         "chunkid": "3", "start": 27}
    ),
    # With dashes
    (
        "mi tarjeta es 4273-9666-4581-5642 con caducidad 07/22",
        "mi tarjeta es <CREDIT_CARD:4273-9666-4581-5642> con caducidad 07/22",
        {"type": "CREDIT_CARD", "value": "4273-9666-4581-5642",
         "chunkid": "4", "start": 14}
    ),
    # Number too short
    (
        "El número de la tarjeta de crédito es 4273 9666 4581",
        "El número de la tarjeta de crédito es 4273 9666 4581",
    ),
    # Not a valid credit card number (fails checksum)
    (
        "El número de la tarjeta de crédito es 4273 9666 4581 5641",
        "El número de la tarjeta de crédito es 4273 9666 4581 5641",
    )
]


# -----------------------------------------------------------------------


@pytest.fixture
def fixture_entry_points(monkeypatch):
    patch_entry_points(monkeypatch)

@pytest.fixture
def fixture_uuid(monkeypatch):
    patch_uuid(monkeypatch)


def test10_credit_card():
    """
    Test task processing, directly instantiating the task
    """
    defaults = {"lang": "es", "country": "any"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g


def test20_credit_card_stats(fixture_entry_points):
    """
    Test stats on task processing, launching through a PiiProcessor
    """
    obj = PiiProcessor()
    obj.build_tasks("es", pii=PiiEnum.CREDIT_CARD)
    doc = SequenceLocalSrcDocument(chunks=[c[0] for c in TESTCASES])
    obj(doc)
    assert obj.get_stats() == {"num": {"calls": 1, "entities": 4},
                               "entities": {"CREDIT_CARD": 4}}


def test30_credit_card_values(fixture_entry_points, fixture_uuid):
    """
    Test PII results on task processing, launching through a PiiProcessor
    """
    obj = PiiProcessor()
    obj.build_tasks("es", pii=PiiEnum.CREDIT_CARD)
    doc = SequenceLocalSrcDocument(chunks=[c[0] for c in TESTCASES])
    got = list(obj(doc))

    assert len(got) == 4

    exp = [t[2] for t in TESTCASES if len(t) > 2]
    for e, g in zip(exp, got):
        g = g.asdict()
        for field in e:
            assert e[field] == g[field]
