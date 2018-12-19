# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 2018

@author: luanhaoran
"""

# Student Name: Haoran Luan ;Student Number 25478028
# Start edit date 18 Dec 2018 last edit 19 Dec 2018
# In this task, there are three steps：
# 1.Check the inputs integer and a list of positive integers
# 2.After right input, starting Loop to find all right pairs
# 3.Output result and ready to input new set of numbers

#==============================================================================
# In first part, we can check the input when we get and problem will show error
# if input is in other format.
# I use the number list to check if every char is a number
#==============================================================================

num_len=1


while num_len!=0:
    num_input=input('Please enter First word. Leave blank to quit.')
    num_list=list(num_input)
    num_len=len(num_input)
    number_list=['0','1','2','3','4','5','6','7','8','9']
    
    fisrt_num="pass"
    list_len=1
    char_check="pass"
    for char in num_list:
        if char not in number_list:
            char_check="fail"
    if char_check=="fail":
        print(str(num_input) + " is not a number!")
        fisrt_num="fail"
            
    while num_len!=0 and fisrt_num=="pass" and list_len!=0:
        thelist=input('please enter the number list and split with comma(,).')
        tl_list=thelist.split(',')
        list_len=len(tl_list)
        second_list="pass"
        if len(tl_list)==0:
            fisrt_num="fail"
        elif list_len<2:
            print("Please input at least two numbers and split with comma(,)")
            second_list="fail"
            list_len=list()
        else:
            for num in tl_list:
                tl_num_list=list(num)
                char_check="pass"
                for char in tl_num_list:
                    if char not in number_list:
                        char_check="fail"
                if char_check=="fail":
                    print(str(num) + " is not a number!")
                    second_list="fail"
            list_len=list()
                        
#==============================================================================
# I use first_num and second_list to control the loop, it will go to
# next step until the number and list pass these two checks
#==============================================================================

        
        while fisrt_num=="pass" and second_list=="pass":
            pair_list=list()
            control_list=tl_list
            
#==============================================================================
# I set up a loop to find the pair values and it will stop after check all 
# numbers. I take out the first number and check whether pair value also in
# the list.
# All pair values will save in a list
# also in this part, the format of item is improtant
#==============================================================================           
            
            while len(control_list)>1:
                item=control_list[0]
                control_list.remove(item)
                pair_item=int(num_input)-int(item)
                if str(pair_item) in control_list:
                    control_list.remove(str(pair_item))
                    group=list()
                    group.append(int(item))
                    group.append(pair_item)
                    pair_list.append(group)
            if pair_list==[]:
                print ("No pair result!")
            else:
                print ("There are " + str(len(pair_list))+ " Pair result " + 
                       str(pair_list) + ".")
#==============================================================================
# Reset the check value to go back
#==============================================================================                

            fisrt_num="fail"
                
                        
print ("Process finished with exit code 0")


    
    
    
