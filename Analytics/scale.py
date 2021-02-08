reply_dict = {0:[0,1], 1:[1,2], 1.5:[2,5], 2:[2]}
comments_dict = {0.5:[0,0.5], 1:[0.5,1], 1.5:[1,2], 2:[2]}
response_dict = {0.1:[0,1], 0.5:[1,2], 1:[2,4], 2:[4]}
delay1_dict = {0.5:[0,1], 1:[1,2], 1.25:[2,7], 1.5:[7,14], 2:[14]}
delay3_dict = {0.5:[0,5], 1:[5,14], 1.25:[14,30], 1.75:[30,60], 2:[60]}
delay2_dict = {0.5:[0,2], 1:[2,7], 1.25:[7,14], 1.75:[14,30], 2:[30]}

def bin_scale(value, scale_dict):

    for k in scale_dict:

        if value == None:
            return 0

        elif (len(scale_dict[k]) ==1) and (value >= scale_dict[k][0]):
            return k

        elif (len(scale_dict[k]) > 1) and (value >= scale_dict[k][0]) and (value < scale_dict[k][1]):
            return  k



# if __name__ == '__main__':
#     print(bin_scale(5, delay2_dict ))