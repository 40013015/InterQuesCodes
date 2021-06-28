
from itertools import permutations

def PermutationStep(num):
  perms = set(permutations(str(num), len(str(num))))
  print(perms)
  new=[]
  for l in perms:
    val=int(''.join(l))  #joins the permuted string value
    new.append(val)
    v=sorted(new)
  print(new)
  print(v)
  #new = sorted([int(''.join(l)) for l in perms])
  #print(new)
  for n in v:
    if str(n) > num:
      return n
  return -1
# keep this function call here
print(PermutationStep(input()))
