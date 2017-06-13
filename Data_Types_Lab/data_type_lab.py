def data_type(data):
    """
        Function to return different results based on different python data 
        types
    """

    # For strings
    if isinstance(data, str):
        return len(data)

    # For None
    elif data == None:
        return 'no value'

    # For Booleans
    elif isinstance(data, bool):
        return data

    # For Integers
    elif isinstance(data, int):
        if data > 100:
            return 'more than 100'
        elif data < 100:
            return 'less than 100'
        else:
            return 'equal to 100'

    # For lists
    elif isinstance(data, list):
        if len(data) >= 3:
            return data[2]
    else:
        return None
