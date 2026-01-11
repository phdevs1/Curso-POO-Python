from celulares import Celular, Celular1, Celular3, Celular4

cel = Celular()
print(cel)

cel1 = Celular1("Huawei", "T1")
print(cel1.marca)

cel2 = Celular3("Iphone", "I13")
print(cel2.marca)
print(cel2.chip)

cel3 = Celular3("Aora", "XX12")
print(cel3.marca)
print(cel3.chip)


cel4 = Celular4("Samsung", "S34")
print("celular4: ", cel4)
print("celular4: ", cel4.marca)
print("celular4: ", cel4.modelo)


# <celular.Celular object at 0x7ff103ffdfd0>
#  imprime celular porque dice que la clase viene del modulo celular
# <__main__.Celular object at 0x7b6725d02090>
#  aparece main porque el objeto pertence al archivo principal, y se ejecuta ahi
