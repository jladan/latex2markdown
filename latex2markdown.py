"""
A Very simple tool to convert latex documents to markdown documents
"""
import re


span_substitutions = [
        (r'\\emph\{(.+)\}', r'*\1*'),
        (r'\\textbf\{(.+)\}', r'**\1**'),
        (r'\\verb;(.+);', r'`\1`'),
        (r'\\includegraphics\{(.+)\}', r'![](\1)'),
        ]

def convert_span_elements(line):
    """ Converts all recognizable span elements into markdown
    """
    for (f, r) in span_substitutions:
        p = re.compile(f)
        line = p.sub(r, line)
    return line

# This next bit is to test the conversion as it builds
from sys import stdin
if __name__=="__main__":
    for line in stdin:
        print(convert_span_elements(line),end='')

