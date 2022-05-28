#1. Model an organisation of employees, management and directors in 3 sets
boardOfDirectors = {"Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Soren"}
management = {"Tine", "Trunte", "Rane"}
employees = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", 
"Allan", "Stine", "Claus", "James", "Lars"}

#1.1 who in the board of directors is not an employee?
print(boardOfDirectors - employees)
#Result: {'Troels', 'Soren', 'Torben', 'Benny', 'Mille', 'Hans'}

#1.2 who in the board of directors is also an employee?
print(boardOfDirectors & employees)
#Result = {'Tine'}

#1.3 how many from the management is also member of the board?
print(len(management & boardOfDirectors))
#Result 1

#1.4 Are all members of the managent also an employee?
print(management <= employees)
#Result true

#1.5 Are all members of the management also in the board?
print(management <= boardOfDirectors)
#Result false

#1.6 Who is an employee, member of the management, and a member of the board?
print(employees & management & boardOfDirectors)
#Result {'Tine'}

#1.7 Who of the employee is neither a memeber or the board or management?
print(employees - management - boardOfDirectors)

#2. List comprehension
#Using a list comprehension create a list of tuples from the folowing datastructure
#{'a': 'Alpha', 'b' : 'Beta', 'g': 'Gamma'}
dict1 = {'a': 'Alpha', 'b' : 'Beta', 'g': 'Gamma'}

newlist = [(k,v) for (k,v) in dict1.items()] #The items() method will return each item in a dictionary, as tuples in a list.
print(newlist)

#3. Sets
#From these 2 sets {'a', 'e', 'i', 'o', 'u', 'y'}
#{'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'} create
#3.1 a Union
#Union returns a set that contains all items from both sets, duplicates are excluded:
set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

unionSet = set1.union(set2)

print(unionSet)

#3.2 Symmetric difference 
#Return a set that contains all items from both sets, except items that are present in both sets:

symmetricDiffSet = set1.symmetric_difference(set2)

print(symmetricDiffSet)

#3.3 Difference
#Returns a set that contains the items that only exist in set x, and not in set y:

differenceSet = set1.difference(set2)

print(differenceSet)

#3.4 Disjoint
#Two sets are disjoint when they have no elements in common. The method isDisjoint returns true 
#if two sets are disjoint 

disjointSet = set1.isdisjoint(set2)

print(disjointSet)

#4 Date Decoder
#A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.
#Create a dict suitable for decoding month names to numbers.
#Create a function which uses string operations to split the date into 3 items using the "-" character.
#Translate the month, correct the year to include all of the digits.
#The function will accept a date in the "dd-MMM-yy" format and respond with a tuple of ( y , m , d ).

date = "8-MAR-85"

months = dict(JAN = '01', FEB = '02', MAR  = '03', APR = '04', MAY = '05', JUN = '06', 
JUL = '07', AUG = '08', SEP = '09', OCT = '10', NOV = '11', DEC = '12')

def format_date(s):
    #Jeg splitter dato string op i en liste med 3 items dd-MMM-yy
    dateItems = s.split("-")
    #Jeg finder den key/måned i dict som svarer til MMM i listen -> get returnere Value udfra key
    monthFormat = months.get(f'{dateItems[1]}')
    #Årstal med 19 foran
    yearFormat = "19" + dateItems[2]
    #Tuple med den samlede formatterede dato (yyyy, mm, dd)
    newFormattedDate = (f'{yearFormat}', f'{monthFormat}', f'{dateItems[0]}')
    return newFormattedDate

print(format_date(date))
   
