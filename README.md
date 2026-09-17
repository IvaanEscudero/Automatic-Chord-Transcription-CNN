# Automatic-Chord-Transcription
Transcripción Automática de Acordes mediante CNN (**WIP**).

Este proyecto tiene como objetivo desarrollar un modelo de Deep Learning basado en Redes Neuronales Convolucionales (CNN) capaz de identificar y transcribir acordes musicales a partir de señales de audio. El modelo procesa cromagramas en las 12 clases de notas musicales a lo largo del tiempo.

El desarrollo del proyecto está estructurado en 5 etapas progresivas. 

**Nota**: Estas fases representan la planificación inicial y son susceptibles a modificaciones o adaptaciones según las necesidades técnicas que surjan durante el desarrollo.


1. Extracción de Características y

El objetivo inicial es comprender y validar los datos de entrada antes de aplicar Inteligencia Artificial.

    - Procesamiento de audios aislados en arrays bidimensionales usando librosa.

    - Generación de cromagramas.

    - Visualización para confirmar la representación de los acordes.

2. Producto Mínimo Viable (MVP)

Un entorno controlado y simplificado para validar la viabilidad del flujo de trabajo de la red neuronal.

    - Restricción del problema a clasificación binaria (ej. Do Mayor vs. Sol Mayor).

    - Creación de un dataset sintético limpio (50 audios por clase, instrumentos MIDI/Virtuales, sin ruido de fondo).

    - Uso de audios completos como una única imagen de entrenamiento, sin aplicar ventanas temporales.

3. Diseño y Entrenamiento de la Arquitectura CNN

Adaptación del reconocimiento de imágenes al contexto de la música.

    - Definición del modelo con capas convolucionales (Conv2D) para buscar texturas espaciales (notas iluminadas al mismo tiempo).

    - Implementación de capas de MaxPooling para reducir la dimensionalidad y hacer que la red sea tolerante a variaciones en el tempo de ejecución.

4. Ventanas Deslizantes

Análisis de pistas de audio reales continuas.

    - División de los archivos de audio en ventanas temporales cortas (fragmentos de 0.5 a 1.0 segundos).

    - Implementación del cruce de datos: sincronización entre los fragmentos de audio extraídos y los archivos de texto que contienen el etiquetado temporal de los acordes.

5. Datasets Reales y Desbalanceo de Clases

Escalado del modelo a entornos de producción o validación con datos reales complejos.

    - Integración de datasets estándar de la industria.

    - Aplicación de técnicas de mitigación de sesgo estadístico (como Weighted Cross-Entropy en la función de pérdida) para evitar que el modelo sobreprediga los acordes más comunes en detrimento de combinaciones menos frecuentes.
