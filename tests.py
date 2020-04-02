import unittest
from call import callMedianteJson 
import app as app

class tests(unittest.TestCase):

    #Test para comprobar que la llamada a los datos se hace de forma correcta
    def test_llamada(self):
        try:
            callMedianteJson(24)
        except ExceptionType:
            self.fail("No se han accedido a los datos de la llamada de forma correcta, ERRROR")

    #Esta test esta centrado en la APIREST.
    #Test para el indice, comprobamos que no hay error.
    def test_index(self):
        response,ok=app.index()
        self.assertEqual(ok, 200)
    
    #Test para la prediccion de 24 horas
    def test_24horas(self):
        response,ok=app.call24horas()
        self.assertEqual(ok, 200)
    
    #Test para la prediccion de 48 horas
    def test_48horas(self):
        response,ok=app.call48horas()
        self.assertEqual(ok, 200)
    
    #Test para la prediccion de 72 horas
    def test_72horas(self):
        response,ok=app.call72horas()
        self.assertEqual(ok, 200)
    

if __name__ == '__main__':
    unittest.main()