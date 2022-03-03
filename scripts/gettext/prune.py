"""
This script is used for removing those useless .po files generated by sphinx-intl tool.

The basic sphinx internationlization workflow:

    SphinxProject --> [.rst] -- `sphinx-build gettext` --> [.pot] -- `sphinx-intl` --> [.po]  <-- translator

Note that once some .rst files are renamed or removed from the project, the old .po/.mo will still exist.
For some reasons we have to remove these files manually. PLEASE make sure that they will not be used again.
Run the script and it will keep .po files that are currently in use and remove others.

See the document for more details:
    https://megengine.org.cn/doc/stable/zh/development/docs/translation.html
"""

import sys
from os import getcwd, chdir, listdir, remove
from os.path import isfile, join, abspath, splitext

chdir(sys.path[0] + "/../../")

pot_path = "build/gettext/reference/api/" # Run "make gettext" first
po_path = ["locales/" + lang + "/LC_MESSAGES/reference/api/" for lang in ["en", "zh_CN", "zh_TW"]]

pot_files = [f for f in listdir(pot_path) if isfile(join(pot_path, f))]

# TODO: add --dry-run mode to preview changes
for pp in po_path:
    print(pp)
    po_files = [f for f in listdir(pp) if isfile(join(pp, f))]
    print("Before number:", len(po_files))
    
    for file_name in po_files:
        if splitext(file_name)[0] + ".pot" not in pot_files:
            remove(abspath(join(pp, file_name)))
            
    po_files = [f for f in listdir(pp) if isfile(join(pp, f))]
    print("After number:", len(po_files))