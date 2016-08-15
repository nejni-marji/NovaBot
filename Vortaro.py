#!/usr/bin/env python
import re
import telegram as tg
import telegram.ext as tg_ext

espdic = open('private/espdic.txt').read().split('\n')
espdic.pop(0)
espdic.remove('')

def vortaro(bot, update, args):
	bot.sendMessage(update.message.from_user.id, lookup(args),
	                parse_mode = tg.ParseMode.MARKDOWN)
	resp = 'Se vi ne ricevis mian privatan mesaĝon, bonvolu private mesaĝi min je /start.'
	bot.sendMessage(update.message.chat_id, resp,
	                reply_to_message_id = update.message.message_id,
	                parse_mode = tg.ParseMode.MARKDOWN)

def lookup(args):
	if not args:
		return 'Vi devas specifi vorton aŭ vortojn.'
	regex = re.compile(r'\b{}\b'.format(' '.join(args)), re.I)
	results = []
	for line in espdic:
		search = regex.search(line)
		if search:
			search = re.sub(r'(.*) : (.*)', r'*\1*: _\2_', search.string)
			results.append(search)
	if not results:
		return 'Mi trovis nenion.'
	return '\n'.join(results)

def main(dp):
	dp.add_handler(tg_ext.CommandHandler('v', vortaro, pass_args = True))
