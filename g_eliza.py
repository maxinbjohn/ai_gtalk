#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

# make sure you have installed xmpp module
# sudo apt-get install python-xmpp

import xmpp
import time
from ConfigParser import SafeConfigParser
from eliza import *

# Message Call Back function to transfer text to eliza and get reply
def messageCB(sess,mess):
    nick=mess.getFrom().getResource()
    text=mess.getBody()
    reply = eliza(text)
    sess.send(xmpp.Message(mess.getFrom(),reply))

def LoopFn(conn):
    try:
        conn.Process(1)
    except KeyboardInterrupt:
    	return 0
    return 1

# Main process establishes the connection to gtalk server   
def main_process():
    parser = SafeConfigParser()
    parser.read('gtalk.ini')
    jid = xmpp.protocol.JID(parser.get('account_details', 'username'))
    cl = xmpp.Client('gmail.com')
    cl.connect(('talk.google.com',5223))
    cl.RegisterHandler('message',messageCB)
    cl.auth(jid.getNode(), parser.get('account_details', 'password'))
    cl.sendInitPresence()
    while LoopFn(cl):
        pass

# invokes the main_process
if __name__ == '__main__':
    main_process()

