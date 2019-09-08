# James Morrissey
# computingID: jpm9rk


def mean(a, b, c):
    the_mean = (a + b + c)/3
    return the_mean


def median(a, b, c):

    maximum = a  # initialize max to a
    minimum = a
    if b > a:   # denote the max as b if a > b
        maximum = b
    if c > maximum:
        maximum = c
    if b < a:   # denote the max as b if a > b
        minimum = b
    if c < minimum:
        minimum = c
    print(maximum,minimum)
    if a > minimum and a < maximum:
        return a
    if b > minimum and b < maximum:
        return b
    if c >= minimum and c <= maximum:
        return c


def rms(a, b, c):
    square_a = a**2
    square_b = b**2
    square_c = c**2
    square_mean = mean(square_a, square_b, square_c)
    rms_value = square_mean**0.5
    return rms_value

def middle_average(a, b, c):
    a_mean = mean(a, b, c)
    a_median = median(a, b, c)
    a_rms = rms(a, b, c)
    three_avg_median = median(a_mean, a_rms, a_median)
    return three_avg_median







