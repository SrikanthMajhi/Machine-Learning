-------------------------Question 1-------------------------------------
# below is the list of the ages  
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# sorting the given list
sort_ages = sorted (ages)
# Printing the sorted list in ascending order
print ("The ascending order of the list is :" ,sort_ages )
# finding the minimum age in the list
min_age=min(sort_ages)
# Printing the minimum age in the list
print("The minimum age in the list is :" , min_age)
# finding the maximum age in the list
max_age=max(sort_ages)
# Printing the minimum age in the list
print("The maximum age in the list is :" ,max_age)
# adding min and max age to the list
ages.extend([min_age,max_age])
ages1=sorted(ages)
# Printing the new list
print("The new list of numbers is  :" ,ages)
mid = len(ages) // 2
if len(ages1)%2==0: 
  res = (ages[mid] + ages[~mid]) / 2
else:
  res = (ages1[mid]) / 2
# Printing the  median of the list  
print("The median of the list is :" ,res)
# Printing the  Average of the list 
avg= sum(ages1)/ len(ages)
print ("The average of the list is : " , avg)
# Printing the range if the list
range_ages = max(ages1)-min(ages1)
print("The range of the list is :",range_ages)

-------------------------Question 2-------------------------------------

dog = dict ()
dog["name"] = ""              	                 
dog["color"] = ""                                         
dog["breed"] = ""                           
dog["legs"] =    None                                            
dog["age"] = None 
print(dog)
dog["name"] = "Dash"              	                 
dog["color"] = "Brown"                                         
dog["breed"] = " Deutsche Schafer's"                           
dog["legs"] = 4                                                
dog["age"] = 4                                                 
print(dog)  


# Creating an empty student dictionary 
student = dict()
print (student)
# creating key values and assigning values to it 
student["First_Name"]="Srikanth"
student["Last_Name"]="Majhi"
student["Gender"]="Male"
student["Age"]=28
student["Martial_Status"]="Single"
student["Skills"]=["SSE"]
student["Country"]="U.S"
student["City"]="OverlandPark"
student["Address"]="5006 W 108TH"
#Printing the student dictionary
print(student)
# printing the length of student
print("Length of the dictionary" ,len(student))
# Printing the value of the key Skills
print("The values in the key skills are : ",student["Skills"])
#Printing the datatype of skiils key 
print("The datatype of the skills key is : ", type(student["Skills"]))
#Adding values to the skills key
student["Skills"].extend(["ML","AI"])
#Printing the new skills 
print("The new values in the key skills are : ",student["Skills"])
#Printing all the keys of the students dictionary 
print("The key's in the student dictionary are : " ,student.keys())
#Printing all the values of the students dictionary 
print("The value's in the student dictionary are : " ,student.values())


                                                   
-------------------------Question 3-------------------------------------

#Creating Sisters Tuple
sisters = ("Santoshi", "Pavani", "Sindhu", "Sneha", "Mithali")  
#Creating Brothers Tuple
brothers = ("Santosh", "Vamsi", "Sai", "Daksith")                       
siblings = sisters + brothers        
# Printing the siblings tuple                                   
print("My Siblings are:",siblings)                                                                                      
# Counting the number of siblings I have                                                                    
len1 = len(siblings)     
# Printing the number of siblings I have 
print("Length of the my siblings", len1)                                                                                        
# Modifying & Adding more family numbers
family_members = siblings + ("Mohan Rao", "Tulasi",)  
# Printing the family members tuple 
print("My family members are ",family_members)                                                                        

-------------------------Question 4-------------------------------------
# Created set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}    
# Created A set
A = {19, 22, 24, 20, 25, 26}                                                              
# Created B set     
B = {19, 22, 20, 25, 26, 24, 28, 27}                                                    
# Created age set  
age = [22, 19, 24, 25, 26, 24, 25, 24]           
# Finding the length of the it_companies set                                       
length_it_comp = len(it_companies)       
# Printing the length of the it_companies set                                          
print("The length of the it_companies set",length_it_comp)                                                                           
# Added twitter to it_companies
it_companies.add("Twitter")                                              
# Printing the it_companies
print("The  IT Companies",it_companies)                    
# Creating multiple it_companies1 set                                         
it_companies1 = {  "Deloitte", "Adobe"}    
# Inserting multiple it_companies1 set to it_companies
it_companies.update(it_companies1)                               
# Printing it_companies after inserting
print("The new It Companies",it_companies)                 
# Removing one company from it_companies                                       
it_companies.remove("Deloitte")    
# Printing after removing                        
print("The new It Companies afrter removing :",it_companies)                                                        
# Joining A and B
print("Union of Aand B",A.union(B))
# Finding A intersection B
print("Intersection of Aand B",A.intersection(B))                                       
# Finding whether A is subset of B         
print("Checking if A is subset of B :",A.issubset(B))                                           
# Finding whether A and B are disjoint sets
print("Checking if A and B are disjoint sets",A.isdisjoint(B))                                         
# Joining A with B
print("Union of A and B ",A.union(B))                                              
# Joining B with A
print("Union of B and A ",B.union(A))                                
# Finding the symmetric difference between A and B              
print("The symmetric difference between A and B  ",A.symmetric_difference(B))                 
# Deleting the set A completely
A.clear()                                                              
# Checking whether it is deleted or not
print(A)                                                               
# Deleting the set B completely
B.clear()                                                              
# Checking whether it is deleted or not
print(B)                                                       
# Converting the list to set         
ageset = set(age)                                              
# Printing the converted set
print("The converted set A is :",ageset)                                                  
# Finding the length of the list  
listlen = len(age)                                             
# Printing the length of the list
print("Length of the new list age",listlen)                                             
# Finding the length of the set       
setlen = len(ageset)                                       
# Printing the length of the set
print("Length of the new set age",setlen)                                                   
-------------------------Question 5-------------------------------------
# importing pi from math module
from math import pi                                                                                    
# Given radius = 30
r = 30                                                                                            
 # Finding the area of circle                 
area_of_circle = pi*r**2                                                
# Printing the area of circle                          
print("Area of circle the with radius 30 is " + str(area_of_circle))    
circum_of_circle = 2*pi*r                                                              
# Finding the circumference of the circle
print("Circumference of circle the with radius 30 is " + str(circum_of_circle))
# Taking the radius as input from the user
radius = float(input("Enter the radius of circle"))       
area_of_circle_new_radius = pi*radius**2               
 # Finding the area of circle
print("Area of circle the with radius "+str(radius) + " is " + str(area_of_circle_new_radius)) 
-------------------------Question 6-------------------------------------

# Loaded given string into given_str 
given_str = "I am a teacher and I love to inspire and teach people"  
# Splitting the given string using split() function
split_string = given_str.split()                                        
 # Printing the string after splitting
print(split_string)                                                
# Converting the list into set to remove duplicates   
result = set(split_string)                                         
# Printing the set with unique words
print(result)           
# Printing the number of unique words                                             
print("The number of unique words in the given string is " + str(len(result)))   
                                                                             
-------------------------Question 7-------------------------------------
# Given Name Age Country City
#  Asabeneh 250 Finland Helsinki
#  defining the sequence in the required way
seq = "Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"  
# Printing the output                                                            
print(seq)                                          
-------------------------Question 8-------------------------------------
# Given radius = 10
radius = 10                                    
# Finding the area          
area = 3.14 * radius ** 2                    
# Printing the string using the formatting string method   
print("The area of a circle with radius {} is {} meters square.".format(radius, int(area)))   
                                                                 
-------------------------Question 9-------------------------------------
 #  Fetching the number of students input from user
no_of_stu= int(input("Enter number of students"))     
weight_in_lbs=[]
 # Running a for loop
for i in range(no_of_stu):                                                    
    student_weights = int(input("Enter the weight of Student of student " + str(i+1) + " : "))   

    # Converting weights in kgs and appending them to the list                                                                      
    weight_in_lbs.append(student_weights*0.453592)       
# Converting Student weight list to list with 2 decimal places
stu_weights_with_precision = ['%.2f' % elem for elem in weight_in_lbs]  
  
# Printing the student weights in kgs with 2 decimal places                                                                         
print(stu_weights_with_precision)   

------------------------------------Question 10-------------------------------------

import numpy
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from collections import Counter
import numpy as np
# creating an array to understand its attributes
a = np.array([1,2,3,6,6,7,10,11])
y = np.array([0,0,1,1,1,0,0,0])
x_train,x_test,y_train,y_test=train_test_split(a,y,test_size=0.5,random_state=4,stratify = y)
#Reshaping the data to 2D
x_train = x_train.reshape(-1,1)
x_test = x_test.reshape(-1,1)
y_train = y_train.reshape(-1,1)
y_test = y_test.reshape(-1,1)
#Printing the new data train and test data set 
print(x_train,x_test,y_train,y_test)
#Function to find out the distance for each individual points 
def KNN(x,y,k,z):
    dist = []
    # Computing Euclidean distance
    dist_ind = np.sqrt(np.sum((x-y)**2, axis=1))
    print(dist_ind)
    # Concatinating the label with the distance
    main_arr = np.column_stack((z,dist_ind))
    print(main_arr)
    # Sorting the distance in ascending order
    main = main_arr[main_arr[:,1].argsort()]
    # Calculating the frequency of the labels based on value of K
    count = Counter(main[0:k,0])
    keys, vals = list(count.keys()), list(count.values())
    if len(vals)>1:
        if vals[0]>vals[1]:
            return int(keys[0])
        else:
            return int(keys[1])
    else:
        return int(keys[0])

k=3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(x_train,y_train)
yprediction = knn.predict(x_test)
print("accuracy= ",accuracy_score(y_test,yprediction))
for i in x_test:
    result = KNN(x_train,i,3,y_train)
    print(result)
print(y_test,yprediction)



																 