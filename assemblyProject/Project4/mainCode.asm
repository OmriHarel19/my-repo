include \masm32\include\masm32rt.inc
include mainFuncs.inc
.code

main proc
	invoke Load

	loopi:
		invoke Update
		invoke Draw
	jmp loopi
ret

	
main endp

end main
