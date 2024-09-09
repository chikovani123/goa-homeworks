print((True or False) and (True and True))
#print(True and True) #True

print((True or False) and (False or False))
#print(True and False) #False

print((False and True) or (True and False))
#print(False or False) #False

print((False or False) and (True or True))
#print(False and True) #False

print((True and True) or (False and True))
#print(True or True) #True

print((False or True) and (True and False))
#print(True and False) #False

print((False and False) or (False or True))
#print(False or True) #True

print((True or False) and (False or True))
#print(True and True) #True

print((True and False) or (True and False))
#print(False or False) #False

print((True and True) or (True and False))
#print(True or False) #True

print((False and False) or (True or False))
#print(False or True) #True

print((True or True) and (False and False))
#print(True and False) #False

print((False or True) and (True or True))
#print(True and True) #True

print((True and False) or (True and False))
#print(False or False) #False

#or ოპერატორს გამოაქვა True თუ ერთ-ერთი მაინც არის True. მხოლოდ მაშინ გამოაქვს False როცა ორივე პირობაა False
#and ოპერატორს ამოაქვს True მხოლოდ თუ ორივე პირობაა True. თუ რომელიმეა False გმოაქვს False

print(True or False)
print(True or True)
print(False or True)
print(False or False)
print(True or False or False)
print(False or False or False)
print(True or True or True)
print(False or True or True)
print(False or True or True or False)
print(False or False or False or True)

print(True and False)
print(True and True)
print(False and True)
print(False and False)
print(True and False and False)
print(False and False and False)
print(True and True and True)
print(False and True and True)
print(False and True and True and False)
print(False and False and False and True)