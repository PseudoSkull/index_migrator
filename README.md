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

Then, in your command line, move to the downloaded folder in your local system and run the file in your command line:
python3 migrate.py

## What it does for you ##

* Checks the page offset provided with the number of pages in both scans, to see if it matches up correctly, before proceeding.
* Moves the index page to the new scan file (if this hasn't already been done).
* Moves the pages according to the page offset parameters in the JSON file.

## To do in the future ##

* Make this work for pages that need to be removed.
* Make this work for the same scan file, and not just a different scan.
* Allow 