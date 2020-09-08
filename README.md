# GORDON COLLEGE WELLNESS CHECK AUTOMATOR

We love being asked if we have cover every single day at 8 AM. It's time to stop LOL

A FEW THINGS TO MENTION:
1) I designed this for Mac, and will be looking into implementing it in Windows in the near future. However, if you have coding experience, its actually super easy to convert this from Mac to Windows, so feel free to give that a shot

2) Your computer will flash for a frame when the script runs. Don't scream LOL

3) You need Chrome for this to work. That is, unless you can code, and you decide that you really want to run the code on Firefox instead

SETUP:
NOTE: Setting this up assumes you know how to navigate a terminal with bash. A little Comp Sci knowledge is needed.
If you're not familiar with bash, feel free to shoot me a message and I will help you set this up! Fear not LOL

After downloading this, navigate to the Wellness folder, wherever you downloaded it. This is so we can install the necessary dependencies.

Enter the following in terminal to download the dependencies (selenium, webdriver-manager, crontab):
    
    pip install -r requirements.txt
  
Now type 'crontab -e' in bash to open up vim. You crontab is used to schedule scripts for your computer to run on a daily/weekly/monthly basis

Type the following:
  
    @daily /usr/bin/python bypass.py

You will be asked something about computer permissions LOL. Click yes. You're basically giving your computer the permissions to run this script daily.

That's about it! If you have any questions, feel free to message me! This task was assignmened to me as a challenge by another CS friend, and here is my response :))) This took me about 50 minutes to research/create.
