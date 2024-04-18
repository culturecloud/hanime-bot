# This project is poorly written. If anyone wants me to rewrite it, open an issue. This version still works; it's just bad code.

# Hanime auto coin collector +
The hanime mobile app gives coins as a reward for clicking on an ad. This has a cooldown of 3 hours. It gets really annoying to open the app every 3 hours and then click on an ad. You can use these coins to get a month of premium, but you can do this as often as you want.

This script when run, will forge a request to the server claiming that you have clicked on the ad. The server then adds the coins to your account. It still checks the last clicked time, so you can only run this once every 3 hours. But this makes it easier to automate getting coins.

Optionaly it will send the amout of coins you currently have to your discord webhook automaticaly.

Tested on ~~current~~ outdated version 3.7.1

Tested on current version 3.11.4 -by zip6como

## Full tutorial with pictures to get this working
You can view a full tutorial on getting this to work here:
https://github.com/zip6como/hanime-auto-coins-plus/wiki

If you get any errors or need any help, feel free to open an issue.

You can do this on the original repository to get help by the original creator of this.

You can do this here to get help by me (zip6como)

## Quickstart (advanced users)
1. Clone this repository 
2. Install all the requirements:
`pip install -r requirements.txt`
3. Open `.env` file and enter your hanime email and password
4. Open the webhook.py and enter your webhook
5. Run the script.

## Does this work on my...?
[Windows Computer](https://github.com/zip6como/hanime-auto-coins-plus/wiki/Windows-Tutorial): yes <br>
[Raspberry Pi](https://github.com/zip6como/hanime-auto-coins-plus/wiki/Linux-Tutorial): yes <br>
[Debian based distro (Ubuntu,Debian,Pop! os, etc.)](https://github.com/zip6como/hanime-auto-coins-plus/wiki/Linux-Tutorial): yes <br>

MacOS mashine: probably [you can install python on OSX but i won't provide any help] <br>
Other linux distro: maybe [you probably can install python on your distro but i won't provide any help] <br>
Android phone: unlikely [i don't know if there is python for android but i won't provide any help] <br>
iPhone: No [apple does not allow you to install apps outside of the appstore and i won't provide any help] <br>

## I have a problem/suggestion
Open an issue [here](https://github.com/zip6como/hanime-auto-coins-plus/issues) don't forget to follow the template.

## How does it work?
When we observe the requests made by the app to it's server, we'll see that, to get coins the app makes a request containing a reward token. The server then validates the reward token and gives us the coins. The token is generated on the client side somewhere when you click on an ad.

What we'd like to do is directly send this request through a script without ever clicking on an ad. So we want to reverse engineer the app a bit to understand how this token is generated.

Hanime app is based on react native framework. So the main logic of the program is mostly written in javascript. Decompiling the apk we get the minified javascript. We quickly find the token generation mechanism. The token is just a SHA-256 hash of a dynamically generated string concatenated with the current time. The server verifies if the hash matches and checks whether if 3 hours have passed since last click on ad.

We can generate random tokens now, but when we try sending this request we get an 
```
{"errors":["Unauthorized"]}
```
in response. On inspection of actual requests made by the app, we see that it includes headers called `X-Claim, X-Signature`. These are probably used to verify whether if the request comes from the actual app or a script like this one. `X-Claim` is just the current time in epoch time standard. But some reversing is required to know how is `X-Signature` generated. 

This time the signature wasn't generated in the javascript code, but inside the react native modules in java. Again the signature turned out to be SHA-256 hash of a dynamically generated string based on current time. 

After this we can include these headers in our request each time to make fake requests.

## Legal
I do not take any responsibility for this tool usage in the malicious purposes. It is free, open-source and provided AS-IS for everyone. <br>
Any requests by Hanime.tv to take this down will be followed. <br>
The original creator of this script (the core of this repository) has not provided a license for his repository so any requests by him to take this down will be followed.

## Contributing
Fork this repositorum and make a pull request. <br>
If your pull request gets accepted you get a spot down below. <br>

You can also just report spelling mistakes or other mistakes anywhere in the repository [here](https://github.com/zip6como/hanime-auto-coins-plus/issues) (but only major ones get credited down below).

## Credits
[WeaveAche](https://github.com/WeaveAche) - The creator of the original script <br> 
--> [ipdan4ik](https://github.com/ipdan4ik) - Contributor to the original script <br>
--> [Golumpa](https://github.com/Golumpa) - Contributor to the original script <br>
--> [Alistair1231](https://github.com/Alistair1231) - Contributor to the original script <br>
[zip6como](https://github.com/zip6como) - Creator of this fork & full tutorial on how to use
           
