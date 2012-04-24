'''
Create a new fuzzer for the FTP protocol.  Note that there's nothing here for interpreting
the responses from the server.
'''

from demo_tools.decorators import demo
from sulley import *

@demo
def setup_ftp():

    # USER: send usename for authentication
    s_initialize('user')
    s_static('USER')
    s_delim(' ')
    s_string('ftp')
    s_static('\r\n')

    # PASS: send password for authentication
    s_initialize('pass')
    s_static('PASS')
    s_string('ftp')
    s_static('\r\n')

    # CWD: Change working remote directory (RFC 697)
    s_initialize('cwd')
    s_static('CWD')
    s_delim(' ')
    s_string('c: ')
    s_static('\r\n')

    # DELE: Delete file from remote server
    s_initialize('dele')
    s_static('DELE')
    s_delim(' ')
    s_string('c:\\test.txt')
    s_static('\r\n')

    # MDTM: get the last modified time of a file. (RFC 3659)
    s_initialize('mdtm')
    s_static('MDTM')
    s_delim(' ')
    s_string('c:\\boot.ini')
    s_static('\r\n')

    # MKD: make directory
    s_initialize('mkd')
    s_static('MKD')
    s_delim(' ')
    s_string('c:\\testdir')
    s_static('\r\n')

setup_ftp()
