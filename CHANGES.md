# Changelog

## 0.4.1
 * plugin_loader accepts the "languages" argument

## 0.4.0
 * added AU phone number detector
 * added PE phone number detector
 * fixed phone numbers
    - spaces in phone numbers
    - control parse errors in phonenumbers
	- improve context detection
 * improved EN age detector
 * added context to UK VAT number
 * improved email regex
 * improved names & subtypes in GOV_ID detectors
 * adjusted for pii-extract-base 0.4.0

## 0.3.0
 * config field `pii_filter` changed to `pii_list` for consistency with
   other plugins
 * added AGE detector for EN
 * added zipcode detector for EN-US

## 0.2.1
 * fixed source name for the detectors

## 0.2.0
 * added area code formats in international phone numbers for EN
 * added Indian phone numbers for EN-IN
 * added Canadian phone numbers for EN-CA
 * documentation fixes

## 0.1.4
 * added French PII (phone numbers, govid)
 
## 0.1.3
 * fix Makefile for installation & unit tests

## 0.1.2
 * improvements in debug output
 * added phone number for EN-UK
 
## 0.1.1
 * fix usage of libphonenumber -- always use a front-end regex
 * added phone number for EN-US

## 0.1.0
 * split from the old `pii-manager`, as a pii-extract plugin
