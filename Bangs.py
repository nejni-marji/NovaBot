#!/usr/bin/env python
import re
import telegram as tg
import telegram.ext as tg_ext

def bang(bot, update):
	text = update.message.text
	bang = re.match('![a-zA-Z0-9]*', text).group()[1:]
	resp = 'You used the bang: `{}`'.format(bang)
	bot.sendMessage(update.message.chat_id, resp)

def main(dp):
	dp.add_handler(tg_ext.MessageHandler([tg_ext.Filters.text], bang))
