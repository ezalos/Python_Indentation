#!/usr/bin/env python

import argparse
from config import keys

import sys
import qarnot
import os

from os import walk

class Qarnot_Wrapper():
	def __init__(self, args=None):
		if False:
			self.conn = qarnot.Connection(client_token=keys['token'])

	def import_folder(self, path):
		f = []
		for (dirpath, dirnames, filenames) in walk(mypath):
			for filename in filenames:
				f.append(dirpath + filename)
		print(f)
		pass


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--directory", help="Directory to upload")
	args = parser.parse_args()
	if args.directory:
		qw = Qarnot_Wrapper()
		qw.import_folder(args.directory)
