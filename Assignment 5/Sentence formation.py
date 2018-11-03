#define people 
people=["Americans","Indians"]
#define action
action=["play","watch"]
#define objects
objects=["Baseball","Cricket"]

# comprehension
value = [" ".join([a,b,c+'.']) for a in people for b in action for c in objects]

#print value
for x in value:
    print(x)
    