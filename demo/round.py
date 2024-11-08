def vir_fib(n):
    i = 0
    curr_num = 0
    next_num = 1
    while i < n:
        tmp = next_num
        next_num = curr_num + next_num
        curr_num = tmp
        i += 1

    return curr_num


def vir_fib2(n):

    def vir_fib_helper(i, curr_num, next_num):
        if i >= n:
            return curr_num
        else:
            return vir_fib_helper(i+1, next_num, curr_num+next_num)

    return vir_fib_helper(0,0,1)
