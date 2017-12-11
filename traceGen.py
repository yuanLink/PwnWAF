#!usr/bin/env python
#   -*- coding:utf-8    -*-

__author__ = "link"

import os
import argparse

DEBUG = 0

def generate_new_file(elf_name, machine, log_path):
    """ generate new c file with argument

    @param elf_name:elf path that we want to be logged
    @param machine: elf machine bit
    @param log_path: the path that we save log file
    """
    fd = open("trace.c", 'r')
    content = ''
    for eachline in fd:
        content += eachline

    fd.close()
    # replace the old infomation
    content = content.replace("TEMPFILENAME", elf_name)
    content = content.replace("TEMPBIT", machine)
    content = content.replace("TEMPLOGNAME", log_path)

    # write to tmp file
    fd = open("tmp_trace.c", 'w')
    fd.write(content)
    fd.close()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate file to log attach flow")
    # group = parser.add_mutually_exclusive_group()
    # group.add_argument("32", action="store_true")
    # group.add_argument("64", action="store_true")
    parser.add_argument("machine",help="bytes of elf(32/64)", choices=['32','64'])
    parser.add_argument("elf_name", help="absolute path of elf")
    parser.add_argument("log_path", help="abdolute path of log.txt")
    
    args = parser.parse_args()
    
    elf_name = args.elf_name
    machine = args.machine
    log_path = args.log_path
    
    if elf_name == None or machine == None or log_path == None:
        print parser.echo
    else:
        print("file name {}, in {} bits machine, log file will save at{}".format(elf_name, machine, log_path))
        generate_new_file(elf_name, machine, log_path)
        # then, we use os to make file
        tmp_path = os.path.realpath("tmp_trace.c")
        print tmp_path
        if machine == '32':
            os.system("gcc -m32 -o {}.out {}".format(tmp_path[:-2], tmp_path))
        elif machine == '64':
            os.system("gcc -o {}.out {}".format(tmp_path[:-2], tmp_path))
        if DEBUG:
            pass
        else:
            os.system("rm {}".format(tmp_path))

