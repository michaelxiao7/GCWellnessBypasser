# GORDON COLLEGE WELLNESS CHECK AUTOMATOR

We love being asked if we have COVID every single day at 8 AM. It's time to stop LOL

A FEW THINGS TO MENTION:
1) I designed this for Mac, and will be looking into implementing it in Windows in the near future. However, if you have coding/Windows experience, its actually super easy to convert this from Mac to Windows, so feel free to give that a shot

2) Your computer will flash for a frame when the script runs. Don't scream LOL

3) You need Chrome for this to work. That is, unless you can code, and you decide that you really want to run the code on Firefox instead

## WHAT IS INCLUDED IN THE DOWNLOAD:
1) bypass.py - The script that regularly schedules a time to complete the Wellness check
2) bypass_test.py - A test script. You make it executatble, you fill in your credentials, and you run it to make sure your dependencies are in place
3) requirements.txt - A text file with the dependencies you need to download for the script to work. I explain how you do that later on in the guide
4) readme.md - Basically just this guide in text form

## HOW DOES THE SCRIPT WORK?:
At a scheduled time every day, the script runs a chunk of code called ***click_button()***
***click_button()*** does the following:
1) It goes to Gordon 360 in a Chrome window (off-screen) and it logs itself in
2) It checks "No" on the Gordon 360 Wellness check, and hits submit
3) It closes the browser, and waits until the next scheduled time

***But what if I'm actually sick???***
Great question! I'm glad you asked.
Gordon 360 has a bug where if you log out and log back in, you will be asked to fill out the Wellness form, even if you've already done it. This allows you to fill out the form a second time and override your previous response. _(In Comp Sci, this is known as a "race condition")_


## PRE-SETUP:
**NOTE:** 
1) Setting this up assumes you know how to navigate a terminal with bash at a novice level. Therefore little Comp Sci knowledge is needed. There are too many small variables (ex. downloading to Desktop instead of Downloads, terminal starting somewhere else besides your user directory etc.) that can mess up the process.

**_HOWEVER_, I will make an extremely specific Bash setup guide further along, although I wouldn't 100% bank on it working unless everything is _EXACTLY_ as I listed them.**

_If you're not familiar with bash or if the bash setup didn't work for you, feel free to shoot me a message and I will help you set this up! Fear not LOL_


2) You will need to have **pip** installed on your Mac, and by extension, you will need **Python** installed as well. If you have ever coded before, you'll probably have both of these already installed, but if not, download Python here:

**Python 3.8.5:** https://www.python.org/downloads/

To install **pip 20.2.4:**, go to terminal and enter the following:

    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

Hit enter, wait for stuff to  download, then enter the following:

    python get-pip.py



## VERY DETAILED SETUP GUIDE BEGINS NOW
Download the code, and move the entire folder to your Desktop. Navigate to the Wellness folder with bash. To do this, open terminal, and type in the following:

    cd Desktop/Wellness

Enter the following in terminal to download the dependencies (selenium, webdriver-manager, schedule):

    pip install -r requirements.txt
  
This installs all of the dependencies needed to run my script.


***Keep terminal open*** and go to **System Preferences -> Energy Saver -> Schedule..**. Schedule a time for your Mac to wake up every single day. This guarantees that even if you're not awake when the script needs to run, the script will be able to run anyways. Feel free to set a "sleep" time as well. For reference, I have my Mac wake up at 7:00 AM, the script runs at 7:00:02 AM (7 AM and 2 seconds) every morning, and optionally, I have it go back to sleep at 7:01 AM because I'm never actually up when the script runs.

Go back to your terminal window. You should still be in the Wellness folder in terminal. Check this by entering in the terminal:

    pwd
    
Terminal should return something like:

    /Users/username/Desktop/Wellness

Now, make the python script executable by entering the following:
    
    chmod +x bypass.py
    
In the meantime, do the same with the test script by doing the following:

    chmod +x bypass_test.py
    
If you are eager to test this script out, move on to ***CUSTOMIZATION GUIDE AND RUNNING THE SCRIPT***, complete your test script, and run the test script!

That's about it for the setup!


## CUSTOMIZATION GUIDE AND RUNNING THE SCRIPT
**Customization:**
To edit the script, open it with any text editor (Pages, for example), and edit the areas where it asks for your _Username_ and _Password_. The script will automatically log you in to Gordon 360 before completing the Wellness check.

You can also edit the time the script runs at the bottom of the script, around the second to last line of code. I left a comment there to help you out.

**Running the Script:**
To actually run the script, navigate to the Wellness folder in terminal (cd Desktop/Wellness) and enter the following:

    ./bypass.py

If nothing happens and the terminal just enters a limbo, the system works! Great job on setting this all up and following along!
Leave it running in the background, and don't close the terminal window. The terminal window needs to be open for the script to be run. The computer must also be on for the script to run since it's running locally on your computer, not on a server (that's why scheduling your computer to wake up is helpful).

**NOTE:** In order for your computer to wake up, your computer MUST BE PLUGGED IN, the computer CANNOT BE CLOSED, and it must be put to SLEEP, NOT SHUT DOWN.
(At night, I have my computer on my desk, plugged in, with the laptop open (laptop screen and keyboard visible), and I put my computer to sleep by clicking the apple icon on the top left of and clicking "sleep")

----------

If you have any questions, feel free to message me! This task was assignmened to me as a challenge by another CS friend, and here is my response :))) This took me about 50 minutes to research/create.
