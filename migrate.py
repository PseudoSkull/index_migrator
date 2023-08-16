import pywikibot
import json
from debug import print_in_red, print_in_green, print_in_yellow, print_in_blue, process_break
from cleanup import get_commons_file_page_count

migrate_info_filename = "migrate_info.json"
migrate_info = json.load(open(migrate_info_filename, "r"))

original_scan_file = migrate_info["original_scan_file"]
new_scan_file = migrate_info["new_scan_file"]
pages_to_insert = migrate_info["pages_to_insert"]
pages_to_delete = migrate_info["pages_to_delete"]
original_page_count = get_commons_file_page_count(original_scan_file)
new_page_count = get_commons_file_page_count(new_scan_file)

def check_page_count_with_page_offset(original_page_count, new_page_count, pages_to_insert):
    number_of_pages_to_insert = len(pages_to_insert)
    number_of_pages_to_delete = len(pages_to_delete)

    page_offset = number_of_pages_to_insert - number_of_pages_to_delete

    expected_new_page_count = original_page_count + page_offset

    # print("\n\n\n")

    numbers_being_compared = "Total page counts on original scan and new scan (when accounting for page offset)"
    stats = f"Old page count: {original_page_count} New page count: {new_page_count} Page offset: {page_offset}"

    if new_page_count == expected_new_page_count:
        print_in_green(f"{numbers_being_compared} match! {stats}")
    else:
        print_in_red(f"{numbers_being_compared} DO NOT MATCH, PLEASE FIX!\nExpected page count: {expected_new_page_count} {stats}")
        exit()