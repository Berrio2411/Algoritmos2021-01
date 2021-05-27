def contarPalabrasV2(parrafo):
  '''Esta funcion describe cuantas veces 
    aparace cada palabra en una parrafo
    utilizando otro for
  '''
  dictPalabrasOcurrencias = {}
  listaPalabras = parrafo.split()
  for palabra in listaPalabras:
    dictPalabrasOcurrencias[palabra] = 0
    for i in range (len(listaPalabras)):
      if palabra == listaPalabras[i]:
        dictPalabrasOcurrencias[palabra] += 1
  return dictPalabrasOcurrencias
