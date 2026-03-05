import sqlite3

con = sqlite3.connect('./data/database.db')
cur = con.cursor()


cur.execute('DROP TABLE IF EXISTS users')
cur.execute('''
    CREATE TABLE users(
        id  TEXT NOT NULL PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        global_display_name TEXT NOT NULL,
        avatar_url TEXT,
        is_bot INTEGER NOT NULL DEFAULT 0,
        UNIQUE (id)
    );
''')


cur.execute('DROP TABLE IF EXISTS servers')
cur.execute("""
    CREATE TABLE servers(
        id TEXT NOT NULL PRIMARY KEY,
        name TEXT NOT NULL,
        icon_url TEXT,
        owner_id TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT (datetime("now")),
        FOREIGN KEY(owner_id) REFERENCES users(id)
    );
""")


cur.execute('DROP TABLE IF EXISTS categories')
cur.execute(''''
    CREATE TABLE categories(
        id TEXT PRIMARY KEY,
        server_id TEXT NOT NULL,
        name TEXT NOT NULL,
        position INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY(server_id) REFERENCES servers(id) ON DELETE CASCADE
    )
''')


cur.execute('DROP TABLE IF EXISTS channels')
cur.execute('''
    CREATE TABLE channels(
        id TEXT NOT NULL,
        server_id TEXT,
        category_id TEXT,
        name TEXT NOT NULL,
        type TEXT NOT NULL,
        topic TEXT,
        position INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY(server_id) REFERENCES servers(id) ON DELETE CASCADE,
        FOREIGN KEY(category_id) REFERENCES categories(id) ON DELETE SET NULL

    )
''')


cur.execute('DROP TABLE IF EXISTS messages')
cur.execute('''
    CREATE TABLE messages (
        id TEXT NOT NULL PRIMARY KEY,
        author_id TEXT NOT NULL,
        channel_id TEXT NOT NULL,
        content TEXT,
        type TEXT NOT NULL,
        is_pinned INTEGER NOT NULL DEFAULT 0,
        created_at TIMESTAMP DEFAULT (datetime('now')),
        edited_at TIMESTAMP,
        parent_message_id TEXT,
        FOREIGN KEY(author_id) REFERENCES users(id),
        FOREIGN_KEY(channel_id) REFERENCES channels(id) ON DELETE CASCADE,
        FOREIGN KEY(parent_message_id) REFERENCES messages(id) ON DELETE SET NULL,
        UNIQUE(id)
    )
''')


cur.execute('DROP TABLE IF EXISTS attachments')
cur.execute('''
    CREATE TABLE attachments(
        id INTEGER PRIMARY KEY,
        message_id TEXT NOT NULL,
        url TEXT NOT NULL,
        file_name TEXT,
        size_bytes INTEGER,
        FOREIGN KEY(message_id) REFERENCES  messages(id) ON DELETE CASCADE,
        UNIQUE(id)
    )
''')


cur.execute('DROP TABLE IF EXISTS reactions')
cur.execute('''
    CREATE TABLE reactions (
        message_id  TEXT NOT NULL,
        user_id TEXT NOT NULL,
        emoji TEXT NOT NULL,
        PRIMARY KEY(message_id, user_id, emoji),
        FOREIGN KEY(message_id) REFERENCES messages(id),
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
''')


cur.execute('DROP TABLE IF EXISTS mentions')
cur.execute('''
    CREATE TABLE mentions(
        message_id TEXT NOT NULL,
        mentioned_user_id TEXT NOT NULL,
        PRIMARY KEY(message_id, mentioned_user_id),
        FOREIGN KEY(message_id) REFERENCES messages(id) ON DELETE CASCADE,
        FOREIGN KEY(mentioned_user_id) REFERENCES users(id)
    )
''')


cur.execute('DROP TABLE IF EXISTS embeds')
cur.execute('''
    CREATE TABLE embeds(
        message_id TEXT NOT NULL,
        url TEXT NOT NULL,
        FOREIGN KEY(message_id) REFERENCES messages(id) ON DELETE CASCADE
    )
''')


cur.execute('DROP TABLE IF EXISTS server_members')
cur.execute("""
    CREATE TABLE server_members(
        server_id TEXT NOT NULL,
        user_id TEXT NOT NULL,
        nickname TEXT,
        joined_at TIMESTAMP DEFAULT (datetime('now')),
        PRIMARY KEY(server_id, user_id),
        FOREIGN KEY(server_id) REFERENCES servers(id) ON DELETE CASCADE,
        FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE,
    )
""")


cur.execute('DROP TABLE IF EXISTS channel_members')
cur.execute("""
    CREATE TABLE channel_members(
        channel_id TEXT NOT NULL,
        user_id TEXT NOT NULL,
        PRIMARY KEY(channel_id, user_id),
        FOREIGN KEY(channel_id) REFERENCES channels(id) ON DELETE CASCADE,
        FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
    )
""")

con.commit()