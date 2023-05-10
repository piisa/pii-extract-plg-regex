"""
Test Peruvian DNI
"""

import pytest

from pii_data.types import PiiEnum, PiiEntity
from pii_data.types.doc.localdoc import SequenceLocalSrcDocument
from pii_extract.api import PiiProcessor

from taux.auxpatch import patch_entry_points
from taux.taskproc import check_tasks

# Import the task descriptor
from pii_extract_plg_regex.modules.es.pe.govid import PII_TASKS


TESTCASES = [
    # Valid simple DNI (with context)
    (
        "El DNI es 12345678.",
        "El DNI es <GOV_ID:12345678>.",
        PiiEntity.build(PiiEnum.GOV_ID, "12345678", "1", 10, lang="es",
                        country="pe", subtype="DNI", detector=1,
                        docid="abcde-11111", process={"stage": "detection"})
    ),
    # Invalid full DNI (checksum fails)
    (
        "El DNI es 12345678-7",
        "El DNI es 12345678-7",
        None
    ),
    # Valid full DNI
    (
        "La identificación es 10117410-2.",
        "La identificación es <GOV_ID:10117410-2>.",
        PiiEntity.build(PiiEnum.GOV_ID, "10117410-2", "3", 21, lang="es",
                        country="pe", subtype="DNI", detector=2,
                        docid="abcde-11111", process={"stage": "detection"})
    ),
    # Invalid simple DNI (too long)
    (
        "Esto no es un DNI: 123456789",
        "Esto no es un DNI: 123456789",
        None
    ),
]


# ----------------------------------------------------------------------


@pytest.fixture
def fixture_entry_points(monkeypatch):
    """
    Patch entry points to ensure the plugin is installed
    """
    patch_entry_points(monkeypatch)


def test10_govid():
    """
    Test the task directly
    """
    defaults = {"lang": "es", "country": "pe"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g


def test20_govid_extract(fixture_entry_points):
    """
    Test task processing through a PiiProcessor
    """
    proc = PiiProcessor()
    proc.build_tasks("es", country="pe", pii=PiiEnum.GOV_ID)

    doc = SequenceLocalSrcDocument(chunks=[c[0] for c in TESTCASES])
    doc.set_id("abcde-11111")

    piic = proc(doc)
    assert len(piic) == 2
    exp = [e[2] for e in TESTCASES if e[2]]
    for e, g in zip(exp, piic):
        assert e.asdict() == g.asdict()
