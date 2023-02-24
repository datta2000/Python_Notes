
'''Touple is a data structure which is also called collection of items,in which
we can store anything like string float ,integer..etc'''


#syntax: tuple_name=(item1, item2,......itemN)

#Note:

   #1.We write the item of the tuple inside paranthesis "()" and each item is seprated by ","
   #2.Duplicate are allowed
   # 3.Immutable in nature(We can't change or update) 

#more than one item is considered as tuple

# Ex:

var1 =1,5,'Datta',8
print(type(var1)) #output: <class 'tuple'>


var2=(1,'Datta','Tekale',98)
print(var2) #output: (1, 'Datta', 'Tekale', 98)

#indexing :

var3=(1,'Datta','Tekale',98)
print(var3[3]) #output: 98
print(var3[1]) #Output : Datta

#slicing :

var4=(1,'Datta','Tekale',98)
print(var3[1:3]) #output : ('Datta', 'Tekale')
print(var3[-1]) 
