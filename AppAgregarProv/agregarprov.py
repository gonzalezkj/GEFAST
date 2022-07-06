class Agregarprov:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        agregarprov = self.session.get("agregarprov")
        if not agregarprov:
            agregarprov = self.session["agregarprov"] = {}
        self.agregarprov = agregarprov

    def addprov(self, proveedor):
        if (str(proveedor.id_proveedor) not in self.agregarprov.keys()):
            self.agregarprov = {}
            self.agregarprov[proveedor.id_proveedor] = {
                "proveedor_id": proveedor.id_proveedor,
                "cuit": proveedor.cuit,
                "razon_social": proveedor.razon_social,
                "condicion": proveedor.condicion_id,
            }
        else:
            prov_id = str(proveedor.id_proveedor)
            if prov_id in self.agregarprov:
                del self.agregarprov[prov_id]
                self.saveprov()
        self.saveprov()

    def saveprov(self):
        self.session["agregarprov"] = self.agregarprov
        self.session.modified = True

    def removeprov(self, proveedor):
        prov_id = str(proveedor.id_proveedor)
        if prov_id in self.agregarprov:
            del self.agregarprov[prov_id]
            self.saveprov()

    def clearprov(self):
        self.session["agregarprov"] = {}
        self.session.modified = True
            
