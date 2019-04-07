"""Main entry point for running discord-hero

discord-hero: Discord Application Framework for humans

:copyright: (c) 2019 monospacedmagic et al.
:license: Apache-2.0 OR MIT
"""

import asyncio
import sys

import hero
from .cache import Cache
from .db import Database


def main(test: bool=False):
    """Run Hero.

    :param test: Whether or not this is a test run.
    :type test: bool
    """
    hero.TEST = test
    try:
        import uvloop
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    except ImportError:
        pass

    if sys.platform == "win32":
        asyncio.set_event_loop(asyncio.ProactorEventLoop())

    loop = asyncio.get_event_loop()
    with hero.Core(loop=loop) as core:
        core.run()
