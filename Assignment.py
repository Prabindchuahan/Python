
'''
roblem 1. you have to write an optimised program to calculate the frequency of each unique string in a give list
1) inut list =['Kasol','kasol','manali','delhi','delhi','manali','kasol']
'''
#solution:
list =['kasol','kasol','manali','delhi','delhi','manali','kasol']
a =list.count("kasol")
b =list.count("manali")
c =list.count("delhi")
d = 'kasol'
e='manali'
f ='delhi'
print(d ,'=', a )
print(e ,'=', b )
print(f,'=', c )
print("-------------------------------------")
#2)
#solution:
input_list = ['1','a','c','b','c','1']
a =input_list.count('1')
b =input_list.count('a')
c =input_list.count('b')
j =input_list.count('c')
d = '1'
e='a'
f ='b'
h ='c'
print(d ,'-', a )
print(e ,'-', b )
print(f,'-', c )
print(h, '-',j)
print('---------------------------------')
#Assignment -2
input_list =[1,9,7,10,4,5,1,11,3]
print( *input_list, sep = ",")
