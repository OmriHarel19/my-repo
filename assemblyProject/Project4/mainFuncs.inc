
include funcs.inc


.code

Load proc
	invoke drd_init,widthW,heightW,0
	invoke drd_imageLoadFile, offset res.bgHD, offset res.bgRAM
	invoke drd_imageLoadFile, offset res.rocketHD, offset res.rocketRAM
	invoke drd_imageLoadFile, offset res.meteorHD, offset res.meteorRAM
	invoke drd_imageLoadFile, offset res.planeHD, offset res.planeRAM
	invoke drd_imageLoadFile, offset plane1HD.planeStand, offset plane1RAM.planeStand
	invoke drd_imageSetTransparent,offset res.rocketRAM,0FFFFFFh
	invoke drd_imageSetTransparent,offset res.meteorRAM,0FFFFFFh
	invoke drd_imageSetTransparent,offset res.planeRAM,0FFFFFFh
		invoke drd_imageSetTransparent,offset plane1RAM.planeStand,0FFFFFFh

ret
Load endp

Update proc 
	invoke move,offset spc
	invoke keepInBound,offset spc
	invoke keyboardSpc,offset spc
	invoke move,offset met
	invoke keyboardSpc,offset rck
	invoke drd_processMessages
ret
Update endp

Draw proc 
	
	invoke drd_imageDraw,offset res.bgRAM,0,0
	invoke drd_imageDraw,offset plane1RAM.planeStand,spc.pos.x,spc.pos.y
	invoke drd_imageDraw,offset res.rocketRAM,rck.pos.x,rck.pos.y
	
	;loop for multiple meteors
	mov edi,0
	LOOPIT:
	cmp edi,0
	jg ENDLOOP
	invoke drawMeteors,offset met,30
	add edi,16
	jmp LOOPIT
	ENDLOOP:

	invoke drd_flip
	
ret

Draw endp 
