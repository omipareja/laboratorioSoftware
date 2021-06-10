from django.db import models

class LibroManager(models.Manager):

    def buscar_libro(self,kword,select):

        if len(kword) == 0:
            return self.all()

        if select == 'isbn':
            return  self.filter(
                isbn__icontains=kword
            )
        if select == 'autor':
            return  self.filter(
                autor__icontains=kword
            )
        if select == 'titulo':
            return  self.filter(
                titulo__icontains=kword
            )
        if select == 'numero_paginas':
            return  self.filter(
                numero_paginas= int(kword)
            )
        if select == 'editorial':
            return  self.filter(
                editorial__icontains=kword
            )
        if select == 'idioma':
            return  self.filter(
                idioma__icontains=kword
            )
        if select == 'estado':
            return  self.filter(
                estado__icontains=kword
            )
        if select == 'precio':
            return  self.filter(
                precio=kword
            )
        if select == 'categoria':
            print('entro')
            return  self.filter(
               categoria__nombre  = kword
            )

    def libros_clientes(self):
        return self.filter(stock__gt= 0)