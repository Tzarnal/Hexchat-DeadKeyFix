import xchat as hexchat
import re

__module_name__ = "DeadKeyFix"
__module_version__ = "1.0"
__module_description__ = "Fixes the Us-International deadkey issue"

checkP = re.compile("¨|´")
replaceP1 = re.compile("¨")
replaceP2 = re.compile("´")

def keypress_cb(word, word_eol, userdata):
	inputtext = hexchat.get_info('inputbox')
	
	m = checkP.search(inputtext)
	if m:
		inputtext = replaceP1.sub('"',inputtext)
		inputtext = replaceP2.sub("'",inputtext)
		hexchat.command('settext {}'.format(inputtext))
		hexchat.command('setcursor {}'.format(len(inputtext)))

def unload_cb(userdata):
	print(__module_name__, 'version', __module_version__, 'unloaded.')

hexchat.hook_print('Key Press', keypress_cb) 
hexchat.hook_unload(unload_cb)

print(__module_name__, 'version', __module_version__, 'loaded.')