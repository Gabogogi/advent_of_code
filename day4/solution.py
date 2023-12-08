def main():
    with open("input.txt", "r") as file:
        sum = 0
        line = file.readline()
        while line:
            #get number lists
            _, nos = line.split(':')
            win_nos_str, my_nos_str = nos.split('|')
            win_nos = [int(num) for num in win_nos_str.split()]
            my_nos = [int(num) for num in my_nos_str.split()]

            counter = 0

            for x in win_nos:
                if x in my_nos:
                    counter += 1
            if counter > 0:
                sum += (2 ** (counter -1))
            line = file.readline()
        print(sum)

if __name__ == '__main__':
    main()

