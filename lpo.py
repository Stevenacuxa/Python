from urllib import request
from urllib.error import URLError
lpo = {"coño":0, "bobo":0, "culiao":0, "pinche":0, "estupido":0, "estupida":0}

def verificar_web (url):
    try:
        f = request.urlopen(url)
    except URLError:
        return('La url ' + url + ' no existe!')
    else:
        aux = f.read()
        contenido = aux.split()
        #palabras_encontradas = []
        cantidad_po = 0 
        for l in lpo:
            for con in contenido:
                if l in con.decode() :
                    #palabras_encontradas.append(l)
                    lpo[l] = lpo[l] +1
        #return palabras_encontradas

url = 'https://es.wiktionary.org/wiki/Wikcionario:Insultos_regionales'
print("\n----------------------------------------\n")
print("\nInforme de sitio:")
print(verificar_web(url))
print(lpo)