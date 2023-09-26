#example 1
words = ['cats', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

#example 2
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)

#range ftn example 3
for i in range(5):
    print(i)

lists = []
for i in list(range(0, 10, 3)):
    lists.append(i)
print(lists)

a = ['mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print(list(enumerate(a)))