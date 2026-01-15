from abc import ABC, abstractmethod
from typing import Any, Union, Protocol, List


# Interface for stages using duck typing.
# Any class with process() can act as a stage.
class ProcessingStage(Protocol):
    """Stage Processing interface for stages,
    its represent how the stages must be."""

    def process() -> Any:
        """A process protocol method which will
        mark the stages, as protocol, so any
        stage that have the process its match."""
        pass


# The base for pipeline processing
class ProcessingPipeline(ABC):
    """Abstract base managing stages. Contains a list of
    stages and orchestrates data flow

    Any one that wanna use inherit from the Processing Pipeline
    must know how to create the stages and how to add more later,
    and also how to process data.

    """

    def __init__(self) -> None:
        """"""
        # Register empty list that hold the stages.
        self.stages: List = [Any]

    @abstractmethod
    def create_stages(self, stages_class: List) -> None:
        """Create a multi stages with a shared interface
        from the list passed, and return the instances created."""
        pass

    @abstractmethod
    def add_stage() -> None:
        """Add stage to the list of stages"""
        pass

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        """Abstract method that must be overrided"""
        pass



# Specialized stage that process pipeline
class InputStage:
    """"""

    def __init__(self) -> None:
        print("Input validation and parsing")

    def process(self, data: Any) -> Any:
        """"""
        pass


# Specialized stage that process pipeline
class TransformStage:
    """"""

    def __init__(self) -> None:
        print("Data transformation and enrichment")

    def process(self, data: Any) -> Any:
        """"""
        pass


# Specialized stage that process pipeline
class OutputStage:
    """"""

    def __init__(self) -> None:
        print("Output formatting and delivery")

    def process(self, data: Any) -> Any:
        """"""
        pass


# A type of adapters
class JSONAdapter(ProcessingPipeline):
    """Adapter for json data,
    that based on the pipeline processing base."""

    def __init__(self, pipeline_id: int) -> None:
        """"""
        self.pipeline_id = pipeline_id
        pass

    # Overrited process for each specialized adapter
    def process(self, data: Any) -> Union[str, Any]:
        """"""
        pass


# A type of adapters
class CSVAdapter():
    """"""

    def __inti__(self, pipeline_id: int) -> None:
        """"""
        self.pipeline_id = pipeline_id

    # Overrited process for each specialized adapter
    def process(self, data: Any) -> Union[str, Any]:
        """"""
        pass


# A type of adapters
class StreamAdapter:
    """"""

    def __init__(self, pipeline_id: int) -> None:
        """"""
        self.pipeline_id = pipeline_id

    # Overrited process for each specialized adapter
    def process(self, data: Any) -> Union[str, Any]:
        """"""
        pass


class NexusManager(ProcessingPipeline):
    """Manager that orchestrating multiple pipelines"""

    def __init__(self) -> None:
        """Constructor for the manager
        Its initialize the stages from parent,
        Create a pipeline capacity"""

        super().__init__()
        self.pipeline_capacity: int = 1000

        print("Initializing Nexus Manager...")
        print(f"Pipeline capacity: {self.pipeline_capacity} streams/second")

    # Create a list of stages.
    def create_stages(self, stages_class: List) -> None:
        """Create a multi stages with a shared interface
        from the list passed, and return the instances created."""

        i: int = 1
        for stage_class in stages_class:
            print(f"stage {i} :", end="")
            # Append the instance created.
            self.stages.append(stage_class())
            i += 1
        return self.stages

    def add_stage(self, stage_type: ProcessingStage) -> None:
        pass

    # Create the multi staring pipelines
    def create_pipelines() -> None:
        """""Create the multi staring pipelines
        which the tree stages:
            InputStage;
            TransformStage;
            OutputStage;
        """
        pass



# Main staring point
def main() -> None:
    """main starting point to structure the flow"""

    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("")
    # Create the boss that handle all the pipes and
    # data flow
    nexus_boss: NexusManager = NexusManager()

    # Create the pipelines that will process the data trough.
    print("")
    print("Creating Data Processing Pipeline...")
    stages_class: List = [InputStage, TransformStage, OutputStage]
    nexus_boss.create_stages(stages_class)


    print("=== Multi-Format Data Processing ===")
    print("")
    print("Processing JSON data through pipeline...")





main()
