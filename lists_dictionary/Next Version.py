version = input().split(".")
join_1 = "".join(version)
int_join = int(join_1)

new_version = int_join + 1
back_to_string = list(str(new_version))
joint_2 = ".".join(back_to_string)

print(joint_2)

# data input
#  1.4.6
# 3.9.9