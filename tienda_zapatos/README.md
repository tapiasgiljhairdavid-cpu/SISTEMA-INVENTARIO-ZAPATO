# Sistema de Inventario de Zapatos

## 1. Informacion del proyecto

- Estudiante: Jahir Tapia
- Asignatura: Acceso a Datos
- Lenguaje: Python
- ORM: SQLAlchemy
- Base de datos: SQLite

## 2. Descripcion

Este programa permite administrar los zapatos de una tienda desde la consola.

Se pueden registrar zapatos con su modelo, talla y precio. Tambien permite ver el inventario, buscar por ID, cambiar precios y eliminar registros.

Los datos se guardan en una base de datos llamada `zapateria.db`.

## 3. Archivos del proyecto

```text
tienda_zapatos/
├── main.py
├── datos.py
├── requirements.txt
├── README.md
└── evidencias/
```

- `main.py`: muestra el menu y recibe los datos.
- `datos.py`: contiene la conexion con SQLite, el modelo Zapato y las funciones CRUD.
- `requirements.txt`: contiene la libreria SQLAlchemy.
- `zapateria.db`: archivo donde se guardan los zapatos. Se crea al ejecutar el programa.
- `evidencias/`: carpeta para guardar las capturas de las pruebas.

## 4. Instalacion y ejecucion

Abre la carpeta del proyecto en Visual Studio Code.

Instala la dependencia con este comando:

```bash
python -m pip install -r requirements.txt
```

Despues ejecuta el programa:

```bash
python main.py
```

Al iniciar se crea la base de datos y la tabla si todavia no existen. Luego aparece el menu para administrar los zapatos.

## 5. Respuestas a las preguntas

### Pregunta 1. Que clase de Python representa la tabla?

La clase `Zapato` representa la tabla de la base de datos. Esta clase hereda de `Base`.

SQLAlchemy identifica el nombre de la tabla con `__tablename__ = "zapatos"`. Sus columnas se definen con `mapped_column`.

El modelo tiene cuatro campos:

- `id`: es la clave primaria y se genera automaticamente.
- `modelo`: guarda el nombre del zapato.
- `talla`: guarda la talla.
- `precio`: guarda el precio.

Cada objeto de la clase `Zapato` representa un registro de la tabla.

### Pregunta 2. Que ocurre al ejecutar el programa por primera vez?

Cuando se ejecuta `main.py` se llama a `inicializar_bd()`.

Esta funcion usa `Base.metadata.create_all(engine)` para crear la tabla si no existe. La conexion usa el archivo `zapateria.db`.

La primera vez se crea el archivo de la base de datos y la tabla `zapatos`. Si ya existen se usan los datos guardados.

### Pregunta 3. Que recorrido siguen los datos al registrar un zapato?

El usuario selecciona la opcion 1 del menu. Luego escribe el modelo, la talla y el precio.

El programa llama a `crear_zapato()` desde `datos.py`. Esta funcion crea un objeto `Zapato` y abre una sesion con `Session(engine)`.

Despues agrega el objeto con `sesion.add(zapato)` y guarda los datos con `sesion.commit()`. Al terminar devuelve `True` si el registro se guardo correctamente.

### Pregunta 4. Para que sirve una sesion de SQLAlchemy?

La sesion permite trabajar con los datos de la base de datos. Se usa para agregar, consultar, modificar y eliminar registros.

El comando `commit()` confirma los cambios y los guarda en SQLite. Sin este comando los cambios no quedan guardados de forma permanente.

### Pregunta 5. Como funciona la busqueda por ID?

La funcion `buscar_zapato(id_zapato)` usa `sesion.get(Zapato, id_zapato)` para buscar el registro por su ID.

Si el zapato existe devuelve un objeto `Zapato` con sus datos. Si no existe devuelve `None`.

El menu revisa el resultado y muestra el mensaje correspondiente.

### Pregunta 6. Como se actualiza el precio?

La funcion `actualizar_precio()` busca primero el zapato usando su ID.

Si el registro existe cambia el atributo `precio` por el nuevo valor. Luego ejecuta `sesion.commit()` para guardar el cambio.

Si el ID no existe la funcion devuelve `False` y no modifica ningun registro.

### Pregunta 7. Que ocurre al eliminar un zapato?

La funcion `eliminar_zapato()` busca el zapato por su ID.

Si lo encuentra usa `sesion.delete(zapato)` para eliminarlo. Luego ejecuta `sesion.commit()` para confirmar el cambio.

Se puede consultar otra vez el inventario para comprobar que el zapato ya no aparece.

### Pregunta 8. Que pasa cuando se cierra y se vuelve a ejecutar el programa?

Los zapatos siguen guardados porque los cambios se almacenan en el archivo `zapateria.db`.

Cuando se ejecuta el programa otra vez se conecta al mismo archivo. Por eso los registros que no fueron eliminados siguen disponibles.

Esto demuestra que los datos no dependen solamente de la memoria del programa.

## 6. Pruebas y evidencias

Realiza las pruebas en tu computador y guarda las capturas dentro de la carpeta `evidencias`.

Usa estos nombres para organizar las imagenes:

| Nombre de la captura | Prueba |
|---|---|
| `01_registrar.png` | Registrar dos zapatos |
| `02_listar.png` | Mostrar todos los zapatos |
| `03_buscar.png` | Buscar un zapato por ID |
| `04_actualizar.png` | Cambiar el precio y mostrar el nuevo valor |
| `05_eliminar.png` | Eliminar un zapato y comprobar que ya no aparece |
| `06_persistencia.png` | Cerrar y abrir el programa para comprobar que los datos siguen guardados |

### Datos para las pruebas

Puedes registrar estos dos zapatos:

- Modelo: Tenis deportivos. Talla: 40. Precio: 150000.
- Modelo: Zapato casual. Talla: 42. Precio: 120000.

Los ID los genera la base de datos. Revisa el listado para saber que ID tiene cada zapato.

Despues cambia el precio de uno de ellos. Busca el registro o lista el inventario para mostrar el precio nuevo.

Elimina el otro zapato y consulta el inventario para comprobar que ya no aparece.

Por ultimo cierra el programa y ejecutalo otra vez. Muestra que el zapato que quedo sigue guardado.

### Pruebas con un ID que no existe

- Buscar: la funcion devuelve `None` y el menu indica que el zapato no fue encontrado.
- Actualizar: la funcion devuelve `False` y no cambia ningun dato.
- Eliminar: la funcion devuelve `False` y no borra ningun registro.

## 7. Conclusiones

1. Aprendi a usar SQLAlchemy para registrar, consultar, actualizar y eliminar datos.
2. Con el ORM puedo trabajar con objetos de Python sin escribir las consultas SQL manualmente.
3. Aprendi que `commit()` permite guardar los cambios en la base de datos.
4. SQLite permite conservar los zapatos aunque se cierre el programa.

## 8. Antes de entregar

- Verifica que tu nombre este correcto.
- Realiza las seis pruebas.
- Guarda las capturas reales en la carpeta `evidencias`.
- Revisa que las imagenes se vean en GitHub.
- Sube todos los archivos al repositorio.
- Copia el enlace del repositorio y entregalo en Moodle.
