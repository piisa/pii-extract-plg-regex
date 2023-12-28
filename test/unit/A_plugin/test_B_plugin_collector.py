"""
Test that all languages & countries in the package are gathered, and how many 
tasks are defined for each one
"""
from itertools import chain

import pytest

from pii_extract.gather.collection import get_task_collection

from taux.auxpatch import patch_entry_points
from taux.taskcount import TASK_COUNT

# ---------------------------------------------------------------------------

@pytest.fixture
def fixture_entry_points(monkeypatch):
    patch_entry_points(monkeypatch)


def test10_taskdict_lang(fixture_entry_points):
    """
    Check languages with tasks
    """
    piic = get_task_collection()
    got = piic.language_list()
    assert ['any', 'de', 'en', 'es', 'fr', 'it', 'pt', 'ro', 'zh'] == got


def test20_taskdict_countries(fixture_entry_points):
    """
    Check countries with tasks
    """
    piic = get_task_collection()
    got = piic.country_list()
    countries = chain.from_iterable(TASK_COUNT.values())
    exp = sorted(set(countries))
    assert exp == got


def test30_taskdict_bylang(fixture_entry_points):
    """
    Check how many tasks per language
    """
    piic = get_task_collection()
    for lang in piic.language_list():
        tasks = piic.taskdef_list(lang, add_any=False)
        tasks = list(tasks)
        assert len(list(tasks)) == sum(TASK_COUNT[lang].values())


def test40_taskdict_tasks(fixture_entry_points):
    """
    Check number of tasks defined, per lang & country
    """
    piic = get_task_collection()

    for lang, countries in TASK_COUNT.items():
        for c, num in countries.items():
            tasks = piic.taskdef_list(lang, country=c, add_any=False)
            assert len(list(tasks)) == num


def test50_tasklist_all(fixture_entry_points):
    """
    Check total number of tasks defined
    """
    piic = get_task_collection()
    tasks = piic.taskdef_list()
    assert len(list(tasks)) == sum(v2 for v1 in TASK_COUNT.values()
                                   for v2 in v1.values())
