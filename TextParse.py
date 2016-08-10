#!/usr/bin/env python
import re
import telegram as tg
import telegram.ext as tg_ext

def text_parse(bot, update):
	bang(bot, update)

def bang(bot, update):
	bang = re.match('![a-zA-Z0-9]*', update.message.text)
	if bang:
		resp = 'You used the bang: *{}*'.format(bang.group())
		print(resp)
		#bot.sendMessage(update.message.chat_id, resp,
		                #parse_mode = tg.ParseMode.MARKDOWN)

def main(dp):
	dp.add_handler(tg_ext.MessageHandler([tg_ext.Filters.text], text_parse))
