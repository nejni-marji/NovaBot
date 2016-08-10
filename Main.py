#!/usr/bin/env python
import telegram as tg
import telegram.ext as tg_ext

def load():
	import Base as Base
	Base.main(dp)
	import TextParse as TextParse
	TextParse.main(dp)
	import Utils as Utils
	Utils.main(dp)

updater = tg_ext.Updater((open('private/token.txt').read()))
dp = updater.dispatcher
load()
updater.start_polling()
updater.idle()
