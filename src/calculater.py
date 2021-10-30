class Calculate:
    @staticmethod
    def sum(x: float, y: float) -> float:
        return x + y

    @staticmethod
    def division(x: float, y: float) -> float:
        return x / y


if __name__ == "__main__":
    print(Calculate.sum(30, 30))
    result = Calculate.sum(30, 30)
    print(f'{Calculate.division(result, 10):.2f}')
