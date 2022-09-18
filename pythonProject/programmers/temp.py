p = input()

def uv_decomposition(p):
    i = 0
    while 1:
        if p[i] == '(':
            i += 1
        else:
            break
    if i == 0:
        while 1:
            if p[i] == ')':
                i += 1
            else:
                break
    return p[:2*i],p[2*i:]

#u,v = uv_decomposition(p)

def switch(u):
    tp = ' '.join(u[1:len(u)-1]).split()
    tp.reverse()

    if not tp or tp[0] != tp[-1]:
        u = '(' + ''.join(tp) + ')'
    return u


#switch(u)

def check(p):
    tp = p
    while tp:
        tp = tp.replace('()', '')
        if tp == tp.replace('()', ''):
            break
    if tp == '':
        return 1
    else:
        return 0

def solution(p):
    if check(p) == 1:
        return p

    u,v = uv_decomposition(p)
    if check(u) == 0:
        return switch(u) + solution(v)
    elif check(v) == 0:
        return solution(u) + solution(v)
    else:
        return u + v



solution(p)


# import math
# W,H = 8,12
# box = math.gcd(W,H)
#
# sub_W = int(W/box)
# sub_H = int(H/box)
#
# sub_W = min(sub_H,sub_W)
# sub_H = max(sub_H,sub_W)
#
# blank = 0
# cnt = 1
# while 1:
#     if sub_W >= 1 and sub_W < 2:
#         blank += sub_H
#         break
#     else:
#         sub_H = math.ceil(sub_H/2)
#         sub_W = sub_W/2
#         cnt += 1
#
# blank * cnt * box
