# def evalRPN(tokens) -> int:
#     stack = []
    
#     for c in tokens:
#         if c.isdigit() or (len(c) > 1 and c[0] == '-' and c[1:].isdigit()):
#             stack.append(c)
#         else:
#             s1 = stack.pop()
#             s2 = stack.pop()
#             stack.append(int(eval(f"{s2}{c}{s1}")))
    
#     return stack[-1]

# inp = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

# print(evalRPN(inp))

# def findDuplicate(nums) -> int:
#     left = 1
#     right = len(nums) - 1
#     while left != right:
#         mid = (left + right) >> 1
#         print(mid, left, right)
#         counter = 0
#         for i in nums:
#             if i <= mid:
#                 counter += 1
#         if counter > mid:
#             right = mid
#             # mid = (mid + 1) >> 1
#         elif left == mid:
#                 return right
#         else:
#             left = mid
#             # mid = (mid + n) >> 1
    
#     return (left + right) >> 1

# findDuplicate([1,2,3,3,4,5])
