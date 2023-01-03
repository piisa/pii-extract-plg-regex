"""
Test that all languages & countries in the package are gathered, and how many 
tasks are defined for each one
"""

import pytest

from pii_extract.build.collection import get_task_collection

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
    got = piic.language_list()
    assert ['any', 'en', 'es', 'fr', 'pt', 'zh'] == got


def test20_taskdict_countries(patch_entry_points):
    """
    Check countries with tasks
    """
    piic = get_task_collection()
    got = piic.country_list()
    assert ['any', 'au', 'br', 'ca', 'cn', 'es', 'gb', 'in', 'mx', 'pt', 'us'] == got


def test30_taskdict_bylang(patch_entry_points):
    """
    Check how many tasks per language
    """
    piic = get_task_collection()
    for lang in piic.language_list():
        tasks = piic.taskdef_list(lang, add_any=False)
        assert len(list(tasks)) == sum(EXPECTED[lang].values())


def test40_taskdict_tasks(patch_entry_points):
    """
    Check number of tasks defined, per lang & country
    """
    piic = get_task_collection()

    for lang, countries in EXPECTED.items():
        for c, num in countries.items():
            tasks = piic.taskdef_list(lang, country=c, add_any=False)
            assert len(list(tasks)) == num


def test50_tasklist_all(patch_entry_points):
    """
    Check total number of tasks defined
    """
    piic = get_task_collection()
    tasks = piic.taskdef_list()
    assert len(list(tasks)) == sum(v2 for v1 in EXPECTED.values()
                                   for v2 in v1.values())
