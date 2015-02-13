# pdflock - Password protect PDF files

Given an input PDF file, output a password protected version.

## Running

Running is as simple as

    $ pdflock.py input.pdf output.pdf
  
To set the password non-interactively, run 

    $ pdflock.py input.pdf output.pdf --password="my secret"

## Installation
This program requires the pyPdf module to be installed.

For Fedora you can install this with `yum install pyPdf`

## Licensing
This program was written by Hannes Ovrén (hannes@ovren.se).
It is released under the GNU GPL version 2 license
