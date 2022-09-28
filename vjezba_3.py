# varijabla - vjezba 2 input i autput

ime = input("Unesi svoje ime: ")

print("Pozdrav, " + ime)

a = int(input("Unesi broj a: "))
b = int(input("Unesi broj b: "))

zbroj = a+b
razlika = a-b
umnožak = a*b
djeljenje=a/b
print("zbroj brojeva {0} i {1} iznosi {2}".format(a, b, zbroj ))
print("Razlika brojeva {0} i {1} iznosi {2}".format(a, b, razlika ))
print("Umnožak brojeva {0} i {1} iznosi {2}".format(a, b, umnožak ))
print("Djeljenje brojeva {0} i {1} iznosi {2}".format(a, b, djeljenje ))
