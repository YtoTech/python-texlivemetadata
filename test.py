import pprint
from texlivemetadata import get_texlive_version_information

output = get_texlive_version_information()
pprint.pprint(output)
