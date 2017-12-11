# PwnWAF
pwn log tools for AWD

## Description
Use traceGen.py to generate elf file.

 * elf\_name: which elf we want to log file
 * log\_path: log file
 * machine: the platform of this elf, (only surpport x86/x86\_64)

**NOTICE**: elf\_name and log\_path must be absolutely path

## Usage:

```bash
python traceGen.py  machine elf_name log_path
```

For example:

```bash
python traceGen.py 64 /path/to/elf/test.bin /path/to/log/log.txt
```

and the elf\_name.out is log bin file.Then rename this file(or others) to make xinetd boot this file. This file will start a child process to exec elf\_name file, and parent process will record info:
```
+-----+
|child| --> execute /path/to/elf/test.bin
+-----+

+------+
|parent| --> log I/O to /path/to/log/log.txt
+------+
```

and log.txt will like this:
```
WRIGING
Welcome to my pwn world!

READING
aaaaaaaaaaaaaaa

WRIGING
your input is :aaaaaaaaaaaaaaa
```
