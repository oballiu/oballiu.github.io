import random

def sim_dice():
    freq_dict={1:0,2:0,3:0,4:0,5:0,6:0}
    for i in range(10000):
        num=random.random()
        if num<1/6:
            freq_dict[1]+=1
        elif num<2/6:
            freq_dict[2]+=1
        elif num<3/6:
            freq_dict[3]+=1
        elif num<4/6:
            freq_dict[4]+=1
        elif num<5/6:
            freq_dict[5]+=1
        elif num<6/6:
            freq_dict[6]+=1
    return freq_dict
freq_dict = sim_dice ()
for i in freq_dict: 
    print('{:2d : {:d}'.format(i,freq_dict[i]))
