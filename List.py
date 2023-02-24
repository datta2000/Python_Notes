#creating Empty list

list1=[]

# We can create list using list function 

list2=list()
print(type(list2))# output: class 'list'>

#indexing in list

list3=['Datta','Tekale',20,13,]
print(list3[2]) # output: 20

#slicing in list

list4=['Datta',45,12,'Tekale',36,'Pavan']
print(list4[1:3]) #output :[45,12]
print(list4[:])#output : ['Datta', 45, 12, 'Tekale', 36, 'Pavan']
print(list4[:4])#output : ['Datta', 45, 12, 'Tekale']
print(list4[-1]) #output : ['Pavan']

# count method:

list5=['Datta',54,12,'Datta','Tekale','Pavan']
print(list5.count('Datta')) #output : 2
print(list5.count(54)) #output : 1


# Index method:

list6=['Datta','Pavan',23,54,12,'Tekale']
print(list6.index('Pavan')) #output : 1
print(list6.index(12)) #output : 4


#insert method:

list7=['Datta','Pavan',23,54,12,'Tekale']
list7.insert(1,'Atul')
print(list7) # output : ['Datta', 'Atul', 'Pavan', 23, 54, 12, 'Tekale']
list7.insert(0,'Karan')
print(list7) #output : ['Karan', 'Datta', 'Atul', 'Pavan', 23, 54, 12, 'Tekale']


#pop(Delete)

list8=['Datta','Pavan',23,54,12,'Tekale']
list8.pop()
print(list8) #output : ['Datta', 'Pavan', 23, 54, 12]
list8.pop(1)
print(list8) # output : ['Datta', 23, 54, 12,]
list8.pop(3) 
print(list8) # output : ['Datta', 23, 54]

#extend:

list9=['Datta','Pavan',23,54,12,'Tekale']
list10=['18','Karan']
list9.extend(list10)
print(list9) #output : ['Datta', 'Pavan', 23, 54, 12, 'Tekale', '18', 'Karan']

#copy:

list11=['Datta','Pavan',23,54,12,'Tekale']
list12=list11.copy()
print(list12)  # output : ['Datta', 'Pavan', 23, 54, 12, 'Tekale']

#another method of copy

list13=['Datta','Pavan',23,54,12,'Tekale']
list14=list13[:]
print(list14) # output : ['Datta', 'Pavan', 23, 54, 12, 'Tekale']


#sort:

list15=['Datta','Pavan',23,54,12,'Tekale']
#list15.sort() 
#print (list15)#output TypeError: '<' not supported between instances of 'int' and 'str'

list16=[15,12,19,8,11]
list16.sort()
print(list16) #output : [8, 11, 12, 15, 19]

#sort in descending order

list17=[15,12,19,8,11]
list17.sort(reverse=True)
print(list17) #output : [19, 15, 12, 11, 8]


#Reverse :

list18=[1,2,3,4,5]
list18.reverse()
print(list18) #output : [5, 4, 3, 2, 1]

#Nested list:

list19=['Datta','Pavan',['Karan',[34]],'Tekale']
print(list19) #output : ['Datta', 'Pavan', ['Karan', [34]], 'Tekale']


#List Comprehension:

list20=['Datta','Tekale','Pavan','Karan']
a=[word for word in list20 if word.startswith('T')]
print(a) #ouput : Tekale

#List Unpacking:

list21=['Datta','Tekale','Atul',45]
n1,n2,n3,n4=list21
print(n1)
print(n2)
print(n3)
print(n4)











