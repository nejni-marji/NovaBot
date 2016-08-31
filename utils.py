#!/usr/bin/env python
import telegram as tg
import telegram.ext as tg_ext

def get_id(bot, update, args):
	commands = {
		'user': get_user,
		'chat': get_chat,
		'message': get_message
	}
	if args[0] in commands:
		commands[args[0]](bot, update)

def get_user(bot, update):
	user = update.message.reply_to_message.from_user
	resp = '{} {}:\n{}'.format(user.first_name, user.last_name, user.id)
	bot.send_message(update.message.chat_id, resp)

def get_chat(bot, update):
	chat = update.message.chat
	resp = '{}:\n{}'.format(chat.title, chat.id)
	bot.send_message(update.message.chat_id, resp)

def get_message(bot, update):
	message = update.message.reply_to_message.message_id
	resp = message
	bot.send_message(update.message.chat_id, resp)

def main(dp):
	dp.add_handler(tg_ext.CommandHandler('id', get_id, pass_args = True))
