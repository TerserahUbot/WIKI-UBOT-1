# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

from importlib import import_module
from sys import argv

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import BOT_VER, LOGS, bot
from userbot.modules import ALL_MODULES

INVALID_PH = '\nERROR: Nomor Telepon yang dimasukkan INVALID' \
             '\n Tip: Gunakan Kode Negara beserta nomornya.' \
             '\n atau periksa nomor telepon Anda dan coba lagi !'

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)


LOGS.info(
    f"⚡ᴡɪᴋɪ-ᴜʙᴏᴛ⚡ ⚙️ V{BOT_VER} [BERHASIL DI AKTIFIN YE!]")


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()