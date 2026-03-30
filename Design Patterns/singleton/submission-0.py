class Singleton:
    _unique_instance: Singleton = None

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if not cls._unique_instance:
            cls._unique_instance = super(Singleton, cls).__new__(cls)
        return cls._unique_instance

    def __init__(self):
        self._value: str

    def getValue(self) -> str:
        return self._value

    def setValue(self, value: str):
        self._value = value

