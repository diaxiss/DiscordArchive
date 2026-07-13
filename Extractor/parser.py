import os
import requests
from typing import Tuple

def parseAttachments(messageId: int, messageAttachments: dict) -> dict:
    attachments = []

    for attachment in messageAttachments:

        id = attachment['id']
        url = attachment['url']
        fileName = attachment['fileName']
        size = attachment['fileSizeBytes']

        if 'cdn.discordapp.com' in url:

            file = requests.get(url)
            if not os.path.exists(f'./data/media/{f"{id}_{fileName}"}'):

                with open(f'./data/media/{id}_{fileName}', 'wb') as output:
                    output.write(file.content)

        url = f'{id}_{fileName}'

        attachments.append({
            'id': id,
            'message_id': messageId,
            'url': url,
            'file_name': fileName,
            'size': size
        })

    return attachments


def parseEmbeds(messageEmbeds: dict) -> dict:

    embeds = []

    for embed in messageEmbeds:
        if embed.get('video'):
            embeds.append({'url': embed.get('video')['canonicalUrl']})

        elif embed.get('url') is not None:
            embeds.append({'url': embed.get('url')})
        else:
            continue
    return embeds


def parseEmoji(emoji: dict) -> dict:
    name = emoji['name']
    code = emoji['code']

    return {'name': name, 'code': code}

def parseReactions(messageId: int, messageReactions:dict) -> dict:

    reactions = []
    for reaction in messageReactions:
        emoji = parseEmoji(reaction['emoji'])
        count = reaction['count']
        users = []
        for user in reaction['users']:
            user = parseUser(user)
            reactions.append({
                'message_id': messageId,
                'user_id': user['id'],
                'emoji': emoji
            })

    return reactions

def parseUser(user: dict) -> dict:
    
    id = user['id']
    name = user['name']
    nickname = user['nickname']
    avatarUrl = user.get('avatarUrl')
    isBot = user.get('isBot', False)

    if not os.path.exists(f'./data/avatars/{id}.png'):
        fetched_image = requests.get(avatarUrl)

        with open(f'./data/avatars/{id}.png', 'wb') as output:
            output.write(fetched_image.content)

    avatarUrl = f'{id}.png'

    return {'id': id, 'name': name, 'nickname': nickname, 'avatarUrl': avatarUrl, 'isBot': isBot}


def parseChannelCategory(json_file: dict, guild_id: str) -> Tuple[dict, dict]:

    channel_id = json_file['channel']['id']
    channel_name = json_file['channel']['name']
    channel_topic = json_file['channel']['topic']
    category_id = json_file['channel']['categoryId']
    category_name = json_file['channel']['category']

    category = {
        'id': category_id,
        'server_id': guild_id,
        'name': category_name
    } if category_id != None else None
    
    channel = {
        'id': channel_id, 
        'name': channel_name,
        'category_id': category_id if (category_id != None) else None,
        'server_id': guild_id if (guild_id != '0') else None,
        'topic': channel_topic,
        'type': 'text'    
    }

    print(channel, category)
    return channel, category


def parseGuild(json_file: dict) -> dict:
    guild_id = json_file['guild']['id']

    guild_name = json_file['guild']['name']
    guild_image = json_file['guild']['iconUrl']
    
    if not os.path.exists(f'./data/guild_icons/{guild_id}.png'):

        fetched_image = requests.get(guild_image)

        with open(f'./data/guild_icons/{guild_id}.png', 'wb') as output:
            output.write(fetched_image.content)

    guild_image = f'{guild_id}.png'

    return {'id': guild_id, 'name': guild_name, 'image': guild_image}