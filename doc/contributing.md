# Adding PII tasks

To add a new PII processing task to this package, prepare a Pull Request on the
repository with the following changes:

 1. If the task type is a new one, you can use the `OTHER` type, or
    start a PR for a new task type in [PiiEnum] in the `pii-data` repository
 2. If it is for a language not yet covered, add a new language subfolder
    under the [modules] folder, using the [ISO 639-1] code for the language
 3. Then
    * If it is a country-independent PII, it goes into the `any` subdir
      (create that directory if it is not present)
    * if it is country-dependent, create a country subdir if not present,
      using a **lowercased version** of its [ISO 3166-1] country code
 4. Under the final chosen subfolder, add the task as a Python `mytaskname.py`
    module (the name of the file is not relevant). The module must contain:
    * The task implementation, which can have any of three flavours (regex,
      function or class), see below
    * The [task descriptor], a list containing all defined tasks (or a single
	  task descriptor). The list variable *must* be named `PII_TASKS`
 5. Then, add a unit test to check the validity for the task code, in the
    proper place under [test/unit/B_modules]. 
 6. Finally, update the [taskcount] dictionary used in unit tests to verify the
    total number of tasks available. Depending on the task type, it might
	be needed to update other unit tests.


## Task implementation

A task can be implemented with either of three shapes: regex, function or
lass. See [task implementation] for a description of how to implement each of
these, including where to add the required documentation explaining the task.
When creating a regex, follow the [PII regex guidelines] to ensure
compatibility.

Whenever a regular expression is too wide, potentially producing significant
false positives, considering adding validation on top if its matches. Two
possibilities for this are:

* Use [context validation] to accept regex matches only in the presence of
  suitable contextual words around the match. An example of context validation
  can be seen in the [international phone number] task.
* If the PII instance allows it, validate its value using additional code, for
  instance through [checksum validation].


### Checksum validation

Many identifiers, specially if they are numeric (such as credit card numbers,
blockchain addresses, government ids, etc) contain a checksum digit or
character that can be used to check if it can be a valid identifier. This can be
implemented inside the task itself e.g. by using a [class implementation] and
adding to the `find()` method (you can check the [credit card] task as an
example).

A simpler possibility is to use the capacities provided by the [python-stdnum]
Python package (see below in [auxiliary-libraries](#auxiliary-libraries)). For
this the [callable implementation] is often adequate, because it can be
used to perform these additional operations on regex matches easily. Two
examples of such implementations are:
 
 * [bitcoin address]
 * [australian tax file number]


### Auxiliary libraries

The following python packages are already used and declared as dependencies
for the `pii-extract-plg-regex` package, so they are guaranteed to be
available:

 * [regex] is a Python Regular Expression library, backwards-compatible with the
   standard `re` module, but with additional functionality (e.g. support for
   management of Unicode codepoints, blocks and scripts)
 * [python-stdnum] provides functions to validate more than a hundred
   identifiers and codes from many countries
 * [phonenumbers] can parse and check telephone numbers from all over the world


## Unit tests

The number of test cases depends on the task implementation, but there should
be at least
   - a positive test: one valid PII that has to be detected. For the cases
     in which the PII is validated, the test should pass the validation,
     so the PII must be a random (fake) one but still valid
   - and a negative test: one PII-like string that is almost, but not quite
     the real one, so it should *not* be recognized

You can see some examples of unit tests:
 * the [test for bitcoin address] is a minimal unit test that just
   instantiates the task and checks a few testcases
 * the [test for emails] does that, and also creates a full object with the
   task, to test the workflow
 * the [test for credit card] adds checking the values of fields in the
   detected PII instances
   

### Launching the tests

The package needs a virtualenv with the dependencies installed; once it is
available it can run the unit tests. The commands are:

       make install-dependencies
       make unit

By default, the process
  * uses python3.8 to create the virtualenv
  * creates the virtualenv in `opt/venv/pii`

It is possible to change those defaults by defining the environment variables
`PYTHON` and `VENV`. For instance:

       export PYTHON=python3.10
       export VENV=/tmp/myvenv
       make install-dependencies
       make unit


[PiiEnum]: https://github.com/piisa/pii-data/tree/main/src/pii_data/types/piienum.py
[task descriptor]: https://github.com/piisa/pii-extract-base/tree/main/doc/task-descriptor.md
[task implementation]: https://github.com/piisa/pii-extract-base/tree/main/doc/task-implementation.md
[PII regex guidelines]: https://github.com/piisa/pii-extract-base/tree/main/doc/regex.md
[callable implementation]: https://github.com/piisa/pii-extract-base/blob/main/doc/task-implementation.md#2-callable-implementation
[class implementation]: https://github.com/piisa/pii-extract-base/blob/main/doc/task-implementation.md#3-class-implementation

[context validation]: https://github.com/piisa/pii-extract-base/blob/main/doc/task-implementation.md#context-based-pii-validation
#context-based-pii-validation
[checksum validation]: #checksum-validation

[credit card]: ../src/pii_extract_plg_regex/modules/any/credit_card.py
[international phone number]: ../src/pii_extract_plg_regex/modules/en/any/international_phone_number.py
[bitcoin address]: ../src/pii_extract_plg_regex/modules/any/bitcoin_address.py
[australian tax file number]: ../src/pii_extract_plg_regex/modules/en/au/tfn.py

[test/unit/B_modules]: ../test/unit/B_modules
[test for bitcoin address]: ../test/unit/B_modules/any/test_bitcoin_address.py
[test for emails]: ../test/unit/B_modules/any/test_email.py
[test for credit card]: ../test/unit/B_modules/any/test_credit_card.py
[taskcount]: ../test/taux/taskcount.py

[modules]: ../src/pii_extract_plg_regex/modules

[ISO 639-1]: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
[ISO 3166-1]: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

[regex]: https://github.com/mrabarnett/mrab-regex
[python-stdnum]: https://github.com/arthurdejong/python-stdnum
[phonenumbers]: https://github.com/daviddrysdale/python-phonenumbers
