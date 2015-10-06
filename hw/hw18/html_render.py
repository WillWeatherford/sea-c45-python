#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.

# indent: start with just x amount of spaces, then use string formatting
# justify right {:>x}

TAB_SIZE = 4
NEWLINE = '\n'


class Content(object):
    def __init__(self, text):
        self.text = text

    def render_html(self, indent, newline='\n'):
        return '{}{}{}'.format(newline, ' ' * indent, self.text)


class Element(object):
    def __init__(self, content=None, **attrs):
        self.tag = ''
        self.doctype = ''
        self.open_tag = '<{t}{a}>'
        self.close_tag = '</{t}>'
        self.multi_line = True
        self.attrs = attrs
        self.children = []
        if content:
            self.append(content)

    def __str__(self):
        return self.render()

    def render(self, f):
        f.write(self.render_html())

    def render_html(self, indent=0, newline=NEWLINE):
        return u'{d}{b_o}{o_t}{c}{b_c}{c_t}'.format(
            d=self.doctype,
            b_o='{}{}'.format(newline, ' ' * indent),
            o_t=self.open_tag.format(t=self.tag, a=self.format_attrs()),
            c=''.join([c.render_html(
                (indent + TAB_SIZE) * self.multi_line,
                NEWLINE * self.multi_line
                ) for c in self.children]),
            b_c='{}{}'.format(newline, ' ' * indent) * self.multi_line,
            c_t=self.close_tag.format(t=self.tag))

    def format_attrs(self):
        return ''.join([' {}="{}"'.format(k, v) for k, v in self.attrs.items()])

    def append(self, child=None):
        if child:
            if isinstance(child, Element):
                self.children.append(child)
                child.parent = self
            elif isinstance(child, str) or isinstance(child, unicode):
                self.children.append(Content(child))
            else:
                raise TypeError('Object appended to Element must be a string'
                                'or another Element; got {} instead'
                                ).format(type(child))


class Html(Element):
    def __init__(self, *args, **kwargs):
        super(Html, self).__init__(*args, **kwargs)
        self.tag = 'html'
        self.doctype = '<!DOCTYPE html>'


class Body(Element):
    def __init__(self, *args, **kwargs):
        super(Body, self).__init__(*args, **kwargs)
        self.tag = 'body'


class Head(Element):
    def __init__(self, *args, **kwargs):
        super(Head, self).__init__(*args, **kwargs)
        self.tag = 'head'


class P(Element):
    def __init__(self, *args, **kwargs):
        super(P, self).__init__(*args, **kwargs)
        self.tag = 'p'


class Ul(Element):
    def __init__(self, *args, **kwargs):
        super(Ul, self).__init__(*args, **kwargs)
        self.tag = 'ul'


class Li(Element):
    def __init__(self, *args, **kwargs):
        super(Li, self).__init__(*args, **kwargs)
        self.tag = 'li'


##########################
# OneLineTag and subclasses


class OneLineTag(Element):
    def __init__(self, *args, **kwargs):
        super(OneLineTag, self).__init__(*args, **kwargs)
        self.multi_line = False


class Title(OneLineTag):
    def __init__(self, *args, **kwargs):
        super(Title, self).__init__(*args, **kwargs)
        self.tag = 'title'


class H(OneLineTag):
    def __init__(self, size, content='', **kwargs):
        super(H, self).__init__(content, **kwargs)
        self.tag = 'h{}'.format(size)


class A(OneLineTag):
    def __init__(self, url, content='', **kwargs):
        super(A, self).__init__(content, href=url, **kwargs)
        self.tag = 'a'


#########################
# Non-closing tags

class EmptyTag(Element):
    def __init__(self, *args, **kwargs):
        super(EmptyTag, self).__init__(*args, **kwargs)
        self.open_tag = '<{t}{a} />'
        self.close_tag = ''
        self.multi_line = False


class Hr(EmptyTag):
    def __init__(self, *args, **kwargs):
        super(Hr, self).__init__(*args, **kwargs)
        self.tag = 'hr'


class Meta(EmptyTag):
    def __init__(self, *args, **kwargs):
        super(Meta, self).__init__(*args, **kwargs)
        self.tag = 'meta'
