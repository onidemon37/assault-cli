from typing import List, Dict

class Results:
    """
    Results handles calculating statistics based on a list of requests that were made
    Here's an example of what information will look like:
    
    Successful requests   500
    Slowest               0.010s
    Fastest               0.001s
    Average               0.003s
    Total Time            0.620s
    Requests Per Minute   4836
    Requests Per Second   80
    """
    
    def __init__(self, total_time: float, requests: List[Dict]):
        self.total_time = total_time
        self.requests = requests
    
    def slowest(self) -> float:
        """
        Returns the slowest request's completion time
        
        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4,
        ... },{
        ...     'status_code': 500,
        ...     'request_time': 6.1,
        ... },{
        ...     'status_code': 200,
        ...     'request_time': 1.04,
        ... }])
        >>> results.slowest()
        6.1
        """
        pass
    
    def fastest(self) -> float:
        """
        Returns the Fastest request's completion time
        
        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4,
        ... },{
        ...     'status_code': 500,
        ...     'request_time': 6.1,
        ... },{
        ...     'status_code': 200,
        ...     'request_time': 1.04,
        ... }])
        >>> results.fastest()
        1.04
        """
        pass
    
    def average_time(self) -> float:
        """
        Returns the  average_time's completion time
        
        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4,
        ... },{
        ...     'status_code': 500,
        ...     'request_time': 6.1,
        ... },{
        ...     'status_code': 200,
        ...     'request_time': 1.04,
        ... }])
        >>> results.average_time()
        9.846666667
        """
        pass
    
    def total_time(self) -> float:
        pass
    
    def successful_requests(self) -> int:
        """
        Returns the number of successful_requests's
        
        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4,
        ... },{
        ...     'status_code': 500,
        ...     'request_time': 6.1,
        ... },{
        ...     'status_code': 200,
        ...     'request_time': 1.04,
        ... }])
        >>> results.successful_requests()
        2
        """
        pass
