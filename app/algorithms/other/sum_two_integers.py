def sum(a: int, b: int):
    """ Sums two integers.

    Restriction: you are not allowed to use the operator + and -

    Example: 5 + 6

        a= 0101
        b= 0110

        - First iteration
        carry = (a&b) << 1 = 1000
        a = a^b = 0011
        b = carry = 1000

        - Second iteration
        carry = (a&b) << 1 = 0000
        a = a^b = 1011
        b = carry = 0000

    """


    carry = -1

    while carry != 0:
        # If two bits are 1, they will sum 10, so we have to shift by one
        carry = (a & b) << 1

        # Sum the bits that do not imply a carry
        a = a ^ b

        # Add the carry
        b = carry


    return a
