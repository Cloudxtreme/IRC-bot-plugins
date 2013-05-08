# tiny.py
# (C) 2013 Martijn Gonlag
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 1, or (at your option)
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import tinyurl
import urllib
import re

class tiny:
    def __init__(self):
    
        self.allowed_functions = {'create': 0, 'undo': 0, 'help': 0}
    
    def help(self, bot, sock, buffer):
        sock.msg(buffer.to, 'Usage: ')
        sock.msg(buffer.to, ' * tiny.create <url> -- generates new tinyurl')
        sock.msg(buffer.to, ' * tiny.undo <url> -- remove tinyurl')
    
    def create(self, bot, sock, buffer):
        arguments = buffer.msg.split()
        url = tinyurl.create_one(arguments[1])
        sock.msg(buffer.to, url)
        
    def undo(self, bot, sock, buffer):
        arguments = buffer.msg.split()
        api_url = urllib.urlopen("http://api.unshort.me?r=%s&t=xml" % (arguments[1])).read()
        search = re.search("<resolvedURL>http://tinyurl.com/([^<]+)</resolvedURL>",  api_url).group(1)
        sock.msg(buffer.to, 'www.' + search)
