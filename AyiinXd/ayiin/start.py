from telethon import Button
from AyiinXd import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    STRING_SESSION,
    blacklistayiin,
    bot,
    tgbot,
)

async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://graph.org/file/84b5927d52cd79e8affee-b287e20624a524c87b.jpg",
                caption="𝗡𝗮𝘆𝗹𝗮-𝗨𝘀𝗲𝗿𝗯𝗼𝘁.\n     **status : Active\n     ketik `.ping` untuk cek bot!**",
                buttons=[(Button.url("Store", "https://t.me/jasebnayla")),
                         (Button.url("Support", "https://t.me/mwonsy"))]
            )
    except Exception as e:
        LOGS.error(e)
        return None
