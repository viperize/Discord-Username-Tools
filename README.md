# Discordize
Discord name generator (finder, sniper, validator or whatever), can either go through a worldlist of English words, generate 3-4 character names or check if names in a namelist are available.

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPL-3.0 License][license-shield]][license-url]


## About Discordize

### Installation Guide Below

**NOTE: Until proxy support is added you may find you are being rate limited, this may be added in the future**

<img src="https://i.imgur.com/ZtOiaQk.png">

Examples of names the bot has generated: *misframed, unworship, unencountered* (+ multiple 4 letter names)

## Getting Started

### Installation

1. Download Python 3 (Install to PATH) [https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe)
2. Clone the repo or click the green `Code` button at the top and `Download as ZIP`
   If downloaded as a ZIP, right click and extract to folder. If you are cloning:
  ```sh
    git clone https://github.com/viperize/Discord-Username-Tools.git
  ```
3. Open command prompt (cmd) and go to the directory you downloaded it at
  ```sh
    cd C:\Users\youruserhere\Documents\Folder
  ```
4. Install requirements
  ```sh
    py -m pip install -r requirements.txt
  ```
5. Insert your discord token into the "token.txt" file, if you dont know how: [https://www.androidauthority.com/get-discord-token-3149920/](https://www.androidauthority.com/get-discord-token-3149920/)
5. Run the program
  ```sh
    python discordNameChecker.py
  ```
Settings are configurable, I have set the delay to 2 seconds by default to prevent getting ratelimited, feel free to change `DELAY`

### Using Discord Webhooks
1. Right click a discord channel and go to "Integrations"
2. Click "View Webhooks" and click "New Webhook"
3. Click "Copy Webhook URL"
4. Paste this webhook into the "discordWebhook.txt" file in the **SAME** directory as the main program and save
  
## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.

[contributors-shield]: https://img.shields.io/github/contributors/viperize/Discord-Username-Tools.svg?style=for-the-badge
[contributors-url]: https://github.com/viperize/Discord-Username-Tools/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/viperize/Discord-Username-Tools.svg?style=for-the-badge
[forks-url]: https://github.com/viperize/Discord-Username-Tools/network/members
[stars-shield]: https://img.shields.io/github/stars/viperize/Discord-Username-Tools.svg?style=for-the-badge
[stars-url]: https://github.com/viperize/Discord-Username-Tools/stargazers/
[issues-shield]: https://img.shields.io/github/issues/viperize/Discord-Username-Tools.svg?style=for-the-badge
[issues-url]: https://github.com/viperize/Discord-Username-Tools/issues
[license-shield]: https://img.shields.io/github/license/viperize/Discord-Username-Tools.svg?style=for-the-badge
[license-url]: https://github.com/viperize/Discord-Username-Tools/blob/main/LICENSE
