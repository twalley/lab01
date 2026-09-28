import sys
from argparse import ArgumentParser
from . import calculator as calculator
from . import converter as converter

def calculat(args):
    try:
        result = calculator.calculate(args.expression)
        print(result)
    except Exception as err:
        print(f"Ошибка калькулятора: {err}")

def convertat(args):
    try:
        result = converter.convert(args.value, args.from_unit, args.to_unit)
        print(result)
    except Exception as err:
        print(f"Ошибка конвертера: {err}")

def main():
    parser = ArgumentParser(prog='toolkit')
    subPhrases = parser.add_subparsers(dest='command', help='доступные команды')
    
    # настройка команды 'calc'
    calc = subPhrases.add_parser('calculator', help='калькулятор')
    calc.add_argument('expression', type=str, help='выражение')
    calc.set_defaults(func=calculat)

    # настройка команды 'convert'
    conv = subPhrases.add_parser('converter', help='конвертер величин')
    conv.add_argument('value', type=float, help='значение для конвертации')
    conv.add_argument('--from', dest='from_unit', type=str, required=True, help='исходная единица')
    conv.add_argument('--to', dest='to_unit', type=str, required=True, help='целевая единица')
    conv.set_defaults(func=convertat)

    args = parser.parse_args()
    
    # проверяем, выбрана ли подкоманда (calc или convert)
    if hasattr(args, 'func'):
        args.func(args)
    else:
        # если запущено без аргументов, выводим help
        parser.print_help()

if __name__ == '__main__':
    main()
# нужно прописать в консоль source .venv/bin/activate для мака, .venv\Scripts\activate для винды
# чтобы запустить ввод с клавиатуры python -m toolkit calculator "выражение", python -m toolkit converter число --from от куда --to куда