"""
Test Spanish DNI & NIE
"""
import pytest

from pii_data.types import PiiEnum, PiiEntity
from pii_data.types.localdoc import SequenceLocalSrcDocument
from pii_extract.api import PiiProcessor

from pii_extract_plg_regex.modules.es.es.govid import PII_TASKS
from taux.mock_entry_points import mock_entry_points
from taux.taskproc import check_tasks



TESTCASES = [
    # A valid DNI
    (
        "Mi DNI es 34657934-Q",
        "Mi DNI es <GOV_ID:34657934-Q>",
        PiiEntity(PiiEnum.GOV_ID, "34657934-Q", "1", 10,
                  lang="es", country="es", subtype="Spanish DNI", detector=1,
                  docid="abcde-11111")
    ),
    # A DNI without dash
    (
        "El DNI 34657934Q es válido",
        "El DNI <GOV_ID:34657934Q> es válido",
        PiiEntity(PiiEnum.GOV_ID, "34657934Q", "2", 7,
                  lang="es", country="es", subtype="Spanish DNI", detector=1,
                  docid="abcde-11111")
    ),
    # A valid NIE
    (
        "El NIE es X3465793-S",
        "El NIE es <GOV_ID:X3465793-S>",
        PiiEntity(PiiEnum.GOV_ID, "X3465793-S", "3", 10,
                  lang="es", country="es", subtype="Spanish NIE", detector=1,
                  docid="abcde-11111")
    ),
    # An invalid DNI
    ("Mi DNI es 34657934-H", "Mi DNI es 34657934-H", []),
]


# ----------------------------------------------------------------------


def test10_dni():
    defaults = {"lang": "es", "country": "es"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g


# ----------------------------------------------------------------------

@pytest.fixture
def patch_entry_points(monkeypatch):
    """
    Mock entry points to esure the plugin is installed
    """
    mock_entry_points(monkeypatch)


def test20_dni_extract(patch_entry_points):
    """
    Test task processing through a PiiProcessor
    """
    proc = PiiProcessor()
    proc.build_tasks("es", country="es", tasks=PiiEnum.GOV_ID)

    doc = SequenceLocalSrcDocument(chunks=[c[0] for c in TESTCASES])
    doc.set_id("abcde-11111")

    piic = proc(doc)
    assert len(piic) == 3
    for e, g in zip(TESTCASES, piic):
        assert e[2].as_dict() == g.as_dict()


def test30_dni_extract_noc(patch_entry_points):
    """
    Test task processing through a PiiProcessor, different country
    """
    proc = PiiProcessor()
    proc.build_tasks("es", country="ar", tasks=PiiEnum.GOV_ID)

    doc = SequenceLocalSrcDocument(chunks=[c[0] for c in TESTCASES])
    doc.set_id("abcde-11111")

    piic = proc(doc)
    assert len(piic) == 0
        
