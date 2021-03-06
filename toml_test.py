#!/usr/bin/env python2
 
import datetime
import json
import sys
import toml_ply
 
def tag(value):
    if isinstance(value, dict):
        d = { }
        for k, v in value.iteritems():
            d[k] = tag(v)
        return d
    elif isinstance(value, list):
        a = []
        for v in value:
            a.append(tag(v))
        return {'type': 'array', 'value': a}
    elif isinstance(value, basestring):
        return {'type': 'string', 'value': str(value)}
    elif isinstance(value, bool):
        return {'type': 'bool', 'value': str(value).lower()}
    elif isinstance(value, int):
        return {'type': 'integer', 'value': str(value)}
    elif isinstance(value, float):
        return {'type': 'float', 'value': repr(value)}
    elif isinstance(value, datetime.datetime):
        sdate = value.strftime('%Y-%m-%dT%H:%M:%SZ')
        return {'type': 'datetime', 'value': sdate}
    assert False, 'Unknown type: %s' % type(value)
 
 
if __name__ == '__main__':
    try:
        tdata = toml_ply.loads(sys.stdin.read())
    except Exception, e:
        print e
        sys.exit(1)
    tagged = tag(tdata)
    print json.dumps(tagged, ensure_ascii=True)
