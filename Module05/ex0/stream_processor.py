from abc import ABC, abstractmethod
from typing import Any, Text


# A Base abstract class
class DataProcessor(ABC):
    """Base class for abstract methods"""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Abstractmethod that for process"""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Abstractmethod for validate"""
        pass

    # Normal method that can be overriding later.
    def format_output(self, result: str) -> str:
        """Regular method with default implementation
        return a string format that will be overriding"""
        return f"Output: {result}"


# Specific NumricProcessor class that override the base methods
class NumericProcessor(DataProcessor):
    """Demonstrate the processing and validation of a numeric data"""

    def __init__(self) -> None:
        """Constructor for numeric class"""
        self.count: int = 0
        self.list_sum: int = 0
        self.average: float = 0.0
        print("Initializing Numeric Processor...")

    # Processing an integers data
    def process(self, data: Any) -> str:
        """Process a specify list of data"""

        # Processing and Calculating statistics.
        count: int = 0
        list_sum: int = 0
        for item in data:
            try:
                list_sum += item
                count += 1
            except TypeError:
                print("Error: some data is not valid")
        # Assign the statistics
        self.count: int = count
        self.list_sum: int = list_sum
        if count != 0:
            self.average: float = list_sum / count
        return (f"Processing data: {data}")

    # Validate that data is integers, else raise error
    def validate(self, data: Any) -> bool:
        """Validate numeric data"""
        if data is None:
            return False
        for item in data:
            try:
                _ = item - 0
            except TypeError:
                return False
        return True

    # Print process result
    def format_output(self, result: str) -> str:
        """Format the result and return it."""
        return (f"{result} Processed {self.count} "
                f"numeric values, sum={self.list_sum} "
                f"avg={self.average}")


# Specific TextProcessor class that override the base methods
class TextProcessor(DataProcessor):
    """Demonstrate the processing and validation of a text data"""

    def __init__(self) -> None:
        """Start and Initializing the text processor"""
        self.text_len: int = 0
        self.words_count: int = 0
        print("Initializing Text Processor...")

    # A helper function to calculate the words count
    def count_word(self, text: str):
        inside_word: int = 0
        count: int = 0
        for char in text:
            if char != " ":
                if not inside_word:
                    count += 1
                    inside_word: int = 1
            else:
                inside_word: int = 0
        return count

    # Processing a and return string data
    def process(self, data: Any) -> str:
        if data:
            self.text_len: int = data.__len__()
            self.words_count: int = TextProcessor.count_word(self, data)
        return (f'Processing data: "{data}"')

    def validate(self, data: Any) -> bool:
        """Check if no data provided, or if data is not
        string"""
        if data is None or data.__class__ is not str:
            return False
        return True

    def format_output(self, result: str) -> str:
        """Return a processing string"""

        return (f"{result} Processed text: {self.text_len} "
                "characters, {self.words_count} words")


# Specific LogProcessor class that override the base methods
class LogProcessor(DataProcessor):
    """Demonstrate the processing and validation of a text data"""

    def __init__(self) -> None:
        """Initializing Log process"""
        print("Initializing Log Processor...")

    def process(self, data: Any) -> str:
        """Process the log data"""
        print(f'Processing data: "{data}"')

    def validate(self, data: Any) -> bool:
        """Validate if the log is valid string"""
        if data.__class__ == str:
            return True
        return False

    def format_output(self, result: str) -> str:
        return f"Output: {result}"
        pass


# Demonstrate a numberic processor----------------------------------------
def test_numeric_processor() -> None:
    """Demonstrating the numberic overriding"""

    # Create instance NumericProcessor
    num_proc: NumericProcessor = NumericProcessor()
    data: list = [1, 2, 3, 4, 5]
    # Processing list
    print(num_proc.process(data))
    # Validate list and return result
    if num_proc.validate(data):
        print("Validation: Numeric data verified")
    else:
        print("Error: Some numeric data is incorrect")

    # Calculate statistics.
    count: int = 0
    list_sum: int = 0
    for item in data:
        count += 1
        list_sum += item
    # Structure the result format.
    result: str = (f"Processed "
                   f"{count} numeric values, "
                   f"sum={list_sum}, avg={list_sum / count}")
    print(num_proc.format_output(result))


# Demonstrate a text processor---------------------------------------------
def test_text_processor() -> None:
    """Demonstrating the text overriding"""


    # Create instance of text processor.
    text_proc: TextProcessor = TextProcessor()
    # Process a text string
    data: str = "Hello Nexus World"
    print(text_proc.process(data))
    # Check and print result
    if text_proc.validate(data):
        print("Validation: Text data verified")
    else:
        print("Error: String data is not valid")
    # Print output format
    result: str = (f"Processed text: {data.__len__()} "
                   f"characters, {count_word(data)} words")
    print(text_proc.format_output(result))


# Demonstrate a log processor------------------------------------------------
def test_log_processor() -> None:
    """Demonstrating the log overriding"""

    # Initiate an log instance
    log_proc: LogProcessor = LogProcessor()
    # Process a log data
    data: str = "Connection timeout"
    log_proc.process(data)
    # Validate log data
    if log_proc.validate(data):
        print("Validation: Log entry verified")
    else:
        print("Error: Log entry not valid")
    # Print output format
    result = "[ALERT] ERROR level detected: Connection timeout"
    print(log_proc.format_output(result))


# test stream processor
def demonstrate_abstraction() -> None:
    """Demonstrate abstraction concept"""

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print("")
    all_process = [NumericProcessor,
                   TextProcessor,
                   LogProcessor]

    # Numeric processor------------------------
    num_proc = NumericProcessor()
    num_data: list = [1, 2, 3, 4, 5]
    print(num_proc.process(num_data))
    if num_proc.validate(num_data):
        print("Validation: Numeric data verified")
        print(num_proc.format_output("Output:"))
    else:
        print("Validation (Error): data is invalid")

    # Text processor---------------------------
    text_proc = TextProcessor()
    text_data: str = "Hello Nexus World"
    print(text_proc.process(text_data))
    if text_proc.validate(text_data):
        print("Validation: Text data verified")
        print(text_proc.format_output("Output:"))
    else:
        print("Validation (Error): data is invalid")

    print("")
    test_text_processor()
    print("")
    test_log_processor()

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")



demonstrate_abstraction()
