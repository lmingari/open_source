Speech — Introducción al software de código abierto
Tiempo total estimado: 35–40 minutos

Buenos días a todos.
Hoy vamos a hablar de software de código abierto, licencias, repositorios y colaboración. Pero más que aprender definiciones aisladas, la idea es entender cómo funciona realmente el software moderno: cómo se construye, cómo se comparte, cómo se reutiliza y qué responsabilidades aparecen cuando usamos código escrito por otras personas.
Aunque esta charla pueda sonar, al principio, como algo dirigido solo a desarrolladores, en realidad no lo es. Si trabajamos en investigación, ciencia de datos, análisis, docencia, ingeniería, administración de sistemas o incluso si simplemente usamos herramientas digitales en nuestro trabajo diario, probablemente dependemos de software de código abierto todo el tiempo.
Muchos programas, librerías, servidores, lenguajes de programación y herramientas científicas que usamos a diario existen gracias a comunidades abiertas. Y eso tiene enormes ventajas: transparencia, colaboración, reutilización, reproducibilidad y velocidad de innovación.
Pero también plantea preguntas importantes.
Si encuentro código en internet, ¿puedo usarlo directamente?
¿Puedo modificarlo?
¿Puedo incluirlo en mi propio proyecto?
¿Puedo publicar resultados obtenidos con ese código?
¿Puedo usarlo dentro de un producto comercial?
¿Y qué pasa si el código no tiene licencia?
La respuesta corta es: depende.
Y casi siempre depende de la licencia.
Por eso, el objetivo de esta sesión es que al final tengamos una intuición clara sobre tres cosas.
Primero, qué significa que un software sea libre, abierto, propietario, de dominio público o simplemente “source-available”, es decir, con el código visible o disponible.
Segundo, qué papel juegan las licencias de software y por qué no son un detalle secundario, sino una parte fundamental de cualquier proyecto.
Y tercero, cómo se organiza el desarrollo colaborativo mediante repositorios, plataformas como GitHub o GitLab, flujos de trabajo y roles dentro de una comunidad.

1. Por qué importa el software de código abierto
El software de código abierto está en todas partes.
Está en servidores web, sistemas operativos, navegadores, bases de datos, bibliotecas científicas, herramientas de visualización, entornos de programación y plataformas de análisis de datos.
En investigación, por ejemplo, usamos constantemente librerías abiertas para procesar datos, generar figuras, ejecutar modelos o automatizar tareas. En la industria, muchas empresas construyen productos comerciales sobre componentes abiertos. Y en el día a día, muchos programas que usamos tienen partes abiertas o dependen de proyectos abiertos.
Esto significa que el código abierto no es algo marginal. Es una infraestructura común.
Pero precisamente porque es tan común, muchas veces lo usamos sin pensar demasiado en sus implicaciones.
Uno de los errores más frecuentes es asumir que si algo está en internet, entonces se puede usar libremente. Pero eso no es así.
Que podamos ver el código no significa automáticamente que podamos copiarlo, modificarlo o redistribuirlo. Para saber qué podemos hacer, necesitamos mirar la licencia.
Una buena forma de entender una licencia es pensar en ella como un contrato de uso.
La licencia nos dice qué permisos tenemos y qué obligaciones aceptamos.
Por ejemplo, puede decirnos que podemos usar el software para cualquier propósito, que podemos modificarlo y que podemos distribuir copias. Pero también puede pedirnos que conservemos el aviso de copyright, que demos atribución a los autores originales o que publiquemos nuestras modificaciones bajo la misma licencia.
Por eso, open source no significa “sin reglas”. Significa que existen permisos amplios, pero definidos legalmente.

2. Copyright y punto de partida legal
Antes de entrar en los tipos de software, necesitamos entender una idea básica: el software está protegido por copyright.
El código fuente se considera una obra intelectual. En muchos contextos legales se trata de forma parecida a una obra literaria, porque al final es una expresión escrita.
Esto quiere decir que, por defecto, la persona o institución que crea el código tiene derechos exclusivos sobre su copia, modificación y distribución.
Y esto es muy importante: si alguien publica código sin licencia, eso no significa que podamos usarlo libremente. De hecho, normalmente significa lo contrario: que no tenemos permisos claros.
La licencia es precisamente el mecanismo mediante el cual el autor nos concede ciertos permisos.
Por eso, cuando entramos en un repositorio, uno de los archivos más importantes no es solo el código. También es el archivo LICENSE.
Sin licencia, el código puede ser visible, pero no necesariamente reutilizable.

3. Tipos de software
Ahora vamos a distinguir varias categorías.
La primera es el software propietario.
El software propietario es aquel cuyo código fuente no está disponible públicamente o cuyo uso, modificación y redistribución están controlados por una empresa o propietario.
Ejemplos típicos son Microsoft Windows, Microsoft Office, Adobe Photoshop o macOS.
En estos casos, normalmente recibimos el programa ya compilado. Podemos usarlo bajo ciertas condiciones, pero no podemos estudiar libremente su funcionamiento interno, modificarlo ni redistribuirlo.
Esto tiene ventajas para el modelo comercial de la empresa, pero también impone limitaciones al usuario.
Si encontramos un error, dependemos del proveedor para que lo corrija. Si necesitamos adaptar el software a una necesidad específica, probablemente no podamos hacerlo. Si el proveedor deja de mantener el producto, podemos perder compatibilidad o soporte.
Frente a esto aparecen otros modelos.
El software libre se centra en las libertades del usuario. La idea principal es que cualquier persona pueda ejecutar, estudiar, modificar y compartir el programa.
Aquí es importante no confundir “libre” con “gratuito”. Un software puede ser libre y aun así estar asociado a servicios comerciales, soporte profesional o modelos de negocio. La palabra clave es libertad, no precio.
Ejemplos conocidos son VLC, LibreOffice, Inkscape o GIMP.
Después tenemos el software de código abierto, u open source software.
En la práctica, software libre y software de código abierto se solapan mucho, pero el enfoque histórico y filosófico no es exactamente el mismo. El software libre pone el énfasis en la libertad del usuario. El open source pone más énfasis en el modelo de desarrollo: colaboración abierta, transparencia, revisión pública y mejora colectiva.
Para que un software sea realmente open source, no basta con que el código esté visible. Debe estar bajo una licencia que cumpla ciertos criterios, como permitir el uso, modificación y redistribución sin discriminar personas, grupos o campos de actividad.
Por ejemplo, una licencia que diga “puedes usar este código solo para investigación académica” no sería open source en sentido estricto. Tampoco lo sería una licencia que prohíba el uso comercial.
Otra categoría es el dominio público.
El software de dominio público no tiene restricciones de copyright, o sus autores han renunciado a esos derechos en la medida en que la ley lo permite. Esto permite un uso prácticamente sin restricciones.
SQLite es un ejemplo muy conocido.
Sin embargo, el dominio público puede ser complicado en algunos países, especialmente en Europa, donde ciertos derechos morales no siempre pueden renunciarse completamente. Por eso algunos proyectos ofrecen una licencia alternativa o de respaldo —también podríamos decir “licencia supletoria”— para garantizar que el software pueda usarse legalmente en distintas jurisdicciones.
Finalmente, tenemos el software source-available.
Aquí la traducción no siempre es perfecta. Podemos decir “software con código fuente disponible”, “software de código visible” o simplemente mantener el término “source-available”.
Este tipo de software permite ver el código, pero impone restricciones que hacen que no sea open source. Por ejemplo, puede prohibir ciertos usos comerciales o limitar la redistribución.
Este punto es clave: código visible no es lo mismo que código abierto.

4. Qué es una licencia de software
Pasemos ahora a las licencias.
Una licencia de software responde a una pregunta muy sencilla:
¿Qué puedo hacer con este código?
Pero la respuesta tiene consecuencias legales y prácticas.
La licencia define si podemos usar el software, modificarlo, redistribuirlo, combinarlo con otros proyectos, incluirlo en un producto comercial o publicar una versión modificada.
También define qué obligaciones tenemos.
Por ejemplo, algunas licencias solo nos piden conservar el aviso de copyright. Otras nos piden incluir una copia de la licencia. Otras, más estrictas, nos obligan a publicar el código fuente si distribuimos una versión modificada.
En el mundo open source, una clasificación muy útil es distinguir entre licencias permisivas y licencias copyleft.
Las licencias permisivas dan mucha libertad y tienen pocas condiciones.
Ejemplos típicos son MIT, BSD y Apache 2.0.
Estas licencias permiten usar el código en proyectos abiertos o cerrados, académicos o comerciales, siempre que se respeten unas obligaciones básicas.
Por eso son muy populares en empresas, universidades y proyectos científicos. Reducen la fricción legal y facilitan que el software sea adoptado por mucha gente.
Por otro lado, las licencias copyleft son más estrictas.
Su objetivo es garantizar que el software y sus versiones derivadas sigan siendo libres o abiertas.
El ejemplo más conocido es la GPL, la GNU General Public License.
La idea de la GPL es que si modificamos un programa y distribuimos esa versión modificada, debemos hacerlo bajo la misma licencia y proporcionar el código fuente.
Esto evita que alguien tome un proyecto abierto, lo modifique, lo cierre y redistribuya una versión propietaria sin devolver esas libertades a los usuarios.
También existe la LGPL, que es una versión más débil o más flexible de copyleft. Se usa especialmente para bibliotecas. Permite que otros programas enlacen con esa biblioteca sin obligar necesariamente a que todo el programa completo sea GPL.
Aquí “linking” puede traducirse como “enlazado”, “vinculación” o, en un lenguaje menos técnico, “uso como biblioteca”.

5. Cómo elegir una licencia
La elección de una licencia depende del objetivo del proyecto.
Si queremos que una biblioteca o herramienta sea adoptada lo más ampliamente posible, una licencia permisiva como MIT, BSD o Apache suele ser una buena opción.
Esto es común en librerías científicas, herramientas web o componentes que queremos que otras personas puedan integrar fácilmente en sus proyectos.
Si, en cambio, queremos asegurarnos de que el proyecto y sus derivados sigan siendo abiertos, entonces una licencia copyleft como GPL puede ser más adecuada.
El kernel de Linux es un ejemplo importante: usa GPLv2 precisamente para proteger la apertura del proyecto a largo plazo.
Apache 2.0 merece una mención especial porque, además de ser permisiva, incluye una concesión explícita de patentes. Esto puede ser importante en entornos industriales, donde las patentes son una preocupación real.
Así que no existe una licencia universalmente “mejor”. Hay licencias más adecuadas para distintos objetivos.
Si queremos máxima adopción, probablemente pensemos en MIT, BSD o Apache.
Si queremos proteger la apertura futura, probablemente pensemos en GPL.
Si nos preocupa el riesgo de patentes, Apache 2.0 puede ser especialmente interesante.

6. Algunos ejemplos concretos
Veamos algunos casos.
Windows es software propietario.
El usuario recibe binarios compilados, pero no puede estudiar libremente el código fuente ni modificar el sistema internamente. La redistribución y modificación están controladas por la licencia.
GIMP, en cambio, es software libre y de código abierto con licencia GPL.
Esto significa que podemos ejecutar el programa, estudiar el código, modificarlo y redistribuirlo, incluyendo versiones modificadas, siempre respetando las condiciones de la GPL.
SciPy es otro ejemplo, pero con una licencia permisiva.
SciPy usa BSD-3-Clause. Esto permite usar, estudiar, modificar y redistribuir el software con pocas restricciones. Además, no obliga a que las modificaciones se publiquen bajo la misma licencia.
BSD-3-Clause y MIT son muy parecidas: simples, flexibles y fáciles de integrar en otros proyectos. Una diferencia es que BSD-3-Clause incluye una cláusula de “no endorsement”. Esto puede traducirse como “cláusula de no respaldo”, “cláusula de no aval” o “cláusula de no promoción”.
La idea es que no podemos usar el nombre de los autores o instituciones originales para promocionar un producto derivado sin permiso.
SQLite es un caso especial, porque está en dominio público.
Eso lo hace extremadamente permisivo, pero también genera un problema curioso: si el proyecto aceptara contribuciones externas normales, esas contribuciones podrían tener copyright y alterar la situación legal del código. Por eso SQLite gestiona las contribuciones de una forma particular.
Este ejemplo muestra que las licencias open source no solo imponen restricciones. También organizan la colaboración. En muchos casos, usar una licencia clara facilita mucho más la contribución que simplemente decir “esto es dominio público”.

7. Repositorios y desarrollo colaborativo
Hasta ahora hemos hablado de derechos, licencias y tipos de software.
Pero el código abierto no es solo una cuestión legal. También es una forma de trabajar.
Para que un proyecto pueda crecer de forma colaborativa, necesita organización.
Necesita un lugar donde guardar el código, la documentación, los archivos de configuración, los ejemplos, los datos auxiliares, las versiones publicadas y el historial de cambios.
Ese lugar es el repositorio.
Un repositorio es un espacio de almacenamiento con control de versiones. En la práctica moderna, el sistema más usado para esto es Git.
Git permite registrar cambios, comparar versiones, volver atrás si algo se rompe, crear ramas de desarrollo y fusionar contribuciones.
Un repositorio típico suele tener un archivo README, que explica qué hace el proyecto y cómo usarlo; un archivo LICENSE, que define las condiciones legales; carpetas con código fuente; documentación; archivos de configuración; pruebas; ejemplos; y otros recursos.
Pero un repositorio por sí solo no resuelve toda la colaboración humana.
Para eso usamos plataformas de alojamiento de código, como GitHub, GitLab, Bitbucket o servicios institucionales basados en Git.
Estas plataformas no solo guardan el código. También permiten discutir cambios, reportar errores, revisar contribuciones, automatizar pruebas, gestionar versiones y coordinar equipos.
En otras palabras, convierten un conjunto de archivos en un proyecto colaborativo.

8. Flujo típico de colaboración
Un proyecto colaborativo suele seguir un flujo bastante estructurado.
Primero, alguien identifica un problema, una necesidad o una posible mejora.
Después, esa idea puede discutirse en un issue, una tarea o una conversación del proyecto.
Luego, alguien implementa una propuesta de cambio. Normalmente lo hace en una rama separada, para no modificar directamente la versión principal.
Después se abre una pull request o merge request.
La traducción puede variar: podemos decir “solicitud de incorporación de cambios”, “propuesta de cambios” o simplemente mantener “pull request” y “merge request”, porque son términos muy usados en la práctica.
Esa propuesta se revisa. Otras personas pueden comentar, pedir cambios, sugerir mejoras o aprobarla.
Cuando el cambio está listo, se fusiona con la rama principal. “Merge” puede traducirse como “fusionar”, “integrar” o “combinar cambios”.
Finalmente, esos cambios pueden formar parte de una nueva versión del software.
Este proceso hace que la evolución del proyecto sea transparente, trazable y revisable.
No se trata solo de escribir código. Se trata de dejar una historia comprensible de por qué se hicieron ciertos cambios, quién los propuso, quién los revisó y cuándo se integraron.

9. Roles en un proyecto colaborativo
En un proyecto abierto no todas las personas tienen el mismo rol.
Los usuarios usan el software. Pueden reportar errores, pedir nuevas funcionalidades o mejorar la documentación simplemente explicando qué les resultó confuso.
Los contribuidores proponen cambios. Estos cambios pueden ser código, documentación, pruebas, ejemplos, traducciones o mejoras en la configuración del proyecto.
Los revisores evalúan esas propuestas antes de que se integren.
Los mantenedores tienen una responsabilidad más amplia. Deciden la dirección del proyecto, mantienen estándares de calidad, gestionan versiones y toman decisiones sobre qué se acepta y qué no.
Y las organizaciones pueden aportar infraestructura, financiación, gobernanza o soporte a largo plazo.
Esta división de roles permite que proyectos muy grandes funcionen de manera ordenada, incluso cuando participan personas de distintos países, instituciones y áreas de conocimiento.

Conclusión
Para cerrar, me gustaría resumir la idea central.
El software moderno no se construye de forma aislada.
Se construye reutilizando componentes, colaborando con otras personas y apoyándose en infraestructuras comunes.
El software de código abierto hace posible gran parte de esta colaboración, pero no funciona simplemente porque el código esté publicado en internet.
Funciona porque hay licencias que definen derechos y obligaciones.
Funciona porque hay repositorios que organizan el código y preservan la historia del proyecto.
Funciona porque hay plataformas que permiten revisar, discutir e integrar cambios.
Y funciona porque hay comunidades con roles, normas y prácticas compartidas.
Por eso, cuando usamos software de código abierto, no solo estamos usando una herramienta técnica. Estamos entrando en un ecosistema legal, social y colaborativo.
Entender ese ecosistema nos ayuda a usar software de forma responsable, a evitar problemas legales, a mejorar la reproducibilidad de nuestro trabajo y, si queremos, a contribuir de forma más efectiva a proyectos existentes.
La próxima vez que entremos en un repositorio, conviene mirar no solo el código, sino también el README, la licencia, las guías de contribución, los issues y la actividad del proyecto.
Ahí es donde realmente vemos cómo el software pasa de ser código individual a convertirse en una herramienta compartida, mantenida y mejorada colectivamente.
Muchas gracias.
