include drd.inc
includelib drd.lib
include data.inc

.code

move proc adrObj:dword
	
	mov ebx,adrObj ;ebx=&pos.x


	mov ecx,[ebx+DMOffset.drc.x]
	add [ebx], ecx
	mov ecx,[ebx+DMOffset.drc.y]
	add [ebx+DMOffset.pos.y],ecx


	;check if picture arrives to the edges of the screen 
	
	;check left side
	mov edx,widthW
	cmp [ebx],edx
	je LEFTSIDE
	RETLEFTSIDE:

	;check right side
	mov edx,0
	cmp [ebx],edx
	je RIGHTSIDE
	RETRIGHTSIDE:

	;check bottom:
	mov edx,heightW
	cmp [ebx+DMOffset.pos.y],edx
	je DOWNSIDE
	RETDOWNSIDE:

	;check top:
	mov edx,0
	cmp [ebx+DMOffset.pos.y],edx
	je TOPSIDE
	RETTOPSIDE:
	

ret

	LEFTSIDE:
	mov ecx,-1
	mov [ebx+DMOffset.drc.x],ecx
	jmp RETLEFTSIDE

	RIGHTSIDE:
	mov ecx,1
	mov [ebx+DMOffset.drc.x],ecx
	jmp RETRIGHTSIDE

	DOWNSIDE:
	mov ecx,-1
	mov [ebx+DMOffset.drc.y],ecx
	jmp RETDOWNSIDE

	TOPSIDE:
	mov ecx,1
	mov [ebx+DMOffset.drc.y],ecx
	jmp RETTOPSIDE
	
move endp

changeDrc proc adrObj:dword, key:dword, adrDrc:dword, value:dword

	;register use: eax,ecx,edi,edx

	invoke GetAsyncKeyState, key
	cmp eax,0
	jne GOTOKEY

ret

	GOTOKEY:
	mov ecx,adrDrc
	mov edi,adrObj
	add ecx,edi
	mov edx,value
	mov [ecx],edx	
ret
changeDrc endp
;remember to change shoot proc parameters and after that add move proc to rck
shoot proc adrObj:dword, key:dword, adrYpos:dword
	
	invoke GetAsyncKeyState, key
	cmp eax,0
	jne SHOOT
	RETSHOOT:
ret
	SHOOT:
		mov ebx,adrObj
		mov ecx,adrYpos
		mov edx,-1
		mov [ebx+ecx],edx
	jmp RETSHOOT

shoot endp

keyboardSpc proc adrObj:dword
	mov ebx, adrObj
	mov [ebx+DMOffset.drc.x],0	;make sure that chr not mov in x
	mov [ebx+DMOffset.drc.y],0	;make sure that chr not mov in y


	invoke changeDrc,ebx,[ebx+DMOffset.keys.right], DMOffset.drc.x, 1
	invoke changeDrc,ebx,[ebx+DMOffset.keys.left], DMOffset.drc.x, -1
	;invoke changeDrc,ebx,[ebx+DMOffset.keys.up], DMOffset.drc.y,-1
	;invoke changeDrc,ebx,[ebx+DMOffset.keys.down], DMOffset.drc.y,1
ret
keyboardSpc endp

keyboardRck proc adrObj:dword 
	mov ebx, adrObj
	invoke shoot,ebx,[ebx+DMOffset.keys.up],DMOffset.pos.y
ret
keyboardRck endp



drawMeteors proc adrObj:dword, waitCount:dword
	;register use: edx,esi,ecx,ebx
	
	mov ebx,adrObj

	;wait:
	;compering wait counter
	mov edx,myWait
	cmp edx,waitCount
	jg WAITP
	inc myWait

	;animation:
	;compering idx array crop
	mov esi,count
	cmp esi,56
	jg RESETANIM
	RETRESETANIM:

	RETWAITP:
	invoke drd_imageDrawCrop,offset res.meteorRAM,[ebx],[ebx+MetOffset.pos.y],meteorXCrop[esi],0,60,66
	
	invoke drd_flip
	
ret
	RESETANIM:
		mov count,0
	jmp RETRESETANIM

	WAITP:
		;increasing idx off crop array
		mov ecx,4
		add count,ecx
		;reseting the counter for the Wait 
		mov ecx,0
		mov myWait,ecx
	jmp RETWAITP

drawMeteors endp

keepInBound proc adrObj:dword
	mov ebx,adrObj

	mov ecx,0
	cmp [ebx],ecx
	jl LEFTBORDER
	RETLEFTBORDER:

	mov ecx,widthW
	cmp [ebx],ecx
	jg RIGHTBORDER
	RETRIGHTBORDER:
ret

	LEFTBORDER:
	mov ecx,widthW
	mov [ebx],ecx
	mov ecx,-1
	add [ebx],ecx
	jmp RETLEFTBORDER

	RIGHTBORDER:
	mov ecx,0
	mov [ebx],ecx
	mov ecx,1
	add [ebx],ecx
	jmp RETRIGHTBORDER

keepInBound endp



random proc 
	push edx
	mov	eax,[rand]
	mov	edx,0019660Dh
	mul	edx
	add	eax,3C6EF35Fh
	mov	[rand],eax
	pop	edx
	mov spc.pos.x, edx
ret
random endp

