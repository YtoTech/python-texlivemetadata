# -*- coding: utf-8 -*-
"""
Get metadata on TexLive installation itself.

Documentation at: https://github.com/YtoTech/python-texlivemetadata

Copyright (c) 2019 Yoan Tournade <yoan@ytotech.com>
Released under MIT License. See LICENSE file.
"""
import subprocess
import re
import datetime
from operator import is_not
from functools import partial

# --------------------
# Texlive installation specification
# --------------------

TLMGR_LIST_LINE_REGEX_PATTERN = r"^(i|\s)\s(\S+):\s(.+)$"
TLMGR_LIST_LINE_REGEX = re.compile(TLMGR_LIST_LINE_REGEX_PATTERN)


def parse_tlmgr_list_line(line):
    regex_match = TLMGR_LIST_LINE_REGEX.match(line)
    if not regex_match:
        raise RuntimeError("Unable to parse tlmr list line ouput: {}".format(line))
    return {
        "installed": regex_match.group(1) == "i",
        "name": regex_match.group(2),
        "shortdesc": regex_match.group(3),
    }

def parse_tlmgr_version_verbose_line(line, line_index):
    if "tlmgr revision" in line:
        version, remaining = line.split("tlmgr revision ")[1].split(" (")
        return {
            "tlmgr_version": version,
            "tlmgr_revision_date": remaining.split(")")[0]
        }
    if "tlmgr using installation" in line:
        return {
            "texlive_installation_path": line.split("tlmgr using installation: ")[1]
        }
    if "TeX Live" in line and "version" in line:
        return {
            "texlive_version": line.split("version ")[1]
        }
    print(line, line_index)
    return {}


def parse_tlmgr_version_verbose(output):
    parsed_entries = {}
    for line_index, line in enumerate(output.splitlines()):
        parsed_entries = {
            **parsed_entries,
            **parse_tlmgr_version_verbose_line(line, line_index)
        }
    return parsed_entries


def get_texlive_version_information():
    cmd = ["tlmgr", "version", "-v"]
    cmd_output = subprocess.run(
        cmd, stdout=subprocess.PIPE, check=True, encoding="utf-8"
    )
    return parse_tlmgr_version_verbose(cmd_output.stdout)
