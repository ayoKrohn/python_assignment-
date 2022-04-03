#1. 
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


