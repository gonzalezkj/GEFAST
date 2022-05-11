class Agregar:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        agregar = self.session.get("agregar")
        if not agregar:
            agregar = self.session["agregar"] = {}
        self.agregar = agregar

    def add(self, articulo):
        if (str(articulo.id_articulo) not in self.agregar.keys()):
            self.agregar[articulo.id_articulo] = {
                "articulo_id": articulo.id_articulo,
                "nombre": articulo.nombre,
                "cantidad": articulo.cantidad,
                "precio": str(articulo.precio),
                "subtotal": float(articulo.precio)*float(articulo.cantidad),
            }
        else:
            for key, value in self.agregar.items():
                if key == str(articulo.id_articulo):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"]=float(value["precio"])
                    value["subtotal"]=float(value["subtotal"])+articulo.precio
                    break 
        self.save()

    def save(self):
        self.session["agregar"] = self.agregar
        self.session.modified = True

    def remove(self, articulo):
        articulo_id = str(articulo.id_articulo)
        if articulo_id in self.agregar:
            del self.agregar[articulo_id]
            self.save()
        
    def decrement(self, articulo):
        for key, value in self.agregar.items():
            if key == str(articulo.id_articulo):
                value["cantidad"] = value["cantidad"] - 1
                value["subtotal"]=float(value["subtotal"])-articulo.precio
                if value["cantidad"] < 1:
                    self.remove(articulo)
                else:
                    self.save()
                break
            else:
                print("El articulo no existe")

    def clear(self):
        self.session["agregar"] = {}
        self.session.modified = True
            
