import argparse
import time
import os

nl = "\n" # newline


def open_sector():
	a = "/"
	for i in range(78):
		a += "*"
	a += nl
	return a

def close_sector():
	a = ""
	for i in range(78):
		a += "*"
	a += "/"
	a += nl
	return a

def three_spaces():
	a = ""
	for i in range(3):
		a += " "
	return a


def insert_sector_name(sector_name):
	a = ""
	a += three_spaces()
	a += sector_name
	a += nl
	return a

def create_sector(sector_name):
	a = ""
	a += nl
	a += open_sector()
	a += insert_sector_name(sector_name)
	a += close_sector()
	return a

def create_header(name, version): # Kopf
	a = ""
	a += nl
	a += open_sector()
	a += nl
	a += "   File                   :     " + name + ".h" + nl
	a += "   Change                 :     " + nl
	a += "   Version                :     " + version + nl
	a += nl
	a += close_sector()
	return a

def create_compiler_switch_start(name):
	a = ""
	a += nl
	a += "#ifndef __"
	a += name.upper()
	a += "_H"
	a += nl
	a += "   #define __"
	a += name.upper()
	a += "_H"
	a += nl
	return a

def create_compiler_switch_end(name):
	a = ""
	a += nl
	a += "#endif /* __"
	a += name.upper()
	a += "_H */"
	a += nl
	return a

def create_ini_prototyp(name):
	a = ""
	a += nl
	a += "void "
	a += name.upper()
	a += "_Ini (void);"
	a += nl
	return a

def create_changes_section():
	a = ""
	a += nl
	a += open_sector()
	a += nl
	a += three_spaces()
	a += "Changes"
	a += nl
	a += nl
	a += nl
	a += nl
	a += close_sector()
	return a

# Argparse
parser = argparse.ArgumentParser()
parser.add_argument("--output_folder", help="")
parser.add_argument("--modul_name", help="")
args = parser.parse_args()



a = ""
a += create_header(args.modul_name, "1")
a += create_compiler_switch_start(args.modul_name)
a += create_sector("Include Files")
a += create_sector("Global Constants")
a += create_sector("Global Type Definitions")
a += create_sector("Global Variables")
a += create_sector("Global Function Prototypes")
a += create_ini_prototyp(args.modul_name)
a += create_changes_section()
a += create_compiler_switch_end(args.modul_name)


f = open(os.path.join(args.output_folder,args.modul_name + ".h"), "w")
f.write(a)
f.close()

print(a)