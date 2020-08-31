from django.shortcuts import render
import requests
# Create your views here.
def receceCep (request):
    print("teste")
    if request.method == 'GET' and 'cep' in request.GET: #se recebeu algum cep por get
        cep = request.GET['cep']
        print(request)
        if (len(str(cep))!=8):
            response = "CEP inválido, insira novamente."
        else: #cep valido
            url = "https://viacep.com.br/ws/{}/json/".format(cep)
            res = requests.get(url)

            json=res.json()
            if ("erro" in json):
                response = "CEP inexistente."
            elif (res.status_code==requests.codes.ok):
                response = "O endereço do CEP {} é:".format(cep)
                response += "\n{} - {}, {} - {}.".format(json["logradouro"], json["bairro"], json["localidade"], json["uf"])
            else:
                response = "Problema com a requisição, tente novamente."
    else:
        response= ""
    print(response)
    return render(request, "main.html", {"res": response})