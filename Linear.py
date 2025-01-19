def linear(t, P):
    """
    This function performs linear interpolation and extrapolation
    :param t: Table of points
    :param P: The point to be interpolated or extrapolated
    :return: result of interpolation or extrapolation
    """
    p = []
    result = 0
    flag = 1

    # Print table header
    print(f"{'f(x)':<15} | {'x':<10}")
    print("-" * 25)

    # Print all points in the table
    for x, y in t:  # Loop through the tuples in the table
        print(f"{y:<15.6f} | {x:<10}")

    # Collecting x-values from the points
    for i in range(len(t) - 1):
        x1 = t[i][0]
        x2 = t[i + 1][0]
        y1 = t[i][1]
        y2 = t[i + 1][1]

        # Check if P is between x1 and x2 for interpolation
        if x1 <= P <= x2:
            result = ((y1 - y2) / (x1 - x2)) * P + ((y2 * x1) - (y1 * x2)) / (x1 - x2)
            flag = 0
            break  # Exit loop once interpolation is done

    # Extrapolation (if no interpolation was performed)
    if flag:
        x1 = t[0][0]
        x2 = t[1][0]
        y1 = t[0][1]
        y2 = t[1][1]
        m = (y1 - y2) / (x1 - x2)
        result = y1 + m * (P - x1)

    return result