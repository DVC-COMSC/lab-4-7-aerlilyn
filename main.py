def main():
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """

    previous_value = int(input('Enter an integer value: '))
    numbers.append(previous_value)

    while True:
        current_value = int(input('Enter the next integer value: '))
        if current_value >= previous_value:
            break
        numbers.append(current_value)
        previous_value = current_value

    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
