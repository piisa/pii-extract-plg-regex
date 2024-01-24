"""
Detection and validation of the identifier for Brazilian Cadastro de Pessoa
Física

It contains two check digits, so it can be validated.
"""

import re

from stdnum.br import cpf

from typing import Iterable

from pii_data.types import PiiEnum


_CPF_REGEX = re.compile(r"\b \d{3} \. \d{3} \. \d{3} - \d{2} \b", flags=re.X)


def BR_cadastro_pessoa_fisica(doc: str) -> Iterable[str]:
    """
    Brazilian número de inscrição no Cadastro de Pessoas Físicas, using regex + checksum
    """
    for candidate in _CPF_REGEX.findall(doc):
        if cpf.is_valid(candidate):
            yield candidate


# Task descriptor
PII_TASKS = {
    "class": "callable",
    "task": BR_cadastro_pessoa_fisica,
    "pii": {
        "type": PiiEnum.GOV_ID,
        "subtype": "Brazilian Cadastro de Pessoas Físicas",
        "method": "regex,checksum"
    }
}
