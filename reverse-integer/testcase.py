from main import Solution


solution = Solution()
print(solution.reverse_integer(123))        # 321
print(solution.reverse_integer(-123))       # -321
print(solution.reverse_integer(120))        # 21
print(solution.reverse_integer(0))          # 0
print(solution.reverse_integer(1534236469)) # 0 (overflow)
print(solution.reverse_integer(-1200))      # -21
print(solution.reverse_integer(100))        # 1