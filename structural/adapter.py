class CoreSystem:
    def get_data(self) -> str:
        return "Target: The default target's behavior."


class XMLToJSONAdaptee:
    """
    Адаптируемый класс содержит некоторое полезное поведение, но его интерфейс
    несовместим с существующим клиентским кодом. Адаптируемый класс нуждается в
    некоторой доработке, прежде чем клиентский код сможет его использовать.
    """

    def get_converted_to_json_data(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class XMLToJSONAdapter(CoreSystem, XMLToJSONAdaptee):
    """
    Адаптер делает интерфейс Адаптируемого класса совместимым с целевым
    интерфейсом благодаря множественному наследованию.
    """

    def get_data(self) -> str:
        return f"Adapter: (TRANSLATED) {self.get_converted_to_json_data()[::-1]}"


def client_code(target: "CoreSystem") -> None:
    """
    Клиентский код поддерживает все классы, использующие интерфейс Target.
    """

    print(target.get_data(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = CoreSystem()
    client_code(target)
    print("\n")

    adaptee = XMLToJSONAdaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.get_converted_to_json_data()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = XMLToJSONAdapter()
    client_code(adapter)
