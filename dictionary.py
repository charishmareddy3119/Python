# s1={ 103:'Tina'
#      102:'Rina'
#      103:'Mina'}
# print(s1)
# print(s1[1:2])
# print(s1[101])

d1 = dict({100:'Tina',200:'Rina',300:'Mina'})
print(d1)
d2 = dict([(333,'Cherry'),(666,'Varshi'),(999,'Nomi')])
print(d2)
d3 = dict((('1','Sanju'),('r','Teju'),('s','Sarvana')))
print(d3)

#len

d1 = dict({100:'mohit',200:'Sai Charan',300:'abhi'})
print(d1.clear())

#get

d1 = dict({100:'mohit',200:'bunny',300:'abhi'})
d = {100:'mohit',200:'bunny',300:'abhi'}
print(d[100])
print(d[400])#key Error
print(d.get(100))
print(d.get(400))#none
print(d.get(100,'mohit'))
print(d.get(400,'mohit'))

#pop
d = {100:'mohit',200:'bunny',300:'abhi'}
print(d.pop(300))
print(d.pop(400))#keyError

#popitem

d = {100:'mohit',200:'bunny',300:'abhi'}
print(d.popitem())

d ={}
print(d.popitem())#keyerror

#Keys

d = {100:'mohit',200:'bunny',300:'abhi'}
print(d.keys())
for k in d.keys():
    print(k)

    #Values

d = {100:'mohit',200:'bunny',300:'abhi'}
print(d,values())
for k in d.values():
    print(k)

#Setdefault
d = {100:'mohit',200:'bunny',300:'abhi'}
print(d.setdefault(100,'mohit'))
print(d.setdefault(400,'vamsi'))
#print(d)

#Update
d = {100:'mohit',200:'bunny',300:'abhi'}
d1 = {'a':'apple'}
d.update(d1)
print(d)
d.update([(333,'A')])
print(d)
   



