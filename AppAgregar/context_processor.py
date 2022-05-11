"""
def importe_total(request):
    total=0.0
    if request.user.is_authenticated:
        if "agregar" in request.session.keys():
                for key, value in request.session['agregar'].items():
                        total=total+(float(value['precio']) * value ['cantidad'])
    return {'importe_total': total}
"""