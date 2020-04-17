#!/usr/bin/env python
# Encoding: utf8

# Author: Hannes Ovrén (hannes@ovren.se)
# Licensed under the GPL version 2

import argparse
import getpass
import os
import sys

from PyPDF2 import PdfFileWriter, PdfFileReader

def protect(ifname, ofname, password):
    with open(ifname, "rb") as ifile, open(ofname, "wb") as ofile:
        reader = PdfFileReader(ifile)
        writer = PdfFileWriter()
        for i in range(reader.getNumPages()):
            writer.addPage(reader.getPage(i))
        writer.encrypt(password)
        writer.write(ofile)
        
def get_password():
    while True:
        try:
            password = getpass.getpass("Set password for PDF file: ")
            repeated = getpass.getpass("Repeat password: ")
        except KeyboardInterrupt:
            print # End the password query line
            return None
        if password == repeated:
            return password
        else:
            print("Passwords did not match")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", metavar="ORIGINAL", help="The PDF file to protect")
    parser.add_argument("output", metavar="OUTPUT", help="Filename of password protected copy")
    parser.add_argument("--password")
    parser.add_argument("--force", action="store_true", help="Force overwriting existing file")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print("Input file {} does not exist.".format(args.input))
        sys.exit(-1)
    if os.path.exists(args.output) and not args.force:
        print("Output file {} already exists.".format(args.input))
        sys.exit(-2) 
    
    password = None
    
    if args.password:
        password = args.password
    else:
        password = get_password()
    
    if password is not None:
        protect(args.input, args.output, password)
        print("Created {}".format(args.output))
        
