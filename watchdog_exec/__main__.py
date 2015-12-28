#!/usr/bin/env python

from argparse import ArgumentParser
from time import sleep
 
from watchdog.observers import Observer

from watchdog_exec.ExecEventHandler import ExecEventHandler


def _build_parser():
    parser = ArgumentParser(description='Execute command on fs event')
    parser.add_argument('directory', help='Directory')
    parser.add_argument('-e', '--exec', help='Execute fallback', required=True)
    parser.add_argument('-m', '--moved', help='Execute on fs moved event', required=False)
    parser.add_argument('-c', '--created', help='Execute on fs created event', required=False)
    parser.add_argument('-d', '--deleted', help='Execute on fs deleted event', required=False)
    parser.add_argument('-a', '--modified', '--altered', help='Execute on fs modified event', required=False)
    parser.add_argument('-f', '--file-only', help='Execute only on file fs events fs', required=False,
                        default=False, action='store_true')
    parser.add_argument('-g', '--directory-only', help='Execute only on file fs events fs', required=False,
                        default=False, action='store_true')
    parser.add_argument('-s', '--specific-file', help='Execute only on events involving this file', required=False)
    return parser


# if __name__ == '__main__':
# scaffold = Scaffold(dict(_build_parser().parse_args()._get_kwargs()))


if __name__ == "__main__":
    # cmd_args = dict(_build_parser().parse_args()._get_kwargs())
    cmd_args = _build_parser().parse_args()
    event_handler = ExecEventHandler(**{k: v for k, v in cmd_args._get_kwargs() if v is not None})
    observer = Observer()
    observer.schedule(event_handler, cmd_args.directory, recursive=True)
    observer.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
