from main import Stack

def p_balance(value):
    stack=Stack()
    for i in value:
        if stack.peek() + i == '[]' or stack.peek() + i == '{}' or stack.peek() + i == '()':
            stack.pop()
        else:
            stack.push(i)
    if stack.isEmpty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"

balance_var = '[([])((([[[]]])))]{()}'
not_balace_var = '((}{[]}}}]])))(((([}[{}}]{])()()'
print(p_balance(balance_var))
print(p_balance(not_balace_var))