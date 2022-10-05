#!/usr/bin/env python
"""
Spyder Editor

This is a temporary script file.
"""
from PyPDF2 import PdfReader, PdfWriter
import click

def encrypt(filename,password):
    reader = PdfReader(filename)
    writer = PdfWriter()
    for page in reader.pages:
        page.compress_content_streams()
        writer.addPage(page)
    writer.encrypt(password)
    with open(filename.removesuffix(".pdf") + ".encrypted.pdf", "wb") as f:
        writer.write(f)

@click.command()
@click.argument('filename')
@click.option('--password', '-p', default='pass$1234', help='Password to encrypt the file')
def main(filename, password):
    print(f"{filename = } ✨")
    encrypt(filename, password)

if __name__ == "__main__":
    main()