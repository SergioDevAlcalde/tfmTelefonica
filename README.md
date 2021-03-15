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

Para ejecutar la carga, ejecutariamos el scrip de pythgon de acceso-webv2.py. De esta forma ya tendriamos una primera carga de datos. 

Luego tendriamos que ejecutar el cuaderno de jupyter e ir viendo los distintos grafos.