
with open("./PythonExanples/main.py") as c:
#with open("./ABAPExamples/zcl_fs_ref_perf_testing.clas.abap", "r") as c:
    t = c.read()

t = t.replace("\\'", "\\\\'")
t = t.replace('"', '\\"')
t = t.replace('\n', '\\n')

print(t)