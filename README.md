Hexchat-DeadKeyFix
==================

This python plugin for Hexchat fixes an issue in GTK that occurs when using a US-International keyboard layout on windows. When trying to input a single quote an accute accent (´) is the result and when trying to input a double quote a trema(¨) is the result.

This plugin fixes that by subsituting a ' for a ´ and a " for a ¨. This is a very ugly solution to the issues and naturally stops you from using the ¨ or ´ entirely in Hexchat, which to me is an acceptable loss for actually being able to use quote marks properly.

Installation
==================

Ensure you have Hexchat installed with python plugin and that you've installed Python 2.7.5 for scripts. If not you can find links here: http://hexchat.github.io/downloads.html

Add the DeadKeyFix.py file to your %appdata%\HexChat\addons folder. 

Relevant Links
==================

Hexchat Issue: https://github.com/hexchat/hexchat/issues/37
GTK Bugzilla Entry: https://bugzilla.gnome.org/show_bug.cgi?id=569581
