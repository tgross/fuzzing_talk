from demo_tools.decorators import demo
from sulley import *

@demo
def setup_zmq():
    '''
    Creates a fuzzer for the framing layer only of ZMTP.
    '''

    s_initialize('zeromq')

    if s_block_start('zmq_message'):
        # initial length field octet
        # if we always wanted to use a bigger length than 255 (no dep argument below),
        # we could set this to \\xFF and fuzzable=False
        s_binary('\\x00', name='initial')

        # we lock in the length of the message length header so it stays valid
        s_sizer('msg_length', length=8)

        if s_block_start('msg_length', dep='initial', dep_value='\\xFF'):
            s_qword(0xDEADBEEF, endian='>', signed=False)
        s_block_end()

        # flags
        s_initialize('flags')
        s_static('\\x00')
        s_binary('\\x00\\x00\\x00') #these are all reserved, so lets fuzz them separately

        # frame body: we're leaving this unconstrained to see what happens when the message
        # length header and actual message length don't match.
        s_initialize('body')
        s_static('CWD')
        s_delim(' ')
        s_string('c: ')
        s_static('\r\n')


setup_zmq()
