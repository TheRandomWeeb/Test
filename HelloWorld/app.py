def calc_decay_factor(orgin, decay_factor, times):
    answer = orgin * (decay_factor ** times)
    return answer


x_orgin = float(input("Enter Orgin: "))
x_decay1 = float(input("Enter first number: "))
x_decay2 = float(input("Enter second number: "))
x_times = float(input("Enter amount of times to calculate: "))

print(calc_decay_factor(x_orgin, x_decay1/x_decay2, x_times))