This is a tool for migrating Index pages or Page namespace pages. The tool should be used under the following circumstances:
* There is a new and more complete scan with more pages that need to be inserted.
* There need to be pages inserted into an existing Index page scan.

**This tool requires admin privileges on the English Wikisource to work properly, because it requires the deletion of pages upon move! As such, please use this tool wisely and pay close attention to the data and the results!**

## Dependencies ##
* pywikibot

## Usage instructions ##

Insert the relevant data into migrate_info.json, as follows:
* original_scan_file - The original scan filename, as it appears on Wikimedia Commons, in string format
* new_scan_file - If applicable, the new scan filename, as it appears on Wikimedia Commons, in string format. If not applicable, use an empty string ("") or null value.
* pages_to_insert - Insert pages to insert, as numbers, in array format.
* pages_to_delete - Insert pages that need to be removed.

(A sample json file is provided in the repository, as an example of a working one.)

Then, in your command line, move to the downloaded folder in your local system and run the file in your command line:

```python3 migrate.py```

## What it does for you ##

* Checks the page offset provided with the number of pages in both scans, to see if it matches up correctly, before proceeding.
* Moves the index page to the new scan file (if this hasn't already been done).
* Moves the pages according to the page offset parameters in the JSON file.

* Automatically reconfigures the index page pagelist and cover image page number according to the page offset.

## Milestones ##
* 08/17/2023: Index:The Revolt of the Angels.pdf -> Index:The Revolt of the Angels v2.djvu, as requested by SpikeShroom
** First ever migrated index page with this application

## To do in the future ##

* Automatically fix all instances of "What links here" to each of the pages
* Remove pages from work (move pages left)
* Move pages within a single index (not to be migrated)
* Switch pages around (for example switch 11 with 13)
* Fix transclused pages of broken index page.
* Make it work with films, for all of the above!