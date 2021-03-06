# texlivemetadata

Get metadata on your TexLive installation using Python.

This library calls tlmgr and parse its ouput so it can then
be processed and used from Python.

# Usage

[![PyPI version](https://badge.fury.io/py/texlivemetadata.svg)](https://badge.fury.io/py/texlivemetadata)


```sh
pip install texlivemetadata
```

## TeXLive version information

```python
import texlivemetadata

# Get version information on current TeXLive installation.
print(texlivemetadata.get_texlive_version_information())
# --->
# {'texlive': {'installation_path': '/opt/texlive/2019',
#              'modules': [{'name': 'TLConfig', 'value': '50190'},
#                          {'name': 'TLUtils', 'value': '50493'},
#                          {'name': 'TLPOBJ', 'value': '50211'},
#                          {'name': 'TLPDB', 'value': '51110'},
#                          {'name': 'TLPaper', 'value': '45795'},
#                          {'name': 'TLWinGoo', 'value': '47907'}],
#              'version': '2019'},
#  'tlmgr': {'revision': '51217', 'revision_date': '2019-05-24 23:47:41 +0200'}}
```

## Package listing

```python
import texlivemetadata

# List all packages exposed by tlmgr list:
print(texlivemetadata.list_packages())

# For listing only installed packages:
print(texlivemetadata.list_installed_packages())
```


## Package information

```python
import texlivemetadata

# To get information on package (and whether it is installed or not):
print(texlivemetadata.get_package_info("12many"))
# --->
# {
#     "cat-date": "2016-06-24T19:18:15+02:00",
#     "cat-license": "lppl",
#     "cat-topics": [
#         "maths"
#     ],
#     "cat-version": "0.3",
#     "category": "Package",
#     "collection": "collection-mathscience",
#     "installed": true,
#     "longdesc": "In the discrete branches of mathematics and the computer sciences, it will only take some seconds before you're faced with a set like {1,...,m}. Some people write $1\\ldotp\\ldotp m$, others $\\{j:1\\leq j\\leq m\\}$, and the journal you're submitting to might want something else entirely. The 12many package provides an interface that makes changing from one to another a one-line change.",
#     "package": "12many",
#     "relocatable": false,
#     "revision": "15878",
#     "shortdesc": "Generalising mathematical index sets",
#     "sizes": {
#         "run": "5k"
#     }
# }
```

## Utils

```python
import texlivemetadata

# To CTAN link for a package:
print(texlivemetadata.get_ctan_link("12many"))
# --->
# "https://ctan.org/pkg/12many"
```