# 2564
import sys
input = sys.stdin.readline
box = list(map(int,input().split()))
n = int(input())
store = []
for _ in range(n+1):
    store.append(list(map(int,input().split())))

LR = []
for i in store:
    temp = []
    if i[0] == 1:
        temp.append(box[1] + i[1])
        temp.append(2*box[0] + box[1] - i[1])
    elif i[0] == 2:
        temp.append(2*box[1] + 2*box[0] - i[1])
        temp.append(i[1])
    elif i[0] == 3:
        temp.append(box[1] - i[1])
        temp.append(2*box[0] + box[1] + i[1])
    elif i[0] == 4:
        temp.append(box[0] + 2*box[1] + i[1])
        temp.append(box[0] + box[1] - i[1])
    LR.append(temp)

guard = LR.pop(-1)
# guard 가 + set 인지 - set 인지 구별

plus_store = []
minus_store = []
center_store = []
for i in LR:
    if 0 < i[0] < sum(box):
        plus_store.append(i)
    elif i[0] > sum(box):
        minus_store.append(i)
    elif i[0] == sum(box):
        center_store.append(i)

ans1 = 0
for i in plus_store:
    ans1 += i[0] + guard[1]
ans2 = 0
for i in minus_store:
    ans2 += abs(i[1] - guard[1])

ans = ans1 + ans2 + sum(box)*len(center_store)
print(ans)


#
label = {'Pokemon':'Pikachu','Digimon':'Agumon','Yugioh':'Black Magician'}
key = input()
if key in label.keys():
    print(label[key])
else:
    print("I don't know")

#
idx = int(input())
label = {i[0]:i[1] for i in [input().split() for _ in range(idx)]}
key = input()
if key in label.keys():
    print(label[key])
else:
    print("I don't know")

#
label = [i for i in input().split()]
paul_dict = {label[i]:label.count(label[i]) for i in range(len(label))}
min_value = min(paul_dict.values())
for key in paul_dict.keys():
    if paul_dict[key] == min_value:
        print(key)
print(min_value)

# 1764
n,m = map(int,input().split())
ls1 = {input() for _ in range(n)}
ls2 = {input() for _ in range(m)}
print(len(ls1.intersection(ls2)))
for i in sorted(list(ls1.intersection(ls2))):
    print(i)

# 5622
num_dict = {2:'ABC',3:'DEF',4:'GHI',5:'JKL',6:'MNO',7:'PQRS',8:'TUV',9:'WXYZ'}
target = list(input())
ans = 0
while target:
    confirm = target.pop()
    for i in range(2,len(num_dict)+2):
        if confirm in num_dict[i]:
            ans += 1+i
            break
print(ans)

# 1620
n,m = map(int,input().split())
poke_dict = {i:input() for i in range(1,n+1)}
poke_dict_rev = {j:i for i,j in zip(poke_dict.keys(),poke_dict.values())}

for _ in range(m):
    target = input()
    if target.isdigit():
        print(poke_dict[int(target)])
    else:
        print(poke_dict_rev[target])

#
label = {'Pokemon':'Pikachu','Digimon':'Agumon','Yugioh':'Black Magician'}
key = input()
print(label.get(key,"I don't know"))


