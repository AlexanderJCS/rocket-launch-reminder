# rocket-launch-reminder
A program that reminds you around 10 minutes before a rocket launch and reminds you of the rocket launches today on program startup. This is project compatible with windows, linux, and mac.

Here is an example of a notification from the program on Windows:

![image](https://user-images.githubusercontent.com/98898166/212386683-7a555c44-6f34-4ade-839a-4c127383e490.png)

*Operating systems other than Windows are not tested and are not guaranteed to work. If it does not work on your operating system, please open an issue.*

# Installing Dependencies

Install dependencies using the command:
```shell
$ pip install requests notify-py
```

# Setting up the program to run on startup (Windows)

To make this program run on startup, first clone this repository. Then, change the file extension of `main.py` to `.pyw` (so the entire filename would look like `main.pyw`). This means the program does not open a console window.

Once done, open Run with Win + R and type `shell:startup`. Finally, add a shortcut to your `main.pyw` file.

# Disclaimer

I do not own any images or data that shows in notifications.

The notification data is provided by [RocketLaunch.live](https://www.rocketlaunch.live/api). The images are provided by Wikipedia or NASA.
