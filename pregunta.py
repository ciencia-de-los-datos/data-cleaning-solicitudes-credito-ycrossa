"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df.drop(['Unnamed: 0'], axis=1, inplace = True)
    df.dropna(inplace = True)

    txt_cols = ["sexo", "tipo_de_emprendimiento", "idea_negocio","barrio","línea_credito"]
    for col in txt_cols:
        df[col]=df[col].str.lower()
        df[col] = df[col].apply(lambda x: str(x).replace("-"," ").replace("_"," "))
    
    df["comuna_ciudadano"] = df["comuna_ciudadano"].fillna(0).astype(int)
    df["fecha_de_beneficio"] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst=True, format='mixed')
    df["monto_del_credito"] = df["monto_del_credito"].apply(lambda x: str(x).strip("$").strip().replace(".00","").replace(",",""))
    
    df.drop_duplicates(inplace = True)
    return df


#print(clean_data().sexo.value_counts().to_list())