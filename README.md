# rocket-launch-reminder
A program that reminds you around 10 minutes before a rocket launch and reminds you of the rocket launches today on program startup. This is project compatible with windows only and is intended for personal use.

It notifies you through the notification center on Windows:

![image](https://user-images.githubusercontent.com/98898166/212238843-76ee3fd2-0958-4b92-978b-5ab22b1bba85.png)

# Installing Dependencies

Install dependencies using the command:
```shell
$ pip install requests notifypy
```

# Setting up the program to run on startup

To make this program run on startup, first clone this repository. Then, change the file extension of `main.py` to `.pyw` (so the entire filename would look like `main.pyw`). This means the program does not open a console window.

Once done, open Run with Win + R and type `shell:startup`. Finally, add a shortcut to your `main.pyw` file.

# Disclaimer

I do not own any images or data that shows in notifications.

The notification data is provided by [RocketLaunch.live](https://www.rocketlaunch.live/api). The images are provided by Wikipedia or NASA.