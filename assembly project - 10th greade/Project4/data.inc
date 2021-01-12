
.const

planeHDS struct
	planeStand byte "pics\plane\planeStand.bmp",0
planeHDS ends

planeRAMS struct 
	planeStand Img<>
	;load plane stand!!
planeRAMS ends

Resorces struct 
	;pp byte planeHD
	bgHD byte "bg.bmp",0
	rocketHD byte "rocket.bmp",0
	meteorHD byte "meteor.bmp",0
	planeHD byte "plane.bmp",0
	bgRAM Img<>
	rocketRAM Img<>
	meteorRAM Img<>
	planeRAM Img<>
Resorces ends

Keys struct 
	left dword ?
	right dword ?
	
	up dword ? 
	down dword ?
	
Keys ends

Dmoot struct
	pos POINT<>
	drc POINT<>	
	keys Keys<>
Dmoot ends

DMOffset struct
	pos POINT<0,4>
	drc POINT<8,12>
	keys Keys<16,20,24,28>
DMOffset ends

Rocket struct
	pos POINT<>
	drc POINT<>	
	keys Keys<up>
Rocket ends

RocketOffset struct
	pos POINT<0,4>
	drc POINT<8,12>	
	keys Keys<16>
RocketOffset ends

Meteor struct
	pos POINT<>
	drc POINT<>
Meteor ends

MetOffset struct
	pos POINT<0,4>
	drc POINT<8,12>
MetOffset ends

.data

;variables & consts
widthW dword 800
heightW dword 600 
count dword 0
waitCountDup dword 0
myWait dword 0
rand dword 0ffffffffh


;objects
res Resorces<>
plane1HD planeHDS<>
plane1RAM planeRAMS<>
spc Dmoot<<300,500>,<1,0>,<VK_LEFT,VK_RIGHT,VK_UP>>
rck Meteor<<100,500>,<0,0>>
met Meteor<<1,1>,<0,1>>
met2 Meteor<<80,1>,<0,1>>
met3 Meteor<<160,1>,<0,1>>
met4 Meteor<<240,1>,<0,1>>
met5 Meteor<<320,1>,<0,1>>
met6 Meteor<<400,1>,<0,1>>
met7 Meteor<<480,1>,<0,1>>
met8 Meteor<<560,1>,<0,1>>
met9 Meteor<<640,1>,<0,1>>
met10 Meteor<<720,1>,<0,1>>


;arrays
;x values for crop animation of meteor
meteorXCrop dword 16 dup(0,60,120,180,240,300,360,420,480,540,600,660,720,780,840,900)

;array of all meteors
meteors Meteor 10 dup(<<met>>,<<met2>>,<<met3>>,<<met4>>,<<met5>>,<<met6>>,<<met7>>,<<met8>>,<<met9>>,<<met10>>)
