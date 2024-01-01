"""
Detection of phone numbers written with international notation (i.e. with
prefix and country code), for ES language
"""


from pii_data.types import PiiEnum

# The pattern for the regex is the same as for English
from ...en.any.international_phone_number import PATTERN_INT_PHONE


# Context that must be found around the phone number
CONTEXT_REGEX = r"""
 \b
 (?:
   tel[ée]fonos? |
   (?: tf | tel | tel[éf] | tfno ) \. |        # abbreviations
   (?: m[óo]vil | celular ) (?: es )? |        # mobile
   ll[aá]m[aeoáéó][bdilmrs]?\w*                # conjugation for "llamar"
 )
 (?! \w )
"""


PII_TASKS = [
    {
        "class": "regex",
        "task": PATTERN_INT_PHONE,
        "name": "international phone number",
        "doc": "detect phone numbers in international notation, using regex + context",
        "pii": {
            "type": PiiEnum.PHONE_NUMBER,
            "subtype": "international",
            "context": {
                "type": "regex",
                "value": CONTEXT_REGEX,
                "width": [64, 64]
            }
        }
    }
]
