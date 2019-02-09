def prime_numbers_till(num):
    init =  [2]
    for i in range(3, num):
        is_prime = True
        for p in init:
            if i % p == 0:
                is_prime = False
        if is_prime:
            init.append(i)

    return init

# make a little change
# made another change

def main_progr():
    inp_num = input("Please enter a number to determine the dividors of: ")
    inp_num = int(inp_num)
    p_list = prime_numbers_till(math.ceil(math.sqrt(inp_num)))

