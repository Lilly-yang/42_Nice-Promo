import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self):
        super().__init__()
        self.new_data = []

    def validate(self, data: typing.Any) -> bool:
        print(f" Trying to validate input '{data}': ", end="")
        # if isinstance(data, int | float | list[int | float] | str | list[str] | dict[str, str] | list[dict[str, str]]):
        #     print(True)
        #     return True
        # else:
        #     print(False)
        #     return False

    def ingest(self, data: typing.Any) -> None:
        if isinstance(data, int | float | list[int | float] | str | list[str] | dict[str, str] | list[dict[str, str]]):
            print(f"Processing data: {data}")
        else:
            print("Got exception: Improper numeric data")
            return False
        # try:
        #     if isinstance(data, int | float | str):
        #         self.new_data.append([str(data)])
        #     elif isinstance(data, list[int | float] | list[str]):
        #         self.new_data.append([str(i) for i in data])
        #     elif isinstance(data, dict[str, str]):
        #         self.new_data.append([k + ":" + v for k, v in data.items()])
        #     elif isinstance(data, list[dict[str, str]]):
        #         for d in data:
        #             self.new_data.append([k + ":" + v for k, v in d.items()])
        #     else:
        #         raise ValueError("Invalide data dype!")
        # except Exception as e:
        #     print(f"e")
        #     return False

    def output(self) -> tuple[int, str]:
        if len(self.new_data):
            oldest_data = self.new_data.pop(0)
            return oldest_data
        else:
            print("No more data.")
            return None


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        super().validate(data)
        if isinstance(data, int | float | list[int | float]):
            print(True)
            return True
        else:
            return(True)
            return False
        
    def ingest(self, data: int | float | list[int | float]) -> None:
        super().ingest(data)
        try:
            if isinstance(data, int | float):
                self.new_data.append([str(data)])
                return True
            elif isinstance(data, list[int | float]):
                self.new_data.append([str(i) for i in data])
                return True
            else:
                raise ValueError("Invalide data dype!")
        except Exception as e:
            print("Got exception: Improper numeric data")
            return False


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        super().validate(data)
        if isinstance(data, str | list[str]):
            print(True)
            return True
        else:
            print(False)
            return False
        
    def ingest(self, data: str | list[str]) -> None:
        super().ingest(data)
        try:
            if isinstance(data, str):
                self.new_data.append([data])
                return True
            elif isinstance(data, list[str]):
                self.new_data.append(data)
                return True
            else:
                raise ValueError("Invalide data dype!")
        except:
            print(f"e")
            return False

class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        super().validate(data)
        if isinstance(data, dict[str, str] | list[dict[str, str]]):
            print(True)
            return True
        else:
            print(False)
            return False
        
    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        super().ingest(data)
        try:
            if isinstance(data, dict[str, str]):
                self.new_data.append([k + ":" + v for k, v in data.items()])
                return True
            elif isinstance(data, list[dict[str, str]]):
                for d in data:
                    self.new_data.append([k + ":" + v for k, v in d.items()])
                return True
            else:
                raise ValueError("Invalide data dype!")
        except:
            print(f"e")
            return False


numbers = []
strings = []
dicts = []


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    print("Testing Numeric Processor...")
    number_processor = NumericProcessor()
    number_processor.validate('42')
    number_processor.validate('Hello')

    print(" Test invalid ingestion of string 'foo' without prior validation:")
    number_processor.ingest('foo')

    number_processor.ingest( [1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(3):
        print(f"Numeric value {i}: ", end="")
        number_processor.output()

    string_processor = TextProcessor()
    dict_processor = LogProcessor()


    ## test validate method with valid and invalid data
    # test NumericProcessor validate method

    # test TextProcessor validate method

    # test LogProcessor validate method


    ## test ingest method with invalid data
    # test NumericProcessor ingest method

    # test TextProcessor ingest method

    # test LogProcessor ingest method


    ## ingest and output various data
    # test NumericProcessor

    # test TextProcessor

    # test LogProcessor



