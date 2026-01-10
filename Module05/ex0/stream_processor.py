from abc import ABC, abstractmethod
from typing import Any


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
        """Regular method that will be overriding"""
        print(f"Output: Processed {result}")


# Specific NumricProcessor class that override the base methods
class NumericProcessor(DataProcessor):
    """Demonstrate the processing and validation of a numeric data"""

    def __init__(self) -> None:
        """"""
        print("Initializing Numeric Processor...")

    # Processing an integers data
    def process(self, data: Any) -> str:
        """Process a specify list of data"""

        return (f"Processing data: {data}")

    # Validate that data is integers, else raise error
    def validate(self, data: Any) -> bool:
        """Validate numeric data"""
        if data is None:
            return False
        for item in data:
            try:
                item - 0
            except TypeError:
                return False
        return True

    # Print process result
    def format_output(self, result: str) -> str:
        """Format the result and return it."""
        return f"Output: {result}"


# Specific TextProcessor class that override the base methods
class TextProcessor(DataProcessor):
    """Demonstrate the processing and validation of a text data"""

    def __init__(self) -> None:
        """Start and Initializing the text processor"""

        print("Initializing Text Processor...")

    # Processing a and return string data
    def process(self, data: Any) -> str:
        return (f'Processing data: "{data}"')

    def validate(self, data: Any) -> bool:
        """Check if no data provider, or if data is not
        string"""
        if data is None or data.__class__ is not str:
            return False
        return True

    def format_output(self, result: str) -> str:
        """Return a processing string"""

        return f"Output: {result}"


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

    # A helper function to calculate the words count
    def count_word(string: str):
        inside_word: int = 0
        count: int = 0
        for char in string:
            if char != " ":
                if not inside_word:
                    count += 1
                    inside_word: int = 1
            else:
                inside_word = 0
        return count

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
    test_numeric_processor()
    print("")
    test_text_processor()
    print("")
    test_log_processor()

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")



demonstrate_abstraction()
