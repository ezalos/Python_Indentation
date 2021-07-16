import re
import os
import argparse

def get_modified_lines_numbers(prv, aft, data):
	prv_lines = prv.split("\n")
	aft_lines = aft.split("\n")
	for i, (p, a) in enumerate(zip(prv_lines, aft_lines)):
		if p != a:
			data[i + 1] = True
	return data

def print_modifs(modifs):
	out = ""
	keys = modifs.keys()
	if len(keys) > 0:
		out += "Modified line"
		out += "" if len(keys) == 1 else "s"
		out += ": "
		for k in keys:
			out += str(k) + " "
	else:
		out += "No line was modified"
	print(out)


def replace(before, after, file_content):
	if after == "\t":
		reg_before = r"(^|\n)([" + after + r"]*)" + before  # + "|" + after + ")"
	else:
		reg_before = r"(^|\n)(" + after + r")*" + before  # + "|" + after + ")"
	"(^|\n)(\t)*    "
	"\1\2\t\t"
	reg_after = r"\1\2" + after
	lag = file_content
	text_after = ""
	list_modifs = {}
	while file_content != text_after:
		file_content = lag
		text_after = re.sub(reg_before, reg_after, file_content)
		list_modifs = get_modified_lines_numbers(file_content, text_after, list_modifs)
		lag = text_after
	return text_after, list_modifs

def file_indent(bef, aft, filename):
	if filename[-3:] == ".py":
		print("Indenting " + filename)
		with open(filename, "r") as f:
			origin = f.read()
		content, modifs = replace(bef, aft, origin)
		print_modifs(modifs)
		with open(filename, "w") as f:
			f.write(content)
	else:
		print("Indent only works with *.py files.")
		print(filename + " is not compatible")

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser = argparse.ArgumentParser(description='Here to solve inconsistencies in python files tabulation', epilog="In the hope it helps you save some precious seconds from time to time")
	parser.add_argument("-i", "--indentation", help="Can use 4 [s]paces or 1 [t]ab. Will indent with 1 tab as default.", choices=['t', 's'], default='t')
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument("-f", "--file", help="File to indent")
	group.add_argument("-d", "--directory", help="Directory to recursively indent")
	args = parser.parse_args()

	if args.indentation == 't':
		aft = '\t'
		bef = ' ' * 4
	else:
		bef = '\t'
		aft = ' ' * 4

	if args.file != None:
		file_indent(bef, aft, args.file)
	else:
		for root, dirs, files in os.walk(".", topdown=False):
			for name in files:
				if name[-3:] == ".py":
					file_indent(bef, aft, name)
