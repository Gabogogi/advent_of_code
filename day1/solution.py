
with open("text2.txt", 'r') as file:
    sum = 0
    line = file.readline()
    while line:
        my_no = []
        for char in line:
            if char.isdigit():
                my_no.append(char)
        last_first = []
        last_first.append(my_no[0])
        last_first.append(my_no[-1])
        final_no = ''.join(last_first)
        print(int(final_no))
        sum += int(final_no)
        line = file.readline()
    print(sum)
