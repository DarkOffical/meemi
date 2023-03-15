from pyrogram.types import Chat, ChatMember
from pyrogram.types import ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters, enums, mime_types

from pyrogram.errors import ChatAdminRequired, BadRequest


async def can_delete(client, grp_id, userid) -> bool:
    user_det = await client.get_chat_member(grp_id, userid)
    return user_det.can_delete_messages


async def is_bot_admin(chat, bot_id: int, bot_member: ChatMember = None) -> bool:
    if chat.type == enums.ChatType.PRIVATE:      # or chat.all_members_are_administrators:
        return True

    if not bot_member:
        bot_member = await chat.get_member(bot_id)
    return bot_member.status in [enums.ChatMemberStatus.ADMINISTRATOR, 'creator']


async def is_user_admin(chat: Chat, user_id: int) -> bool:
    try:
        chat_member = await chat.get_member(user_id)
        if chat_member.status in [enums.ChatMemberStatus.ADMINISTRATOR, 'creator']:
            return True
        else:
            return False
    except Exception as e:
        pass


async def is_user_not_admin(chat, user_id: int) -> bool:
    chat_member = await chat.get_member(user_id)
    if chat_member.status not in [enums.ChatMemberStatus.ADMINISTRATOR, 'creator']:
        return True
    else:
        return False
