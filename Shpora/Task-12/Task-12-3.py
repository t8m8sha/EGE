ans = []
for n in range(4,10_000):
    st = '1'+'2'*n
    while '12' in st or '322' in st or '222' in st:
        if '12' in st:
            st = st.replace('12','2',1)
        if '322' in st:
            st = st.replace('322','21',1)
        if '222' in st:
            st = st.replace('222','3',1)
    summ = sum(map(int, st))
    ans.append(summ)
print(max(ans))


