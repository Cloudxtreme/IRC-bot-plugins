# dictionaryattack.py
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
#
# To-Do:
#   * Add threading capability
#   * Add ability to crack single hash

from hashlib import md5
from urllib2 import urlopen
import sys 

class dictionaryattack:
    def __init__(self):
       self.allowed_functions = {'help': 1, 'crack': 10 }
    	
    def help(self, bot, sock, buffer):
        sock.msg(buffer.to, "Usage: ")
        sock.msg(buffer.to, " * dictionaryattack.help")
        sock.msg(buffer.to, " * dictionaryattack.crack <hash list url> <word list url>")

    def crack(self, bot, sock, buffer):
        cracked_hashes = {}
        arguments = buffer.msg.split()
        for line in urlopen(arguments[1]):
            cracked_hashes[line.rstrip()] = None
            num_uncracked = len(cracked_hashes)

        for word in urlopen(arguments[2]):
            word = word.rstrip()
            hash = md5(word).hexdigest()

            if hash not in cracked_hashes: continue

            cracked_hashes[hash] = word
            num_uncracked -= 1
            if not num_uncracked: break

        for hash in cracked_hashes:
            if hash: sock.msg(buffer.to, "Found %s as %s" % (hash, cracked_hashes[hash]))
