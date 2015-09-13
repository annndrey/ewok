#!/usr/bin/env python
# encoding: utf-8
import json
from subprocess import Popen, PIPE
from django.conf import settings

wrapper = '''
(function run(globals) {
    try {
        console.log(JSON.stringify({"result": (%(func)s).apply(null, %(args)s)}))
    } catch (e) {
        console.log(JSON.stringify({error: e.message}));
    }
})(%(globals)s);
'''

try:
    node = settings.NODE_EXEC
except:
    node = 'node'


def execute(code, args=None, g=None, node_exec=node):
    if args is None:
        args = []

    if g is None:
        g = {}

    assert isinstance(code, (str, unicode))
    assert isinstance(g, dict)
    assert code.strip(" ").strip("\t").startswith('function'), "Code must be function"

    prc = Popen(node_exec, shell=False, stderr=PIPE, stdout=PIPE, stdin=PIPE)

    c = wrapper % {
        'func': code,
        'globals': json.dumps(g),
        'args': json.dumps(args)
    }

    prc.stdin.write(c)
    prc.stdin.close()
    prc.wait()

    result = json.loads(prc.stdout.read())

    if 'result' in result:
        return result.get('result')
    else:
        raise Exception((
            result.get('error'),
            prc.stderr.read(),
        ))


if __name__ == '__main__':
    print execute('''function test () {
        return 10;
    }''')

    print execute('''function (args) {
        var result = 0;

        args.map(function (i) {
            result += i;
        });
        return result;
    }''', args=[[1, 2, 3, 4, 5]])

    print execute('''function () {
        return 1.0/0;
    }''')