def escribir_en_archivo(texto):
    try:
        if not isinstance(texto, str):
            raise TypeError("Se esperaba una cadena de texto. No se pudo escribir el entero")
        
        with open("texto.txt", "w") as archivo:
            archivo.write(texto)
        print("Operación de escritura completada")
    except TypeError as e:
        print("Error:", e)
    except IOError as e:
        print("Error de E/S:", e)
    except Exception as e:
        print("Ocurrió un error:", e)

texto_a_escribir = 5
escribir_en_archivo(str(texto_a_escribir))  
