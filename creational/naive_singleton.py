class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Connection(metaclass=SingletonMeta):
    def ping(self) -> None:
        print("This method checks the connection stability")


if __name__ == "__main__":
    s1 = Connection()
    s2 = Connection()

    if id(s1) == id(s2):
        print("Connection works, both variables contain the same instance.")
    else:
        print("Connection failed, variables contain different instances.")
    s1.ping()
    s2.ping()
