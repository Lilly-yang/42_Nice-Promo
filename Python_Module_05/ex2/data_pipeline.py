import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        super().__init__()
        self.new_data: list[tuple[int, str]] = []
        self.rank = 0

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
        # print(f" Trying to validate input '{data}': ", end="")
        if isinstance(data, (int, float)):
            # print(True)
            return True
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    # print(False)
                    return False
            # print(True)
            return True
        else:
            # print(False)
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if isinstance(data, (int, float)):
            # print(f" Processing data: {data}")
            self.new_data.append((self.rank, str(data)))
            self.rank += 1
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    print(" Got exception: Improper numeric data")
                    return None
            # print(f" Processing data: {data}")
            for item in data:
                self.new_data.append((self.rank, str(item)))
                self.rank += 1
        else:
            print(" Got exception: Improper numeric data")
            return None


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        # print(f" Trying to validate input '{data}': ", end="")
        if isinstance(data, str):
            # print(True)
            return True
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    # print(False)
                    return False
            # print(True)
            return True
        else:
            # print(False)
            return False

    def ingest(self, data: str | list[str]) -> None:
        if isinstance(data, str):
            # print(f" Processing data: {data}")
            self.new_data.append((self.rank, data))
            self.rank += 1
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    print(" Got exception: Improper numeric data")
                    return None
            # print(f" Processing data: {data}")
            for item in data:
                self.new_data.append((self.rank, item))
                self.rank += 1
        else:
            print(" Got exception: Improper numeric data")
            return None


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        # print(f" Trying to validate input '{data}': ", end="")
        if isinstance(data, dict):
            for k, v in data.items():
                if not isinstance(k, str) or not isinstance(v, str):
                    # print(False)
                    return False
            # print(True)
            return True
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    for k, v in item.items():
                        if not isinstance(k, str) or not isinstance(v, str):
                            # print(False)
                            return False
                else:
                    # print(False)
                    return False
            # print(True)
            return True
        else:
            # print(False)
            return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if isinstance(data, dict):
            for k, v in data.items():
                if not isinstance(k, str) or not isinstance(v, str):
                    print(" Got exception: Improper numeric data")
                    return None
            # print(f" Processing data: {data}")
            values = [v for v in data.values()]
            self.new_data.append((self.rank, ": ".join(values)))
            self.rank += 1
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    for k, v in item.items():
                        if not isinstance(k, str) or not isinstance(v, str):
                            print(" Got exception: Improper numeric data")
                            return None
                else:
                    print(" Got exception: Improper numeric data")
                    return None
            # print(f" Processing data: {data}")
            for item in data:
                values = [v for v in item.values()]
                self.new_data.append((self.rank, ": ".join(values)))
                self.rank += 1
        else:
            print(" Got exception: Improper numeric data")
            return None


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        data_list = [item[-1] for item in data]
        print(f"{','.join(data_list)}")


class JSONExportPlugin(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output")
        data_dict = {}
        for item in data:
            data_dict['item_'+str(item[0])] = item[-1]
        print(data_dict)


class DataStream():
    def __init__(self) -> None:
        print("Initialize Data Stream...")
        self.processors: dict[str, DataProcessor] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        name = type(proc).__name__.replace("Processor", "")
        self.processors[name] = proc

    def process_stream(self, stream: list[typing.Any]) -> None:
        # self.on_processor = []
        for item in stream:
            valid = 0
            for processor in self.processors.values():
                if processor.validate(item):
                    valid = 1
                    processor.ingest(item)
                    break
            if not valid:
                print("DataStream error - "
                      f"Can't process element in stream: {item}")
                # self.on_processor.append(item)

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if len(self.processors):
            for name, processor in self.processors.items():
                print(f"{name} Processor: "
                      f"total {processor.rank} items processed, "
                      f"remaining {len(processor.new_data)} on processor")
        else:
            print("No processor found, no data")
        print("")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors.values():
            data_list = []
            for _ in range(nb):
                try:
                    data_list.append(processor.output())
                except Exception:
                    pass
            plugin.process_output(data_list)


data_batch_1 = ['Hello world',
                [3.14, -1, 2.71],
                [{'log_level': 'WARNING',
                  'log_message': 'Telnet access! Use ssh instead'},
                 {'log_level': 'INFO', 'log_message': 'User wil isconnected'}],
                42,
                ['Hi', 'five']]
data_batch_2 = [21,
                ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
                [{'log_level': 'ERROR', 'log_message': '500 server crash'},
                 {'log_level': 'NOTICE',
                  'log_message': 'Certificateexpires in 10 days'}],
                [32, 42, 64, 84, 128, 168],
                'World hello']


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")

    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("Registering Processors")
    data_stream.register_processor(NumericProcessor())
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())

    print(f"\nSend first batch of data on stream: {data_batch_1}")
    data_stream.process_stream(data_batch_1)
    data_stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, CSVExportPlugin())
    data_stream.print_processors_stats()

    print(f"Send another batch of data: {data_batch_2}")
    data_stream.process_stream(data_batch_2)
    data_stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, JSONExportPlugin())
    data_stream.print_processors_stats()
