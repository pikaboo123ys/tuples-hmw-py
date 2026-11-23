T = ("read", "exercise", "eat")
print(max(T))
print(min(T))

t = ("drink water", "walk", "journal")
a, b, c = t
print(t)

a, b, c = "wake early", "stretch", "plan day"
T = a, b, c
print(T)

L = list(T)

L = []
for x in T:
    L.append(x)
print(L)

T = ("water", "read", "walk", "run", "sleep", "cook", "study", "clean", "stretch", "journal")
print(T[3])
print(T[-3])
print(T[2:7])

T = ("water", "read", "walk", ("stretch", "journal", ("sleep", "eat"), "plan", "cook"), "focus")

print(T[3][1])
print(T[3][2][1])
