def print_operation(num1, num2, operation, ret=False):
    """
    num1: first input number as a string
    num2: second input number as a string
    operation: an arithmetic operation as a string
               one of +, -, *, or /

    applies the operation to num1 and num2 and
    returns the result as a String if ret is True,
    prints it otherwise
    """
    ##################################
    ### START OF YOUR CODE: Part 1 ###
    ##################################
    if operation not in ["+", "-", "*", "/"]:
        raise ValueError("Unknown operation.")

    try:
        a, b = float(num1), float(num2)
    except ValueError:
        raise ValueError("Cannot convert to a number.")

    if operation == "/":
        assert b != 0, "Cannot divide by zero."

    res = 0
    try:
        if operation == "+":
            res = a + b
        elif operation == "-":
            res = a - b
        elif operation == "*":
            res = a * b
        elif operation == "/":
            res = a / b
    except Exception as e:
        raise Exception("An error occurred: " + str(e))

    if ret:
        return str(res)
    else:
        print(str(int(a)) + " " + operation + " " + str(int(b)) + " = " + str(int(res)))

    ##################################
    ### END OF YOUR CODE: Part 1 #####
    ##################################


if __name__ == "__main__":
    # test your solutions

    print_operation("5", "2", "+")  # should print "5 + 2 = 7"
    print_operation("3", "4", "-")  # should print "3 - 4 = -1"
    print_operation("4", "2", "*")  # should print "4 * 2 = 8"
    print_operation("6", "3", "/")  # should print "6 / 3 = 2"
    print_operation("1a", "2", "+")  # should throw "Cannot convert to a number."
    print_operation("1", "bc", "*")  # should throw "Cannot convert to a number."
    print_operation("4", "0", "/")  # should throw "Cannot divide by zero."
    print_operation("4", "0", "%")  # should assert "Unknown operation."

    print("\n====================================\n")
