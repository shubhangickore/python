# a=b=c=70
# print(f"a={a},b={b},c={c}")
# ax,bx,cx=50,20,3.5
# print(f"ax={ax}, bx={bx},cx={cx}")

# print(f"Addition={a+b}")
# print(f"substraction={a-b}")
# print(f"multiplication={a*b}")
# print(f"division={a/b}")
# print(f"modulo={a%b}")

set_var={44,88,22}
print(f"Type of set_var = {type(set_var)}")
set_var.add(5)
set_var.discard(88)
union_set=set_var.union({44,22,66})
set_diffrence = set_var.diffrence(union_set)
print(f"SET DIFF IS :{set_diffrence}")
