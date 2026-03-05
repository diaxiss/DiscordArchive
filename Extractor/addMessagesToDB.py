def addGuildToDB(guild: dict, con, cur) -> bool:
    
    if guild['id'] == '0':
        return False

    cur.execute('''
        INSERT OR IGNORE INTO servers
        VALUES(?, ?, ?)
        ''',
        [
            guild['id'],
            guild['name'],
            guild['image']
        ])


def addCategoryToDB(category: dict, con, cur) -> bool:
    
    if category == None:
        return False

    cur.execute('''
        INSERT OR IGNORE INTO categories(id, name, server_id)
        VALUES(?, ?, ?) 
        ''',
        [
            category['id'],
            category['name'],
            category['server_id']
        ]
    )

def addChannelToDB(channel: dict, con, cur) -> bool:
    
    cur.execute('''
        INSERT OR IGNORE INTO channels(id, server_id, category_id, name, type, topic)
        VALUES (?, ?, ?, ?, ?, ?)
        ''',
        [
            channel['id'], 
            channel['server_id'],
            channel['category_id'],
            channel['name'],
            channel['type'],
            channel['topic']
        ]
    )

def addUserToServer(user: dict, server_id, con, cur) -> bool:
    
    if server_id == '0':
        return False

    cur.execute('''
        INSERT OR IGNORE INTO server_members(user_id, server_id, nickname)
        VALUES(?, ?, ?)
    ''',
    [
        user['id'],
        server_id,
        None
    ])

def addUserToChannel(user: dict, channel_id, con, cur) -> bool:

    cur.execute('''
        INSERT OR IGNORE INTO channel_members
        VALUES(?, ?)
    ''',
    [
        channel_id,
        user['id']
    ])


def addMessageToDB(message: dict, con, cur) -> bool:
        
    # ================
    # USERS
    # ================
    
    # insert author or ignore
    cur.execute('''
        INSERT OR IGNORE INTO users
        VALUES(?, ?, ?, ?, ?)
    ''', [
        message['author'].get('id'),
        message['author'].get('name'),
        message['author'].get('nickname'),
        message['author'].get('avatarUrl'),
        1 if message['author'].get('is_bot') else 0
    ])

    # insert mentioned user or ignore
    for mention in message['mentions']:
        cur.execute('''
            INSERT OR IGNORE INTO users
            VALUES(?, ?, ?, ?, ?)
        ''', [
            mention.get('id'),
            mention.get('name'),
            mention.get('nickname'),
            mention.get('avatarUrl'),
            1 if mention.get('is_bot') else 0
        ])

    # insert users from reactions
    for reaction in message['reactions']:
        cur.execute('''
            INSERT OR IGNORE INTO users
            VALUES(?, ?, ?, ?, ?)
        ''', [
            reaction.get('id'),
            reaction.get('name'),
            reaction.get('nickname'),
            reaction.get('avatarUrl'),
            1 if reaction.get('is_bot') else 0
        ])


    # MESSAGES
    cur.execute('''
        INSERT OR IGNORE INTO messages
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', [
        message.get('id'),
        message['author'].get('id'),
        message.get('channel_id'),
        message.get('content'),
        message.get('type'),
        message.get('isPinned'),
        message.get('timestamp'),
        message.get('timestampEdited'),
        message.get('reference')
    ])

    # ATTACHMENTS

    for attachment in message['attachments']:
        cur.execute('''
            INSERT OR IGNORE INTO attachments
                (message_id, url, file_name, size_bytes)
            VALUES(?, ?, ?, ?)
        ''', [
            message.get('id'),
            attachment.get('url'),
            attachment.get('file_name'),
            attachment.get('size')
        ])

    # REACTIONS

    for reaction in message['reactions']:
        cur.execute('''
            INSERT OR IGNORE INTO reactions
            VALUES(?, ?, ?)
        ''', [
            message.get('id'),
            reaction.get('user_id'),
            reaction['emoji'].get('name')
        ])

    # MENTIONS
    for mention in message['mentions']:
        cur.execute('''
            INSERT OR IGNORE INTO mentions
            VALUES(?, ?)
        ''',[
            message['id'],
            mention.get('id')
        ])

    # EMBEDS

    for embed in message['embeds']:
        cur.execute('''
            INSERT INTO embeds
            VALUES(?, ?)
        ''', [
            message['id'],
            embed.get('url')
        ])