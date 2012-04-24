from sulley import *
import sulley_zmq
from demo_tools.decorators import demo

@demo
def zmq_session():

    # session state will be stored here
    session = sessions.session(session_filename='zmq.session')

    # define the target
    host = '192.168.14.132'
    target_port = 5555
    netmon_port = 26001
    procmon_port = 26002
    target = sessions.target(host, target_port)

    session.add_target(target)

    # tie a sequence of requests together into the nodes of a session
    session.connect(s_get('zeromq'))

    #start our fuzzer
    session.fuzz()


zmq_session()
