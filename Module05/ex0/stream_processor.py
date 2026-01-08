class DataProcessor():
    """Base class"""


class NumericProcessor():
    def process(self, data: Any) -> str
    def validate(self, data: Any) -> bool
    def format_output(self, result: str) -> str

class TextProcessor():
    def process(self, data: Any) -> str
    def validate(self, data: Any) -> boo
    def format_output(self, result: str) -> str

class LogProcessor():
    def process(self, data: Any) -> str
    def validate(self, data: Any) -> boo
    def format_output(self, result: str) -> str


