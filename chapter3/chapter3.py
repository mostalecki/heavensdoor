def check_non_descending(num):
    # Check if digits are in non-descending order
    if num != ''.join(sorted(num)):
        return False
    return True


def check_pairs(num):
    # Return true if there are at least two groups
    # of identical adjacent digits in the number
    digit_pairs = ['22', '33', '44', '55', '66', '77', '88', '99']
    group_counter = 0
    for pair in digit_pairs:
        if pair in num:
            # 3 is the max number of pairs since
            # numbers in this range are 6 digit
            num = num.replace(pair, '', 3)
            group_counter += 1
        if group_counter > 1:
            return True
    return False


if __name__ == '__main__':
    # The range we check is (372**2, 809**2) as stated in point 3
    nums = list(map(str, range(372**2, 809**2 + 1)))

    # First we filter numbers for those with non-descending order
    # as it is faster to check than the other condition, and rules out
    # vast majority of numbers
    non_descending_nums = list(filter(check_non_descending, nums))

    # Next we check which of the remaining numbers contain at least
    # two groups of identical adjacent digits
    final_nums = list(filter(check_pairs, non_descending_nums))

    print(f'{len(final_nums)} numbers meet the given criteria')

    if input('Print numbers? (y/n): ') == 'y':
        print(final_nums)
