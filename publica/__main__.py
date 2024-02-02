# Okay a new beginning
from .importer import parse_url

import argparse
import os

parser = argparse.ArgumentParser(
    prog='python -m publica',  # TODO
    description='Yet another lib server for home',
    epilog='Thanks for using Publica. Source can be found on Github'
)
parser.add_argument('action',
                    choices=['dist', 'serve', 'clean', 'import'])
parser.add_argument('url', type=str,
                    help="URL to be imported")
args = parser.parse_args()


def dist():
    print('This is DIST')


def serve():
    print('This is SERVE')


def import_(url):
    # Sorry for using an identifier :)
    expo = parse_url(url)
    with open(f'./contents/{expo.title}.md', mode='w', encoding='utf-8') as f:
        f.write(expo.text())


def clean():
    print("Cleaning your dist dir")
    os.rmdir("./dist")


if __name__ == '__main__':
    match args.action:
        case 'dist':
            dist()
        case 'serve':
            serve()
        case 'clean':
            clean()
        case 'import':
            import_(args.url)
