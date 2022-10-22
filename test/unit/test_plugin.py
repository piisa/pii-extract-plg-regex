
import pii_extract_plg_regex.plugin as mod


def test10_constructor():
    """
    Test basic construction
    """
    ep = mod.PluginEntryPoint()
    assert str(ep) == '<PluginEntryPoint: regex>'


def test20_tasklist():
    """
    Test list of tasks
    """
    ep = mod.PluginEntryPoint()
    tl = list(ep.get_tasks())
    assert len(tl) == 22
