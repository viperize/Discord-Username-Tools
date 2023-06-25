# :\\__ Discordize - Discord Name Generator & Checker
# :\\__ Viperize - MIT License
#----------------------------------------------
# | Version
#----------------------------------------------
__version__ = 0.1

# | Imports
#----------------------------------------------
import requests
import string
import json
import ast
from time import sleep
from random import shuffle, choice
from colorama import Fore, init
from datetime import datetime

init(autoreset=True)

# | Constants
#----------------------------------------------
NAMELIST_URL = "https://gist.githubusercontent.com/viperize/b66da66a62f724b3c8ce08ca4d1cde00/raw/da3ceae1c46359f676b6520e7eb162d13cb688ff/"
URL = "https://discord.com/api/v10/users/@me"
DELAY = 2

# | Variables
#----------------------------------------------
token = "PUT YOUR TOKEN INTO THE FILE TOKEN.TXT, NOT HERE"
headers = {}

# | Main Class
#----------------------------------------------
class UsernameChecker:


    def __init__(self, webhook=None, debugging=False):
        self.validUsernames = []
        self.webhook = webhook
        self.debugging = debugging
        self.timeStarted = datetime.now()

    def check_username(self, username):
        data = {"username": username}

        try:
            r = requests.patch(URL, headers=headers, data=json.dumps(data))
            rJson = r.json()

            # If rate limited
            if r.status_code == 429:
                retryTime = max(rJson.get("retry_after"), 5)
                print(Fore.RED + f"You have been rate limited! Will resume in {retryTime}s")
                sleep(retryTime)

            else:
                errors = rJson.get("errors")

                if errors:
                    if errors.get("username"):
                        # Invalid username
                        if self.debugging:
                            print(Fore.RED + username)
                    else:
                        # Valid username
                        print(Fore.GREEN + username)
                        self.validUsernames.append(username)
                        with open("validUsernames.txt", "a") as f:
                            f.write(f"{username}\n")
                        if self.webhook:
                            self.send_to_discord(username)
                else:
                    print(Fore.RED + f'Error validating >> {rJson.get("message")}')

        except Exception as e:
            print(Fore.RED + f"Username check errored: {e}")

    def from_text_list(self, file="./checkUsernames.txt"):
        with open(file, "r") as f:
            for name in f:
                sleep(DELAY)
                self.check_username(name.strip())

        self.is_completed()

    def generate_names(self, users_wanted=1, max_length=20, name_url=NAMELIST_URL):
        nameList = None

        # Get namelist
        try:
            nameListReq = requests.get(name_url).text
            nameList = ast.literal_eval(nameListReq)
            shuffle(nameList)
        except Exception as e:
            print(Fore.RED + "Namelist was unable to load" + str(e))
            return

        # Check each name
        for name in nameList:
            if len(name) > max_length:
                continue

            self.check_username(name)
            if len(self.validUsernames) >= users_wanted:
                break
            sleep(DELAY)

        self.is_completed()

    def generate_names_chars(self, users_wanted, char_length):
        characters = string.ascii_lowercase + "._"

        while len(self.validUsernames) < users_wanted:
            random_string = ""
            while len(random_string) < char_length:
                random_character = choice(characters)

                if random_string[-1:] == random_character and random_character in [".", "_"]:
                    continue

                random_string += random_character

            sleep(DELAY)
            self.check_username(random_string)

        self.is_completed()

    def send_to_discord(self, name):
        data = {
            "embeds": [
                {
                    "title": f"**{name}**",
                    "url": "https://github.com/viperize/",
                    "color": 706405,
                    "footer": {
                        "text": "Discordize"
                    },
                    "timestamp": str(datetime.now())
                }
            ]
        }
        try:
            requests.post(self.webhook, json=data)
        except Exception as e:
            print(Fore.RED + f"Error sending data to webhook: {e}")

    def is_completed(self):
        print(f"\nCompleted in {round((datetime.now()-self.timeStarted).seconds)} seconds")
        print(f"{Fore.LIGHTYELLOW_EX}Available Names: {', '.join(self.validUsernames)}")

# | Functions
#----------------------------------------------
def check_if_outdated():
    cv = requests.get("https://gist.githubusercontent.com/viperize/3524b6d04936ed4e40bea72a94357c73/raw/currentDiscordizeVersion").text
    if cv != str(__version__):
        print(Fore.RED + "[!] THIS VERSION IS OUTDATED, PLEASE UPDATE")

def check_token():
    global token, headers
    
    with open("./token.txt", "r") as f:
        token = f.read().strip()

    headers = {
        "Content-Type": "application/json",
        "Authorization": token,
    }

    discordUser = requests.get(URL, headers=headers)
    if discordUser.status_code == 401:
        print(Fore.RED + "Invalid token inside the file token.txt")
        exit()

    return discordUser.json().get("username")

def show_options():
    discordName = check_token()
    print(Fore.LIGHTYELLOW_EX +
f"""
=============================================================================

██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ ██╗███████╗███████╗
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗██║╚══███╔╝██╔════╝
██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║██║  ███╔╝ █████╗  
██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║██║ ███╔╝  ██╔══╝  
██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝██║███████╗███████╗
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝╚══════╝
                                                                    
>> >> Viperize (https://github.com/Viperize)
>> >> v0.1
>> >> {discordName}
{Fore.WHITE}
> 1 ) Check username list
> 2 ) Generate usernames
> 3 ) Generate 3 character names
> 4 ) Generate 4 character names
{Fore.LIGHTYELLOW_EX}
=============================================================================

""")

# | Initialise
#----------------------------------------------
if __name__ == "__main__":
    check_if_outdated()

    while True:
        show_options()

        try:
            d_webhook = None
            debugging = False
            operation = input(">> ")

            if operation not in ["1", "2", "3", "4"]:
                raise Exception("Invalid input")

            discord = input("Use a webhook? (y/n) ")
            if discord.lower() not in ["y", "n"]:
                raise Exception("Invalid webhook option")
            if discord.lower() == "y":
                with open("./discordWebhook.txt", "r") as f:
                    try:
                        f_url = f.read().strip()
                        wr = requests.get(f_url).json()
                        if wr.get("token"):
                            d_webhook = f_url
                        else:
                            raise Exception("Invalid discord webhook")
                    except Exception as e:
                        print(Fore.RED + f"Error with webhook: {e}")

            debugging_prompt = input("Display unsuccessful names? (y/n) ")
            if debugging_prompt.lower() not in ["y", "n"]:
                raise Exception("Invalid input")
            if debugging_prompt.lower() == "y":
                debugging = True

            checkerInstance = UsernameChecker(d_webhook, debugging)

            if operation == "1":
                checkerInstance.from_text_list()
            else:
                users = input("Number of usernames to generate: ")
                if not users.isdigit():
                    raise Exception("Invalid input for number of users")

                if operation in ["3", "4"]:
                    checkerInstance.generate_names_chars(int(users), int(operation))
                    sleep(5)
                    continue

                max_length = input("Maximum length of username: ")
                if not max_length.isdigit():
                    raise Exception("Invalid input for maximum length")
                if int(max_length) < 3:
                    raise Exception("Invalid username length")
                checkerInstance.generate_names(int(users), int(max_length))

            sleep(5)

        except Exception as e:
            print(Fore.RED + f"Error: {e}\n\n")
            sleep(1)
