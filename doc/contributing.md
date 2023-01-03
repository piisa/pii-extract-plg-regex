# Adding PII tasks

To add a new PII processing task to this package, prepare a Pull Request on the
repository with the following changes:

 1. If the task type is a new one, you can use the `TASK_OTHER` type, or
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
    * The [task descriptor], a list containing all defined tasks. The list
      variable *must* be named `PII_TASKS`
 5. Finally, add a unit test to check the validity for the task code, in the
    proper place under [test/unit/modules]. The numbe of test cases depends
	on the task implementation, bur there should be at least
     - a positive test: one valid PII that has to be detected. For the cases
       in which the PII is validated, the test should pass the validation,
       so the PII must be a random (fake) one but still valid
     - and a negative test: one PII-like string that is almost, but not quite
       the real one, so it should *not* be recognized


## Task implementation

A task can be implemented with either of three shapes: regex, function or
lass. See [task implementation] for a description of how to implement each of
these, including where to add the required documentation explaining the task.

An example of context validation can be seen in the [international phone
number] task.


[PiiEnum]: https://github.com/piisa/pii-data/src/pii_extract/types/piienum.py
[task descriptor]: https://github.com/piisa/pii-extract-base/doc/task-descriptor.md
[task implementation]: https://github.com/piisa/pii-extract-base/doc/task-implementation.md
[modules]: ../src/pii_extract_plg_regex/modules
[test/unit/lang]: ../test/unit/lang
[international phone number]: ../src/pii_extract_regex/modules/en/any/international_phone_number.py

[ISO 639-1]: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
[ISO 3166-1]: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
[regex]: https://github.com/mrabarnett/mrab-regex
