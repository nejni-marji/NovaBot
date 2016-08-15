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

def lookup(args):
	if not args:
		return 'Vi devas specifi vorton aŭ vortojn.'
	results = []
	for line in espdic:
		check = line.lower(), *list(i.lower() for i in espdic[line])
		if args in check or 'to ' + args in check:
			results.append('*{}*: _{}_'.format(line, ', '.join(espdic[line])))
	return '\n'.join(sorted(results))
	if not results:
		return 'Mi trovis nenion.'
	return '\n'.join(results)

def main(dp):
	dp.add_handler(tg_ext.CommandHandler('v', vortaro, pass_args = True))
