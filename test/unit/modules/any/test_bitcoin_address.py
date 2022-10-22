"""
Test bitcoin addresses
"""

from pii_extract_plg_regex.modules.any.bitcoin_address import PII_TASKS
from taux.taskproc import check_tasks


TESTCASES = [
    # A valid bitcoin address
    (
        "BTC address: 1JayVxfVgdaFKirkZTZVK4CdRnFDdFNENN",
        "BTC address: <BITCOIN_ADDRESS:1JayVxfVgdaFKirkZTZVK4CdRnFDdFNENN>",
    ),
    (
        "BTC address: bc1qwxxvjxlakxe9rmxcphh4yy8a2t6z00k4gc4mpj",
        "BTC address: <BITCOIN_ADDRESS:bc1qwxxvjxlakxe9rmxcphh4yy8a2t6z00k4gc4mpj>",
    ),
    # An invalid bitcoin address
    (
        "BTC address: 1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW623",
        "BTC address: 1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW623",
    ),
]


def test10_bitcoin_address():
    """
    Test task processing
    """
    defaults = {"lang": "any", "country": "any"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
