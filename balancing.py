from main import Stack


def balance(s):
    stack = Stack()
    correct = {'(': ')', '{': '}', '[': ']'}

    for item in s:
        for key, value in correct.items():
            if item in key:
                stack.push(item)
            elif item in value:
                if stack.isEmpty() or key[value.index(item)] != stack.peek():
                    return 'Не сбалансировано'
                stack.pop()

    return 'Не сбалансировано' if stack.size() != 0 else 'сбалансировано'


if __name__ == '__main__':
    print(balance('[([])((([[[]]])))]{()}'))
    print(balance('(((([{}]))))'))
    print(balance('{{[(])]}}'))
    print(balance('}{}'))
