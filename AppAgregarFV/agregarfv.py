class AgregarFV:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        agregarfv = self.session.get("agregarfv")
        if not agregarfv:
            agregarfv = self.session["agregarfv"] = {}
        self.agregarfv = agregarfv

    def addfv(self, factura):
        if (str(factura.id_tipo_comprobante) not in self.agregarfv.keys()):
            self.agregarfv = {}
            self.agregarfv[factura.id_tipo_comprobante] = {
                "factura_id": factura.id_tipo_comprobante,
                "nombre": factura.nombre,
                "letra": factura.letra,
            }
        self.savefv()

    def savefv(self):
        self.session["agregarfv"] = self.agregarfv
        self.session.modified = True

    def clearfv(self):
        self.session["agregarfv"] = {}
        self.session.modified = True
            
