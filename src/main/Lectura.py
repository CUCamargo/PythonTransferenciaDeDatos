import requests;


class LecturaArchivos:

    def lectura(self):
        self.palabras = []
        try:
            fichero = open("Clientes.txt", "r")
            lineas = fichero.read()
            word = []
            word = lineas.split(",")
            while lineas != '':
                self.palabras.append(lineas)
                lineas = fichero.readline()

            print(word)

            if len(word)>0:
                tam = int(len(word))
                tam = (tam/5)
            for i in range(int(tam)):
                print(i)
                if i >0:
                    self.empleado = {'surname': word[i*5+1], 'firstname': word[i*5]}
                    respEmp = requests.post('http://localhost:8080/servicios/anadirempleado', data=self.empleado)
                    respEmp.json()

                    self.aeropuerto = {'name': word[i*5+4]}
                    respAir = requests.post('http://localhost:8080/servicios/añadirairport', data=self.aeropuerto)
                    respAir.json()

                    self.pais = {'name': word[i*5+2]}
                    respPais = requests.post('http://localhost:8080/servicios/añadirpais', data=self.pais)
                    respPais.json()

                    self.idioma = {'name': word[i*5+3]}
                    respIdiom = requests.post('http://localhost:8080/servicios/añadirlenguajes', data=self.idioma)
                    respIdiom.json()
                else:
                    self.empleado = {'surname': word[i+1], 'firstname': word[i+0]}
                    respEmp = requests.post('http://localhost:8080/servicios/anadirempleado', data=self.empleado)
                    respEmp.json()

                    self.aeropuerto = {'name': word[i+4]}
                    respAir = requests.post('http://localhost:8080/servicios/añadirairport', data=self.aeropuerto)
                    respAir.json()

                    self.pais = {'name': word[i+2]}
                    respPais = requests.post('http://localhost:8080/servicios/añadirpais', data=self.pais)
                    respPais.json()

                    self.idioma = {'name': word[i+3]}
                    respIdiom = requests.post('http://localhost:8080/servicios/añadirlenguajes', data=self.idioma)
                    respIdiom.json()

            #else:print("El documento no tiene informarción")
        except FileNotFoundError:
            print("FileNotFoundError. El archivo no existe")
            input()

eje = LecturaArchivos();
eje.lectura();