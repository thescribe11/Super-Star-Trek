def create_array(rows, cols, value=0) -> list:
    """ method to create 2D array of identical items """
    return [[value for c in range(cols)] for r in range(rows)]