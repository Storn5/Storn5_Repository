import sys

MEM_SIZE = 1024 # 1 KB of memory

def parse(code):
    memory = [0] * MEM_SIZE
    pointer = 0
    while_state = False
    while_pointer = 0
    c = 0
    
    while c < len(code):
        if code[c] == '>':
            if pointer < MEM_SIZE-1: pointer += 1
        elif code[c] == '<':
            if pointer > 0: pointer -= 1
        elif code[c] == '+':
            if memory[pointer] < 255: memory[pointer] += 1
            # else: memory[pointer] = 0
        elif code[c] == '-':
            if memory[pointer] > 0: memory[pointer] -= 1
            # else: memory[pointer] = 255
        elif code[c] == '.':
            print(chr(memory[pointer]), end='')
        elif code[c] == ',':
            memory[pointer] = ord(input()[0])
        elif code[c] == '[':
            while_pointer = c
            while_state = True if memory[pointer] > 0 else False
        elif code[c] == ']':
            if while_state: c = while_pointer-1
        # DEBUGGING PURPOSES ONLY
        # elif code[c] == '?':
        #     print(memory[pointer], end='')
        # if code[c] == '+' or code[c] == '-':
        #    print(memory[0:5])
        
        c += 1

def main():
    code = open(sys.argv[1], 'r').read()
    parse(code)

if __name__ == '__main__':
    main()