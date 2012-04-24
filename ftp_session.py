from sulley import *
import sulley_ftp
from demo_tools.decorators import demo

@demo
def ftp_session():

    # We need to receive the FTP banner
    def receive_banner(sock):
        sock.recv(1024)

    # session state will be stored here
    session = sessions.session(session_filename='ftp.session')

    # define the target
    host = '192.168.14.128'
    target_port = 21
    netmon_port = 26001
    procmon_port = 26002
    target = sessions.target(host, target_port)

    # set up monitoring of the target application
#    target.netmon = pedrpc.client(host, netmon_port)
#    target.procmon = pedrpc.client(host, procmon_port)
#    target.procmon_options = { 'proc_name': 'Bisonftp.exe' }

    session.pre_send = receive_banner
    session.add_target(target)

    # tie a sequence of requests together into the nodes of a session
    session.connect(s_get('user'))
    session.connect(s_get('user'), s_get('pass'))
    session.connect(s_get('pass'), s_get('cwd'))
    session.connect(s_get('pass'), s_get('dele'))
    session.connect(s_get('pass'), s_get('mdtm'))
    session.connect(s_get('pass'), s_get('mkd'))


    #start our fuzzer
    session.fuzz()


ftp_session()
