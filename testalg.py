import itertools

PBJcondiment = ['peanutbutter','jelly']
fruit = ['strawberry','banana']
inside = PBJcondiment + fruit
n = 1
i = 0
PBJSammies = []
SuperSammies = {}

def validate1(recipe): 
  """
  @param tempsammies is a list from the list of lists (PBJSammies, GCSammies, CSammies, SSammies, HSammies)
  @return whether this recipe is a SuperSammie
  """
  # we don't want plain sandwiches! 
  if len(recipe) <= 2: 
    return False  

  else:
    return True  

for x in xrange(1,len(inside)+1): 
	tempsammies = list(itertools.combinations(inside,x))
	k = 0 
	for j in tempsammies: 
		value = list(tempsammies[k])
		PBJSammies.append(value)
		k += 1
		n += 1

while i < len(PBJSammies): 
	PBJSammies[i].append('slicedbread')
	i += 1

i = 0
while i < len(PBJSammies):
	if validate1(PBJSammies[i]) is False: 
		PBJSammies.pop(i)
	else: 
		i += 1

for j in PBJSammies: 
	key = 'PBJ'
	SuperSammies.update({key:PBJSammies})

"""print PBJSammies
print len(PBJSammies)
print SuperSammies"""

n = 1
i = 0 
bread = ['slicedbread','roll']
vegetable = ['lettuce','tomato']
other = ['pickles','chips']
ColdSammieprotein = ['tuna','hardboiledegg']
ColdSammiecondiment = ['mustard','mayonnaise']
CSammies = []

def validate2(recipe, bread, vegetable, other, protein, condiment):
  """
  @param recipe is a list from the list of lists (CSammies, SSammies, HSammies),
  vegetable and protein are lists specific to these sandwiches
  @return whether this recipe is a SuperSammie
  """
  if len(recipe) <= 3:
    return False

  if (len(set(recipe) & set(vegetable)) == 0) or (len(set(recipe) & set(protein)) == 0):
    return False

  if (len(set(recipe) & set(protein)) != 1):
    return False

  if (len(set(recipe) & set(bread)) != 1):
    return False

  if (len(set(recipe) & set(other)) > 1):
    return False

  if (len(set(recipe) & set(condiment)) != 1):
    return False

  else:
    return True

inside = bread + vegetable + other + ColdSammieprotein + ColdSammiecondiment
for i in xrange(1,len(inside)+1):
	tempsammies = list(itertools.combinations(inside,i))
	k = 0
	for j in tempsammies:
		value = list(tempsammies[k])
		CSammies.append(value)
        	k += 1
        	n += 1
print len(CSammies)

    # insert only SuperSammies into SuperSammies dictionary value
i = 0 #reset the value of the index
while i < len(CSammies):
      	if validate2(CSammies[i],bread,vegetable,other,ColdSammieprotein,ColdSammiecondiment) is False:
        	CSammies.pop(i)
      	else:
        	i += 1
for j in CSammies:
      	key = 'CS'
      	SuperSammies.update({key:CSammies})

print len(CSammies)
print SuperSammies
