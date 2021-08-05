'''
friendsOfFriends(d) [15 pts]
Background: we can create a dictionary mapping people to sets of their friends. For example, we might say:
d = { }
d["jon"] = set(["arya", "tyrion"])
d["tyrion"] = set(["jon", "jaime", "pod"])
d["arya"] = set(["jon"])
d["jaime"] = set(["tyrion", "brienne"])
d["brienne"] = set(["jaime", "pod"])
d["pod"] = set(["tyrion", "brienne", "jaime"])
d["ramsay"] = set()

With this in mind, write the function friendsOfFriends(d) that takes such a dictionary mapping people to sets of friends and returns a new dictionary mapping all the same people to sets of their friends of friends. For example, since Tyrion is a friend of Pod, and Jon is a friend of Tyrion, Jon is a friend-of-friend of Pod. This set should exclude any direct friends, so Jaime does not count as a friend-of-friend of Pod (since he is simply a friend of Pod) despite also being a friend of Tyrion's.

Thus, in this example, friendsOfFriends should return:
{
 'tyrion': {'arya', 'brienne'}, 
 'pod': {'jon'}, 
 'brienne': {'tyrion'}, 
 'arya': {'tyrion'}, 
 'jon': {'pod', 'jaime'}, 
 'jaime': {'pod', 'jon'}, 
 'ramsay': set()
}
'''


def readDict():
    a = {}
    n = int(input())
    for i in range(n):
        s = input().split()
        a[s[0]] = set(s[1:])
    return a

def mutualfriend(d,i):
    m=[]
    for j in d[i]:
        if j in d:
            for k in d[j]:
                if k not in m and  k not in d[i] and k not in i:
                        m.append(k)
                
    return m
def friendsOfFriends(d):
    # your code goes here
    a={}
    for i in d:
        if i not in a:
            a[i]=mutualfriend(d,i)
    return a
d = friendsOfFriends(readDict())

for i in sorted(d.keys()):
    print(i, sorted(d[i]))
