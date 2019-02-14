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

def write():
	a = ""
	a += "*" 
	for i in range(2):
		a += " "
	return a


def insert_sector_name(sector_name):
	a = ""
	a += write()
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

def create_header(name, typ, version): # Kopf
	a = ""
	a += nl
	a += open_sector()
	a += write() + "File           :  " + name + typ + nl
	a += write() + "Version        :  " + version + nl
	a += close_sector()
	return a

def create_compiler_switch_start(name):
	a = ""
	a += nl
	a += "#ifndef __"
	a += name.upper()
	a += "_H"
	a += nl
	a += "#define __"
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

def create_ini_function(name):
	a = ""
	a += nl
	a += "void "
	a += name.upper()
	a += "_Ini (void)" + nl
	a += "{" + nl
	a += nl
	a += "}" + nl
	return a

def create_changes_section():
	a = ""
	a += nl
	a += open_sector()
	a += write() + nl
	a += write()
	a += "Changes        :  " + nl
	a += write() + nl
	a += write() + nl
	a += write() + nl
	a += close_sector()
	return a


def create_function_description():
	a = ""
	a += nl
	a += open_sector()
	a += write() + "Function Name  :  " + nl
	a += write() + "Description    :  " + nl
	a += write() + "Parameter(s)   :  " + nl
	a += write() + "Return Value   :  " + nl
	a += close_sector()
	return a

def end_of_file(name):
	a = ""
	a += nl
	a += open_sector()
	a += write() + "END OF FILE    :  " + name + ".h" + nl
	a += close_sector()
	return a	


# Argparse
parser = argparse.ArgumentParser()
parser.add_argument("--output_folder", help="")
parser.add_argument("--modul_name", help="")
args = parser.parse_args()


# Create .h File
a = ""
a += create_header(args.modul_name, ".h","1")
a += create_compiler_switch_start(args.modul_name)
a += create_sector("Include Files")
a += create_sector("Global Constants")
a += create_sector("Global Type Definitions")
a += create_sector("Global Variables")
a += create_sector("Global Function Prototypes")
a += create_ini_prototyp(args.modul_name)
a += create_changes_section()
a += create_compiler_switch_end(args.modul_name)
a += end_of_file(args.modul_name)

f = open(os.path.join(args.output_folder,args.modul_name + ".h"), "w")
f.write(a)
f.close()

#print(a)





# Create .c File
a = ""
a += create_header(args.modul_name, ".c","1")
a += create_sector("Include Files")
a += create_sector("Local Constants")
a += create_sector("Local Type Definitions")
a += create_sector("Local Variables")
a += create_sector("Local Function Prototypes")
a += create_sector("Local Functions")
a += create_sector("Global Functions")
a += create_function_description()
a += create_ini_function(args.modul_name)
a += create_changes_section()
a += end_of_file(args.modul_name)

f = open(os.path.join(args.output_folder,args.modul_name + ".c"), "w")
f.write(a)
f.close()

#print(a)