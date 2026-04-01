def shume_nr_qift():
    total =0
    for number in range(1,10):
        if number % 2 == 0:
            total = total + number
    return total

print(shume_nr_qift())