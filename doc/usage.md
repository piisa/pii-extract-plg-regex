# Usage

Once the package is installed, the plugin is automatically recognized and its
tasks made available to the PIISA framework, so no further work is needed.

Instead, upon installation it defines a plugin entry point. This plugin is 
picked up by executing scripts and classes in [pii-extract-base], and thus its
functionality is exposed to it.


## Configuration

The plugin can be customized via a [PIISA configuration]. The configuration
section has as tag `piisa:config:extract_plg_regex:main:v1`, and it
should contain a dictionary.

This version recognizes one optional field in the dictionary: `pii_list`. 
It can be used to select the PII types that will be loaded; if defined
it should contain a list of PiiEnum names, and then _only_ the tasks for
those types will be loaded.


[PIISA configuration]: https://github.com/piisa/piisa/docs/configuration.md
[importing arbitrary tasks]: external.md#object-based-api
[import external tasks]:external.md#file-based-api
[pii-extract-base]: https://github.com/piisa/pii-extract-base
