# -*- coding: utf-8 -*-

# Original script by Xesyto on github
# Revamped by Joeytje50 on github

import hexchat
import re

__module_name__ = "DeadKeyFix"
__module_version__ = "2.2"
__module_description__ = "Fixes the Us-International deadkey issue"

prev = ''

def keypress_cb(word, word_eol, userdata):
	global prev
	specialChars = {
		'65104': {
			'a': u'à',
			'o': u'ò',
			'e': u'è',
			'i': u'ì',
			'u': u'ù'
		},
		'65105': {
			'a': u'á',
			'o': u'ó',
			'e': u'é',
			'i': u'í',
			'u': u'ú',
			'y': u'ý',
			'c': u'ç'
		},
		'65106': {
			'a': u'â',
			'o': u'ô',
			'e': u'ê',
			'i': u'î',
			'u': u'û'
		},
		'65107': {
			'a': u'ã',
			'o': u'õ',
			'n': u'ñ'
		},
		'65111': {
			'a': u'ä',
			'b': u'ö',
			'e': u'ë',
			'i': u'ï',
			'u': u'ü',
			'y': u'ÿ'
		}
	}
	accents = {
		'65104': '`',
		'65105': "'",
		'65106': '^',
		'65107': '~',
		'65111': '"'
	}
	
	#When there is no current charset derived from server or channel it is set to IRC
	#IRC is not a recognized encoding type so default to utf-8 in that case.
	if(charset == "IRC"):
		charset = "utf-8"
	
	textraw = hexchat.get_info('inputbox')
	text = unicode(textraw, charset)
	loc = hexchat.get_prefs("state_cursor")

	if prev in accents and word[2] in specialChars[prev]:		
		text = insert(specialChars[prev][word[2]],text,loc)
	elif prev in accents and word[2] == ' ':		
		text = insert(accents[prev],text,loc)
	elif prev in accents and word[0] in accents:		
		text = insert(accents[prev] + accents[word[0]],text,loc)
	elif prev in accents and int(word[3]) != 0:		
		text = insert(accents[prev] + word[2],text,loc)
	elif word[0] in accents:
		prev = word[0]
		return
	else:
		if int(word[3]) != 0:
			prev = ''
		return
	prev = ''
		
	loc = hexchat.get_prefs("state_cursor")

	settex = u"settext " + text

	hexchat.command( settex.encode(charset) )
	hexchat.command('setcursor {}'.format(loc+1))	
	
	return hexchat.EAT_HEXCHAT

def unload_cb(userdata):
	print(__module_name__, 'version', __module_version__, 'unloaded.')

def insert(char,text,loc):
	return u"{}{}{}".format(text[:loc] , char , text[loc:])

hexchat.hook_print('Key Press', keypress_cb) 
hexchat.hook_unload(unload_cb)

print(__module_name__, 'version', __module_version__, 'loaded.')
