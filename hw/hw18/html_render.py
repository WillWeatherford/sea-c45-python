#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.

# indent: start with just x amount of spaces, then use string formatting
# justify right {:>x}

TAB_SIZE = 4


class Content(object):
    def __init__(self, text):
        self.text = text

    def render_html(self, indent, newline='\n'):
        return '{}{}{}'.format(newline, ' ' * indent, self.text)


class Element(object):
    def __init__(self, content=None, **attrs):
        self.tag = ''
        self.extra_tag = ''
        self.content_newline = '\n'
        self.children = []
        self.append(content)
        self.attrs = attrs

    def __str__(self):
        return self.render()

    def render(self, f):
        f.write(self.render_html())

    def render_html(self, indent=0, newline='\n'):
        child_indent = indent + TAB_SIZE
        return u'{x}{n}{i}<{t}{a}>{c}{n}{i}</{t}>'.format(
            x=self.extra_tag,
            n=newline,
            i=u' ' * indent,  # possible to use int in string format better?
            a=self.format_attrs(),
            t=self.tag,
            c=u''.join([child.render_html(
                child_indent) for child in self.children]))

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
        self.child_newline = ''

    def render_html(self, indent=0, newline=u'\n'):
        return u'{n}{i}<{t}{a}>{c}</{t}>'.format(
            n=newline,
            i=u' ' * indent,  # possible to use int in string format better?
            t=self.tag,
            a=self.format_attrs(),
            c=u''.join(
                [child.render_html(0, u'') for child in self.children]))


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

class Hr(Element):
    def __init__(self, *args, **kwargs):
        super(Hr, self).__init__(*args, **kwargs)
        self.tag = 'hr'

    def render_html(self, indent=0):
        return u'\n{i}<{t}{a} />'.format(
            i=u' ' * indent,  # possible to use int in string format better?
            t=self.tag,
            a=self.format_attrs(),
            c=u''.join(
                [child.render_html(0, '') for child in self.children]))


class Meta(Hr):
    def __init__(self, *args, **kwargs):
        super(Meta, self).__init__(*args, **kwargs)
        self.tag = 'meta'
