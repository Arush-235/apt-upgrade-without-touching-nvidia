from os import system as s
import subprocess as sp

p = sp.Popen(["apt-cache pkgnames cuda"],stdout=sp.PIPE,shell=True)
(out1,err) = p.communicate()
o1 = str(out1).split("\\n")
o1.pop()
o1[0] = o1[0][2:]
p = sp.Popen(["apt-cache pkgnames nvidia"],stdout=sp.PIPE,shell=True)
(out2,err) = p.communicate()
o2 = str(out2).split("\\n")
o2.pop()
o2[0] = o2[0][2:]
o= o1 + o2
for i in o:
    s(f"sudo apt-mark hold {i}")
s("sudo apt upgrade")
