watchdog_exec
=============

Cross-platform command-line execute-on-fs-event tool.

## Install
Written+tested with Python 2.7, but would probably work unedited on Python 3:

    pip install https://github.com/SamuelMarks/watchdog_exec/archive/master.zip#egg=watchdog_exec

## Example runs

On fs event involving files and folders in current directory, run `echo $src $dst` command, unless it the fs event is modified, then run `python $src` command.

    python -m watchdog_exec . --execute echo --modified python

Using short arguments, and restricting to only execute when events involve "__main__.py":

    python -m watchdog_exec . -e echo -a echo -s __main__.py


## Usage

    usage: python -m watchdog_exec [-h] -e EXEC [-m MOVED] [-c CREATED] [-d DELETED]
                                   [-a MODIFIED] [-f] [-g] [-s SPECIFIC_FILE]
                                   directory
    
    Execute command on fs event
    
    positional arguments:
      directory             Directory
    
    optional arguments:
      -h, --help            show this help message and exit
      -e EXEC, --exec EXEC  Execute fallback
      -m MOVED, --moved MOVED
                            Execute on fs moved event
      -c CREATED, --created CREATED
                            Execute on fs created event
      -d DELETED, --deleted DELETED
                            Execute on fs deleted event
      -a MODIFIED, --modified MODIFIED, --altered MODIFIED
                            Execute on fs modified event
      -f, --file-only       Execute only on file fs events fs
      -g, --directory-only  Execute only on file fs events fs
      -s SPECIFIC_FILE, --specific-file SPECIFIC_FILE
                            Execute only on events involving this file
