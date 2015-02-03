# Original script by Xesyto on github
# Revamped by Joeytje50 on github

import hexchat
import re

__module_name__ = "DeadKeyFix"
__module_version__ = "2.0"
__module_description__ = "Fixes the Us-International deadkey issue"

prev = ''

def keypress_cb(word, word_eol, userdata):
	global prev
	specialChars = {
		'65104': {
			'a': 'à',
			'o': 'ò',
			'e': 'è',
			'i': 'ì',
			'u': 'ù'
		},
		'65105': {
			'a': 'á',
			'o': 'ó',
			'e': 'é',
			'i': 'í',
			'u': 'ú',
			'y': 'ý',
			'c': 'ç'
		},
		'65106': {
			'a': 'â',
			'o': 'ô',
			'e': 'ê',
			'i': 'î',
			'u': 'û'
		},
		'65107': {
			'a': 'ã',
			'o': 'õ',
			'n': 'ñ'
		},
		'65111': {
			'a': 'ä',
			'b': 'ö',
			'e': 'ë',
			'i': 'ï',
			'u': 'ü',
			'y': 'ÿ'
		}
	}
	accents = {
		'65104': '`',
		'65105': "'",
		'65106': '^',
		'65107': '~',
		'65111': '"'
	}
	text = hexchat.get_info('inputbox')
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

	hexchat.command('settext {}'.format(text))
	hexchat.command('setcursor {}'.format(loc+1))	
	
	return hexchat.EAT_HEXCHAT

def unload_cb(userdata):
	print(__module_name__, 'version', __module_version__, 'unloaded.')

def insert(char,text,loc):
	return text[:loc] + char + text[loc:]

hexchat.hook_print('Key Press', keypress_cb) 
hexchat.hook_unload(unload_cb)

print(__module_name__, 'version', __module_version__, 'loaded.')
