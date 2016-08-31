#!/usr/bin/env python
import telegram as tg
import telegram.ext as tg_ext
from json import loads, dumps
from urllib.request import urlopen
from os.path import isfile
from random import randrange

# Please note that /private/xkcd/xkcd.json's first item is arbitrary and
# should absolutely never be called for any reason. I typically overwrite it
# with the most recent comic.

def get_json(num):
	url = 'http://www.xkcd.com/{}/info.0.json'
	json_file = urlopen(url.format(num))
	json_data = loads(json_file.read().decode('utf-8'))
	json_file.close()
	return json_data

def boot():
	error = {
		"safe_title": "404 Error", "alt": "Not Found", "day": "1",
		"transcript": "404 -    Not Found", "year": "2008",
		"img": "http://imgs.xkcd.com/static/terrible_small_logo.png",
		"link": "", "month": "4", "num": 404, "title": "404 Error",
		"news": ""
	}
	if isfile('private/xkcd/xkcd.json'):
		json_file = open('private/xkcd/xkcd.json', 'r')
		comics = loads(json_file.read())
		json_file.close()
	else:
		comics = [error]
	num_json = len(comics) - 1
	num_latest = get_json('')['num']
	if num_json < num_latest:
		for num in range(num_json + 1, num_latest + 1):
			print('Downloading comic {}...'.format(num))
			if num == 404:
				comics.append(error)
				continue
			comics.append(get_json(num))
			json_file = open('private/xkcd/xkcd.json', 'w')
			json_file.write(dumps(comics))
			json_file.close()
	return comics

def xkcd(bot, update, args):
	if args:
		arg = args[0]
	else:
		arg = randrange(1, len(comics))
	special = {
		'latest' : len(comics) - 1,
		'random' : 4 # chosen my fair dice roll, guaranteed to be random
	}
	if arg in special:
		num = special[arg]
	else:
		num = int(arg)
	comic = comics[num]
	#bot.send_photo(update.message.chat_id, latest['img'], latest['alt'])
	caption = '#{}: {}: {}'.format(comic['num'], comic['title'], comic['alt'])
	bot.send_photo(update.message.chat_id, comic['img'], caption)

def update_xkcd(bot, update):
	global comics
	comics = boot()

def main(dp):
	global comics
	comics = boot()
	dp.add_handler(tg_ext.CommandHandler('xkcd', xkcd, pass_args = True))
	dp.add_handler(tg_ext.CommandHandler('update_xkcd', update_xkcd))
