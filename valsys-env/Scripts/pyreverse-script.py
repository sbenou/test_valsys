#!C:\Users\lenovo\Documents\test_valsys\valsys-env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pylint==2.3.1','console_scripts','pyreverse'
__requires__ = 'pylint==2.3.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pylint==2.3.1', 'console_scripts', 'pyreverse')()
    )
