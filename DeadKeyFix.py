# Original script by Xesyto on github
# Revamped by Joeytje50 on github

import hexchat
import re

__module_name__ = "DeadKeyFix"
__module_version__ = "2.0"
__module_description__ = "Fixes the Us-International deadkey issue"

prev = ''

def keypress_cb(word, word_eol, userdata):
	print(word)
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
	if prev in accents and word[2] in specialChars[prev]:
		text += specialChars[prev][word[2]]
	elif prev in accents and word[2] == ' ':
		text += accents[prev]
	elif prev in accents and word[0] in accents:
		text += accents[prev] + accents[word[0]]
	elif prev in accents and int(word[3]) != 0:
		text += accents[prev] + word[2]
	elif word[0] in accents:
		prev = word[0]
		return
	else:
		if int(word[3]) != 0:
			prev = ''
		return
	prev = ''
	hexchat.command('settext {}'.format(text))
	hexchat.command('setcursor {}'.format(len(text)))
	return hexchat.EAT_HEXCHAT

def unload_cb(userdata):
	print(__module_name__, 'version', __module_version__, 'unloaded.')

hexchat.hook_print('Key Press', keypress_cb) 
hexchat.hook_unload(unload_cb)

print(__module_name__, 'version', __module_version__, 'loaded.')
