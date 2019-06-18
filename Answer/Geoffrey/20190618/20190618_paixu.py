### 1、
languages = [(1, 'Go'), (2, 'Ruby'), (3, 'Swift'),
             (4, 'Erlang'), (5, 'Kotlin'), (6, 'Python')]

languages_sorted = []
languages_sorted_a = []
languages_sorted_b = []

n = len(languages)
for i in range(0,n):
    if i >= 3:
        languages_sorted_a.append(languages[i])
    else:
        x = 2 - i
        languages_sorted_b.append(languages[x])

languages_sorted = languages_sorted_a + languages_sorted_b
print(languages_sorted)

### 2、
languages = [(1, 'Go'), (2, 'Ruby'), (3, 'Swift'),
             (4, 'Erlang'), (5, 'Kotlin'), (6, 'Python')]

languages_sorted = []
languages_a = languages[3:]
languages_b = []
n = len(languages)
for i in range(0,n):
    if i < 3:
        x = 2 -i
        languages_b.append(languages[x])

languages_sorted = languages_a  + languages_b
print(languages_sorted)
