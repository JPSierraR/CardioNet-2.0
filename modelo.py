import pandas as pd
import pickle

def Random_forest(Edad, Sexo, Tipo_dolor_pecho, Presion_sanguinea, Colesterol, Glucosa_en_sangre_mayor_120, Resultados_EKG, Frecuencia_cardiaca_max, Angina_de_esfuerzo, Depresion_ST, Inclinacion_ST, Numero_de_vasos_fluor):
    # Crear el diccionario con nombres de columnas
    datos = {
        'Edad': [Edad],
        'Sexo': [Sexo],
        'Tipo_dolor_pecho': [Tipo_dolor_pecho],
        'Presion_sanguinea': [Presion_sanguinea],
        'Colesterol': [Colesterol],
        'Glucosa_en_sangre_mayor_120': [Glucosa_en_sangre_mayor_120],
        'Resultados_EKG': [Resultados_EKG],
        'Frecuencia_cardiaca_max': [Frecuencia_cardiaca_max],
        'Angina_de_esfuerzo': [Angina_de_esfuerzo],
        'Depresion_ST': [Depresion_ST],
        'Inclinacion_ST': [Inclinacion_ST],
        'Numero_de_vasos_fluor': [Numero_de_vasos_fluor]
    }

    # Crear DataFrame a partir del diccionario
    df = pd.DataFrame(datos)

    # Cargar el modelo y objetos necesarios
    filename = 'modelo_clas_rf.pkl'
    modelTree, labelencoder, variables = pickle.load(open(filename, 'rb'))

    # Realizar predicciones
    Y_fut = modelTree.predict(df[variables])

    #print("Resultados de predicción:")
    #print(Y_fut)
    return Y_fut[0]

if __name__ == "__main__":
    # Valores de ejemplo para prueba
    Edad = 70
    Sexo = 1
    Tipo_dolor_pecho = 4
    Presion_sanguinea = 160
    Colesterol = 230
    Glucosa_en_sangre_mayor_120 = 1
    Resultados_EKG = 2
    Frecuencia_cardiaca_max = 110
    Angina_de_esfuerzo = 1
    Depresion_ST = 1
    Inclinacion_ST = 1
    Numero_de_vasos_fluor = 1

    # Llamar a la función con los valores de prueba
    prediccion = Random_forest(Edad, Sexo, Tipo_dolor_pecho, Presion_sanguinea, Colesterol, Glucosa_en_sangre_mayor_120, Resultados_EKG, Frecuencia_cardiaca_max, Angina_de_esfuerzo, Depresion_ST, Inclinacion_ST, Numero_de_vasos_fluor)

    # Mostrar el resultado
    print("Predicción:", prediccion)
