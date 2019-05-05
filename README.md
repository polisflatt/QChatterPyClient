# QChatterPyClient
A client for QChatter made in Python using QChatterPy

*QChatterPyClient, version 1.0*

QChatterPyClient is a *free* program written in Python 3 that interfaces with QChatterServer, and acts as a client, being able to send and receive messages from two or more parties. It also includes the QChatterPy library that can interface with QChatterServer on a level more easier to create external programs for. This program is not a TUI nor it is a GUI, but rather, it is a simple terminal program that gets from stdin and outputs to stdout. It is a very basic program, and is mainly a proof of concept.

To run you will need:

 - Python 3 (3.6+, most likely; I don't know)
 - Asyncio Python Library (asynchronous programming) 
 - PyGame Python Library (sound)
 - Blessed Python Library (Terminal colors, formatting, etc)
 - Knowledge of Python 3, because you need to edit configuration files written lazily in Python 3 and you must be able to deal with errors, due to the instability and crudeness of the program.

Before you begin, you may want to edit the **settings.py** and **constants.py** file, which contains both some options and the server URL. 

Run **main.py** with Python 3 and get ready for any kind of error. Fix them, then, you will be asked for a username and password. There is a 99.99% chance that you don't have one! You must register an account. 

Run **main.py** with the argument --register. After --register, type your username, your password, and then your confirmed password. Enclose any string that has spaces with "".

Now, run **main.py** and sign in with the credentials. You are now asked for a channel, but, you don't know any, chances are. Type anything, and press enter. Typing a message will print your message, but you will see an alphanumerical string that seems almost magical--and it is. You need to add yourself to the channel list first (sorry, too lazy to make it do this automatically!). But, you also need to create a channel before you can join it.

Type "/create_channel," followed by (spaced) the channel name, a password for it, and a confirmation of the password. You should either see: nothing (error), PHP errors (normal), random alphanumerical string (error/normal), or text that says something meaningful (error/normal/good). 

Now, type "/join_channel", followed by (spaced) the channel name. You are now in the channel. You can now, hopefully, type without any kind of error.

Type "/help" to see some other basic commands.

Dominance over a channel is denoted by a master password. If you want to be an OP visibly, type "/get_op," followed by the master password. Your master password is the password you used when you created the channel.

 
