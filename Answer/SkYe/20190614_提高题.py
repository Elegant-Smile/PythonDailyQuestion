num_list=eval(input())#[1,5,1,2,7,3]
count_list = {}
for num in num_list:
    count_list[num] = count_list.get(num,0)+1
length = len(num_list)
over_length_num = 0
for k,v in count_list.items():
    if v > length/2:
        print(k)
        over_length_num+=1
    else:
        continue
if over_length_num == 0:
    print(0)
