from threading import Lock, Thread


class SingletonMeta(type):
    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """we will lock instance initialization so it would not create many instances in multiple threads"""
        with Lock():
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Connection(metaclass=SingletonMeta):
    def __init__(self, url: str) -> None:
        self.url = url


def test_singleton(url: str) -> None:
    singleton = Connection(url)
    print(singleton.url)


if __name__ == "__main__":
    print("If you see the sa rent values, "
          "then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")

    thread1 = Thread(target=test_singleton, args=("con://name:pass",))
    thread2 = Thread(target=test_singleton, args=("con://wow:omg",))
    thread1.start()
    thread2.start()
