import json
import sqlite3
import requests
import os

from addMessagesToDB import *
from parser import *


allFields = set(
        { 'reactions': True,
        'interaction': None,
        'id': True,
        'mentions': True,
        'isPinned': True,
        'attachments': True,
        'type': True,
        'author': True,
        'inlineEmojis': True,
        'reference': True,
        'timestampEdited': True,
        'content': True,
        'stickers': False,
        'callEndedTimestamp': False,
        'timestamp': True,
        'embeds': True }
    )


def printMessage(message: dict) -> None:

    print(f"id: {message['id']}")
    print(f"type: {message['type']}")
    print(f"channel: {message['channel']}")
    print(f"category: {message['category']}")
    print(f"author: {message['author']}")
    print(f"content: {message['content']}")
    print(f"attachments: {message['attachments']}")
    print(f"reactions: {message['reactions']}")
    print(f"mentions: {message['mentions']}")
    print(f"isPinned: {message['isPinned']}")
    print(f"timestamp: {message['timestamp']}")
    print(f"timestampEdited: {message['timestampEdited']}")
    print(f"reference: {message['reference']}")
    print(f"embeds: {message['embeds']}")


def extractor(path: str):
    con = sqlite3.connect('./data/database.db')
    cur = con.cursor()
    
    with open(f'{path}', 'r', encoding='utf-8') as input:
        json_file = json.load(input)

    guild = parseGuild(json_file)
    
    if guild['id'] != 0:
        addGuildToDB(guild, con, cur)

    channel, category = parseChannelCategory(json_file, guild['id'])

    addCategoryToDB(category, con, cur)
    addChannelToDB(channel, con, cur)

    userSet = set()

    for message in json_file['messages']:

        id = message['id']
        type = message['type']
        author = parseUser(message['author'])

        if author['id'] not in userSet:
            userSet.add(author['id'])
            addUserToServer(author, guild['id'], con, cur)
            addUserToChannel(author, channel['id'], con, cur)

        content = message['content']
        attachments = parseAttachments(id, message['attachments'])
        reactions = parseReactions(id, message['reactions'])
        mentions = [parseUser(mention) for mention in message['mentions']]
        isPinned = message['isPinned']
        inlineEmojis = [parseEmoji(emoji) for emoji in message['inlineEmojis']]
        timestamp = message['timestamp']
        timestampEdited = message['timestampEdited']
        reference = message.get('reference')
        if reference:
            reference = reference.get('messageId')

        embeds = parseEmbeds(message['embeds'])


        parsedMessage = {
            'id': id,
            'type': type,
            'channel_id': channel['id'],
            'category_id': category['name'] if category else None,
            'author': author,
            'content': content,
            'attachments': attachments,
            'reactions': reactions,
            'mentions': mentions,
            'isPinned': isPinned,
            'timestamp': timestamp,
            'timestampEdited': timestampEdited,
            'reference': reference,
            'embeds': embeds,
        }

        addMessageToDB(parsedMessage, con, cur)
    
    con.commit()
    con.close()

def main():
    extractor()

if __name__ == '__main__':
    main()