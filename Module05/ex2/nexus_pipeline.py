from abc import ABC, abstractmethod
from typing import Any


class ProcessingPipeline(ABC):
    """Base class for pipeline process"""
    pass


class InputStage():
    """"""

    def __init__(self) -> None:
        pass

    def process(self, data: Any) -> Any:
        """"""
        pass

class TransformStage():
    """"""

    def __init__(self) -> None:
        pass

    def process(self, data: Any) -> Any:
        """"""
        pass


class OutputStage():
    """"""

    def __init__(self) -> None:
        pass

    def process(self, data: Any) -> Any:
        """"""
        pass
