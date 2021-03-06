import sys
import types

# True if we are running on Python 3.
PY3 = sys.version_info[0] == 3

if PY3: # pragma: no cover
    string_types = str,
    integer_types = int,
    class_types = type,
    text_type = str
    binary_type = bytes
    long = int
else:
    string_types = basestring,
    integer_types = (int, long)
    class_types = (type, types.ClassType)
    text_type = unicode
    binary_type = str
    long = long

# TODO check if errors is ever used

def text_(s, encoding=None, errors='strict'):
    if isinstance(s, binary_type):
        if not encoding:
            try:
                return s.decode('utf-8')
            except UnicodeDecodeError:
                encoding = 'latin-1'
        return s.decode(encoding, errors)
    return s # pragma: no cover

def bytes_(s, encoding=None, errors='strict'):
    if isinstance(s, text_type): # pragma: no cover
        if not encoding:
            try:
                return s.encode('latin-1')
            except UnicodeEncodeError:
                encoding = 'utf-8'
        return s.encode(encoding, errors)
    return s

if PY3: # pragma: no cover
    def native_(s, encoding=None, errors='strict'):
        if isinstance(s, text_type):
            return s
        if not encoding:
            try:
                return str(s, 'utf-8')
            except UnicodeDecodeError:
                encoding = 'latin-1'
        return str(s, encoding, errors)
else:
    def native_(s, encoding=None, errors='strict'):
        if isinstance(s, text_type): # pragma: no cover
            return s.encode(encoding, errors)
        if not encoding:
            try:
                return s.encode('latin-1')
            except UnicodeEncodeError:
                encoding = 'utf-8'
        return str(s)

if PY3: # pragma: no cover
    import builtins
    exec_ = getattr(builtins, "exec")
    def reraise(exc_info):
        etype, exc, tb = exc_info
        if exc.__traceback__ is not tb:
            raise exc.with_traceback(tb)
        raise exc
else: # pragma: no cover
    def exec_(code, globs=None, locs=None):
        """Execute code in a namespace."""
        if globs is None:
            frame = sys._getframe(1)
            globs = frame.f_globals
            if locs is None:
                locs = frame.f_locals
            del frame
        elif locs is None:
            locs = globs
        exec("""exec code in globs, locs""")
    exec_("""def reraise(exc_info):
    raise exc_info[0], exc_info[1], exc_info[2]
""")

if PY3: # pragma: no cover
    from io import StringIO
    from io import BytesIO
else:
    from StringIO import StringIO
    BytesIO = StringIO

if PY3: # pragma: no cover
    import builtins
    exec_ = getattr(builtins, "exec")


    def reraise(tp, value, tb=None):
        if value.__traceback__ is not tb:
            raise value.with_traceback(tb)
        raise value


    del builtins

else: # pragma: no cover
    def exec_(code, globs=None, locs=None):
        """Execute code in a namespace."""
        if globs is None:
            frame = sys._getframe(1)
            globs = frame.f_globals
            if locs is None:
                locs = frame.f_locals
            del frame
        elif locs is None:
            locs = globs
        exec("""exec code in globs, locs""")


    exec_("""def reraise(tp, value, tb=None):
    raise tp, value, tb
""")

if PY3: # pragma: no cover
    from urllib import parse
    urlparse = parse
    from urllib.parse import quote as url_quote
    from urllib.parse import quote_plus as url_quote_plus
    from urllib.parse import unquote as url_unquote
    from urllib.parse import urlencode as url_encode
    from urllib.request import urlopen as url_open
else:
    import urlparse
    from urllib import quote as url_quote
    from urllib import quote_plus as url_quote_plus
    from urllib import unquote as url_unquote
    from urllib import urlencode as url_encode
    from urllib2 import urlopen as url_open

if PY3: # pragma: no cover
    xrange_ = range
else:
    xrange_ = xrange


if PY3: # pragma: no cover
    def iteritems_(d):
        return d.items()
else:
    def iteritems_(d):
        return d.iteritems()

