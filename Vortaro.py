#!/usr/bin/env python
import re
import telegram as tg
import telegram.ext as tg_ext

espdic_lines = open('private/espdic.txt').read().split('\n')
espdic_lines.pop(0)
espdic_lines.remove('')
espdic = {}

def vortaro(bot, update, args):
	user = update.message.from_user.username
	user_id = update.message.from_user.id
	print('{} ({}) searches:\n{}'.format(user, user_id, ' '.join(args)))
	bot.sendMessage(update.message.from_user.id, lookup(' '.join(args)),
	                parse_mode = tg.ParseMode.MARKDOWN)
	if update.message.chat_id < 0:
		resp = 'Se vi ne ricevis mian privatan mesaĝon, bonvolu private mesaĝi min je /start.'
		bot.sendMessage(update.message.chat_id, resp,
		                reply_to_message_id = update.message.message_id,
		                parse_mode = tg.ParseMode.MARKDOWN)

def lookup(query):
	if not query:
		return 'Vi devas specifi vorton aŭ vortojn.'
	espdic = {}
	regex = re.compile(query, re.I)
	for line in espdic_lines:
		check = regex.search(line)
		if check:
			word = check.string.split(' : ')[0]
			definition = check.string.split(' : ')[1].split(', ')
			espdic[word] = definition
	exact_results = []
	fuzzy_results = []
	for word in espdic:
		check = word.lower(), *list(i.lower() for i in espdic[word])
		if query in check or 'to ' + query in check:
			exact_results.append('*{}*: _{}_'.format(word, ', '.join(espdic[word])))
		else:
			fuzzy_results.append('*{}*: _{}_'.format(word, ', '.join(espdic[word])))
	if not (exact_results or fuzzy_results):
		return 'Nenio trovita.'
	exact = '\n'.join(sorted(exact_results))
	fuzzy = '\n'.join(sorted(fuzzy_results))
	results = exact + '\n\n' + fuzzy
	return results

def main(dp):
	dp.add_handler(tg_ext.CommandHandler('v', vortaro, pass_args = True))
