import sys

def pyramid_exec(in_code):
    global current_stack
    code = in_code + []
    start = -1
    prev_result = -1
    result = -1
    for a in range(len(code)):
        if code[a][-1] == "<":
            if start != -1:
                print("Error: Too many start counters.")
                sys.exit()
            else:
                start = a
    code[start] = code[start][:-1]
    while result == -1:
        current = code[start][-1]
        code[start] = code[start][:-1]
        if current == "0":
            if start == 0 or len(code[start - 1]) == 0:
                result = 0
            else:
                start -= 1
                prev_result = 0
        elif current == "1":
            if start == len(code) - 1 or len(code[start + 1]) == 0:
                result = 1
            else:
                start += 1
                prev_result = 1
        elif current == ".":
            if len(code[start]) == 1:
                result = "."
        elif current == "?":
            user_in = raw_input("Input: ")
            if user_in in ["0", "1", "."]:
                code[start] = code[start] + user_in
            else:
                print("Error: Not a valid input.")
                sys.exit()
        elif current in ["v", "@", "^"]:
            result = current + str(prev_result)
        elif current == "o":
            print("".join(str(x) for x in current_stack))
            current_stack = []
        elif current == "p":
            code[start].append(current_stack[-1])
            current_stack = current_stack[:-1]
        elif current == "f":
            current_stack = current_stack[::-1]
    return result

def pyramid_init():
    global current_stack
    code_check = 1
    code = [[]]
    while code_check:
        code_check = raw_input(">>> ")
        if code_check == "---":
            code.append([])
        else:
            code[len(code) - 1].append(code_check)
    code[len(code) - 1] = code[len(code) - 1][:-1]

    stack = int(raw_input("Stack: "))
    current_stack = []
    current_result = pyramid_exec(code[stack])
    while type(current_result) == str:
        current_stack.append(int(current_result[-1]) if current_result[-1] in ["0", "1"] else ".")
        if current_result[0] == "^":
            stack = (stack - 1) % len(code)
            current_result = pyramid_exec(code[stack])
        elif current_result[0] == "v":
            stack = (stack + 1) % len(code)
            current_result = pyramid_exec(code[stack])
        elif current_result[0] == "@":
            current_result = pyramid_exec(code[stack])
    print(current_stack)

pyramid_init()
