# GRUPO 1: 
    Emma Montalbán
    Erika Samara Alvares
    Juan Carlos Menendez Gijón
    Francisco Polonio Monterroso

# TEMÁTICA: Calidad del aire en Madrid año 2022 (por día y hora)

# OBJETIVO:
1. Escenario: Modelo predictivo de los efectos de la calidad del aire en la salud.
* Calidad del aire vs salud, teniendo en cuenta datos metereológicos
* Datos: Aire, metereología

# RECOGIDA DE DATOS: PORTAL DEL AYUNTAMIENTO DE MADRID

1.  CALIDAD DEL AIRE
    https://datos.madrid.es/sites/v/index.jsp?vgnextoid=aecb88a7e2b73410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD

    * Datos horarios desde 2001
    En este conjunto de datos puede obtener la información recogida por las estaciones de control de calidad del aire, con los datos horarios por anualidades desde 2001.

    * Estaciones de control
    En este conjunto de datos se reflejan todas las estaciones fijas de la red de vigilancia de la calidad del aire del Ayuntamiento de Madrid y sus metadatos asociados.

2. Metereología 
    https://datos.madrid.es/sites/v/index.jsp?vgnextoid=fa8357cec5efa610VgnVCM1000001d4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD

    * Datos horarios desde 2019
    En este conjunto de datos puede obtener la información recogida por las estaciones meteorológicas, con los datos horarios, horarios por anualidades desde enero de 2019.

    * Estaciones de control
    En este conjunto de datos puede obtener la ubicación de todas las estaciones de control que pueden medir lo siguientes parametros:

    81 - VELOCIDAD VIENTO
    82 - DIR. DE VIENTO
    83 - TEMPERATURA
    86 - HUMEDAD RELATIVA
    87 - PRESION BARIOMETRICA
    88 - RADIACION SOLAR
    89 - PRECIPITACIÓN

# INTERPRETACIÓN DATASETS:

1.  CALIDAD DEL AIRE
    * Datos horarios desde 2019
      - Documentación de referencia 
        https://datos.madrid.es/FWProjects/egob/Catalogo/MedioAmbiente/Aire/Ficheros/Interprete_ficheros_%20calidad_%20del_%20aire_global.pdf

      - Interpretación columnas:
        PROVINCIA: Código de Provincia 
        MUNICIPIO: Código de Municipio
        ESTACION: Ubicación de las estaciones de medida
        MAGNITUD: Parámetro contaminantebmedido
        PUNTO_DE_MUESTREO: Código estación completo (provincia,municipio y estación) más magnitud y técnica de medida
        AÑO: año
        MES: mes 
        DIA: día   
        H: indica el valor de la magnitud contaminante correspondiente. 
            “H01” hace referencia a la 1 de la mañana, 
            “H02” a las 2 de la mañana, y así sucesivamente hasta las 24h
        V01, ..., V024: Validación de la H01, ..., H024.Dónde:
            "V" hace referencia a valor válido
            "N" a valor no válido

        - Magnitudes de medida de los contaminantes atmosféricos
          Se han seleccionado los siguientes contaminantes atmósfericos porque son los que se necesitan para calcular el índice de calidad del aire (ICA)
            MAGNITUD    DESCRIPCION                TECNICA DE MEDIDA
            01          SO2: Dióxido de Azufre     38 Fluorescencia ultravioleta
            06          CO: Monóxido de Carbono    48 Absorción infrarroja
            08          NO2: Dióxido de Nitrógeno  08 Quimioluminiscencia  
            09          PM2.5: Partículas < 2.5 μm 47 Microbalanza
            10          PM10: Partículas < 10 μm   47 Microbalanza
            14          O3: Ozono                  06 Absorción ultravioleta 
            20          TOL: Tolueno               59 Cromatografía de gases
            30          BEN: Benceno               59 Cromatografía de gases
            35          EBE: Etilbenceno           59 Cromatografía de gases

    * Estaciones de control 
      - Documentación de referencia 
        https://datos.madrid.es/FWProjects/egob/Catalogo/MedioAmbiente/Aire/Ficheros/Estructura_C.A.Estaciones.pdf

      - Interpretación columnas
        CODIGO: Código nacional de cada estación 
        CODIGO_CORTO: Últimas dos cifras del código nacional
        ESTACION: Nombre de la estación
        DIRECCION: Dirección postal cercana o aproximada
        LONGITUD_ETRS89: Longitud geográfica expresada en el sistema ETRS 89
        LATITUD_ETRS89: Latitud geográfica expresada en el sistema ETRS 89
        ALTITUD Altitud topográfica expresada en metros sobre el nivel del mar.
        COD_TIPO: Código tipo de estación UT/UF/ S
        NOM_TIPO: Nombre tipo de estación Urbana de Tráfico/Urbana de Fondo/Suburbana
        NO2: Dióxido de nitrógeno X indica que se mide ese parámetro
        SO2: Dióxido de azufre X indica que se mide ese parámetro
        CO: Monóxido de carbono X indica que se mide ese parámetro
        PM10: Partículas PM10 X indica que se mide ese parámetro
        PM2_5: Partículas PM2.5 X indica que se mide ese parámetro
        O3: Ozono X indica que se mide ese parámetro
        BTX: Hidrocarburos aromáticos:Benceno, Tolueno, Etilbenceno. X indica que se mide ese parámetro
        COD_VIA: Código de vía.
        VIA_CLASE: Descripción del tipo de vía Calle, Avenida, Plaza, etc.
        VIA_PAR: Descripción parcial del tipo de vía
        VIA_NOMBRE: Nombre de la vía
        Fecha alta: Fecha de alta de la estación
        COORDENADA_X_ETRS89: Coordenada geográfica X expresada en el sistema ETRS 89
        COORDENADA_Y_ETRS89: Coordenada geográfica Y expresada en el sistema ETRS 89
        LONGITUD: Longitud geográfica en grados decimales
        LATITUD Latitud geográfica en grados decimales

      - Estaciones de control
        Seleccionamos las siguientes estaciones de control porque son las que coinciden con las estaciones de control de los datos metereológicos ya que nos permitirá realizar las relaciones entre los datos de calidad del aire y los datos metereológicos.

        28079008: Escuelas Aguirre  URBANA TRAFICO
        28079018 C/ Farolillo       URBANA FONDO
        28079024 Casa de Campo      SUBURBANA
        28079035 Pza. del Carmen    URBANA FONDO
        28079036 Moratalaz          URBANA TRAFICO

2. METEREOLOGÍA
    * Datos horarios desde 2019
    Los datos meteorológicos que se proporcionan en estos ficheros son exclusivamente para evaluar la calidad del aire medida por la Red de Calidad del Aire de la Comunidad de Madrid. Los datos meteorológicos oficiales son los proporcionados por la Agencia Estatal de Meteorología (AEMET).

    - Documentación de referencia 
        https://datos.madrid.es/FWProjects/egob/Catalogo/MedioAmbiente/DatosMeteorologicos/Ficheros/Interpretaci%C3%B3n_datos_meteorologicos.pdf

    - Interpretación columnas:
        PROVINCIA: Código de Provincia 
        MUNICIPIO: Código de Municipio
        ESTACION: Ubicación de las estaciones de medida
        MAGNITUD: Parámetro metereológico medido
        PUNTO_DE_MUESTREO: Código estación completo (provincia,municipio y estación) más magnitud y técnica de medida
        AñO: año
        MES: mes 
        DIA: día   
        H: indica el valor de la magnitud meteorológica correspondiente. 
            “H01” hace referencia a la 1 de la mañana, 
            “H02” a las 2 de la mañana, y así sucesivamente hasta las 24h
        V01, ..., V024: Validación de la H01, ..., H024.Dónde:
            "V" hace referencia a valor válido
            "N" a valor no válido

    - Magnitudes de medida de los datos metereológicos:
        MAGNITUD    DESCRIPCION             TECNICA UNIDAD DESCRIPCIÓN_UNIDAD
        80          RADIACIÓN ULTRAVIOLETA  89      m/s     metros por segundo
        81          VELOCIDAD DEL VIENTO    89      Grd     grados
        82          DIRECCIÓN DEL VIENTO    89      ºc      grados centígrados  
        83          TEMPERATURA             89      %       porcentaje
        86          HUMEDAD RELATIVA        89      mbar    milibar
        88          RADIACIÓN SOLAR         89      W/m2    vatios por metro cuadrado
        89          PRECIPITACIÓN           89      l/m2    litros por metro cuadrado 

    * Estaciones de control
    En este conjunto de datos se reflejan todas las ubicaciones de los sensores meteorológicos pertenecientes al Sistema Integral de Vigilancia, Predicción e Información de la Calidad del Aire del Ayuntamiento de Madrid y sus metadatos asociados.

    - Documentación de referencia
        https://datos.madrid.es/FWProjects/egob/Catalogo/MedioAmbiente/DatosMeteorologicos/Ficheros/Estructura_Estaciones%20meteorol%C3%B3gicas.pdf

    - Interpretacion de las columnas
        CODIGO: Código nacional de cada estación
        CODIGO_CORTO: Últimas dos cifras del código nacional
        ESTACION: Nombre de la estación
        DIRECCION: Dirección postal cercana o aproximada
        LONGITUD_ETRS89: Longitud geográfica expresada en el sistema ETRS 89
        LATITUD_ETRS89: Latitud geográfica expresada en el sistema ETRS 89
        ALTITUD: Altitud topográfica expresada en metros sobre el nivel del mar.
        VV: Velocidad de viento expresada en m/s
        DV: Dirección del viento expresada en grados sexagesimales Entre 0 y 359 º (0=N, 90=E,180=S, 270=O)
        T: Temperatura expresada en grados celsius.
        HR: Humedad relativa expresada en % Entre 0 y 100%
        PB: Presión barométrica expresada en milibares.
        RS: Radiación solar expresada en w/m2
        P: Lluvia. Precipitación acumulada en mm. (equivalente a l/m2)
        COD_VIA: Código de vía.
        VIA_CLASE: Descripción del tipo de vía Calle, Avenida, Plaza, etc.
        VIA_PAR: Descripción parcial del tipo de vía
        VIA_NOMBRE: Nombre de la vía
        NUM_VÍA: Número postal aproximado.
        COORDENADA_X_ETRS89: Coordenada geográfica X expresada en el sistema ETRS 89
        COORDENADA_Y_ETRS89 Coordenada geográfica Y expresada en el sistema ETRS 89
        LONGITUD Longitud geográfica en grados decimales
        LATITUD Latitud geográfica en grados decimales

    - Estaciones de control
        28079008 Escuelas Aguirre
        28079018 Farolillo
        28079024 Casa de Campo
        28079035 Plaza del Carmen
        28079036 Moratalaz


# ANÁLISIS PRELIMINAR
Este análisis preliminar nos permite determinar que varibles incluiremos en en análisis definitivo.

1. CONTAMINANTES PARA EL ESTUDIO:
En Madrid, los más relevantes en cuanto a sus efectos para la salud son:
* Dióxido de nitrógeno (NO2):
    Es un contaminante atmosférico que se produce fundamentalmente en las combustiones de los vehículos de motor.

    Hasta el 80% de las emisiones de este contaminante procede del tráfico rodado, sobre todo de los vehículos diésel. El resto de las emisiones se origina durante la combustión de gas, petróleo y carbón, en centrales térmicas, actividades industriales, calefacciones, incineradoras, etc

    Los principales síntomas asociados a episodios de alta contaminación por dióxido de nitrógeno son:
    - Picor de ojos, nariz y garganta.
    - Irritación de los bronquios con tos, flemas, dificultad para respirar.

* Partículas en suspensión: 
    Constituyen un contaminante atmosférico procedente    tanto de fuentes naturales (tormentas de arena, erupciones volcánicas, incendios forestales, etc.) como de la actividad humana (tráfico, especialmente vehículos diésel, incineradoras, calefacciones de carbón, minería, procesos industriales, etc.).
    - PM2,5 (tamaño inferior a 2,5 micras): 
        Proceden fundamentalmente de la actividad humana, pueden penetrar hasta las partes más profundas del pulmón y pasar a la sangre, y por ello resultan especialmente nocivas.
    - PM10 ():tamaño inferior a 10 micras
        Al ser más grandes quedan en buena parte retenidas en las porciones superiores del aparato respiratorio, como las fosas nasales o los grandes bronquios. Resultan menos perjudiciales para la salud que las PM2,5, pero no son inocuas y se ha observado un aumento de la demanda de atención urgente por crisis asmáticas cuando aumenta su concentración en el aire.

    En nuestra Comunidad, una causa muy frecuente de aumento de partículas es la llegada de polvo del desierto del Sáhara empujado por vientos del sur.

    Este polvo, que puede permanecer en el aire durante horas y presentarse como una neblina de color marrón, puede llevar en su composición materia mineral (arcillas, cuarzos, carbonatos, etc.) y también biológico, como fragmentos vegetales, polen, virus, bacterias, etc.


* Ozono troposférico(O3):
    Es un gas incoloro que puede resultar beneficioso o nocivo para la salud, dependiendo de si se encuentra en las capas más altas de la atmósfera o a nivel del suelo. Por ello se habla de:

    - Ozono bueno (ozono estratosférico): 
        Se localiza en la estratosfera, a una distancia de la superficie terrestre de entre 12 a 50 km, formando una capa que nos protege de los dañinos rayos ultravioleta del sol. Este es el ozono al que se hace referencia cuando se habla del “agujero de la capa de ozono”.
    - Ozono malo (ozono troposférico): 
        Se localiza en la troposfera, es decir, la parte de la atmósfera donde se desarrolla la vida humana. Este ozono se forma como resultado de reacciones químicas, en presencia de la luz solar, a partir de los contaminantes emitidos por automóviles, centrales térmicas, refinerías, procesos industriales diversos etc. Cuanto mayor sea la luz solar y la temperatura, mayor será la cantidad de ozono que se forme; por ello, las mayores concentraciones de este gas se dan en verano.


    Los posibles síntomas asociados a episodios de contaminación por ozono, entre otros, son:

    - Irritación ocular y de las vías respiratorias con tos, molestias de garganta, dolor torácico al respirar profundamente.
    - Mayor dificultad para respirar con normalidad, sobre todo al hacer ejercicio.
    - Mayor susceptibilidad a las infecciones respiratorias.
    - Ataques de asma y agravamiento de ésta y otras enfermedades  respiratorias, como el enfisema o la bronquitis crónica.
    
2. OBTENCION DEL ICA (INDICE DE CALIDAD DEL AIRE)
    El Índice de Calidad del Aire (ICA) establecido por la Red de Vigilancia y Control de la Contaminación Atmosférica de la Comunidad de Madrid (REVA). 
    El ICA de Madrid se basa en la concentración de cuatro contaminantes principales: 

    * dióxido de azufre (SO2)
    * dióxido de nitrógeno (NO2)
    * partículas en suspensión (PM10) 
    * ozono (O3).

    El cálculo del ICA de Madrid se realiza asignando un valor numérico a cada uno de los contaminantes y luego promediando estos valores ponderados. La fórmula utilizada para calcular el ICA es la siguiente:

    - ICA = (ICA_SO2 + ICA_NO2 + ICA_PM10 + ICA_O3) / 4

    Donde ICA_SO2, ICA_NO2, ICA_PM10 y ICA_O3 son los valores individuales del índice de calidad del aire para cada contaminante, que se calculan de la siguiente manera:

    - ICA_SO2 = (Concentración_SO2 / Valor_Límite_SO2) * 100
    - ICA_NO2 = (Concentración_NO2 / Valor_Límite_NO2) * 100
    - ICA_PM10 = (Concentración_PM10 / Valor_Límite_PM10) * 100
    - ICA_O3 = (Concentración_O3 / Valor_Límite_O3) * 100

    En cada fórmula, se divide la concentración del contaminante por el valor límite establecido para ese contaminante y se multiplica por 100 para obtener un porcentaje. Luego, se promedian los valores de ICA de los cuatro contaminantes para obtener el índice de calidad del aire general.


    * Supongamos que tenemos los siguientes datos ficticios para las concentraciones  de los contaminantes en Madrid:

        Dióxido de Azufre (SO2): Concentración = 15 μg/m³, Valor Límite = 50 μg/m³
        Dióxido de Nitrógeno (NO2): Concentración = 40 μg/m³, Valor Límite = 40 μg/m³
        Partículas en Suspensión (PM10): Concentración = 25 μg/m³, Valor Límite = 50 μg/m³
        Ozono (O3): Concentración = 60 μg/m³, Valor Límite = 120 μg/m³
3. VALORES LIMITE CONTAMINANTES
Compuesto   Valor límite /      Concentración       Nº máximo de superaciones
            objetivo / 
            Umbral de Alerta

* PM10: 	Media anual. 	     40 μg/m3 	 
            Media diaria. 	     50 μg/m3 	         35 días/año
* SO2   	Media diaria. 	     125 μg/m3 	         3 días/año
            Media horaria. 	     350 μg/m3 	         24 horas/año
            Umbral de alerta     500 μg/m3
            (3 horas consecutivas en área representativa de 100 km o zona o aglomeración entera). 	 	 
* NO2   	Media anual. 	     40 μg/m3 	 
            Media horaria. 	     200 μg/m3 	        18 horas/año
            Umbral de alerta     400 μg/m3
            (3 horas consecutivas en área representativa de 100 km o zona o aglomeración entera). 	 	 
* O3   	    Máxima diaria de     120 μg/m3 	        25 días /  año,
            las medias móviles octohorarias.  	promediados en un período de 3 años
            Umbral de información:
            Media horaria. 	      180 μg/m3 	 
            Umbral de alerta. 
            Media horaria. 	      240 μg/m3 	 
 	 

Calculamos el índice de calidad del aire para cada contaminante utilizando las fórmulas proporcionadas anteriormente:

ICA_SO2 = (15 / 50) * 100 = 30
ICA_NO2 = (40 / 40) * 100 = 100
ICA_PM10 = (25 / 50) * 100 = 50
ICA_O3 = (60 / 120) * 100 = 50

Luego, promediamos los valores de ICA de los cuatro contaminantes para obtener el índice de calidad del aire general:

ICA = (30 + 100 + 50 + 50) / 4 = 57.5

En este ejemplo ficticio, el índice de calidad del aire en Madrid sería de aproximadamente 57.5.


# TIPOLOGIA ESTACIONES DE MEDIDA DE LOS CONTAMINANTES
Las estaciones que miden la calidad del aire en Madrid se clasifican en diferentes categorías según su ubicación y los contaminantes que monitorean. Estas categorías incluyen estaciones urbanas de tráfico, estaciones urbanas de fondo y estaciones suburbanas.

* Estaciones Urbanas de Tráfico: 
    Estas estaciones se encuentran en áreas de alta densidad de tráfico y monitorean principalmente los contaminantes relacionados con las emisiones de los vehículos, como dióxido de nitrógeno (NO2), partículas en suspensión (PM10 y PM2.5) y monóxido de carbono (CO). Son representativas de la calidad del aire en áreas donde el tráfico es intenso, como calles principales y avenidas transitadas.

* Estaciones Urbanas de Fondo: 
    Estas estaciones se ubican en áreas urbanas, pero no necesariamente cerca de vías de tráfico intenso. Monitorean una gama más amplia de contaminantes atmosféricos, incluidos los contaminantes primarios como el dióxido de nitrógeno (NO2), las partículas en suspensión (PM10 y PM2.5), el ozono (O3) y el dióxido de azufre (SO2). Estas estaciones proporcionan información sobre la calidad del aire en zonas urbanas más generales, no específicamente relacionadas con el tráfico.

* Estaciones Suburbanas: 
    Estas estaciones se encuentran en áreas residenciales o rurales a las afueras de la ciudad. Monitorean contaminantes similares a las estaciones urbanas de fondo, pero su ubicación en áreas menos urbanizadas permite evaluar la calidad del aire en entornos menos influenciados por el tráfico y otras fuentes de contaminación urbana.

En resumen, las estaciones urbanas de tráfico se enfocan en los contaminantes relacionados con el tráfico vehicular, las estaciones urbanas de fondo monitorean una gama más amplia de contaminantes en áreas urbanas generales y las estaciones suburbanas proporcionan información sobre la calidad del aire en áreas residenciales o rurales a las afueras de la ciudad.

# ESTRUCTURA DEL PROYECTO:
1.  DATA 
    Carpeta con los csv reccopilados del portal de datos abiertos del Ayuntamiento de Madrid.
    * aire:
    Carpeta con los csv originales referentes a la calidad del aire en en año 2022/meses recogidos por la estaciones:
        - estaciones.cvs
    * metereología:
    Carpeta con los csv originales referentes a la metereología en en año 2022/meses recogidos por la estaciones:
        - Estaciones_control_datos_metereológicos.csv
    * aux: 
    Carpetea con los csv ya procesados con las columnas que nos interesan
        - aire_2022.csv
        - metee_2022.csv
    * Dataset final, en el que nos basamos para el análisis:
        - calidad_aire_2022.cvs
    
2. NOTEBOOKS
    * Preparacion_dataset
    Carpeta con los notebooks necesarios para la creacción del dataset final sobre el que ser realizará el análisis
      - 1.Creaccion_columnas_aire.ipynb
      - 2.Creaccion_columnas_metereología.ipynb
      - 3.Fusion_datasets.ipynb
    * 1.Tratamiento_nulos.ipynb
    * 2.Tratamiento_outliers.ipynb
    * 3.Analisis_descriptivo.ipynb
    * 4.Analisis_univariante.ipynb
    * 5.Analisis_bivariante.ipynb
    * 6.Analisis_multivariante.ipynb





   