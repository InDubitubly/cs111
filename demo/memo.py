memo={0:0, 1:1}
def vir_fib_memo(n):
    if n in memo:
        return memo[n]
    else:
        answer_at_n = vir_fib_memo(n-1) + vir_fib_memo(n-2)
        memo[n] = answer_at_n
        return memo[n]
