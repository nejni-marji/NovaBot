#!/usr/bin/env python
import re
import telegram as tg
import telegram.ext as tg_ext

espdic_lines = open('private/espdic.txt').read().split('\n')
espdic_lines.pop(0)
espdic_lines.remove('')
espdic = {}
for line in espdic_lines:
	word = line.split(' : ')[0]
	definition = line.split(' : ')[1].split(', ')
	espdic[word] = definition

def vortaro(bot, update, args):
	bot.sendMessage(update.message.from_user.id, lookup(' '.join(args)),
	                parse_mode = tg.ParseMode.MARKDOWN)
	resp = 'Se vi ne ricevis mian privatan mesaĝon, bonvolu private mesaĝi min je /start.'
	bot.sendMessage(update.message.chat_id, resp,
	                reply_to_message_id = update.message.message_id,
	                parse_mode = tg.ParseMode.MARKDOWN)

def lookup(query):
	if not query:
		return 'Vi devas specifi vorton aŭ vortojn.'
	results = []
	for word in espdic:
		check = word.lower(), *list(i.lower() for i in espdic[word])
		if query in check or 'to ' + query in check:
			results.append('*{}*: _{}_'.format(word, ', '.join(espdic[word])))
	if not results:
		return 'Mi trovis nenion.'
	return '\n'.join(sorted(results))

def main(dp):
	dp.add_handler(tg_ext.CommandHandler('v', vortaro, pass_args = True))
