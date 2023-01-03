# Modules for PII detection

There is a Python module for each PII entity detection task; they are structured
by language & country:
 * The first folder level indicates the language the task is to be applied to.
   It's either
     - [any] for tasks applicable to any language (i.e. language-independent
       tasks), or
	 - the two-letter [ISO 639-1] language code for the language
 * The first folder level indicates the country the task is to be applied to
   (except for the `any` language, which has no second level). It is either
     - [any] for tasks that are country-independent
	 - the two-leter [ISO 3166-1 alpha-2] code for the country
	 
Note that in some cases the folder name has an appended underscore. This is to
avoid it becoming a reserved Python keyword, e.g. `in_` for the folder for
India.


## Structure

A task module is a Python module containing a `PII_TASKS` Python list, which
has at least one [task definition]; there can be more than one
	 
	 
[ISO 639 1]: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
[ISO 3166-1 alpha-2]: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
[task definition]: https://github.com/piisa/pii-extract-base/doc/tasks.md
