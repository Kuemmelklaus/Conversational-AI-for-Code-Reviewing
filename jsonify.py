
with open("./PythonExanples/main.py") as c:
    t = c.read()

t = t.replace("\\'", "\\\\'")
t = t.replace('"', '\\"')
t = t.replace('\n', '\\n')

print(t)