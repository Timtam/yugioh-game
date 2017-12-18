import argparse
import os.path

from ygo import globals
from ygo import i18n
from ygo.parsers.login_parser import LoginParser
from ygo.server import Server
from ygo.utils import parse_lflist, connect_db

def main():
	server = Server(port = 4000, default_parser = LoginParser)
	if os.path.exists('locale/de/cards.cdb'):
		globals.german_db = connect_db('locale/de/cards.cdb')
	if os.path.exists('locale/ja/cards.cdb'):
		globals.japanese_db = connect_db('locale/ja/cards.cdb')
	if os.path.exists('locale/es/cards.cdb'):
		globals.spanish_db = connect_db('locale/es/cards.cdb')
	for i in ('en', 'de', 'ja', 'es'):
		globals.strings[i] = i18n.parse_strings(os.path.join('locale', i, 'strings.conf'))
	globals.lflist = parse_lflist('lflist.conf')
	parser = argparse.ArgumentParser()
	parser.add_argument('-p', '--port', type=int, default=4000, help="Port to bind to")
	args = parser.parse_args()
	server.port = args.port
	globals.server = server
	server.run()

main()