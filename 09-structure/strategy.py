# Version 1

class Analyzer:
    # The base class has some shared functionality e.g. reading data
    def __init__(self):
        self.data = []
        self.processed = []

    def read_data(self, filename):
        # Read some data from the file here
        # self.data = ...
        pass

    def analyze(self):
        raise NotImplementedError

# The subclasses customize the behaviour of the base class:

class DirectAnalyzer(Analyzer):
    def analyze(self):
        # Implement the Direct Analysis™ algorithm
        print("Running Direct Analysis™")
        # self.processed = ...

class ReverseAnalyzer(Analyzer):
    def analyze(self):
        # Implement the Reverse Analysis™ algorithm
        print("Running Reverse Analysis™")
        # self.processed = ...


my_analyzer = ReverseAnalyzer()
my_analyzer.read_data("my_data.csv")
my_analyzer.analyze()


#########


# Version 2

class Analyzer:
    # This class has some functionality for e.g. reading data
    # but delegates the actual analysis (algorithm) to a different class
    def __init__(self, algorithm):
        self.data = []
        self.processed = []
        self.algorithm = algorithm

    def read_data(self, filename):
        # Read some data from the file here
        # self.data = ...
        pass

    def analyze(self):
        self.processed = self.algorithm.run(self.data)


class Algorithm:
    # The base algorithm does not process the data
    def run(self, data):
        return data
        # or maybe raises an error!


class DirectAlgorithm(Algorithm):
    def run(self, data):
        # Run the Direct Analysis™ algorithm on the data
        print("Running Direct Analysis™")
        # return ...

class ReverseAlgorithm(Algorithm):
    def run(self, data):
        # Run the Reverse Analysis™ algorithm on the data
        print("Running Reverse Analysis™")
        # return ...


my_algorithm = ReverseAlgorithm()
my_analyzer = Analyzer(my_algorithm)
my_analyzer.read_data("my_data.csv")
my_analyzer.analyze()
