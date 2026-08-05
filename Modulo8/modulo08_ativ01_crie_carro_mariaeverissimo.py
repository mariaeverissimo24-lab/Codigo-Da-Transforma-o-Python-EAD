class Carro:
    def __init_(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo 

    def exibir_info(self):
        return f"Marca: {self.marca} | Modelo:
{self.modelo}"

 # meu_carro = Carro("Chevrolet", "Camaro")
 meu_carro = Carro("Ford", "Mustang")
print(meu_carro.exibir_info())
