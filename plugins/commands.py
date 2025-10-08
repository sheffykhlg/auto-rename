@Client.on_message(filters.private & filters.command("banned_users") & filters.user(Config.ADMIN))
async def banned_users(_, m: Message):
    all_banned_users = await codeflixbots.get_all_banned_users()
    banned_usr_count = 0
    text = ''

    async for banned_user in all_banned_users:
        user_id = banned_user['_id']
        ban_duration = banned_user['ban_status']['ban_duration']
        banned_on = banned_user['ban_status']['banned_on']
        ban_reason = banned_user['ban_status']['ban_reason']
        banned_usr_count += 1
        text += f"> **user_id**: `{user_id}`, **Ban Duration**: `{ban_duration}`, " \
                f"**Banned on**: `{banned_on}`, **Reason**: `{ban_reason}`\n\n"

    reply_text = f"Total banned user(s): `{banned_usr_count}`\n\n{text}"
    if len(reply_text) > 4096:
        with open('banned-users.txt', 'w') as f:
            f.write(reply_text)
        await m.reply_document('banned-users.txt', caption="Banned users list")
        os.remove('banned-users.txt')
    else:
        await m.reply_text(reply_text, quote=True)
