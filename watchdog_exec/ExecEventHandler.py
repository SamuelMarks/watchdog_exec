from __future__ import print_function
from subprocess import check_output
from os import path

from watchdog.events import FileSystemEventHandler


class ExecEventHandler(FileSystemEventHandler):
    """Logs all the events captured."""

    def __init__(self, **cmd_args):
        self.created_exec = cmd_args.get('created', cmd_args['exec'])
        self.deleted_exec = cmd_args.get('deleted', cmd_args['exec'])
        self.moved_exec = cmd_args.get('moved', cmd_args['exec'])
        self.modified_exec = cmd_args.get('modified', cmd_args['exec'])
        self.file_only = cmd_args['file_only']
        self.directory_only = cmd_args['directory_only']
        self.specific_file = cmd_args.get('specific_file')

    def should_exec(self, is_directory):
        what = 'directory' if is_directory else 'file'
        if self.specific_file:
            if what == 'directory':
                return False
            return True
        else:
            return what == 'directory' and not self.file_only or what == 'file' and not self.directory_only

    def execute(self, cmd, src, dst=None):
        def get_args():
            if self.specific_file and self.specific_file not in {src, path.basename(src)}:
                raise StopIteration
            yield cmd
            yield src
            if dst:
                yield dst

        args = list(get_args())
        return check_output(args, shell=True, universal_newlines=True) if args else ''

    def on_moved(self, event):
        super(ExecEventHandler, self).on_moved(event)

        if self.should_exec(event.is_directory):
            print(self.execute(self.moved_exec, event.src_path, event.dest_path), end='')

    def on_created(self, event):
        super(ExecEventHandler, self).on_created(event)

        if self.should_exec(event.is_directory):
            print(self.execute(self.created_exec, event.src_path), end='')

    def on_deleted(self, event):
        super(ExecEventHandler, self).on_deleted(event)

        if self.should_exec(event.is_directory):
            print(self.execute(self.deleted_exec, event.src_path), end='')

    def on_modified(self, event):
        super(ExecEventHandler, self).on_modified(event)

        if self.should_exec(event.is_directory):
            print(self.execute(self.modified_exec, event.src_path), end='')
