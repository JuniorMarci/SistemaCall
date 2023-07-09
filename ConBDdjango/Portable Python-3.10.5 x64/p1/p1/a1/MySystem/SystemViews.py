# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models import Chamada, Agente, Interlocutor
from django.core.paginator import Paginator
from datetime import timedelta

def sv1(request):

    '''

    from datetime import datetime, timedelta

    if request.method == "POST":
        inicio = "20/04/2008 10:20"
        duracao = "18:00"
        arquivo = "audio5.mp3"
        agentes = ['55769099', '55198088']
        interlocutores = ['55117399', '55123088']
        servico = "N/D"
        habilidades = "32009"
        id_chamada = "0000535345345"

        chamada = Chamada()
        chamada.inicio_chamada = datetime.strptime(inicio, "%d/%m/%Y %H:%M")
        chamada.duracao = timedelta(minutes=int(duracao.split(':')[0]), seconds=int(duracao.split(':')[1]))
        chamada.servico = servico
        chamada.habilidades = habilidades
        chamada.id_chamada = id_chamada
        chamada.arquivo = arquivo
        chamada.save()

        # Adicionar agentes à chamada
        for agente in agentes:
            obj_agente, created = Agente.objects.get_or_create(nome=agente)
            chamada.agentes.add(obj_agente)

        # Adicionar interlocutores à chamada
        for interlocutor in interlocutores:
            obj_interlocutor, created = Interlocutor.objects.get_or_create(nome=interlocutor)
            chamada.interlocutores.add(obj_interlocutor)

        '''

    chamadas = Chamada.objects.all()



    if request.method == "POST":
            agente_filtrado = request.POST.get('agente_filtrado')

            if agente_filtrado:
                chamadas = Chamada.objects.filter(agentes__nome__icontains=agente_filtrado)
            else:
                chamadas = Chamada.objects.all()

            interlocutor_filtrado = request.POST.get('interlocutor_filtrado')

            if interlocutor_filtrado:
                chamadas = Chamada.objects.filter(interlocutores__nome__icontains=interlocutor_filtrado)
            else:
                chamadas = Chamada.objects.all()

            habilidade_filtrada = request.POST.get('habilidade_filtrada')

            if habilidade_filtrada:
                chamadas = Chamada.objects.filter(habilidades__icontains=habilidade_filtrada)
            else:
                chamadas = Chamada.objects.all()

            idchamada_filtrado = request.POST.get('idchamada_filtrado')

            if idchamada_filtrado:
                chamadas = Chamada.objects.filter(id_chamada__icontains=idchamada_filtrado)
            else:
                chamadas = Chamada.objects.all()


            maiores_filtrado = request.POST.get('maiores_filtrado')

            if maiores_filtrado:
                maiores_filtrado = int(maiores_filtrado)
                chamadas = Chamada.objects.filter(duracao__gt=timedelta(seconds=maiores_filtrado))
            else:
                chamadas = Chamada.objects.all()

            menores_filtrado = request.POST.get('menores_filtrado')

            if menores_filtrado:
                menores_filtrado = int(menores_filtrado)
                chamadas = Chamada.objects.filter(duracao__lt=timedelta(seconds=menores_filtrado))
            else:
                chamadas = Chamada.objects.all()





    # Cria uma instância do Paginator com todas as chamadas e o número de itens por página
    paginator = Paginator(chamadas, 3)

    # Obtém o número da página a ser exibida
    numero_pagina = request.GET.get('pagina')

    try:
        # Obtém a página atual com base no número da página
        pagina_atual = paginator.get_page(numero_pagina)
    except EmptyPage:
        # Lida com uma página inexistente, redireciona ou exibe uma mensagem de erro
        return HttpResponse('Página inválida')


    return render(request, 'TemplatesSystem/TS.html', {'pagina_atual': pagina_atual})

    #return render(request, 'TemplatesSystem/TS.html', {'itens': Chamada.objects.all(),'var':"MSG!"})
