# question ----> Spy number


input_number = 1124

# add_of_all_digit = product_of_all_digit
# add_of_all_digit = 1+1+2+4 => 8
# product_of_all_digit = 1*1*2*4 => 8


def spy(num):
    num_string = str(num)
    sum_num = 0
    mul_num = 1
    for i in num_string:
        sum_num += int(i)
        mul_num *= int(i)
    
    if sum_num == mul_num:
        return f"{num} is a spy number"
    else:
        return f"{num} is not a spy number"
    
num = 1124
print(spy(num))

