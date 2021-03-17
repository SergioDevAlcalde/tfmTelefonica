# tfmTelefonica


## Que tecnologias necesitas tener instaladas?

```bash
docker
```

```bash
python en su version 3.7 o superior
```

```bash
Tu IDE o editor de cogido favorito 
```


## Instalacion del docker con la base de datos.

Con docker instalado, ejecutamos el siguiente comando:
 
```bash
docker pull mongo 
```
Una vez termine. vamos a la carpeta donde tenemos clonado el proyecto, y dentro de la carpeta docker ejecutamos el siguiente comando:

```bash
docker compose up -d 
```

## Librerias necesarias de python.

Se necesita pymongo para acceder a la informacion de la base de datos. Con anaconda se instala de la siguiente forma:

```bash
conda install -c anaconda pymongo
```

Para ejecutar la carga:
1. archivo "carga-inicial proceso.py" ejecuta la carga desde ficheros csv de carpeta "cotz" a base de MongoDB.
   Estos ficheros contienen cotizaciones desde 2014/09/17 hasta 2021/01/06. 
2. archivo "acceso-web proceso.py" ejecuta la carga desde web "yahoo finance" de datos de cotización diarios, 
   es para ejecución periódica que actualice BBDD. ( no es necesaria para modelaje de datos).
3. archivo "carga-inicial critomonedas.py" ejecuta la carga desde ficheros csv de carpeta "critomoneda cotz" a base de MongoDB.
   Estos ficheros contienen cotizaciones desde comienzo de registro de cada criptomoneda hasta 2021/01/06. 
4. archivo "acceso-web critomoneda.py" ejecuta la carga desde web "yahoo finance" de datos de cotización diarios, 
   es para ejecución periódica que actualice BBDD. ( no es necesaria para modelaje de datos).
5. archivo "acceso_criptomonedas d200316.ipynb" , se trata de un "jupyter notebook" con la recuperación de datos cargados
   en MongoDB para estudiar realaciones de bitcoin con tecnológicas.( si se ejecuta paso 4, y 5 si se quiere, se puede 
   ejecutar parte explicada en ANEXO I.odt)
