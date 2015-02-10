Hexchat-DeadKeyFix
==================

This python plugin for Hexchat fixes an issue in GTK that occurs when using a US-International keyboard layout on windows. All accents ( ` ~ ^ ' " ) will be placed on the next character typed, including ones that don't normally get an accent.

This plugin fixes that by changing back to the normal behaviour of the quotes, and placing accents on top of those letters that would normally get accents. A whole list can be seen in the source code.

Installation
==================

Ensure you have Hexchat installed with python plugin and that you've installed Python 2.7.5 for scripts. If not you can find links here: http://hexchat.github.io/downloads.html

Add the proper DeadKeyFix.py file to your %appdata%\HexChat\addons folder. If you've got python 2.x installed, you should add DeadKeyFix.py, and if you have Python 3.x installed, you should add DeadKeyFix-3.py.

Relevant Links
==================

Hexchat Issue: https://github.com/hexchat/hexchat/issues/37
GTK Bugzilla Entry: https://bugzilla.gnome.org/show_bug.cgi?id=569581
