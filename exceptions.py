class Error(Exception):
    """Base class for other exceptions"""
    pass


class MatrixNotSquareError(Error):
    """Raised matrix is not NxN"""
    pass
