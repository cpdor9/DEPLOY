sample = [1, 2, 5, 6, 7]


def std_dev(sample):
    """Thiss is to calculate std dev."""
    x_bar = gmean(sample)
    tempsd = 0
    sd = 0
    for i in sample:
        tempsd += (i - x_bar)**2
    sd = (tempsd/len(sample))**0.5
    return sd


def gmean(sample):
    """Thiss is to calculate mean"""
    tempvar = 0
    for i in sample:
        tempvar += i
        means = tempvar/len(sample)
        return means

print(std_dev(sample))
