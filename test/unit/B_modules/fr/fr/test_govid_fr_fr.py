"""
Test French NIR & NIF
"""
import pytest

from pii_data.types import PiiEnum, PiiEntity
from pii_data.types.doc.localdoc import SequenceLocalSrcDocument
from pii_extract.api import PiiProcessor

from taux.taskproc import check_tasks
from taux.auxpatch import patch_entry_points

# Import the task descriptor
from pii_extract_plg_regex.modules.fr.fr.govid import PII_TASKS


TESTCASES = [
    # A valid NIR
    (
        "NIR 253072B07300470.",
        "NIR <GOV_ID:253072B07300470>.",
        PiiEntity.build(PiiEnum.GOV_ID, "253072B07300470", "1", 4, lang="fr",
                        country="fr", subtype="French NIR", detector=1,
                        docid="abcde-11111", process={"stage": "detection"})
    ),
    (
        "NIR 2 53 07 2B 073 004 70.",
        "NIR <GOV_ID:2 53 07 2B 073 004 70>.",
        PiiEntity.build(PiiEnum.GOV_ID, "2 53 07 2B 073 004 70",
                        "2", 4, lang="fr",
                        country="fr", subtype="French NIR", detector=1,
                        docid="abcde-11111", process={"stage": "detection"})
    ),
    # A valid NIF
    (
        "NIF 2123123123123.",
        "NIF <GOV_ID:2123123123123>.",
        PiiEntity.build(PiiEnum.GOV_ID, "2123123123123", "3", 4, lang="fr",
                        country="fr", subtype="French NIF", detector=1,
                        docid="abcde-11111", process={"stage": "detection"})
    ),
    # An invalid NIR
    (
        "NIR 6253072C07300443.",
        "NIR 6253072C07300443.",
        None
    ),
    # An invalid NIF
    (
        "NIF 21231231231235.",
        "NIF 21231231231235.",
        None
    )
]


# ----------------------------------------------------------------------

@pytest.fixture
def fixture_entry_points(monkeypatch):
    """
    Mock entry points to ensure the plugin is installed
    """
    patch_entry_points(monkeypatch)


def test10_govid():
    """
    Test the task directly
    """
    defaults = {"lang": "fr", "country": "fr"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g


def test20_govid_extract(fixture_entry_points):
    """
    Test task processing through a PiiProcessor
    """
    proc = PiiProcessor()
    proc.build_tasks("fr", country="fr", pii=PiiEnum.GOV_ID)

    doc = SequenceLocalSrcDocument(chunks=[c[0] for c in TESTCASES])
    doc.set_id("abcde-11111")

    piic = proc(doc)
    assert len(piic) == 3
    exp = [e[2] for e in TESTCASES if e[2]]
    for e, g in zip(exp, piic):
        assert e.asdict() == g.asdict()
