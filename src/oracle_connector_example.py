import os, sys

if "ORACLE_HOME" not in os.environ:
    os.environ['ORACLE_HOME'] = "/opt/algorithm/instantclient"
    if "LD_LIBRARY_PATH" in os.environ:
        os.environ['LD_LIBRARY_PATH'] = "{}:/opt/algorithm/instantclient/lib".format(os.environ['LD_LIBRARY_PATH'])
    else:
        os.environ['LD_LIBRARY_PATH'] = "/opt/algorithm/instantclient/lib"
    os.execl(sys.executable, 'python3', __file__, "/usr/local/bin/algorithmia-pipe")


import Algorithmia
import cx_Oracle

# API calls will begin at the apply() method, with the request body passed as 'input'
# For more details, see algorithmia.com/developers/algorithm-development/languages
def apply(input):
    connection = cx_Oracle.connect("hr", "fakepassword", "dbhost.example.com/orclpdb1")
    return "hello {}".format(input)
