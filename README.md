# MeemaBot
My personal Discord bot, now rewrittten with discord.py

Trello to track progress: https://trello.com/b/y1TgGcpQ/meema-bot

This bot was originally created for the Touhou ~ Fanworks 'n Chill Discord server, and has been used across a couple small-medium scale Discord servers.
As of late, the original discord.js source code has been lost, so this repo acts to make sure the source code isn't lost again, and others are free to use and repurpose it as they see fit.  (And to potentially keep better track of things like feature requests.)

Important history: https://www.youtube.com/watch?v=qTKx9C01Peo

If you would like to use this for yourself, here's the instructions for installation.

## Prep

#### music.py
I use this github gist as my music bot, with a couple adjustments.  Simply save it as music.py and comment out lines 503 to the end.
https://gist.github.com/vbe0201/ade9b80f2d3b64643d854938d40a0a2d

#### auth.py
Obviously I can't share my auth.py due to containing the token, though I can show you how to set it up.
```
def setAuth():
    token = 'your token here'
    prefix = 'prefix'
    
    return (token, prefix)

```
Quite literally that's all you need.  You could even store other data in setAuth if you wish when you pass the tuple.
Obviously you need a bot token created through Discord's developer page for this to work properly.

## Installation
These instructions assume you're running it on either a Linux (Ubuntu-based) or Windows platform, as these are the platforms I regularly run the bot on.

1. In terms of dependencies, make sure you have these things installed: Python 3.5 or higher + pip, FFmpeg (If on Windows: place the binaries in the bot folder, add Python to your PATH)
`sudo apt-get install python3 python3-pip ffmpeg`

2. In a Terminal or PowerShell window, install these with pip in the bot directory:
`pip install -U discord.py pynacl youtube-dl`
On Ubuntu, I noticed that you may have to run it this way, through python3 (if you have python 2.4 installed)
`python3 -m pip install -U discord.py pynacl youtube-dl`

3. Unlike discord.js, this bot actually has exception handling, so running a simple bash script (or batch script on Windows) is unnecessary, but I run one anyway.  The reason being the planned `update` command with the bot, which restarts the bot without needing to access the server computer.  I have a simple bash script set up this way:
```
#!/bin/bash
echo Starting bot loop, Ctrl+C to exit...
while (true)
do
	python3 bot.py
done
```
Run `chmod u+x <bash script here>` as well so you can run it in your terminal.

I noticed that keyboard interrupts are a bit finnicky with Python compared to my old node.js setup so this could be improved - let me know if you have any suggestions. For now you may need to press Ctrl+C several times.

If you're on Windows, here's my example batch script I've been using:
```
title Meema Bot Loop
:loop
node .\bot.js
goto loop
```

4. Before you actively run the bot, take a look at the behavior at the coroutine handling the event `on_message`.
```
if message.content.startswith(prefix):
        pieces = message.content.split()
        cmd = pieces[0]
        log_channel = bot.get_channel(541002881688666133)
        await log_channel.send(message.author.name + "#" + message.author.discriminator + ' used the ' + cmd + ' command in ' + message.guild.name + '.')
```
At present, this links to a specific Discord server that logs when actions happen.  This was used in the past to track when issues went wrong, and is mainly for debug purposes.  I still use it when testing new commands with the bot.  This function logs the user's name (not ID), the server it was used in, and the command used - though obviously for the privacy minded, this is likely already too much (and unnecessary at that), and I completely understand that.  Therefore, it is your choice what to do with this code, be it omitting it entirely for privacy's sake, or keeping it in and changing the channel ID.  Should you choose to keep this code, do know that this code will not work as is if your bot instance is not in my bot test server, and that server will remain private.  Make your own bot test server and adjust the channel ID if you wish.
(This section may become depreciated soon, as I may also have it tied to a debug variable in the auth tuple.  Stay tuned.)

5. To run the bot, just run the bash/batch script you had set up earlier in a Terminal/PowerShell window.

That's all you need!
