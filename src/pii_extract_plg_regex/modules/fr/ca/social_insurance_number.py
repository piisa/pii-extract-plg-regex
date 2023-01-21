"""
Reuse the SIN code implemented for en
"""

from pii_data.types import PiiEnum

from ...en.ca.social_insurance_number import Canadian_social_insurance_number

PII_TASKS = {
    "class": "callable",
    "task": Canadian_social_insurance_number,
    "method": "soft-regex,checksum",
    "pii": {
        "type": PiiEnum.GOV_ID,
        "subtype": "Canadian Social Insurance Number"
    }
}
