from __future__ import print_function
import os.path
import re
import requests
import sys


class NoelShackError(Exception):
    pass


class NoelShack:
    API_URL = 'http://www.noelshack.com/api.php'

    def upload(self, file):
        with open(file, 'rb') as f:
            r = requests.post(self.API_URL, files={'fichier': f})

        if not 'www.noelshack.com' in r.text:
            raise NoelShackError(r.text)

        return self.parse(r.text)

    def parse(self, url):
        return re.sub(r'www\.noelshack\.com/([0-9]+)-([0-9]+)-([0-9]+)-(.+)',
                      r'image.noelshack.com/fichiers/\1/\2/\3/\4',
                      url)


def main(argv):
    if 2 != len(argv):
        print("Usage: {0} file".format(argv[0]), file=sys.stderr)
        return 1

    file = argv[1]

    if not os.path.isfile(file):
        print("{0}: No such file".format(file), file=sys.stderr)
        return 1

    ns = NoelShack()

    try:
        print(ns.upload(file))
    except NoelShackError as e:
        print(str(e), file=sys.stderr)
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
