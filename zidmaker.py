import random
zid = set()
for i in range(1,1000001):
	x = random.randint(1000000000000000,9999999999999999)
	zid.add(x)
#print(zid)
zz = list(zid)
print("zid count: ", len(zid))
for x in range(10):
  with open("zid"+str(x)+".txt","w") as f:
    for y in range(100000):
      z = 100000*x
      f.write(str(zz[z+y]))
      f.write('\n')
  f.close()