"""
Test Chinese government ids (Resident Identity Card & Passport)
"""

from taux.taskproc import check_tasks

# Import the task descriptor
from pii_extract_plg_regex.modules.zh.cn.govid import PII_TASKS


TESTCASES = [
    # A valid RIC
    ("公民身份号码 360426199101010071",
     "公民身份号码 <GOV_ID:360426199101010071>"),
    # An invalid RIC
    ("公民身份号码 360426199101010072",
     "公民身份号码 360426199101010072"),
    # An invalid RIC (one aditional digit)
    ("公民身份号码 3604261991010100717",
     "公民身份号码 3604261991010100717"),
    # A correct passport number
    ("中华人民共和国护照 D12345678",
     "中华人民共和国护照 <GOV_ID:D12345678>"),
    # An incorrect passport number (invalid letter)
    ("中华人民共和国护照 K12345678",
     "中华人民共和国护照 K12345678"),
    # An incorrect passport number (only 7 digits)
    ("中华人民共和国护照 D1234567",
     "中华人民共和国护照 D1234567"),
]


def test10_govid_zh_cn():
    """
    Test task processing, directly instantiating the task
    """
    defaults = {"lang": "zh", "country": "cn"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
