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

from urllib2 import urlopen
import feedparser
import tinyurl

class news:
    def __init__(self):
        self.printed = []
        self.allowed_functions = { 'help':0, 'cnn':0, 'cnet':0 }
        
    def help(self, bot, sock, buffer):
        sock.msg(buffer.to, "Usage: ")
        sock.msg(buffer.to, " * news.cnn -- change cnn to your favorite news site")
        sock.msg(buffer.to, " * news.cnn more -- to load more news")         
     
    def get_five(self, rss, more=False):
        feeds = { 'cnn':'http://rss.cnn.com/rss/cnn_latest.rss', 'cnet':'http://feeds.feedburner.com/cnet/tcoc.rss' }
        d = feedparser.parse(feeds[rss])

        num = 0
        buffer = ""
        for e in d.entries:
            if e.link not in self.printed or not more:
                url = tinyurl.create_one(e.link)
                if e.link not in self.printed: self.printed.append(e.link)
                buffer += '\x0304%s\x03 \x0300-- Read more: %s\n' % (e.title, url)
                num += 1
                if num == 5: break

        return buffer

    def cnn(self, bot, sock, buffer):
        more = buffer.msg.split()
        if len(more) > 1 and more[1] == "more":
            sock.msg(buffer.to, self.get_five('cnn', more=True))
        else:
            sock.msg(buffer.to, self.get_five('cnn'))
            
    def cnet(self, bot, sock, buffer):
        more = buffer.msg.split()
        if len(more) > 1 and more[1] == "more":
            sock.msg(buffer.to, self.get_five('cnet', more=True))
        else:
            sock.msg(buffer.to, self.get_five('cnet'))
