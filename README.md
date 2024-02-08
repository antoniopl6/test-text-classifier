# Prueba técnica Junior Data Scientist en Factor Energia - Antonio Pintado - antoniopl99612@gmail.com
DESCRIPCIÓN DEL ENTREGABLE:
En la carpeta /prueba se puede ver un notebook el cual ha sido desarrollado para crear el modelo de clasificación (desarrollado en Google Colab),
El objetivo del modelo es clasificar emails en las siguientes categorías:

  0. Solicitudes de ayuda / contacto urgente
  1. Reenvío de facturas
  2. Consulta contratos y documentación
  3. Problemas con el área de clientes y problemas técnicos
  4. Cambios de documentación / titularidad / bajas (cambio papeleos)
  5. Reclamaciones y quejas
  6. Consultas generales

Una vez entrenado el modelo, se guardó el resultado, incluyendo tanto el modelo Disbert adaptado al problema como el tokenizador. Esto permite que el modelo pueda ser utilizado por el servicio Python cuando llegue una petición POST.

En la carpeta /analysis se puede encontrar un notebook, en el cual se proporciona un análisis de los emails, teniendo en cuenta diferentes variables temporales.

Adicionalmente, también se han tocado los archivos de docker_compose y Dockerfile de la aplicación de Python.