"""
    TODO: The code was designed to work with a dictionary
    however, the input, which is a ting, has repeated values
    fix that
    The correct answer is 227850

"""

def main():
    dist_dict = {
        
        78:1276

    }
    my_list = []

    for key in dist_dict.keys():
        count = 0
        time_values = [x for x in range(key + 1)]

        for x in time_values:
            my_dist = (key - x) * x
            if my_dist > dist_dict[key]:     
                count += 1


        my_list.append(count)
    print(my_list) 
    print(product_of_list(my_list)) 

def product_of_list(lst):
    product = 1
    for x in lst:
        product *= x
    return product


if __name__ == '__main__':
    main()
