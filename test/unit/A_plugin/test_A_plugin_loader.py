from itertools import chain
from pii_data.types import PiiEnum
from pii_extract_plg_regex import defs, VERSION
import pii_extract_plg_regex.plugin_loader as mod

from taux.taskcount import TASK_COUNT


def test10_constructor():
    """
    Test basic construction
    """
    ep = mod.PiiExtractPluginLoader()
    assert str(ep) == f'<PiiExtractPluginLoader: regex {VERSION}>'


def test20_tasklist():
    """
    Test list of tasks
    """
    ep = mod.PiiExtractPluginLoader()
    tl = list(ep.get_plugin_tasks())

    exp = chain.from_iterable(lang.values() for lang in TASK_COUNT.values())
    assert sum(exp) == len(tl)


def test30_tasklist_filter():
    """
    Test list of tasks, for specific PII types
    """
    # Fetch only GOV_ID & CREDIT_CARD tasks
    config = {
        defs.FMT_CONFIG: {
            "pii_filter": [PiiEnum.GOV_ID, PiiEnum.CREDIT_CARD]
        }
    }
    ep = mod.PiiExtractPluginLoader(config=config)
    tl = list(ep.get_plugin_tasks())

    #print([(t["pii"][0]["type"], t["pii"][0]["country"]) for t in tl])
    assert len(tl) == 19
