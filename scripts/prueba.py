class Pato:
    def hablar(self):
        print("Cua!")


def llama_hablar(y):
    y.hablar()


class Animal:
    def numero(self, x):
        print(x)


p = Pato()
p.hablar()
llama_hablar(p)
a = Animal()
a.numero(2)
