my_list=[1,2,3,4,5]       #creating a list named my_list, Which is a list of integers
print(my_list)
m_list=['String',100,3.2] # A list named m_list, which contains mixed datatype
print(m_list)
print('the length of the list=',len(m_list))        # len will provide the length of the list

# .append() method

m_list.append('avi')      # the appand() will add the element at the end of list
print('the append list =',m_list)

# .pop() method

m_list.pop()              # this will remove the last element of the list
print('the pooped list =',m_list)

# we can also remove the particular element using .pop() and Index no.

m_list.pop(0)             # this will remove the element which is at Index[0](String)
print('the pooped list at index [0]=',m_list)

#The Sort method(this will sort the elements in order)

list1=['a','c','e','d','b']
list2=[1,4,5,3,2]
list1.sort()
list2.sort()
print('the sorted list1=',list1)
print('the sorted list2=',list2)

# Reverse method(this will reverse the elements of a list)
list1.reverse()
print('the reversed list1=',list1)
list2.reverse()
print('the reversed list2=',list2)