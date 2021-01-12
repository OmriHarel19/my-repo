from pwn import *
import re
import sys

#debbuging the connection
context.log_level = 'debug'

#connect
conn = remote('pwnable.kr', 9007)

#throw away the starting message
conn.recvuntil("sec... -")

#find 100 coins
for coins in range(100):
	
	#find n value
	conn.recvuntil("N=")
	n = int(conn.recvuntil(" ")) 

	#find c value
	conn.recvuntil("C=")
	c = int(conn.recvuntil("\n"))

	print("n: ",n,", c: ",c)

	start = 0
	mid = int(n/2)
	end = n
	
	#find coin in binary search:
	print("coin number: ",coins)
	
	for i in range(c):
		print("this is weigh number:", i+1)
		print("start: ",start,", mid: ", mid, ", end: ", end)
		
		#send idx's
		a = [str(i) for i in range(start,mid+1)] # creates a list from start up to (mid)
		conn.sendline(" ".join(a))
		
		
		#receive resault:
		res = int(conn.recvuntil("\n"))
		print("received: ", res)
		
		#case when the coin is not in this half:
		if res % 10 == 0:
			print("% 10 == 0")
			#when we get to the last check:
			if i == (c-1):
				print("last weigh")
				if (mid - start) == 0:
					print("sending idx")
					conn.sendline(str(start + 1))
					print(conn.recvline())

			else:
				mid += 1
				start = mid
				mid += int((end - mid)/2)
		
		#case when the coin is in this half:	
		else:
			print("% 10 != 0")
			#when we get to the last check:
			if i == (c-1):
				print("last weigh")
				if (mid - start) == 0:
					print("sending idx")
					conn.sendline(str(start))
					print(conn.recvline())
			
			else:
				end = mid
				mid = start + int((mid - start)/2)
	print("end of coin ",coins) 

