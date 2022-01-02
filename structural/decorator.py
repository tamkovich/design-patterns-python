class BaseNotifier:
    """
    Базовый интерфейс Компонента определяет поведение, которое изменяется
    декораторами.
    """

    def operation(self) -> str:
        pass


class Notifier(BaseNotifier):
    """
    Конкретные Компоненты предоставляют реализации поведения по умолчанию. Может
    быть несколько вариаций этих классов.
    """

    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(BaseNotifier):
    """
    Базовый класс Декоратора следует тому же интерфейсу, что и другие
    компоненты. Основная цель этого класса - определить интерфейс обёртки для
    всех конкретных декораторов. Реализация кода обёртки по умолчанию может
    включать в себя поле для хранения завёрнутого компонента и средства его
    инициализации.
    """

    _component: BaseNotifier = None

    def __init__(self, component: BaseNotifier) -> None:
        self._component = component

    @property
    def component(self) -> BaseNotifier:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class SMSDecorator(Decorator):
    """
    Конкретные Декораторы вызывают обёрнутый объект и изменяют его результат
    некоторым образом.
    """

    def operation(self) -> str:
        """
        Декораторы могут вызывать родительскую реализацию операции, вместо того,
        чтобы вызвать обёрнутый объект напрямую. Такой подход упрощает
        расширение классов декораторов.
        """
        return f"SMSDecorator({self.component.operation()})"


class FacebookDecorator(Decorator):
    """
    Декораторы могут выполнять своё поведение до или после вызова обёрнутого
    объекта.
    """

    def operation(self) -> str:
        return f"FacebookDecorator({self.component.operation()})"


def client_code(component: BaseNotifier) -> None:
    """
    Клиентский код работает со всеми объектами, используя интерфейс Компонента.
    Таким образом, он остаётся независимым от конкретных классов компонентов, с
    которыми работает.
    """

    print(f"RESULT: {component.operation()}")


if __name__ == "__main__":
    simple = Notifier()
    print("Client: I've got a simple notifier:")
    client_code(simple)

    decorator1 = SMSDecorator(simple)
    decorator2 = FacebookDecorator(decorator1)
    print("Client: Now I've got a decorated notifier:")
    client_code(decorator1)
    client_code(decorator2)
