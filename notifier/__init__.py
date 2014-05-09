import sys

from notifier.util import *

from notifier.providers import PrintNotify


def init(**providers):
    if 'print' not in providers:
        providers['print'] = PrintNotify()

    provider = sys.argv[1] if len(sys.argv) > 1 else 'print'

    if provider not in providers:
        exit('Unknown provider. Known providers are: {}'.format(', '.join(providers.keys())))
    return providers[provider]
