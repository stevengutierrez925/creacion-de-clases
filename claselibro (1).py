class libro:
    def __init__(self, titulo, autor, genero, paginas):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.paginas = paginas

    def obtener_titulo(self):
        return self.titulo

    def establecer_titulo(self, titulo):
        self.titulo = titulo

    def obtener_autor(self):
        return self.autor

    def establecer_autor(self, autor):
        self.autor = autor

    def obtener_genero(self):
        return self.genero

    def establecer_genero(self, genero):
        self.genero = genero

    def obtener_paginas(self):
        return self.paginas

    def establecer_paginas(self, paginas):
        self.paginas = paginas

    def es_ficcion(self):
        genero = self.genero.lower()
        return "ficcion" in genero or "novela" in genero


if __name__ == "__main__":
    l = libro("el hobbit", "tolkien", "ficcion fantastica", 310)
    print("es ficcion?", l.es_ficcion())
