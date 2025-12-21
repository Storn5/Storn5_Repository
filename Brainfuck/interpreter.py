import sys

if len(sys.argv) < 2:
    print('ERROR: No argument')
    print('USAGE: python interpreter.py [filename]')
    exit()

mem_size = 30_000
memory = [0] * mem_size
pointer = 0
program_pointer = 0
sourcecode = ''
sourcecode_len = len(sourcecode)
input_buffer = ''

def jump_after_matching_closing_loop():
    global sourcecode, program_pointer
    loop_level = 0
    while program_pointer < sourcecode_len:
        if sourcecode[program_pointer] == '[':
            loop_level += 1
        elif sourcecode[program_pointer] == ']':
            loop_level -= 1
        if loop_level == 0:
            break
        program_pointer += 1

def jump_after_matching_opening_loop():
    global sourcecode, program_pointer
    loop_level = 0
    while program_pointer < sourcecode_len:
        if sourcecode[program_pointer] == ']':
            loop_level += 1
        elif sourcecode[program_pointer] == '[':
            loop_level -= 1
        if loop_level == 0:
            break
        program_pointer -= 1

def pointer_right():
    global pointer, memory
    pointer = (pointer + 1) % mem_size
def pointer_left():
    global pointer, memory
    pointer = (pointer - 1) % mem_size
def increment():
    global pointer, memory
    memory[pointer] = (memory[pointer] + 1) % 256
def decrement():
    global pointer, memory
    memory[pointer] = (memory[pointer] - 1) % 256
def output():
    global pointer, memory
    print(chr(memory[pointer]), end='')
def read_input():
    global pointer, memory, input_buffer
    if len(input_buffer) == 0:
        input_buffer = input().strip()
    if len(input_buffer) > 0:
        memory[pointer] = ord(input_buffer[0])
        input_buffer = input_buffer[1:]
def start_loop():
    global sourcecode, program_pointer
    if memory[pointer] == 0:
        jump_after_matching_closing_loop()
def end_loop():
    global sourcecode, program_pointer
    if memory[pointer] != 0:
        jump_after_matching_opening_loop()

operators_dict = {
    '>': pointer_right,
    '<': pointer_left,
    '+': increment,
    '-': decrement,
    '.': output,
    ',': read_input,
    '[': start_loop,
    ']': end_loop
}

with open(sys.argv[1]) as sourcecode_file:
    sourcecode = sourcecode_file.read()
sourcecode_len = len(sourcecode)

while program_pointer < sourcecode_len:
    next_char = sourcecode[program_pointer]
    if next_char in operators_dict:
        operators_dict[next_char]()
    program_pointer += 1
