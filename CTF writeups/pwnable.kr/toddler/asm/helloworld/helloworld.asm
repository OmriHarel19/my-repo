    global _start
    _start:
    jmp short string ;jump to string (jump short to avoid null bytes)

    code:
    pop rsi ; rsi = adr of "hello world"
    xor rax, rax
    mov al, 1 ; rax = 1 -> #write syscall
    mov rdi, rax ; rdi(fd) = 1 -> write to STDOUT
    mov rdx, rdi
    add rdx, 14 ; rdx = len of string
    syscall

    xor rax, rax
    add rax, 60 ; rax = 60 -> #exit syscall
    xor rdi, rdi; rdi = 0 -> exit on success exit(0)
    syscall

    string:
    call code ;call code pushing adr of string (jumping backwords to avoid null bytes)
    db  'Hello, world!',0x0A, 0x0D
