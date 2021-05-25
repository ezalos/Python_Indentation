from os import walk
import time
import subprocess
import re
import platform

class BinCute():
	def __init__(self, binary, leaks=False):
		self.binary = binary
		self.command = ""
		self.raw_output = None
		self.output = ""
		self.time = None
		self.leaks = leaks

	def prepare_command(self, args):
		self.command = self.binary
		if type(args) == type(""):
			self.command += " " + args
		elif type(args) == type([]):
			for arg in args:
				self.command += " " + str(arg)
		else:
			print("Wrong args tyoe: ", type(args))

	def launch(self):
	  t = time.process_time()
	  # print(self.command)
	  self.raw_output = subprocess.run(self.command, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, shell=True)
	  self.time = time.process_time() - t
	  self.stdout = self.raw_output.stdout.decode('utf-8')
	  self.stderr = self.raw_output.stderr.decode('utf-8')

	def clean_output(self, colors=False, white_spaces=False):
		output = self.stdout
		if colors:
			output = re.sub(r'[\t ]+', r' ', output)
		if white_spaces:
			output = re.sub(r'\x1b\[[0-9;]+m', r'', output)
		self.output = output
		return self.output



def get_file_list(mypath):
	f = []
	for (dirpath, _, filenames) in walk(mypath):
		for filename in filenames:
			f.append(dirpath + "/" + filename)
	return f


if __name__ == "__main__":
	mypath = "tests_copy"
	files = get_file_list(mypath)
	Bc = BinCute("python3 Indent.py")
	for f in files:
		print("-" * 30)
		Bc.prepare_command("-f '" + f + "'")
		Bc.launch()
		print(Bc.stdout)
		print(Bc.stderr)

