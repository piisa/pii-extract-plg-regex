"""
Test that all languages & countries in the package are gathered, and how many 
tasks are defined for each one
"""

import pytest

from pii_extract.load import get_task_collection

from taux.mock_entry_points import mock_entry_points


@pytest.fixture
def patch_entry_points(monkeypatch):
    mock_entry_points(monkeypatch)


EXPECTED = {
    'any': {
        'any': 4},
    'en': {
        'any': 1,
        'au': 2,
        'ca': 1,
        'gb': 1,
        'in': 1,
        'us': 1
    },
    'es': {
        'any': 1,
        'es': 2,
        'mx': 1
    },
    'fr': {
        'ca': 1
    },
    'pt': {
        'br': 1,
        'pt': 1
    },
    'zh': {
        'cn': 4
    }
}


# ---------------------------------------------------------------------------


def test10_taskdict_lang(patch_entry_points):
    """
    Check languages with tasks
    """
    piic = get_task_collection()
    taskdict = piic.taskdef_dict()
    assert sorted(taskdict) == sorted(EXPECTED)


def test20_taskdict_countries(patch_entry_points):
    """
    Check countries defined
    """
    piic = get_task_collection()
    taskdict = piic.taskdef_dict()

    for lang, countries in EXPECTED.items():
        assert sorted(taskdict[lang]) == sorted(countries)


def test30_taskdict_tasks(patch_entry_points):
    """
    Check number of tasks defined
    """
    piic = get_task_collection()
    taskdict = piic.taskdef_dict()

    for lang, countries in EXPECTED.items():
        for c, num in countries.items():
            assert len(taskdict[lang][c]) == num
