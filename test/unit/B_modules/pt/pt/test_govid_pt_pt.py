"""
Test Portuguese NIF & CC
"""
import pytest

from pii_data.types import PiiEnum, PiiEntity
from pii_data.types.doc.localdoc import SequenceLocalSrcDocument
from pii_extract.api import PiiProcessor

from taux.auxpatch import patch_entry_points
from taux.taskproc import check_tasks

# Import the task descriptor
from pii_extract_plg_regex.modules.pt.pt.govid import PII_TASKS


TESTCASES = [
    # A valid NIF
    (
        "Meu NIF é PT 123 456 789",
        "Meu NIF é <GOV_ID:PT 123 456 789>",
        PiiEntity.build(PiiEnum.GOV_ID, "PT 123 456 789", "1", 10,
                        lang="pt", country="pt", subtype="Portuguese NIF",
                        detector=1, docid="abcde-11111", status="detected",
                        process={"stage": "detection"})
    ),
    # A NIF without spacing or prefix
    (
        "O NIF 123456789 é valido",
        "O NIF <GOV_ID:123456789> é valido",
        PiiEntity.build(PiiEnum.GOV_ID, "123456789", "2", 6,
                        lang="pt", country="pt", subtype="Portuguese NIF",
                        detector=1, docid="abcde-11111",
                        process={"stage": "detection"})
    ),
    # A valid CC
    (
        "O CC é 00000000 0 ZZ4",
        "O CC é <GOV_ID:00000000 0 ZZ4>",
        PiiEntity.build(PiiEnum.GOV_ID, "00000000 0 ZZ4", "3", 7,
                        lang="pt", country="pt", subtype="Portuguese CC",
                        detector=1, docid="abcde-11111",
                        process={"stage": "detection"})
    ),
    # An invalid NIF
    ("Meu NIF é PT 123 456 788", "Meu NIF é PT 123 456 788", []),
]


def test10_cpf():
    defaults = {"lang": "pt", "country": "bt"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g


# ----------------------------------------------------------------------

@pytest.fixture
def fixture_entry_points(monkeypatch):
    """
    Mock entry points to esure the plugin is installed
    """
    patch_entry_points(monkeypatch)


def test10_nif_cc():
    """
    Test task processing, directly instantiating the task
    """
    defaults = {"lang": "pt", "country": "pt"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g


def test20_nif_cc_extract(fixture_entry_points):
    proc = PiiProcessor()
    proc.build_tasks("pt", country="pt", pii=PiiEnum.GOV_ID)

    doc = SequenceLocalSrcDocument(chunks=[c[0] for c in TESTCASES])
    doc.set_id("abcde-11111")

    for e, g in zip(TESTCASES, proc(doc)):
        assert e[2].asdict() == g.asdict()
