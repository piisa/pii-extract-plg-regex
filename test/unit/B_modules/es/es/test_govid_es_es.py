"""
Test Spanish DNI & NIE
"""
import pytest

from pii_data.types import PiiEnum, PiiEntity
from pii_data.types.doc.localdoc import SequenceLocalSrcDocument
from pii_extract.api import PiiProcessor

from taux.auxpatch import patch_entry_points
from taux.taskproc import check_tasks

# Import the task descriptor
from pii_extract_plg_regex.modules.es.es.govid import PII_TASKS


TESTCASES = [
    # A valid DNI
    (
        "Mi DNI es 34657934-Q.",
        "Mi DNI es <GOV_ID:34657934-Q>.",
        PiiEntity.build(PiiEnum.GOV_ID, "34657934-Q", "1", 10, lang="es",
                        country="es", subtype="DNI", detector=1,
                        docid="abcde-11111", process={"stage": "detection"})
    ),
    # A DNI without dash
    (
        "El DNI 34657934Q es válido",
        "El DNI <GOV_ID:34657934Q> es válido",
        PiiEntity.build(PiiEnum.GOV_ID, "34657934Q", "2", 7, lang="es",
                        country="es", subtype="DNI", detector=1,
                        docid="abcde-11111", process={"stage": "detection"})
    ),
    # A valid NIE
    (
        "El NIE es X3465793-S",
        "El NIE es <GOV_ID:X3465793-S>",
        PiiEntity.build(PiiEnum.GOV_ID, "X3465793-S", "3", 10, lang="es",
                        country="es", subtype="NIE", detector=1,
                        docid="abcde-11111", process={"stage": "detection"})
    ),
    # An invalid DNI
    ("Mi DNI es 34657934-H", "Mi DNI es 34657934-H", None),
    # DNIs with extra digits
    ("0034657934-Q", "0034657934-Q", None),
    # A DNI with prefix
    (
        "Identificación DNI34657934-Q",
        "Identificación DNI<GOV_ID:34657934-Q>",
        PiiEntity.build(PiiEnum.GOV_ID, "34657934-Q", "6", 18, lang="es",
                        country="es", subtype="DNI", detector=1,
                        docid="abcde-11111", process={"stage": "detection"})
    )
]


# ----------------------------------------------------------------------


@pytest.fixture
def fixture_entry_points(monkeypatch):
    """
    Mock entry points to ensure the plugin is installed
    """
    patch_entry_points(monkeypatch)


def test10_dni():
    """
    Test task processing, directly instantiating the task
    """
    defaults = {"lang": "es", "country": "es"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g


def test20_dni_extract(fixture_entry_points):
    """
    Test task processing through a PiiProcessor
    """
    proc = PiiProcessor()
    proc.build_tasks("es", country="es", pii=PiiEnum.GOV_ID)

    doc = SequenceLocalSrcDocument(chunks=[c[0] for c in TESTCASES])
    doc.set_id("abcde-11111")

    piic = proc(doc)
    assert len(piic) == 4
    exp = [e[2] for e in TESTCASES if e[2]]
    for e, g in zip(exp, piic):
        assert e.asdict() == g.asdict()


def test30_dni_extract_noc(fixture_entry_points):
    """
    Test task processing through a PiiProcessor, different country
    """
    proc = PiiProcessor()
    proc.build_tasks("es", country="gb", pii=PiiEnum.GOV_ID)

    doc = SequenceLocalSrcDocument(chunks=[c[0] for c in TESTCASES])
    doc.set_id("abcde-11111")

    piic = proc(doc)
    assert len(piic) == 0
