;;rep


%define jumpDist 0x5200
;; not changeable
%define repAmount 0x100
%define repDist 0x2*repAmount

mov bx, 0xCCCC
xchg bx,ax ;; bx = loc, ax = CCCC

;; es = StackSeg
push ss
pop es
;;copy repmovsw+reset_code to es:0x0
lea si,[bx+@copy]
mov cl, (@reset_loop_end-@reset_loop)/2 + 0x1+0x1
rep movsw
;; bomb 0xCCCC to es
mov dx,ax
int 0x86
int 0x86

std
;; es = Arena, ds = StackSeg
push ds
push es
pop ds
pop es
;; write repmovsw in Arena
add bx, jumpDist ;; bx = repmovsw loc
mov di, bx
xor si,si
movsw
;; prepare for REP
mov dx, repDist
add di,dx
mov si,dx
inc ch
mov ax,jumpDist
jmp bx

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

@copy:
rep movsw
@reset_loop:
add bx, ax
mov di,bx
movsw
mov si, dx
add di, dx 
inc ch
dec bp
db 0x75
		;; 0x75ff - jnz short 0xff
db 0xff
		;; 0xffe3 - jmp bx
db 0xe3
@reset_loop_end:
