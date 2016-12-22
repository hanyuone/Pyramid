import sys

def pyramid_exec(in_code):
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
        elif current in ["d", "r", "u", "b"]:
            result = current + str(prev_result)
    return result

def pyramid_init():
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
        if current_result[0] == "u":
            stack = (stack - 1) % len(code)
            current_result = pyramid_exec(code[stack])
        elif current_result[0] == "d":
            stack = (stack + 1) % len(code)
            current_result = pyramid_exec(code[stack])
        elif current_result[0] == "r":
            current_result = pyramid_exec(code[stack])
        elif current_result[0] == "b":
            print(current_stack)
            current_stack = []
            current_result = pyramid_exec(code[stack])
    print(current_stack)

pyramid_init()
