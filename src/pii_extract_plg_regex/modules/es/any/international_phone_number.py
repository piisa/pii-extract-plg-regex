"""
Detection of phone numbers written with international notation (i.e. with
prefix and country code), for ES language
"""


from pii_data.types import PiiEnum

# The pattern for the regex is the same as for English
from ...en.any.international_phone_number import PATTERN_INT_PHONE


PII_TASKS = [
    {
        "class": "regex",
        "task": PATTERN_INT_PHONE,
        "name": "international phone number",
        "doc": "detect phone numbers using international notation",
        "pii": {
            "type": PiiEnum.PHONE_NUMBER,
            "subtype": "international",
            "context": {
                "value": ["tf", "teléfono", "telefono"],
                "width": [16, 0],
                "type": "word",
            },
        }
    }
]
