from django.shortcuts import render

from cargobr.carga.forms import CargaForm


def cargaView(request):
    form = CargaForm(request.POST or None)
    context = {'form': form, 'title': 'Preencha os campos abaixo para cadastrar uma carga' }
    if form.is_valid():
        form.save()
        context = {'title': 'Carga cadastrada com sucesso!'}

    return render(request, 'carga.html', context)
