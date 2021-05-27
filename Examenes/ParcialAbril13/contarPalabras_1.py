def contarPalabrasV1(parrafo):
  '''Esta funcion describe cuantas veces 
    aparace cada palabra en una parrafo
    utilizando la instrucción count
  '''
  dictPalabrasOcurrencias = {}
  listaPalabras = parrafo.split()
  for palabra in listaPalabras:
    dictPalabrasOcurrencias[palabra] = listaPalabras.count(palabra)
  return dictPalabrasOcurrencias