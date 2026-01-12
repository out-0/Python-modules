from abc import ABC, abstractmethod
from typing import List, Any, Dict, Union, Optional


# Base abstract class which the parent for the
# specialized streams below.
class DataStream(ABC):
    """Abstract class for data streaming"""

    def __init__(self):
        """A Constructor for storing a default batch
        data so can be used in the normal methods below
        if not overrided"""
        # counter to use in the default get_status method
        # if not overrided
        self.element_count_processed: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """An Abstract method to process a batch of data"""
        pass

    # Default method that can overrided
    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None
                    ) -> List[Any]:
        """A default data filtering that will be overriding"""
        return data_batch

    # Default method that can overrided
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return a default statistics"""

        return {"Data Proceded: ": self.element_count_processed}


# A Boss class that show the demonstration of polymorphism
# with processing a minimal status about all specialized
# classes processing.
class StreamProcessor:
    """Structuring a minimal result
    about sharing the same interface
    between the specialized stream systems."""

    def __init__(self, stream_systems: List[DataStream]) -> None:
        """Initializer"""
        self.stream_systems: List[DataStream] = stream_systems

    def process_all(self, systems_data: List[List]) -> str:
        """Process data for all systems"""

        systems_count: int = systems_data.__len__()
        stream_systems: List = self.stream_systems
        i: int = 0
        # Loop trough stream systems and pass the data provided
        # to the system by its process_batch method, even if its
        # not printed we got the element_count_processed in the system ocject.
        while i < systems_count:
            stream_systems[i].process_batch(systems_data[i])
            i += 1

        i: int = 0
        # get the type of data based on its the class of sytem.
        # for structure the formate demo.
        while i < systems_count:
            if isinstance(stream_systems[i], SensorStream):
                system_type: str = "SensorStream"
                element_count: int = stream_systems[i].element_count_processed
                print(f"- {system_type}: {element_count} readings processed")
            elif isinstance(stream_systems[i], TransactionStream):
                system_type: str = "TransactionStream"
                element_count: int = stream_systems[i].element_count_processed
                print(f"- {system_type}: {element_count} operations processed")
            elif isinstance(stream_systems[i], EventStream):
                system_type: str = "EventStream"
                element_count: int = stream_systems[i].element_count_processed
                print(f"- {system_type}: {element_count} events processed")
            i += 1


# ###################Sensor stream ################################
class SensorStream(DataStream):
    """Specialized Sensor detector that overriding the
    base structure and handle a specific kind of data"""

    def __init__(self, stream_id: str) -> None:
        """Sensor constructor that notify
        initialization and print id"""

        # Use the base method and update
        super().__init__()
        self.stream_id: str = stream_id
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Environmental Data")

    # the overrided abstractmethod
    # that process and format the data provided.
    def process_batch(self, data_batch: List[Any]) -> str:
        """Processing a data"""

        # Count the total elements that processed
        # and override the default 0 count.
        self.element_count_processed: int = data_batch.__len__()

        try:
            # Format manually instead of join since not authorized
            formatted: str = "["
            for item in data_batch:
                for k in item:
                    formatted += f"{k}:{item[k]}, "
            formatted: str = formatted[:-2] + "]"  # Remove last part ", "
        except Exception:
            print("Error: check the data entered, offten must be dictionary.")

        # Extracting the temps since the most important in
        # a sensor logic, and store them so can calculate
        # the average later in get_status.
        self.temps_list: List = []
        for dic in data_batch:
            for key in dic:
                if key == "temp":
                    # Assign the value into the self to be used later.
                    self.temps_list.append(dic[key])

        return f"Processing sensor batch: {formatted}"

    # Overrided the default method to specify the formatting.
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistic,
        Overrided version of get status"""
        # Get the element processed
        processed_count: int = self.element_count_processed
        total_temps_count: int = self.temps_list.__len__()
        average: float = 0
        for temp in self.temps_list:
            average += temp
        try:
            # get average of the temps if multiple.
            average: int = average / total_temps_count
        except ZeroDivisionError:
            print("Error: some temps have 0 value")

        return {
            "Sensor analysis: ": f"{processed_count} readings processed, ",
            "avg temp: ": f"{average}°C"
            }


# ####################Transaction steam #############################
class TransactionStream(DataStream):
    """Specialized Transaction steam that interpret
    the Transaction data provided"""

    def __init__(self, stream_id: str) -> None:
        """Transaction constructor that
        initialize the stream is and print
        some info"""

        # Use the base method and update
        super().__init__()
        self.stream_id: str = stream_id
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Financial Data")

    # the overrided abstractmethod
    # that process and format the data provided.
    def process_batch(self, data_batch: List[Any]) -> str:
        """Processing a data"""

        # Count the total elements that processed
        # and override the default 0 count.
        self.element_count_processed: int = data_batch.__len__()
        # For safety if data not valid type
        try:
            # Manually format the dictionary to show as a list
            # format, instead of using join since not authorized
            formatted: str = "["
            for item in data_batch:
                for k in item:
                    formatted += f"{k}:{item[k]}, "
            formatted: str = formatted[:-2] + "]"  # Remove last part ", "
        except Exception:
            print("Error: check the data entered, offten must be dictionary.")

        # Extracting the net flow which is the result
        # from multi buying and selling operations
        # subtracted.
        # and store them so can print 'net flow'
        # later in get_status.
        all_buying: int = 0
        all_selling: int = 0
        for dic in data_batch:
            for key in dic:
                if key == "buy":
                    all_buying += dic[key]
                elif key == "sell":
                    all_selling += dic[key]
        # assign the net flow to self so
        # can be used in get_status
        self.units: int = all_buying - all_selling

        return f"Processing transaction batch: {formatted}"

    # Override the default method to specify the formatting.
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistic,
        Overrided version of get status"""

        # Get the element processed
        data_count: int = self.element_count_processed
        if self.units > 0:
            net_flow_string: str = f"+{self.units} units"
        elif self.units < 0:
            net_flow_string: str = f"-{self.units} units"
        else:
            # if the units is 0
            net_flow_string: str = f"{self.units} units"

        return {
            "Transaction analysis: ": f"{data_count} operations, ",
            "net flow: ": net_flow_string
            }


# ################# Even stream ###############################
class EventStream(DataStream):
    """Interpret the list of events and handle structure
    them in a good format"""

    def __init__(self, stream_id: str) -> None:
        """Event constructor that notify
        initialization the stream and print
        some info"""

        # Use the base method and update
        super().__init__()
        self.stream_id: str = stream_id
        print("Initializing Event Stream...")
        print(f"Stream ID: {self.stream_id}, Type: System Events")

    # the overrided abstractmethod
    # that process and format the data provided.
    def process_batch(self, data_batch: List[Any]) -> str:
        """Processing a data"""

        # Count the total elements that processed
        # and override the default 0 count.
        self.element_count_processed: int = data_batch.__len__()
        self.errors_count: int = 0

        try:
            # Manually format the dictionary to show as a list
            # format, instead of using join since not authorized
            # and also count errors detected for get status.
            formatted: str = "["
            for item in data_batch:
                formatted += f"{item}, "
                if item == "error":
                    self.errors_count += 1
            formatted: str = formatted[:-2] + "]"  # Remove last part ", "
        except Exception:
            print("Error: check the data entered, offten must be dictionary.")

            return f"Processing event batch: {formatted}"

    # Override the default method to specify the formatting.
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistic,
        Overrided version of get status"""

        # Get the element processed
        data_count: int = self.element_count_processed
        errors_count: int = self.errors_count

        return {
            "Event analysis: ": f"{data_count} events, ",
            f"{errors_count} error detected": ""
            }


# Main start
def test_data_stream() -> None:
    """The main entry point to demonstrate data stream"""

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("")

    # ########## Demonstrate the Sensor Stream #####################
    sensors_stream: SensorStream = SensorStream("SENSOR_001")
    sensors_data: List[Any] = [
        {"temp": 22.5},
        {"humidity": 65},
        {"pressure": 1013}
    ]
    print(sensors_stream.process_batch(sensors_data))
    # Formate the output dictionary from
    # get_status and print is as the demo string.
    status: Dict = sensors_stream.get_stats()
    for key in status:
        print(f"{key}{status[key]}", end="")
    print("")

    print("")
    # ########## Demonstrate the transaction stream ################
    transactions_stream: TransactionStream = TransactionStream("TRANS_001")
    transactions_data: List[Any] = [
        {"buy": 100},
        {"sell": 150},
        {"buy": 75},
    ]
    print(transactions_stream.process_batch(transactions_data))
    status: Dict = transactions_stream.get_stats()
    for key in status:
        print(f"{key}{status[key]}", end="")
    print("")

    print("")
    # ########### Demonstrate Events stream ####################
    events_stream: EventStream = EventStream("EVENT_001")
    # Just a normal list as showed in demo.
    events_data: List[Any] = ["login", "error", "logout"]
    print(events_stream.process_batch(events_data))
    status: dict = events_stream.get_stats()
    for key in status:
        print(f"{key}{status[key]}", end="")
    print("")

    print("")
    # ######## Dimonstrate polymorphic ##########
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print("")
    print("Batch 1 Results:")
    mother_processor: StreamProcessor = StreamProcessor([sensors_stream,
                                                        transactions_stream,
                                                        events_stream])
    all_systems_data: List[List] = [
        [{"temp": 20}, {"ressure": 1010}],  # Sensor data.
        [{"buy": 50}, {"sell": 60}, {"buy": 100}, {"sell": 400}],  # trans data
        ["login", "sudo", "logout"]  # Events data
    ]
    # Process and print the data processed and its type.
    mother_processor.process_all(all_systems_data)


test_data_stream()
