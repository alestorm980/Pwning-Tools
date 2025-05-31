#!/usr/bin/python3
from pwn import *

elf = context.binary = ELF("<elf>")
context.arch = "amd64|i386"
context.terminal = ['tmux', 'splitw', '-h']

libc = None


gs = '''
'''

def start():
    global libc

    if args.GDB:
        #libc = ELF("")
        return gdb.debug(elf.path, gdbscript=gs)
    elif args.REMOTE:
        #libc = ELF('')
        return remote('','')
    else:
        #libc = ELF("./lib/libc.so.6")
        return process(elf.path)

io = start()

io.interactive()
