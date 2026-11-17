import datos


def mostrar_zapato(zapato):
    print(
        f"ID: {zapato.id} | "
        f"Modelo: {zapato.modelo} | "
        f"Talla: {zapato.talla} | "
        f"Precio: ${zapato.precio:.2f}"
    )


def main():
    datos.inicializar_bd()

    while True:
        print("\n===== TIENDA DE ZAPATOS =====")
        print("1. Registrar zapato")
        print("2. Listar zapatos")
        print("3. Buscar zapato por ID")
        print("4. Actualizar precio")
        print("5. Eliminar zapato")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                modelo = input("Modelo: ").strip()
                talla = int(input("Talla: "))
                precio = float(input("Precio: "))

                if not modelo or talla <= 0 or precio <= 0:
                    print("Datos no válidos.")
                    continue

                if datos.crear_zapato(modelo, talla, precio):
                    print("Zapato registrado correctamente.")
                else:
                    print("No se pudo registrar.")

            elif opcion == "2":
                zapatos = datos.listar_zapatos()

                if not zapatos:
                    print("No hay zapatos registrados.")
                else:
                    for zapato in zapatos:
                        mostrar_zapato(zapato)

            elif opcion == "3":
                id_zapato = int(input("ID del zapato: "))
                zapato = datos.buscar_zapato(id_zapato)

                if zapato is None:
                    print("Zapato no encontrado.")
                else:
                    mostrar_zapato(zapato)

            elif opcion == "4":
                id_zapato = int(input("ID del zapato: "))
                precio = float(input("Nuevo precio: "))

                if precio <= 0:
                    print("El precio debe ser positivo.")
                    continue

                if datos.actualizar_precio(id_zapato, precio):
                    print("Precio actualizado.")
                else:
                    print("Zapato no encontrado.")

            elif opcion == "5":
                id_zapato = int(input("ID del zapato: "))

                if datos.eliminar_zapato(id_zapato):
                    print("Zapato eliminado.")
                else:
                    print("Zapato no encontrado.")

            elif opcion == "6":
                print("Hasta pronto.")
                break

            else:
                print("Opción no válida.")

        except ValueError:
            print("Error: ingrese valores numéricos válidos.")


if __name__ == "__main__":
    main()
