from winotify import Notification, audio
import requests

from dataclasses import dataclass
from datetime import datetime

import time
import json

with open("config.json", "r") as f:
    CONFIG = json.load(f)


@dataclass()
class Launch:
    id: int
    time: datetime
    provider: str
    rocket: str
    launch_site: str
    mission_name: str
    description: str
    link: str


def get_link(full_str: str) -> str:  # sourcery skip: use-next
    """
    Takes a full string with a URL and returns only the first URL. Used to find the URL in
    the "quicktext" field of the data to watch the launch. The link must have a space at
    the end or be at the end of the string.

    :param full_str: The full string with the URL included
    :return: only the URL
    """

    start_index = full_str.index("htt")

    for i, char in enumerate(full_str[start_index:]):
        if char == " ":
            end_index = i + start_index
            break

    else:  # nobreak
        end_index = len(full_str)

    return full_str[start_index:end_index]


class RocketReminder:
    def __init__(self):
        self.launches = None
        self.launch_reminders = {}  # key/value pairs of launch IDs and if the user has been reminded yet.

        self.get_launches()

    def get_launches(self):
        raw_data = requests.get("https://fdo.rocketlaunch.live/json/launches/next/5").json()

        launches = []

        for launch in raw_data["result"]:
            launch_site = launch["pad"]["location"]["name"]

            if statename := launch["pad"]["location"]["statename"] is not None:
                launch_site += f", {statename}"

            if self.launch_reminders.get(launch["id"]) is None:
                self.launch_reminders[launch["id"]] = False

            launches.append(Launch(
                id=launch["id"],
                time=datetime.fromtimestamp(int(launch["sort_date"])),
                provider=launch["provider"]["name"],
                rocket=launch["vehicle"]["name"],
                launch_site=launch_site,
                mission_name=launch["name"],
                description=launch["launch_description"],
                link=get_link(launch["quicktext"])
            ))

        self.launches = launches

    def remind_startup(self):
        self.get_launches()

        for launch in self.launches:
            if launch.time.date() == datetime.now().date() and \
                    launch.time > datetime.now():

                reminder = Notification(
                    app_id="Launch Today",
                    title=f"{launch.provider} {launch.rocket} launch today at {launch.time.strftime('%H:%M')}",
                    msg=f"{launch.description} | Data by RocketLaunch.Live",
                    duration="long"
                )

                reminder.set_audio(audio.SMS, loop=False)
                reminder.add_actions(label="Launch Video", launch=launch.link)

                reminder.show()

    def update(self):
        self.get_launches()

        for launch in self.launches:
            t_minus = launch.time.timestamp() - time.time()

            if 0 < t_minus < CONFIG["remind_before_launch_mins"] * 60 and \
                    not self.launch_reminders.get(launch.id):

                self.launch_reminders[launch.id] = True

                reminder = Notification(
                    app_id="Launch Reminder",
                    title=f"{launch.provider} {launch.rocket} launch in {t_minus // 60} mins",
                    msg=f"{launch.description} | Data by RocketLaunch.Live",
                    duration="long"
                )

                reminder.set_audio(audio.LoopingAlarm2, loop=False)
                reminder.add_actions(label="Launch Video", launch=launch.link)

                reminder.show()


def main():
    rocket_reminder = RocketReminder()

    if CONFIG["remind_on_startup"]:
        rocket_reminder.remind_startup()

    while True:
        rocket_reminder.update()
        time.sleep(CONFIG["refresh_secs"])


if __name__ == "__main__":
    main()
