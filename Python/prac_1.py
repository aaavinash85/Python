  #wap to proagrma to find the numbers b/w 2000 and 3200 which are divisible by 7 but not multiple of 5
l=[]   #declaring a array
i=0
for i in range(1999,3201):
  	if(i%7==0 and i%5!=0):
  	    l.append(i)
  	    print (i)
  	  		