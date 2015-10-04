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
    def __init__(self, content=None, **attrs):
        self.tag = ''
        self.extra_tag = ''
        # self.indent = indent
        self.content = []
        self.children = []
        self.parent = None
        self.append(content)

    def __str__(self):
        return self.render()

    def render(self, f):
        f.write(self.render_html())

    def render_html(self, indent=0):
        child_indent = indent + TAB_SIZE
        return u'{x}\n{i}<{t}>{c}{ch}\n{i}</{t}>'.format(
            x=self.extra_tag,
            i=u' ' * indent,  # possible to use int in string format better?
            t=self.tag,
            c=self.format_content(child_indent),
            ch=u''.join([child.render_html(
                child_indent) for child in self.children]))

    def format_content(self, indent):
        return u''.join(['\n{}{}'.format(
            u' ' * indent, c) for c in self.content if c])

    def append(self, child=None):
        if child:
            if isinstance(child, Element):
                self.children.append(child)
                child.parent = self
            elif isinstance(child, str) or isinstance(child, unicode):
                self.content.append(child)
            else:
                raise TypeError, ('Object appended to Element must be a string'
                                  'or another Element; got {} instead'
                                  ).format(type(child))


class Html(Element):
    def __init__(self, *args, **kwargs):
        super(Html, self).__init__(*args, **kwargs)
        self.tag = 'html'
        self.extra_tag = '<!DOCTYPE html>'


class Body(Element):
    def __init__(self, *args, **kwargs):
        super(Body, self).__init__(*args, **kwargs)
        self.tag = 'body'


class P(Element):
    def __init__(self, *args, **kwargs):
        super(P, self).__init__(*args, **kwargs)
        self.tag = 'p'
