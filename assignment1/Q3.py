def save_error(error, errors=None):
    # If no list is provided, create a new one
    if errors is None:
        errors = []

    errors.append(error)
    return errors
print(save_error("E1"))
print(save_error("E2"))
print(save_error("E3"))