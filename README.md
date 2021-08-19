# Telegram auto-add stickers

<!-- ABOUT THE PROJECT -->
## About The Project

Automate the process of importing stickers to Telegram, usefull when migrating from Whatsapp.

## Installation

### Getting Telegram app id and hash:

1. Log into [Telegram](https://my.telegram.org/) and navigate to "API development tools". 
   
2. The name and URL of your application does not matter. Just copy the "App api_id" and "App api_hash" info.

### Telegram sticker bot

1. Clone the repo:
   ```sh
   git clone 
   ```

2. Install dependencies (ideally inside a virtual environment):
   ```sh
   pip install -r dependencies.txt
   ```

3. Put all your sticker files (.webp) inside a folder, and create a yaml file (the name does not matter) as bellow:
   ```yaml
   name: "YOUR_PACK_NAME"
   default_emoji: ':EMOJI:'
   ```
   Note that the `default_emoji` field uses single quotes, this is important, or else the Telegram Sticker bot will not recognize your messages.


4.  Run the script:
   ```sh
   python import_stickers.py -id YOUR_ID -ha YOUR_HASH -f STICKER_FOLDER
   ```

> Note: Make sure you don't already have a pack with the same name specified in the yaml file.