def rm(params=None):
	"""
RM(1)                                                                      User Commands                                                                      RM(1)

NAME
       rm - remove files or directories

SYNOPSIS
       rm [OPTION]... FILE...

DESCRIPTION
       This manual page documents the GNU version of rm.  rm removes each specified file.  By default, it does not remove directories.

       If  the  -I or --interactive=once option is given, and there are more than three files or the -r, -R, or --recursive are given, then rm prompts the user for
       whether to proceed with the entire operation.  If the response is not affirmative, the entire command is aborted.

       Otherwise, if a file is unwritable, standard input is a terminal, and the -f or --force option is not given, or the -i  or  --interactive=always  option  is
       given, rm prompts the user for whether to remove the file.  If the response is not affirmative, the file is skipped.

OPTIONS
       Remove (unlink) the FILE(s).

       -f, --force
              ignore nonexistent files and arguments, never prompt

       -i     prompt before every removal

       -I     prompt  once  before removing more than three files, or when removing recursively; less intrusive than -i, while still giving protection against most
              mistakes

       --interactive[=WHEN]
              prompt according to WHEN: never, once (-I), or always (-i); without WHEN, prompt always

       --one-file-system
              when removing a hierarchy recursively, skip any directory that is on a file system different from that of the corresponding command line argument

       --no-preserve-root
              do not treat '/' specially

       --preserve-root
              do not remove '/' (default)

       -r, -R, --recursive
              remove directories and their contents recursively


       -d, --dir
              remove empty directories

       -v, --verbose
              explain what is being done

       --help display this help and exit

       --version
              output version information and exit

       By default, rm does not remove directories.  Use the --recursive (-r or -R) option to remove each listed directory, too, along with all of its contents.

       To remove a file whose name starts with a '-', for example '-foo', use one of these commands:

              rm -- -foo

              rm ./-foo

       Note that if you use rm to remove a file, it might be possible to recover some of its contents, given sufficient expertise and/or time.  For greater  assur      ance that the contents are truly unrecoverable, consider using shred.

AUTHOR
       Written by Paul Rubin, David MacKenzie, Richard M. Stallman, and Jim Meyering.

REPORTING BUGS
       GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
       Report rm translation bugs to <http://translationproject.org/team/>

COPYRIGHT
       Copyright @ 2014 Free Software Foundation, Inc.  License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
       This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       unlink(1), unlink(2), chattr(1), shred(1)

       Full documentation at: <http://www.gnu.org/software/coreutils/rm>
       or available locally via: info '(coreutils) rm invocation'

GNU coreutils 8.23                                                           March 2015                                                                       RM(1)
	"""

	return ""
