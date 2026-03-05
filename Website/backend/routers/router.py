from fastapi import APIRouter
import sqlite3

router = APIRouter()

@router.get('/servers')
def get_servers():
    con = sqlite3.connect('./data/database.db')
    cur = con.cursor()
    
    servers = cur.execute('''
        SELECT 
            s.id,
            s.name,
            s.icon_url,
            (SELECT c.id 
            FROM channels c
            WHERE c.server_id = s.id
            LIMIT 1) as first_channel
        FROM servers s
    ''').fetchall()

    for idx, server in enumerate(servers):

        servers[idx] = {
            'id': server[0],
            'name': server[1],
            'image': server[2],
            'first_channel': server[3]
        }

    return {'servers': servers}


@router.get('/dms')
def get_dms():
    con = sqlite3.connect('./data/database.db')
    cur = con.cursor()

    dms = cur.execute('''
        SELECT
            c.id,
            u.global_display_name,
            u.avatar_url
        FROM channels c
        LEFT JOIN channel_members cm
            ON c.id = cm.channel_id
        LEFT JOIN users u
            ON cm.user_id = u.id
        WHERE c.server_id is NULL
    ''').fetchall()

    for idx, dm in enumerate(dms):
        dms[idx] = {
            'id': dm[0],
            'name': dm[1],
            'image': dm[2]
        }
    
    return {'dms': dms}


@router.get('/server/{id}')
def get_channels(id: str):
    con = sqlite3.connect('./data/database.db')
    cur = con.cursor()

    channels = cur.execute('''
        SELECT
            c.id as id,
            c.name as name,
            c.topic as topic,
            c.type as type
        FROM channels c
        WHERE c.server_id = ?
    ''',
        [
            id
        ]).fetchall()

    for idx, channel in enumerate(channels):

        channels[idx] = {
            'id': channel[0],
            'name': channel[1],
            'topic': channel[2],
            'type': channel[3]
        }

    return {'channels': channels}


@router.get('/server/{id}/members')
def get_members(id:str):
    con = sqlite3.connect('./data/database.db')
    cur = con.cursor()

    members = cur.execute('''
        SELECT
            u.global_display_name,
            sm.nickname,
            u.avatar_url,
            u.id
        FROM servers s
        LEFT JOIN server_members sm
            ON s.id = sm.server_id 
        LEFT JOIN users u
            ON sm.user_id = u.id
        WHERE s.id = ?
        GROUP BY u.id
    ''', [id]).fetchall()

    for idx, member in enumerate(members):
        members[idx] = {
            'display_name':  member[0] if member[1] is None else member[1],
            'image': member[2] 
        }
    
    return {'members': members}


@router.get('/channel/{id}')
def get_channel_messages(id: str):
    con = sqlite3.connect('./data/database.db')
    cur = con.cursor()


    messages = cur.execute('''
        SELECT
            m.id as id,
            m.author_id as author,
            u.name as name,
            u.global_display_name as nickname,
            u.avatar_url as avatar_url,
            u.is_bot as is_bot,
            m.content as content,
            m.type as type,
            m.is_pinned as is_pinned,
            m.created_at as created_at,
            m.edited_at as edited_at,
            m.parent_message_id as parent_message_id
        FROM messages m
        JOIN users u
            ON m.author_id = u.id
        WHERE m.channel_id = ?
        ORDER BY m.created_at ASC
        LIMIT 1000
        OFFSET 0
    ''', [id]).fetchall()

    result = []
    for row in messages:
        message_id = row[0]

        attachments = cur.execute('''
            SELECT url, file_name, size_bytes
            FROM attachments
            WHERE message_id = ?
        ''', [message_id]).fetchall()

        reactions = cur.execute('''
            SELECT user_id, emoji
            FROM reactions
            WHERE message_id = ?
        ''', [message_id]).fetchall()

        mentions = cur.execute('''
            SELECT mentioned_user_id
            FROM mentions
            WHERE message_id = ?
        ''', [message_id]).fetchall()

        embeds = cur.execute('''
            SELECT url
            FROM embeds
            WHERE message_id = ?
        ''', [message_id]).fetchall()

        result.append({
            'author':{
                'id': row[1],
                'name': row[2],
                'nickname': row[3],
                'avatar_url': row[4],
                'is_bot': row[5]
            },
            'content': row[6],
            'type': row[7],
            'is_pinned': row[8],
            'created_at': row[9],
            'edited_at': row[10],
            'parent_message_id': row[11],

            'attachments': [{
                'url': a[0],
                'file_name': a[1],
                'size_bytes': a[2]
            } for a in attachments],

            'reactions': [{
                'user_id': r[0],
                'emoji': r[1]
            } for r in reactions],

            'mentions': [{
                'mentioned_user_id': m[0]
            } for m in mentions],

            'embeds': [{
                'url': e[0]
            } for e in embeds]

        })
    
    return {'messages': result}