
from pii_data.types import PiiEnum
from pii_extract_plg_regex import defs
import pii_extract_plg_regex.plugin_loader as mod


def test10_constructor():
    """
    Test basic construction
    """
    ep = mod.PiiExtractPluginLoader()
    assert str(ep) == '<PiiExtractPluginLoader: regex>'


def test20_tasklist():
    """
    Test list of tasks
    """
    ep = mod.PiiExtractPluginLoader()
    tl = list(ep.get_plugin_tasks())
    assert len(tl) == 22


def test30_tasklist_filter():
    """
    Test list of tasks, add a PII filter 
    """
    config = {
        defs.FMT_CONFIG: {
            "pii_filter": [PiiEnum.GOV_ID, PiiEnum.CREDIT_CARD]
        }
    }
    ep = mod.PiiExtractPluginLoader(config=config)
    tl = list(ep.get_plugin_tasks())
    #print([t["pii"][0]["type"] for t in tl])
    assert len(tl) == 13
