export interface User{
    id: string,
    name: string,
    nickname: string,
    avatar_url: string,
    is_bot: boolean
}

export interface Embed{
    url: string
}

export interface Attachment{
    file_name: string,
    size_bytes: number,
    url: string
}

export interface Reaction{
    emoji: string,
    users: string[]
}

export interface Message{
    id: string,
    type: string,
    author: User,
    content: string,
    created_at: Date,
    edited_at: Date,
    is_pinned: boolean,
    parent_message_id: string | null,
    mentions: User[],
    attachments: Attachment[],
    embeds: Embed[],
    reactions: Reaction[]
}