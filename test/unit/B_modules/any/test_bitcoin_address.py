"""
Test bitcoin addresses
"""

from taux.taskproc import check_tasks

# Import the task descriptor
from pii_extract_plg_regex.modules.any.bitcoin_address import PII_TASKS


TESTCASES = [
    # Valid bitcoin addresses
    (
        "BTC address: 1JayVxfVgdaFKirkZTZVK4CdRnFDdFNENN",
        "BTC address: <BLOCKCHAIN_ADDRESS:1JayVxfVgdaFKirkZTZVK4CdRnFDdFNENN>",
    ),
    (
        "the address is bc1qwxxvjxlakxe9rmxcphh4yy8a2t6z00k4gc4mpj",
        "the address is <BLOCKCHAIN_ADDRESS:bc1qwxxvjxlakxe9rmxcphh4yy8a2t6z00k4gc4mpj>",
    ),
    # An invalid bitcoin address
    (
        "BTC address: 1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW623",
        "BTC address: 1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW623",
    )
]


def test10_bitcoin_address():
    """
    Test task processing, directly instantiating the task
    """
    defaults = {"lang": "any", "country": "any"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
