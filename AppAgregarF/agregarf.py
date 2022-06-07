class AgregarF:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        agregarf = self.session.get("agregarf")
        if not agregarf:
            agregarf = self.session["agregarf"] = {}
        self.agregarf = agregarf

    def addf(self, factura):
        if (str(factura.id_tipo_comprobante) not in self.agregarf.keys()):
            self.agregarf = {}
            self.agregarf[factura.id_tipo_comprobante] = {
                "factura_id": factura.id_tipo_comprobante,
                "nombre": factura.nombre,
                "letra": factura.letra,
            }
        self.savef()

    def savef(self):
        self.session["agregarf"] = self.agregarf
        self.session.modified = True

    def clearf(self):
        self.session["agregarf"] = {}
        self.session.modified = True
            
