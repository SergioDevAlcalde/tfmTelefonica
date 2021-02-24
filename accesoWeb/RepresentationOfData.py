from accesoWeb.GetData import *


def representData():
    goog = getDataByOneCollection("tfmTelefonica", "Google")
    amazon = getDataByOneCollection("tfmTelefonica", "Amazon")
    facebook = getDataByOneCollection("tfmTelefonica", "Facebook")
    microsoft = getDataByOneCollection("tfmTelefonica", "Microsoft")
    bitcoinEur = getDataByOneCollection("tfmTelefonica", "Bitcoin_EUR")
    bitcoinUSD = getDataByOneCollection("tfmTelefonica", "Bitcoin_USD")

    # Seleccionamos datos de interes
    goog_cierre = goog[["Date", "Close"]]
    fb_cierre = facebook[["Date", "Close"]]
    amzn_cierre = amazon[["Date", "Close"]]
    msft_cierre = microsoft[["Date", "Close"]]
    btc_usd_cierre = bitcoinUSD[["Date", "Close"]]

    # Renombrar columna de cierre de cada DataFrame, para que no se confundan al hacer el merge
    goog_cierre = goog_cierre.rename(columns={"Close": "CloseGoog"})
    fb_cierre = fb_cierre.rename(columns={"Close": "CloseFb"})
    amzn_cierre = amzn_cierre.rename(columns={"Close": "CloseAmzn"})
    msft_cierre = msft_cierre.rename(columns={"Close": "CloseMsft"})
    btc_usd_cierre = btc_usd_cierre.rename(columns={"Close": "ClosBtcEur"})

    # Establecer el índice en la columna Date para cada archivo

    goog_cierre.set_index('Date', inplace=True)
    fb_cierre.set_index('Date', inplace=True)
    amzn_cierre.set_index('Date', inplace=True)
    msft_cierre.set_index('Date', inplace=True)
    btc_usd_cierre.set_index('Date', inplace=True)

    df_combinado = btc_usd_cierre.join(goog_cierre).join(amzn_cierre).join(fb_cierre).join(msft_cierre)
    df_combinado.head()

    print(df_combinado.describe().transpose())

    logicOfRepresentation(df_combinado)


def logicOfRepresentation(df_combinado):
    # Extracción de las filas y las columnas para usarlas como auxiliaraes para sustituir valores perdidos
    filas = df_combinado.shape[0]
    columnas = df_combinado.shape[1]
    df_combinado_null = df_combinado.isnull()
    ''' Con este par de loops se recorre el dataframe identificandose los valores perdidos y sustituyendolos por el valor de la fila
            anterior, que se corresponde que el valor de cierre para cada compañía el día anterior. 
            La lógica que sigue esta sustitución es la siguiente: Los valores perdidos se corresponden a días donde no hay actividad de 
            las casas de cambio, por lo que el valor asignado se corresponde'''
    for c in range(columnas):
        for f in range(filas):
            if df_combinado_null.iloc[f, c] == True:
                df_combinado.iloc[f, c] = df_combinado.iloc[(f - 1), c]
            else:
                df_combinado.iloc[f, c] = df_combinado.iloc[f, c]
    print(df_combinado.head())


representData()
