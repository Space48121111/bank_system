s1 = 'https://github.com/stella-vir/perseverance_bank_system/blob/master/screenshots/Screen%20Shot%202022-10-08%20at%2016.53.00.png'
s2 = 'https://github.com/stella-vir/perseverance_bank_system/blob/master/screenshots/Screen%20Shot%202022-10-08%20at%2016.53.00png'
# str1 str2 reserved names
# h h +=1

s11 = 'abc'
s22 = 'abd'

if s1 == s2:
    print('Yessss')
print('Nope')

p1, p2= 0, 0

while len(s1) and len(s2):
    if len(s1) != len(s2):
        print('Not equal')
        break
    if s1[p1] and s2[p2]:
        if s1[p1] == s2[p2]:
            print(p1, p2, s1[p1], s2[p2])
            p1 += 1
            p2 += 1
        else:
            print('Not equal', p1, p2, s1[p1], s2[p2])
            break
