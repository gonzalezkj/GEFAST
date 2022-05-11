class Agregarcli:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        agregarcli = self.session.get("agregarcli")
        if not agregarcli:
            agregarcli = self.session["agregarcli"] = {}
        self.agregarcli = agregarcli

    def addcli(self, cliente):
        if (str(cliente.id_cliente) not in self.agregarcli.keys()):
            self.agregarcli = {}
            self.agregarcli[cliente.id_cliente] = {
                "cliente_id": cliente.id_cliente,
                "cuit": cliente.cuit,
                "razon_nombre": cliente.razon_nombre,
                "condicion": cliente.condicion_id,
            }
        else:
            cliente_id = str(cliente.id_cliente)
            if cliente_id in self.agregarcli:
                del self.agregarcli[cliente_id]
                self.savecli()
        self.savecli()

    def savecli(self):
        self.session["agregarcli"] = self.agregarcli
        self.session.modified = True

    def removecli(self, cliente):
        cliente_id = str(cliente.id_cliente)
        if cliente_id in self.agregarcli:
            del self.agregarcli[cliente_id]
            self.savecli()

    def clearcli(self):
        self.session["agregarcli"] = {}
        self.session.modified = True
            
