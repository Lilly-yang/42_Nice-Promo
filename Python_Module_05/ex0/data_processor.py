import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self):
        super().__init__()
        self.new_data = []

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        oldest_data = self.new_data.pop(0)
        return oldest_data


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        print(f" Trying to validate input '{data}': ", end="")
        if isinstance(data, (int, float)):
            print(True)
            return True
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    print(False)
                    return False
            print(True)
            return True
        else:
            print(False)
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if isinstance(data, (int, float)):
            print(f" Processing data: {data}")
            self.new_data.append(str(data))
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    print(" Got exception: Improper numeric data")
                    return None
            print(f" Processing data: {data}")
            self.new_data.extend([str(item) for item in data])
        else:
            print(" Got exception: Improper numeric data")
            return None


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        print(f" Trying to validate input '{data}': ", end="")
        if isinstance(data, str):
            print(True)
            return True
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    print(False)
                    return False
            print(True)
            return True
        else:
            print(False)
            return False

    def ingest(self, data: str | list[str]) -> None:
        if isinstance(data, str):
            print(f" Processing data: {data}")
            self.new_data.append(data)
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    print(" Got exception: Improper numeric data")
                    return None
            print(f" Processing data: {data}")
            self.new_data.extend(data)
        else:
            print(" Got exception: Improper numeric data")
            return None


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        print(f" Trying to validate input '{data}': ", end="")
        if isinstance(data, dict):
            for k, v in data.items():
                if not isinstance(k, str) or not isinstance(v, str):
                    print(False)
                    return False
            print(True)
            return True
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    for k, v in item.items():
                        if not isinstance(k, str) or not isinstance(v, str):
                            print(False)
                            return False
                else:
                    print(False)
                    return False
            print(True)
            return True
        else:
            print(False)
            return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if isinstance(data, dict):
            for k, v in data.items():
                if not isinstance(k, str) or not isinstance(v, str):
                    return None
            print(f" Processing data: {data}")
            values = [v for v in data.values()]
            self.new_data.append(": ".join(values))
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    for k, v in item.items():
                        if not isinstance(k, str) or not isinstance(v, str):
                            return None
                else:
                    return None
            print(f" Processing data: {data}")
            for item in data:
                values = [v for v in item.values()]
                self.new_data.append(": ".join(values))
        else:
            print(False)
            return False


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    number_processor = NumericProcessor()
    number_processor.validate(42)
    number_processor.validate('Hello')

    print(" Test invalid ingestion of string 'foo' without prior validation:")
    number_processor.ingest('foo')

    number_processor.ingest([1, 2, 3, 4, 5])
    print(" Extracting 3 values...")
    for i in range(3):
        print(f" Numeric value {i}: {number_processor.output()}")

    print("\nTesting Text Processor...")
    string_processor = TextProcessor()
    string_processor.validate(42)
    string_processor.ingest(['Hello', 'Nexus', 'World'])
    print(" Extracting 1 values...")
    for i in range(1):
        print(f" Text value {i}: {string_processor.output()}")

    print("\nTesting Log Processor...")
    dict_processor = LogProcessor()
    dict_processor.validate('Hello')
    dict_processor.ingest([
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
        ])
    print(" Extracting 2 values...")
    for i in range(2):
        print(f" Text value {i}: {dict_processor.output()}")
