def tokenize(expression):
    #Разбиваеv строку на числа (включая отрицательные), операторы и скобки.
    tokens = []
    current_number = []
    
    # Очищаем строку от пробелов
    expression = expression.replace(" ", "")
    
    for i, char in enumerate(expression):
        # Проверяем, является ли минус знаком отрицательного числа
        if char == '-':
            # Минус относится к числу, если он первый в строке или идет после оператора/открывающей скобки
            is_unary = (i == 0) or (expression[i - 1] in '+-*/(')
            
            if is_unary:
                current_number.append(char)
                continue
        elif char == '+' and expression[i-1] in '+-*/(':
            # Если после оператора или открывающейся сколбки идёт знак плюс, то его просто убираем
            continue
        else: 
            if char in '*/' and expression[i-1] in '+-*/':
                # Если после всех предыдущих проверок есть оператор * или / перед которым любые другие операторы то кидаем ошибку последовательности операторов
                raise RuntimeError(f'Ошибка последовательности операторов')
        
        # Сборка дробного числа через .
        if char.isdigit() or char == '.':
            current_number.append(char)
        elif char in '+-*/()':
            # Если текущий символ оператор, значит число закончилось и можно его добавить в массив токенов
            if current_number:
                tokens.append(''.join(current_number))
                current_number = []
            tokens.append(char)
            # Текущий символ не является оператором, числом, скобкой или точкой -> кидаем ошибку что символ неизвестен
        else:
            raise RuntimeError(f'Ошибка - неизвестный символ')
            
    if current_number:
        tokens.append(''.join(current_number))
        
    return tokens

def is_number(token):
    # Функция проверки является ли токен числом переводом его во float
    try:
        float(token)
        return True
    except ValueError:
        return False

def infix_to_postfix(tokens):
    # Переводит токены в обратную польскую нотацию (ОПН).
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = [] # Список для итогового выражения в ОПН
    operators = [] # Стек для временного хранения операторов и скобок
    
    for token in tokens:
        if is_number(token): # Если токен это число, сразу добавляем его в список ОПН
            output.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            if operators and operators[-1] == '(':
                operators.pop()
        elif token in precedence:
            while (operators and operators[-1] in precedence and 
                   precedence[operators[-1]] >= precedence[token]):
                output.append(operators.pop())
            operators.append(token)
            
    while operators:
        output.append(operators.pop())
        
    return output

def evaluate_postfix(postfix_tokens):
    # Вычисляет выражение записанное в формате обратной польской нотации
    stack = []
    
    for token in postfix_tokens:
        if is_number(token):
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Ошибка - деление на ноль!")
                stack.append(a / b)
                
    return stack[0] if stack else 0

def calculate(expression):
    try:
        tokens = tokenize(expression)
        # print(tokens)
        postfix = infix_to_postfix(tokens)
        # print(postfix)
        result = evaluate_postfix(postfix)
        return result
    except Exception as e:
        return f"{e}"

# Примеры тестов:
if __name__ == "__main__":
    examples = [
        "2+3*4",
        "10 / 4",
        "-2 * -3",
        "1+-2",
        "2*/3",
        "2+a",
        "1/0",
        "2-+1",
        "2*(3+-4)",
        "2.34+-9*(12+1)"
    ]
    
    for ex in examples:
        print(f"Выражение: {ex} => Результат: {calculate(ex)}")
