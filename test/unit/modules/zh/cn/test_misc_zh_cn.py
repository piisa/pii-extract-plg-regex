"""
Test PII elements for Chinese (Phone numbers, street addresses & diseases)
"""

from pii_extract_plg_regex.modules.zh.cn.misc import PII_TASKS
from taux.taskproc import check_tasks


TESTCASES = [
    # Phone number
    ("045-4123456",
     "<PHONE_NUMBER:045-4123456>"),
    # Not a phone number (too many digits in the first part)
    ("70045-4123456", "70045-4123456"),
    # ----- We are missing here tests for STREET_ADDRESS & DISEASE
]


def test10_misc_zh_cn():
    defaults = {"lang": "zh", "country": "cn"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
