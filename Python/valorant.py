

def decide(maps,lastmap,rnd,players,mapno,fake):
    
    def msearch(l,target,low,high):
        if low>high:
            return False
        else:
            mid=(low+high)//2
            if l[mid]==target:
                return mid
            else:
                if l[mid]>target:
                    return msearch(l,target,low,mid-1)
                else:
                    return msearch(l,target,mid+1,high)
    index=msearch(maps,lastmap,0,len(maps)-1)
    fconstant=(2/len(maps))*fake
    def ovsc(rnd):
        if rnd%fake:
            return rnd
        else:
            return 0
    if index<(len(maps)-1)/2:
        print("You can enter site",maps[len(maps)-1],"with a loss of atmost",players//mapno,"players")
        print("The overall chances of failure are",ovsc(rnd)*fconstant,"%")
    else:
        print("You can enter site",maps[0],"with a loss of atmost",players//mapno,"players")
        print("The overall chances of failure are",ovsc(rnd)*fconstant,"%")
fake=int(input("How many different strats do you intend to apply?: "))
mapname=str(input("Enter the map name: "))
roundno=int(input("Enter the roundno: "))
lastmap=str(input("Enter the last site you entered: "))
print()
print()
maplist=["icebox","bind","split","fracture","ascent","breeze"]

if mapname.lower()=="haven":
    decide(['a','b','c'],lastmap.lower(),roundno,5,3,fake)
elif mapname.lower() in maplist:
    decide(['a','b'],lastmap.lower(),roundno,5,3,fake)
else:
    print("enter correct details")