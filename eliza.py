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

import httplib
import urllib

# We POST the parameter 'my_string' to the www-ai.ijs.si website
# Obtains the reply and prints it on the screen

def eliza(my_dialog):
    params = urllib.urlencode({'Entry1': my_dialog})
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("www-ai.ijs.si")
    conn.request("POST", "/eliza-cgi-bin/eliza_script", params, headers)
    response = conn.getresponse()
    data = response.read()
    reply_from_eliza= str(data.split('</strong>')[2]).split('\n')[1]
    return "%s\r\n" % (reply_from_eliza,)
    conn.close()

# invoking the eliza function to test it's functionality in pythonic way
if __name__== '__main__':
    str = eliza('I love python')
    print str

