def importe_total(request):
    total=0.0
    if request.user.is_authenticated:
        if "agregar" in request.session.keys():
                for key, value in request.session['agregar'].items():
                        total=total+value['totalcant']
    return {'importe_total': total}

def importe_totalsiniva(request):
    total=0.0
    if request.user.is_authenticated:
        if "agregar" in request.session.keys():
                for key, value in request.session['agregar'].items():
                        total=total+value['subtotal']
    return {'totalsiniva': total}