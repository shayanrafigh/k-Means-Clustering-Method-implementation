import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return '(%d,%d)' % (self.x,self.y)
    def __add__(self,other):
        a = self.x + other.x
        b = self.y + other.y
        return Point(a,b)
    def __mul__(self,other):
        return self.x*other.x + self.y*other.y
    def __sub__(self,other):
        a = self.x - other.x
        b = self.y - other.y
        return Point(a,b)

class cluster:
    def __init__(self,name=0,centroid=Point(),l=[]):
        self.name=name
        self.centroid=centroid
        self.l=l
    def __str__(self):
        return ' %s cluster  %s  with centroid= %s' % (self.name,self.centroid,printplist(self.l))
def dis(p1,p2):
    return math.sqrt(math.pow((p1.y - p2.y), 2) + math.pow((p1.x- p2.x), 2)) 
SAMPLES =[]
import random
for i in range(0,50):
    x=float(random.randint(1,90))
    y=float(random.randint(1,90))
    SAMPLES.append(Point(x,y))
def printplist(s):
    for i in range(len(s)):
        print(s[i] ,end="")
def mini(l):
    s=[]
    w=""
    for i in l:
        s.append(i[1])
    for j in l:
        if(j[1]==min(s)):
            w=j[0]
    return w
def updatecentroid(cl):
    if len(cl.l)!=0:
        s=Point(0,0)
        for i in cl.l:
            s=s+i
        x=s.x/len(cl.l)
        y=s.y/len(cl.l)
        cl.centroid=Point(x,y)
def kmean(k,SAMPLES):
    clusterlist=[]
    listofdis=[]
    listofc=[]
    dist=0
    ss=0
    namecc=""
    namec=""
    still=False
    for i in range(1,k+1):
        clusterlist.append(cluster(i,SAMPLES[i],[]))
    while(True):
    #for qq in range(0,20):
        still=False
        for j in SAMPLES:
            for i in clusterlist:
                dist=dis(i.centroid,j)
                namec=i.name
                listofdis.append((namec,dist))
            namecc=mini(listofdis)
            for item in clusterlist:
                if(namecc==item.name):
                    if j not in item.l:
                        still=True
                        item.l.append(j)
                        namecc=item.name
                        for v in clusterlist:
                            if v.name!=namecc:
                                if j in v.l:
                                    v.l.remove(j)
            listofdis=[]
        for item in clusterlist:
            updatecentroid(item)
        if still==False:
            break
        ss=0
        listofc=[]
    return clusterlist  
def sumofdistance(cl):
    s=0
    for item in cl.l:
        s=(dis(item,cl.centroid)**2)+s
    #d=s/len(cl.l)
    return int(s)
def elbowmethod():
    List=[]
    k=[]
    ss=0
    for i in range(1,10):
        List.append(kmean(i,SAMPLES))
    for item in List:
        for cl in item:
            ss=sumofdistance(cl)+ss  
        ss=ss/len(item)             
        k.append(int(ss))
    z=sum(k)/len(k)
    print(k)
    #print(z)
    h=10000
    d=0
    for i in range(len(k)):
        if abs(z-k[i])<h:
            h=k[i]
            d=i+1   
    return d        
numberOfk=elbowmethod()
#print(numberOfk)
l=kmean(4,SAMPLES)
for i in l:
  print("-----")
  print(i)   
def normalshow():   
    x=[]
    y=[]
    for i in SAMPLES:
        x.append(i.x)
        y.append(i.y)
    from matplotlib import pyplot as plt
    plt.scatter(x,y,color='red')
    plt.axis([0, 100, 0, 100])
    plt.show()
def aftercluster():   
    showx=[]  
    showy=[]
    x=[] 
    y=[]
    for item in l:
        for i in item.l:
            x.append(i.x)
            y.append(i.y)
        showx.append(x)
        showy.append(y)
        x=[]
        y=[]                          
    cc=["red","blue","green","yellow","cyan","magenta","black"]
    from matplotlib import pyplot as plt
    for i in range(len(showx)):
        plt.scatter(showx[i],showy[i],c=cc[i])
    plt.axis([0, 100, 0, 100])
    plt.show()    
normalshow()  
aftercluster()    
input()

            
        
    
        
    
    
    
    
