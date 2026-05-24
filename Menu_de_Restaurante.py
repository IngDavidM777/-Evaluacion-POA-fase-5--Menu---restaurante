#sistema Menu-Restaurante , promocion descuento.
#David_Geovany_Achicanoy_Meneses
#Grupo_213022B_2201
#Programa: Ingenieria_de_Sistemas
#Codigo_Fuente:David_Meneses_(autor)

# matriz de productos 
menu = [
    ["Consome de Pollo", "Sopas y Cremas", 9000],
    ["Alitas BBQ", "Comida rapida", 20000],
    ["Hamburguesa Vegetariana", "Comida Saludable", 18000],
    ["Jugo Natural", "Bebida", 7000],
    ["Salmon al Ajillo", "Pescados y Mariscos", 25000],
    ["Brwonie con Helado", "postres", 12000],
]
# variables de promocion
categoria_objetivo = ("postres", "Pescados y Mariscos")
umbral_precio = 10000
descuento = 15
#funcion calculo precio final aplicando descuento
def calcular_precio_final(producto, categoria_objetivo, umbral_precio, descuento):
    nombre,categoria, precio_base = producto
    if categoria in categoria_objetivo and precio_base > umbral_precio:
        precio_final = precio_base - (precio_base * descuento / 100)
        aplicar_descuento = True
    else:
        precio_final = precio_base
        aplicar_descuento = False
    return precio_final, aplicar_descuento
# Generacion de resumen
print("MENU DE RESTAURANTE: Pregunta por nuestra PROMOCIÓN!!")
for producto in menu:
    nombre, categoria, precio_base = producto
    precio_final, aplicar_descuento = calcular_precio_final(
        producto, categoria_objetivo, umbral_precio, descuento
    )
# salidas muestra de resultados
    print(f"producto: {nombre}")
    print(f"categoria: {categoria}")
    print(f"precio base: ${precio_base} COP")
    if aplicar_descuento:
        print(f"Descuento Aplicado: {descuento}%")
    else:
        print("Descuento Aplicado: No Aplica")
    print(f"Precio Final: ${int(precio_final)} COP")
    print("Gracias por elegir esta promocion.")
    print("_" * 30)
    
 ###########################################
  