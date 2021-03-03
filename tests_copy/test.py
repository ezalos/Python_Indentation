import re
import argparse

def replace(before, after, file):
	# print(file)
	reg_before = r"^(" + after + r")*" + before
	# print(reg_before)
	reg_after = r"\1" + after + ""
	lag = file
	text_after = ""
	while file != text_after:
		file = lag
		text_after = re.sub(reg_before, reg_after, file)
		lag = text_after
	return text_after

def file_indent(bef, aft, filename):
	if filename[-3:] == ".py":
		with open(filename) as f:
			content = f.read()
		content = replace(bef, aft, content)
		f.write(content)
	else:
		print("This program only works with *.py files.")

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser = argparse.ArgumentParser(description='Here to solve inconsistencies in python files tabulation', epilog="In the hope it helps you save some precious seconds from time to time")
	parser.add_argument("-i", "--indentation", help="Can use 4 [s]paces or 1 [t]ab. Will indent with 1 tab as default.", choices=['t', 's'], default='t', type=ascii)
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument("-f", "--file", help="File to indent", type=ascii)
	group.add_argument("-d", "--directory", help="Directory to recursively indent", type=ascii)
	args = parser.parse_args()

	if ags.indentation == 't':
		aft = '\t'
		bef = '    '
	else:
		bef = '\t'
		aft = '    '

	if args.file:
		with open(args.file) as f:
		replace(bef, aft, f)

	replace("aaa", "bbb", "aaaaaaaahelloaaa")
