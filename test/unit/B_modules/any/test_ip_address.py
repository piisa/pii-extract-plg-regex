"""
Test IP addresses
"""

from taux.taskproc import check_tasks

# Import the task descriptor
from pii_extract_plg_regex.modules.any.ip_address import PII_TASKS


TESTCASES = [
    # A valid IP address
    (
        "My IP address is 10.45.122.65",
        "My IP address is <IP_ADDRESS:10.45.122.65>",
    ),
    # An invalid IP address
    (
        "My IP address is 310.45.122.65",
        "My IP address is 310.45.122.65"),
    # An IP address without its proper context, hence undetected
    (
        "My address is 10.45.122.65",
        "My address is 10.45.122.65"
    )
]


def test10_ipaddress():
    """
    Test task processing, directly instantiating the task
    """
    defaults = {"lang": "any", "country": "any"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
