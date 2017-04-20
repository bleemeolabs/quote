#!/usr/bin/python3

import argparse
import time
import random
import urllib.request


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--hostname', default='quote.bleemeo.com')
    parser.add_argument('--address', default='localhost')
    parser.add_argument('--port', default=80, type=int)
    parser.add_argument('--delay', default=1.0, type=float)
    parser.add_argument('--random', default=False, action='store_true')
    parser.add_argument('--verbose', default=False, action='store_true')
    args = parser.parse_args()

    while True:
        request = urllib.request.Request(
            'http://%s:%s/' % (args.address, args.port),
            headers={'Host': args.hostname},
        )
        try:
            resp = urllib.request.urlopen(request)
        except Exception as exc:
            print('Request failed: %s' % exc)
            resp = None

        if args.verbose and resp is not None:
            print('Response is:\n%s' % resp.read().decode('utf-8'))
        if args.random:
            time.sleep(random.random() * args.delay)
        else:
            time.sleep(args.delay)


if __name__ == '__main__':
    main()
