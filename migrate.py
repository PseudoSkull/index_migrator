import json
import pywikibot
import re
from debug import print_in_red, print_in_green, print_in_yellow, print_in_blue, process_break
from edit_mw import save_page
from cleanup import get_commons_file_page_count

migrate_info_filename = "migrate_info.json"
migrate_info = json.load(open(migrate_info_filename, "r"))
print(migrate_info)

original_scan_file = migrate_info["original_scan_file"]
new_scan_file = migrate_info["new_scan_file"]
pages_to_insert = migrate_info["pages_to_insert"]
pages_to_delete = migrate_info["pages_to_delete"]
original_page_count = get_commons_file_page_count(original_scan_file)
new_page_count = get_commons_file_page_count(new_scan_file)



############ PAGE OFFSET ############


def get_page_offset(pages_to_insert, pages_to_delete):
    number_of_pages_to_insert = len(pages_to_insert)
    number_of_pages_to_delete = len(pages_to_delete)

    page_offset = number_of_pages_to_insert - number_of_pages_to_delete
    return page_offset

def get_offset_page_number(original_page_number, page_offset):
    return original_page_number + page_offset

# for now, logic later to handle multiple insertions throughout file
page_offset = get_page_offset(pages_to_insert, pages_to_delete)



def check_page_count_with_page_offset():
    print("Checking page count with page offset...")
    expected_new_page_count = original_page_count + page_offset

    numbers_being_compared = "Total page counts on original scan and new scan (when accounting for page offset)"
    stats = f"Old page count: {original_page_count} New page count: {new_page_count} Page offset: {page_offset}"

    if new_page_count == expected_new_page_count:
        print_in_green(f"{numbers_being_compared} match! {stats}")
    else:
        print_in_red(f"{numbers_being_compared} DO NOT MATCH, PLEASE FIX!\nExpected page count: {expected_new_page_count} {stats}")
        exit()



############# INDEX MIGRATION #############

def parse_pagelist_tag(pagelist_tag):
    if "\n-\n" in pagelist_tag:
        pagelist_tag = pagelist_tag.split("\n-\n")
        pagelist_tag_beginning = pagelist_tag[0]
        pagelist_tag_to_use = pagelist_tag[1]
    else:
        pagelist_tag_to_use = pagelist_tag
    
    pagelist_parameters = pagelist_tag_to_use.splitlines()

    new_parameters = []

    for parameter in pagelist_parameters:
        parsed_parameter = parameter.split("=")
        actual_page_number = parsed_parameter[0]


    if type(pagelist_tag) == list:
        pagelist_tag = pagelist_tag_beginning + "\n" + pagelist_tag_to_use
    else:
        pagelist_tag = pagelist_tag_to_use
    
    return pagelist_tag

def parse_index_page(index_page_text):
    # parse pages tag:
    pagelist_tag_pattern = r"<pagelist\n(.*)\n\/>"
    pagelist_tag = re.search(pagelist_tag_pattern, index_page_text).group(1)
    pagelist_tag = parse_pagelist_tag(pagelist_tag)
    index_page_text = re.sub(pagelist_tag_pattern, pagelist_tag, index_page_text)

    # parse cover image parameter


def migrate_index_page():
    site = pywikibot.Site("en", "wikisource")
    original_index_page = pywikibot.Page(site, original_scan_file)
    new_index_page = pywikibot.Page(site, new_scan_file)

    original_index_page_text = original_index_page.text
    new_index_page_text = new_index_page.text

    new_pagelist_tag = parse_index_page(original_index_page_text)





############# PAGE NAMESPACE MIGRATION #############





############# MAIN #############

def __main__():
    check_page_count_with_page_offset()
