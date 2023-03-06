# Pii Extractor plugin: regex

[![version](https://img.shields.io/pypi/v/pii-extract-plg-regex)](https://pypi.org/project/pii-extract-plg-regex)
[![changelog](https://img.shields.io/badge/change-log-blue)](CHANGES.md)
[![license](https://img.shields.io/pypi/l/pii-extract-plg-regex)](LICENSE)
[![build status](https://github.com/piisa/pii-extract-plg-regex/actions/workflows/pii-extract-plg-regex-pr.yml/badge.svg)](https://github.com/piisa/pii-extract-plg-regex/actions)

This repository builds a Python package that installs a [pii-extract-base]
plugin to performs PII detection for text data based on regular expressions
(with optional context).

The PII Tasks in the package are [structured by language & country], since many
of the PII elements are language- and/or -country dependent.


## Requirements

The package
 * needs at least Python 3.8
 * needs the [pii-data] and the [pii-extract-base] base packages
 * uses the [python-stdnum] package to validate numeric identifiers


## Usage

The package does not have any user-facing entry points, and it is [used
automatically] by the PIISA framework.


## Building

The provided [Makefile] can be used to process the package:
 * `make pkg` will build the Python package, creating a file that can be
   installed with `pip`
 * `make unit` will launch all unit tests (using [pytest], so pytest must be
   available)
 * `make install` will install the package in a Python virtualenv. The
   virtualenv will be chosen as, in this order:
     - the one defined in the `VENV` environment variable, if it is defined
     - if there is a virtualenv activated in the shell, it will be used
     - otherwise, a default is chosen as `/opt/venv/bigscience` (it will be
       created if it does not exist)


## Contributing

To add a new PII processing task, please see the [contributing instructions].


[pii-data]: https://github.com/piisa/pii-data
[pii-extract-base]: https://github.com/piisa/pii-extract-base
[structured by language & country]: src/pii_extract_plg_regex/modules
[python-stdnum]: https://github.com/arthurdejong/python-stdnum
[Makefile]: Makefile
[pytest]: https://docs.pytest.org
[usage]: doc/usage.md
[contributing instructions]: doc/contributing.md
