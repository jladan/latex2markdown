"""
A Very simple tool to convert latex documents to markdown documents
"""
import re
from sys import stderr

prepend = ''
item_sub = ''

span_substitutions = [
        (r'\\emph\{(.*?)\}', r'*\1*'),
        (r'\\textbf\{(.*?)\}', r'**\1**'),
        (r'\\verb;(.*?);', r'`\1`'),
        (r'\\includegraphics\{(.*?)\}', r'![](\1)'),
        # and to get rid of comments
        (r'%.*', r''),
        ]

def convert_span_elements(line):
    """ Converts all recognizable span elements into markdown
    """
    for (f, r) in span_substitutions:
        p = re.compile(f)
        line = p.sub(r, line)
    # and for the special case of list items...
    p = re.compile(r'\\item')
    line = p.sub(item_sub, line)
    return line

def start_blocks(line):
    """ Sets global state based on what block has been entered
    """
    global prepend
    global item_sub

    p = re.compile(r'\\begin\{(.*?)\}')
    m = p.match(line)
    if m:
        m = m.group(1)
        if m == "quote":
            prepend = '> '
        elif m == 'itemize':
            item_sub = '-'
        elif m == 'enumerate':
            item_sub = '1.'
        elif m == 'verbatim':
            prepend = '    '
        else:
            stderr.write('unsupported blocktype: %s\n' % m)
        return '\n'
    return line

def end_blocks(line):
    """ Sets global state based on what block has been left
    """
    global prepend
    global item_sub

    p = re.compile(r'\\end\{(.+)\}')
    m = p.match(line)
    if m:
        m = m.group(1)
        if m == "quote":
            prepend = ''
        elif m == 'itemize':
            item_sub = ''
        elif m == 'enumerate':
            item_sub = ''
        elif m == 'verbatim':
            prepend = ''
        elif m == 'document':
            exit()
        else:
            stderr.write('end of unsupported blocktype: %s\n' % m)
        return '\n'
    return line

def process_line(line):
    line = start_blocks(line)
    line = end_blocks(line)
    line = prepend + convert_span_elements(line)
    return line

# This next bit is to test the conversion as it builds
from sys import stdin
if __name__=="__main__":
    # First find the beginning of the document
    while not(stdin.readline().startswith(r'\begin{document}')):
        pass
    for line in stdin:
        print(process_line(line),end='')

