# Copyright (C) YusrilRNLD
# Ram-Ubot < https://github.com/YusrilRNLD/U-Bot >
# ReEdit by @YUSRIL4YOU
# All rights reserved.
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.

from userbot import CMD_HELP, BLACKLIST_CHAT, CMD_HANDLER as cmdfrom userbot.events import registerfrom userbot.utils import ram_cmd# ================= CONSTANT =================# FROM RAM-UBOT# ============================================

@register(outgoing=True, pattern='^G(?: |$)(.*)')async def _(typew): await typew.client.send_message( typew.chat_id, "**GAK ADA KEREN KERENNYA LU BEGITU NGENTOD, BAPAK LU SUJUD SUJUD DI DEPAN GUA NGENTOD GARA GARA KEBINGUNGAN GA BISA NGASIH MAKAN LU, MAKANYA DIA MINTA DI SANTUNIN PLUS DI KASIH BANSOS SAMA GUA BANGSAT!!!**", reply_to=typew.reply_to_msg_id) await typew.delete() CMD_HELP.update({ "salam": f"P or `{cmd}p`\\nUsage: Untuk Memberi salam.\\n\nL or `{cmd}l`\\nUsage: Untuk Menjawab Salam."})