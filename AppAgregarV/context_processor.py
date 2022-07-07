def importe_total(request):
    total=0.0
    if request.user.is_authenticated:
        if "agregarv" in request.session.keys():
                for key, value in request.session['agregarv'].items():
                        total=total+value['totalcant']
    return {'totalventaIVA': total}

def importe_totalsiniva(request):
    total=0.0
    if request.user.is_authenticated:
        if "agregarv" in request.session.keys():
                for key, value in request.session['agregarv'].items():
                        total=total+value['subtotal']
    return {'totalventa': total}