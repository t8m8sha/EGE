def f(x,s):
    if x >= 39: return s % 2 == 0
    if s == 0: return False
    h = [f(x + 1,s - 1),
         f(x + 3,s - 1),
         f(x * 2,s - 1)]
    return any(h) if (s-1) % 2 == 0 else all(h)
print('19)',[s for s in range(1,39) if f(s,2)])
print('20)',[s for s in range(1,39) if not f(s,1) and f(s,3)])
print('21)',[s for s in range(1,39) if not f(s,2) and f(s,4)])


