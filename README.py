# Problem-1538A---Stone-Game
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    _max = max(lst)
    _min = min(lst)
    pos_max = 0
    pos_min = 0
    for i in range(n):
        if lst[i] == _max:
            pos_max = i
        if lst[i] == _min:
            pos_min = i
    f_m = max(pos_max, pos_min)+1
    s_m = max(n - pos_min, n-pos_max)
    t_m = ((pos_min + 1) + (n - pos_max))
    fo_m = (pos_max + 1) + (n - pos_min)
    print(min(f_m, s_m, t_m, fo_m))
