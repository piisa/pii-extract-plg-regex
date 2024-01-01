"""
Portuguese Government-issued IDs:
  - NIF (Número de identificação fiscal)
  - CC (Número de Cartão de Cidadão)
"""

import re

from typing import Iterable

from stdnum.pt import nif, cc

from pii_data.types import PiiEnum, PiiEntity
from pii_data.types.doc import DocumentChunk
from pii_extract.build.task import BaseMultiPiiTask


# regex for NIF & CC
_NIF_PATTERN = r"(?: PT \x20?)? (?: \d{3} \x20 \d{3} \x20 \d{3} | \d{9} )"
_CC_PATTERN = r"\d{8} \x20? \d \x20? [A-Z0-9]{2}\d"


class PortugueseNifCc(BaseMultiPiiTask):
    """
    Portuguese Government-issued identifiers, using regex + checksum:
      - Número de Identificação Fiscal (NIF)
      - Cartão de Cidadão (CC)
    """
    pii_name = "Portuguese NIF and CC numbers"
    pii_method = "regex,checksum"


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Compile the regexes
        self.nif = re.compile(_NIF_PATTERN, flags=re.X)
        self.cc = re.compile(_CC_PATTERN, flags=re.X)


    def find(self, chunk: DocumentChunk) -> Iterable[PiiEntity]:
        """
        Find & validate instances of either NIF or CC
        """
        info_nif, info_cc = self.pii_info

        # NIF
        for item in self.nif.finditer(chunk.data):
            item_value = item.group()
            if nif.is_valid(item_value):
                yield PiiEntity(info_nif, item_value, chunk.id, item.start())
        # CC
        for item in self.cc.finditer(chunk.data):
            item_value = item.group()
            if cc.is_valid(item_value):
                yield PiiEntity(info_cc, item_value, chunk.id, item.start())


# Task descriptor
PII_TASKS = {
    "class": "PiiTask",
    "task": PortugueseNifCc,
    "pii": {
        "type": PiiEnum.GOV_ID,
        "subtype": ["Portuguese NIF", "Portuguese CC"]
    }
}
