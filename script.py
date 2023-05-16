def add_binary(a, b):
    # Calculate the sum of a and b
    sum_decimal = a + b

    # Convert the sum to binary
    sum_binary = bin(sum_decimal)[2:]

    return sum_binary


# Example usage
print(add_binary(1, 1))  # Output: "10"
print(add_binary(5, 9))  # Output: "1110"
