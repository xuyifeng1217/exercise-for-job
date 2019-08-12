#

def get_time(m,h):
    ans = m+h/60
    return ans
n = int(input())
dict_ = {}
for i in range(n):
    h,m = list(map(int,input().strip().split()))
    dict_[i+1] = [h,m]
x = int(input())
x = x/60
last_h,last_m = list(map(int,input().strip().split()))
last_time = get_time(last_h,last_m)
res = 0
for i in dict_.keys():
    get_up = get_time(dict_[i][0],dict_[i][1])
    if get_up+x<=last_time:
        res = i
    else:
        break
print(dict_[res][0],dict_[res][1])
        