#!/usr/bin/env python
import telegram as tg
import telegram.ext as tg_ext

def load():
	import base
	base.main(dp)
	import text_parse
	text_parse.main(dp)
	import utils
	utils.main(dp)
	import vortaro
	vortaro.main(dp)
	import xkcd
	xkcd.main(dp)

updater = tg_ext.Updater((open('private/token.txt').read()))
dp = updater.dispatcher
load()
updater.start_polling()
updater.idle()
