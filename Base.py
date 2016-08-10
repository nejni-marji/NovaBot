#!/usr/bin/env python
import telegram as tg
import telegram.ext as tg_ext

def start(bot, update):
	bot.sendMessage(update.message.chat_id, 'Komencita!')

def main(dp):
	dp.add_handler(tg_ext.CommandHandler('start', start))
