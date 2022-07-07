class AgregarV:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        agregarv = self.session.get("agregarv")
        if not agregarv:
            agregarv = self.session["agregarv"] = {}
        self.agregarv = agregarv

    def add(self, articulo):
        a = 1
        if (str(articulo.id_articulo) not in self.agregarv.keys()):
            self.agregarv[articulo.id_articulo] = {
                "articulo_id": articulo.id_articulo,
                "nombre": articulo.nombre,
                "cantidad": a,
                "totalcant": a*articulo.precio*21/100+articulo.precio,
                "precio": str(articulo.precio),
                "subtotal": float(articulo.precio)*float(a),
            }
        else:
            for key, value in self.agregarv.items():
                if key == str(articulo.id_articulo):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"] = float(value["precio"])
                    value["subtotal"] = float(value["subtotal"])+articulo.precio
                    value["totalcant"] = float(value["totalcant"])+articulo.precio*1.21
                    break 
        self.save()

    def save(self):
        self.session["agregarv"] = self.agregarv
        self.session.modified = True

    def remove(self, articulo):
        articulo_id = str(articulo.id_articulo)
        if articulo_id in self.agregarv:
            del self.agregarv[articulo_id]
            self.save()
        
    def decrement(self, articulo):
        for key, value in self.agregarv.items():
            if key == str(articulo.id_articulo):
                value["cantidad"] = value["cantidad"] - 1
                value["subtotal"] = float(value["subtotal"])-articulo.precio
                value["totalcant"] = float(value["totalcant"])-articulo.precio*1.21
                if value["cantidad"] < 1:
                    self.remove(articulo)
                else:
                    self.save()
                break
            else:
                print("El articulo no existe")

    def clear(self):
        self.session["agregarv"] = {}
        self.session.modified = True
            
