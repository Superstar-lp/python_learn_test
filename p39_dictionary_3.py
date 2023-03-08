d = dict.fromkeys("FishC")
print(d)
d['s']=115
print(d)

# update([other])
d.update({'i':105,'h':104})
print(d)
d.update(F='70',C='67')
print(d)

## 查
d['s']
print(d.get('c',"这里没有c"))
