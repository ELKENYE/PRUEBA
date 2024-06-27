listadelibros = ()
listadeautores = ()
listadegeneros = ()
precioenvio = 3000
preciounitariolibro=20000
iva = 600
preciofinal = preciounitariolibro+precioenvio
preciofinaliva = preciounitariolibro+precioenvio+iva
stockdeventas={




}
try:
    while True:
        print("--------------------------------------------------------------------------------------------------------")
        print("1.Registrar Libro")
        print("2.Lista De Todos Los Libros")
        print("3.Registrar Ventas")
        print("4.Imprimir Reporte De Ventas ")
        print("5.Generar Txt")
        print("0.Salir Del Programa")
        op=int(input("Ingrese una opcion"))
        if op==1:
            print("----------------------REGISTRAR LIBRO----------------------")
            print("Ingrese un libro que desea agregar (Recuerde que tiene que tener: Título, Autor, Género )")
            listadelibros = input("Ingrese el titulo del libro")
            listadeautores = input("Ingrese el Autor del libro")
            listadegeneros = input("Ingrese el Genero del libro")
        elif op==2:
            print("----------------------LISTA DE TODOS LOS LIBROS----------------------")
            print("Lista de libros:")
            print(listadelibros)
            print(listadeautores)
            print(listadelibros)
        elif op==3:
            print("----------------------REGISTRAR VENTAS----------------------")
            librocomprado = input("Ingrese el nombre del libro que desea comprar")
            print("EL PRECIO DE EL LIBRO ", {preciounitariolibro})
            print("EL PRECIO MAS ENVIO: ",{preciofinal})
            print("SU COMPRA ESTA EN PROCESO....")
            print("----------------------BOLETA FINAL----------------------")
            print("PRECIO DEL LIBRO",{preciounitariolibro})
            print("PRECIO DEL ENVIO",{precioenvio})
            print("PRECIO DEL IVA",{iva})
            print("PRECIO DEL PRECIO FINAL",{preciofinaliva})
        elif op==4:
            print("----------------------IMPRIMIR REPORTE DE VENTAS----------------------")
            print("INGRESE UN GENERO PARA EL REPORTE DE VENTAS")
            op2 = int(input("¿desea ingresar un genero en especifico? 1.si/2.no"))
            if op2==1:
                elegirgenero=("ingrese el genero que desea el reporte".lower)
                if elegirgenero=="ACCION":
                    print("----------------------IMPRIMIR REPORTE DE VENTAS----------------------")
                    print("EL ESTOCK DISPONIBLE ES DE." , {})
                elif elegirgenero=="TERROR":
                    print("----------------------IMPRIMIR REPORTE DE VENTAS----------------------")
                    print("EL ESTOCK DISPONIBLE ES DE." , {})
                elif elegirgenero=="ROMANCE":
                    print("----------------------IMPRIMIR REPORTE DE VENTAS----------------------")
                    print("EL ESTOCK DISPONIBLE ES DE." , {})
                elif elegirgenero=="AVENTURA":
                    print("----------------------IMPRIMIR REPORTE DE VENTAS----------------------")
                    print("EL ESTOCK DISPONIBLE ES DE." , {})
            elif op2==2:
                print("1.ACCION")
                print("2.TERROR")
                print("3.ROMACE")
                print("4.SUSPENSO")
                print("5.AVENTURA")
            op3= int(input("INGRESE UNA OPCION DE GENERO"))
            if op2==1:
                print("----------------------IMPRIMIR REPORTE DE VENTAS----------------------")
                print("EL ESTOCK DISPONIBLE ES DE." , {})
            elif op2==2:
                print("----------------------IMPRIMIR REPORTE DE VENTAS----------------------")
                print("EL ESTOCK DISPONIBLE ES DE." , {})
            elif op2==3:
                print("----------------------IMPRIMIR REPORTE DE VENTAS----------------------")
                print("EL ESTOCK DISPONIBLE ES DE." , {})
            elif op2==4:
                print("----------------------IMPRIMIR REPORTE DE VENTAS----------------------")
                print("EL ESTOCK DISPONIBLE ES DE." , {})
            elif op2==5:
                print("----------------------IMPRIMIR REPORTE DE VENTAS----------------------")
                print("EL ESTOCK DISPONIBLE ES DE." , {})
        elif op==5:
            print("----------------------GENERAR TXT----------------------")
            
        elif op==0:
            print("----------------------SALISTE----------------------")
except:
    print("INGRESE UNA OPCION VALIDA")
#>:3
