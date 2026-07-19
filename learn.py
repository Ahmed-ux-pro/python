x = "i love"
y= "python" 
   #concatenation 
print (x+y)
print (x + " " +y)
print (x + '\n' +y)
 # you can only concatenate two strings no any other var

print ("hello wo\brld") #it will remove the 'o'
print ("i \
love \
python")
#will be printed in one line

#it will print one slash  
print ("i love back slash \\")

#carriade return 
print  ("abcde \r123")  #it will replace '123' with 'abc'      |  'abc' removed   |

# horizontal tab
print ("hello\tworld")

#character hex value
print ("\x41\x48\x4D\x45\x44")    #hex values from google

            # to print multible lines 
print ("""first
second 
third  """)           
                  # or
print ("first\n second \n third")

# to know the variable type
x= 10 
print (type(x))      # will say that it's integer

# casting a number to a string
decade =str (21)
print (type(decade))   #says string
print (decade)
statement = "i love music from " + decade +"s."

room1 = "service" 
room2 = ""
room1 = bool(room1)     #says True
room2 = bool(room2)     #says False

                                 # string methods
                            #   print (help . str)       
name = "Ahmed Haitham" 
print (name . lower())       #all letters will be  lower case
print (name . upper())       #all letters will be  upper case
print (name . title())       #first letter of each word will be upper case
print (name . capitalize())  #only first letter will be upper case
print (name . replace ("Ahmed" , "moka") )
print (len(name)) 
print (name . strip())       #to remove the space
print (name . find ("a"))    #finds the first 'a' 
print (name . rfind ("a"))   #finds the last  'a'
print (name . isdigit())     #it's a bool, says True when the string only contains numbers.
print (name . isalpha())     #it's a bool, says True when the string only contains letters (no spaces)
print (name .count("a"))     

#indexing  (single item)
print (name [0])      #prints the first letter    'A'
print (name [-2])     #negative means counting from right so it prints 'a'
print (name.startswith("A"))      # true  
print (name.endswith("r"))        # false         like boolean

#slicing   (multiple items)
print (name[0 : 3])     #prints from the first till the third 
print (name[0 :  ])     #prints the full string    | as a range |
print (name[0 :: 3])    
      #[begining : end]       and the end doesn't get printed
      #[begining :: steps]    steps means letting items (steps-1) and printing the following one item then letting items and printing the following and so on.
      #because it's [begining : end : steps]

# building menu
shop ="menu" . upper()
print (shop.center(12 , "-"))
print ("coffee" .ljust(9, '.') + '10$'.rjust(6)) 
# the center method center the variable between what you give it
# the ljust method puts characters you give after the variable
# the rjust method puts spaces you choose


x=bool (True)     #upper case
print (x)         #prints 'True'

x = float (12)     #identifier

# complex type   الاعداد المركبة
comp = 3+4j         #j means تخيلي
print (comp.real)   # prints  3
print (comp.imag)   # pirnts  4
print (type(comp))  #says complex value

#             ||      #i have to import math           ||
import math                    # to import the mathematical values like  pi  or  e 
v = -3.6  
gpa = 3.78
print (abs(v))                 #remove the negative sign                  3.6
print (round (gpa))            #converge to the nearest integer           3
print (round (gpa ,1))         #converge to the nearest decimal number    3.8
result = pow(3,2)              #means 3^2 = 9
result =max (v , gpa)          # result = the bigger value
result =min(v , gpa)

#             ||       i have to import math           ||
import math                    # to import the mathematical values like  pi  or  e 
print (math.e)                 # 2.72   you know
print (math.sqrt(16))          # square root
print (math.ceil(gpa))         #round the float up to the higher int
print (math.floor (gpa))       #round the float down to the lower int

#    input function  
name = input ("what's your name? ")   
print (f'hello {name}')    #the 'f' here is put to return the variable

 #                    |||           the if  statement        |||

age = float (input ("Enter your age : "))
if age >= 18 and age <=100 :
     print ("welcome") 
elif age <= 0 :
     print ("you haven't been born yet !!") 
elif age < 18 :
     print ("you are still a child")
else :
     print ("you are too old ")

#a shortcut for if else statement 
# x if condition else y       like :
num = 12
print ("positive" if num >0 else "negative")   
# other example :
result = "even" if num %2 ==0  else "odd"

# format specifiers                              #i see it's so important
price1 = 1230.567
price2 = -3455.45
price3 = 40922.442

print (f"price1 is : {price1:<,.6f}")
print (f"price2 is : {price2:+,.6f}")
print (f"price3 is : {price3:+,.6f}")
