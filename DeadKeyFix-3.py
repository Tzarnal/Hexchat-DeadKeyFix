# -*- coding: utf-8 -*-

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
			'u': u'ù',

			'A': u'À',
			'O': u'Ò',
			'E': u'È',
			'I': u'Ì',
			'U': u'Ù'
		},
		'65105': {
			'a': u'á',
			'o': u'ó',
			'e': u'é',
			'i': u'í',
			'u': u'ú',
			'y': u'ý',
			'c': u'ç',

			'A': u'Á',
			'O': u'Ó',
			'E': u'É',
			'I': u'Í',
			'U': u'Ú',
			'Y': u'Ý',
			'C': u'Ç'
		},
		'65106': {
			'a': u'â',
			'o': u'ô',
			'e': u'ê',
			'i': u'î',
			'u': u'û',

			'A': u'Â',
			'O': u'Ô',
			'E': u'Ê',
			'I': u'Î',
			'U': u'Û'
		},
		'65107': {
			'a': u'ã',
			'o': u'õ',
			'n': u'ñ',

			'A': u'Ã',
			'O': u'Õ',
			'N': u'Ñ'
		},
		'65111': {
			'a': u'ä',
			'o': u'ö',
			'e': u'ë',
			'i': u'ï',
			'u': u'ü',
			'y': u'ÿ',

			'A': u'Ä',
			'O': u'Ö',
			'E': u'Ë',
			'I': u'Ï',
			'U': u'Ü',
			'Y': u'Ÿ'
		}
	}
	accents = {
		'65104': '`',
		'65105': "'",
		'65106': '^',
		'65107': '~',
		'65111': '"'
	}
	
	charset =  hexchat.get_info('charset')
	#When there is no current charset derived from server or channel it is set to IRC
	#IRC is not a recognized encoding type so default to utf-8 in that case.
	if(charset == "IRC"):
		charset = "utf-8"

	text = hexchat.get_info('inputbox')
	loc = hexchat.get_prefs("state_cursor")

	if prev in accents and word[2] in specialChars[prev]:		
		#insert an accented character
		text = insert(specialChars[prev][word[2]],text,loc)		
	elif prev in accents and word[2] == ' ':		
		#insert a clean accent ( input was accent followed by space )
		text = insert(accents[prev],text,loc)		
	elif prev in accents and word[0] in accents:		
		#Insert two accents ( input was accent followed by accent )
		text = insert(accents[prev] + accents[word[0]],text,loc)
		loc+=1
	elif prev in accents and int(word[3]) != 0:		
		#insert an accent and a character (character and accent do not combine)
		text = insert(accents[prev] + word[2],text,loc)		
		loc+=1
	elif word[0] in accents:
		#store an accent input
		prev = word[0]		
		return
	else:
		#regular character input
		if int(word[3]) != 0:
			prev = ''			
		return
	prev = ''
			
	settex = u"settext " + text
	hexchat.command( settex )

	hexchat.command('setcursor {}'.format(loc+1))	
	
	return hexchat.EAT_HEXCHAT

def unload_cb(userdata):
	print(__module_name__, 'version', __module_version__, 'unloaded.')

def insert(char,text,loc):
	return u"{}{}{}".format(text[:loc] , char , text[loc:])

hexchat.hook_print('Key Press', keypress_cb) 
hexchat.hook_unload(unload_cb)

print(__module_name__, 'version', __module_version__, 'loaded.')
