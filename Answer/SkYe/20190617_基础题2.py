raw_string = input(">>")
sub_string = input(">>")
steps = len(sub_string)
times = 0
for n in range(len(raw_string)):
    if n+steps > len(raw_string):
        break
    else:
        if sub_string == raw_string[n:n+steps]:
            times += 1
print(">>{}".format(times))
