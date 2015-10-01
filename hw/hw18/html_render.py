#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.

# indent: start with just x amount of spaces, then use string formatting
# justify right {:>x}

TAB_SIZE = 4


class Element(object):
    def __init__(self, content='', indent=0, **attrs):
        self.name = ''
        self.indent = indent
        self.children_indent = indent + TAB_SIZE
        self.content = ''
        self.children = []
        self.parent = None
        self.append(content)

    def __str__(self):
        return self.render()

    def render(self, f):
        html = u'{i}<{n}>{c}{ch}</>'.format(
            i=' ' * self.indent,
            n=self.name,
            c=self.content,
            ch=''.join([str(child) for child in self.children]))
        f.write(html)

    def format_content(self, content):
        return '\n{}{}\n'.format(' ' * self.children_indent, content)

    def append(self, child=None):
        if child:
            if isinstance(child, Element):
                self.children.append(child)
                child.indent = self.children_indent
                child.parent = self
            elif isinstance(child, str):
                self.content = ''.join(
                    [self.content, self.format_content(child)])
            else:
                raise TypeError('Object appended to Element must be a string'
                                'or another Element; got {} instead'
                                ).format(type(child))
