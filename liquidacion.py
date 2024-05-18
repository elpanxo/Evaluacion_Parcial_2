# Solicitar al usuario que ingrese el nombre, el sueldo base y las horas extra trabajadas del trabajador y devolver los datos ingresados
def ingreso_datos():
    nombre = input("Ingrese el nombre del trabajador: ")
    sueldo_base = float(input("Ingrese el sueldo base del trabajador: "))
    horas_extra = float(input("Ingrese las horas extra trabajadas en el mes: "))
    return nombre, sueldo_base, horas_extra

# Definir la función para calcular la liquidación del sueldo
def calcular_liquidacion(sueldo_base, horas_extra):
    pago_horas_extra = horas_extra * (sueldo_base / 160) * 1.5  # Calcular el pago por horas extra, multiplicando las horas extra por una tasa
    total_ingresos = sueldo_base + pago_horas_extra  # Calcular el total de ingresos sumando el sueldo base y el pago por horas extra
    descuento_fonasa = total_ingresos * 0.07  # Calcular el descuento de Fonasa, que es el 7% de los ingresos totales
    descuento_afp = (sueldo_base + pago_horas_extra) * 0.10  # Calcular el descuento de AFP, que es el 10% del sueldo base más el pago por horas extra
    sueldo_neto = total_ingresos - descuento_fonasa - descuento_afp  # Calcular el sueldo neto restando los descuentos del total de ingresos
    return pago_horas_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto  # Devolver los datos ingresados 

# Definir la función para mostrar la liquidación del sueldo e imprimir cada datos ingresado
def mostrar_liquidacion(nombre, sueldo_base, pago_horas_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto):
    print("--- Liquidación de sueldo ---")
    print("Nombre del trabajador:", nombre)
    print("Sueldo base:", sueldo_base)
    print("Pago por horas extra trabajadas:", pago_horas_extra)
    print("Total ingresos:", total_ingresos)
    print("Descuento Fonasa:", descuento_fonasa)
    print("Descuento AFP:", descuento_afp)
    print(f"Sueldo neto a pagar: {sueldo_neto:,.0f}")

def generar_archivo(nombre, sueldo_base, pago_horas_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto):
    with open("liquidacion_sueldo.txt", "w") as archivo:
        archivo.write("--- Liquidación de sueldo ---\n")
        archivo.write(f"Nombre del trabajador: {nombre}\n")
        archivo.write(f"Sueldo base: {sueldo_base}\n")
        archivo.write(f"Pago por horas extra: {pago_horas_extra}\n")
        archivo.write(f"Total ingresos: {total_ingresos}\n")
        archivo.write(f"Descuento Fonasa: {descuento_fonasa}\n")
        archivo.write(f"Descuento AFP: {descuento_afp}\n")
        archivo.write(f"Sueldo neto a pagar: {sueldo_neto:,.0f}\n") 
        
        # Imprimir mensaje de confirmación en la consola
        print("Los datos de la liquidación de sueldo se han guardado en el archivo *liquidacion_sueldo.txt*")

# Llamar a la función ingreso_datos() para obtener los datos del trabajador
nombre, sueldo_base, horas_extra = ingreso_datos()
pago_horas_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto = calcular_liquidacion(sueldo_base, horas_extra)
# Llamar a la función mostrar_liquidacion() para calcular los detalles de la liquidación
mostrar_liquidacion(nombre, sueldo_base, pago_horas_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto)
# Llamar a la función mostrar_liquidacion() para mostrar los resultados en la consola
generar_archivo(nombre, sueldo_base, pago_horas_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto)
