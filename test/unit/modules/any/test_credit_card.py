"""
Test credit card numbers
"""

import pytest

from pii_data.types import PiiEnum
from pii_data.types.localdoc import SequenceLocalSrcDocument
from pii_extract.api import PiiProcessor

from pii_extract_plg_regex.modules.any.credit_card import PII_TASKS

from taux.mock_entry_points import mock_entry_points
from taux.taskproc import check_tasks


TESTCASES = [
    # A valid credit card number
    (
        "El número de la tarjeta de crédito es 4273 9666 4581 5642",
        "El número de la tarjeta de crédito es <CREDIT_CARD:4273 9666 4581 5642>",
    ),
    # Without spaces
    ("La tarjeta es 4273966645815642", "La tarjeta es <CREDIT_CARD:4273966645815642>"),
    # With text afterwards
    (
        "El número de la tarjeta es 4273 9666 4581 5642 probablemente",
        "El número de la tarjeta es <CREDIT_CARD:4273 9666 4581 5642> probablemente",
    ),
    # With dashes
    (
        "mi tarjeta es 4273-9666-4581-5642 con caducidad 07/22",
        "mi tarjeta es <CREDIT_CARD:4273-9666-4581-5642> con caducidad 07/22",
    ),
    # Too short
    (
        "El número de la tarjeta de crédito es 4273 9666 4581",
        "El número de la tarjeta de crédito es 4273 9666 4581",
    ),
    # Not a valid credit card number
    (
        "El número de la tarjeta de crédito es 4273 9666 4581 5641",
        "El número de la tarjeta de crédito es 4273 9666 4581 5641",
    )
]


# -----------------------------------------------------------------------

def test10_credit_card():
    """
    Test task processing
    """
    defaults = {"lang": "es", "country": "any"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g


# -----------------------------------------------------------------------

@pytest.fixture
def patch_entry_points(monkeypatch):
    mock_entry_points(monkeypatch)


def test20_credit_card_stats(patch_entry_points):
    """
    Test task processing through a PiiProcessor
    """
    obj = PiiProcessor()
    obj.build_tasks("es", tasks=PiiEnum.CREDIT_CARD)
    doc = SequenceLocalSrcDocument(chunks=[c[0] for c in TESTCASES])
    obj(doc)
    assert obj.get_stats() == {"calls": 1, "entities": 4, "CREDIT_CARD": 4}
