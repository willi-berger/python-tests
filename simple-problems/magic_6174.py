
def pad_with_zero(number, length=4):
    number = str(number)
    while len(number) < length:
        number = "0" + number
    return number

def re_arrange_number(number_string, highest_first=True):
    number_string = pad_with_zero(number_string)
    number_digits = list(number_string)
    number_digits.sort(reverse=highest_first)
    number_rearranged = "".join(number_digits)
    return number_rearranged;

num_0 = 1467
num_0 = pad_with_zero(num_0)
i = 0
while i < 100:
    i += 1
    num_a = re_arrange_number(num_0)
    num_b = re_arrange_number(num_0, False)
    print("*{0}\n {1}\n-{2}\n ----".format(num_0, num_a, num_b))

    num_n = pad_with_zero(str(int(num_a) - int(num_b)))
    print("=" + num_n)
    print()
    if num_n == num_0:
        break
    num_0 = num_n


