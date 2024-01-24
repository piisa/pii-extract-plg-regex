"""
Detection of phone numbers written with international notation (i.e. with
prefix and country code), with no language constraints
"""


from pii_data.types import PiiEnum

# The pattern for the regex is the same as for English
from ...en.any.international_phone_number import PATTERN_INT_PHONE


PII_TASKS = [
    {
        "class": "regex",
        "task": PATTERN_INT_PHONE,
        "name": "international phone number",
        "doc": "phone numbers using international notation",
        "pii": {
            "type": PiiEnum.PHONE_NUMBER,
            "subtype": "international"
        }
    }
]
