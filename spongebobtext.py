def sponge(s):
    return ''.join(c.upper() if i % 2 == 1 else c for i, c in enumerate(s.lower()))

sbt = sponge(input('Enter text:\n'))
print(sbt)
