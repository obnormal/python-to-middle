from abc import abstractmethod


class ArithmeticOperation:

    def __init__(self, handler=None):
        """
            Инициализация класса
        :param handler: следующий обработчик в цепочке
        """
        self._next_handler = handler

    @abstractmethod
    def calculate(self, operation: str) -> int:
        """
            Расчет результата вычислительной операции
            :param operation: операция записанная в виде строки
            :return: целочисленный результат
        """
        pass


class MinusOperation(ArithmeticOperation):
    """Операция вычитания"""

    def calculate(self, expression):
        operands = expression.split('-')

        if len(operands) == 2:
            left_operand, right_operand = map(int, operands)
            result = left_operand - right_operand
        else:
            result = self._next_handler.calculate(expression)

        return result


class PlusOperation(ArithmeticOperation):
    """Операция сложения"""

    def calculate(self, expression):
        operands = expression.split('+')

        if len(operands) == 2:
            left_operand, right_operand = map(int, operands)
            result = left_operand + right_operand
        else:
            result = self._next_handler.calculate(expression)

        return result


class DevideOperation(ArithmeticOperation):
    """Операция деления"""

    def calculate(self, expression):
        operands = expression.split('/')

        if len(operands) == 2:
            left_operand, right_operand = map(int, operands)
            result = left_operand / right_operand
        else:
            result = self._next_handler.calculate(expression)

        return result


class MultiplyOperation(ArithmeticOperation):
    """Операция умножения"""

    def calculate(self, expression):
        operands = expression.split('*')

        if len(operands) == 2:
            left_operand, right_operand = map(int, operands)
            result = left_operand * right_operand
        else:
            result = self._next_handler.calculate(expression)

        return result
