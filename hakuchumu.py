import re
s = input()

print("YES" if re.match("^(dream|dreamer|erase|eraser)+$", s) else "NO")

# s = s.replace("eraser", "")
# s = s.replace("erase", "")
# s = s.replace("dreamer", "")
# s = s.replace("dream", "")

# if s == "":
#     print("YES")
# else:
#     print("NO")
