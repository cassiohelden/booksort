class SortingServiceException(Exception):
    """
    Raises when trying to filter with null parameter
    """

    def __init__(self):
        super(SortingServiceException, self).__init__(
            'This exception occurred when view try to search for null parameter'
        )

