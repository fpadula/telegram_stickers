import argparse
import yaml
import os
from telethon import TelegramClient
import emoji

async def process_stickers(client, sticker_filename_list, packname,
                            default_emoji):
    # Getting client info    
    me = await client.get_me()
    print("Creating stickers for user with phone", me.phone)
    # Processing stickers one by one
    async with client.conversation('Stickers', max_messages=10000) as conv:
        await conv.send_message('/newpack')
        _ = await conv.get_response()        
        await conv.send_message(packname)
        _ = await conv.get_response()
        for sticker_file_name in sticker_filename_list:
            await conv.send_file(sticker_file_name)
            _ = await conv.get_response()
            await conv.send_message(emoji.emojize(default_emoji))
            _ = await conv.get_response()                
        await conv.send_message("/publish")
        _ = await conv.get_response()                
        await conv.send_message("/skip")
        _ = await conv.get_response()      
        await conv.send_message("sn"+packname)
        _ = await conv.get_response()        

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-id", "--api_id", help= ("Your App API id."),
                        type=int, required=True)
    parser.add_argument("-ha", "--hash", help= ("Your App API hash."),
                        required=True)
    parser.add_argument("-f", "--folder", help= ("The root folder of a sticker"
                                                 "pack."), required=True)

    # Openning sticker pack description file (.yaml inside folder)
    args = parser.parse_args()
    yaml_files = [f for f in os.listdir(args.folder) if f.endswith('.yaml')]
    if len(yaml_files) != 1:
        raise ValueError(("More than one configuration file (.yaml) found. Only"
        "one expected"))
    (top_folders, folder) = os.path.split(args.folder)
    pack_desc_fname = os.path.join(top_folders, folder, yaml_files[0])

    with open(pack_desc_fname) as pack_desk_file:
        pack = yaml.load(pack_desk_file, Loader=yaml.FullLoader)

    # Signing in
    client = TelegramClient('anon', args.api_id, args.hash)

    # Processing stickers
    sticker_files_names = [os.path.join(top_folders, folder, f) for f in
                            os.listdir(args.folder) if f.endswith('.webp')]

    with client:
        client.loop.run_until_complete(process_stickers(client,
                                                        sticker_files_names,
                                                        pack["name"],
                                                        pack["default_emoji"]))        

if __name__ == '__main__':
    main()