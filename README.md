1. ¿Por qué fue necesario normalizar la humedad y la temperatura?: porque no eran datos de la misma escala.
2. ¿En qué operaciones se utilizó X_normalizado y para qué se conservó X?: El X_normalizado se usó en todas las operaciones siguientes a la declaración de variables inicial donde si se usó el X.
3. ¿Qué ocurrió al utilizar solamente 100 épocas?: Al dejar solo 100 épocas y tomarlo cada 50, los errores fueron relativamente bajos de 29% y 22%
4. ¿Más épocas siempre produjeron una mejora importante?: Entre mas épocas el error se vuelve mas bajo llegando a solo el 3% en promedio.
5. ¿Qué efecto tuvo una tasa de aprendizaje demasiado pequeña?: Con una tasa de aprendizaje del 0.2 el error es bajo de solo el 4%.
6. ¿Qué efecto tuvo una tasa de aprendizaje alta o muy alta?: Con la tasa del 80% el error en la primera época fue del 30% pero después disminuyó hasta un 1.6 % en la quinta época.
7. ¿Qué representa el signo del peso correspondiente a la humedad?: Indica si una mayor humedad favorece o desfavorece la decisión de regar se espera que sea negativo.
8. ¿Qué representa el signo del peso correspondiente a la temperatura?: Representa la influencia de esta variable sobre la decisión de riego. Un peso positivo indica que, al aumentar la temperatura, aumenta la probabilidad de regar; un peso negativo indicaría lo contrario.
9. ¿Por qué una probabilidad debe convertirse en 0 o 1 mediante un umbral?: Para poder predecir si el modelo acertó o no, de una manera mas rápida y sencilla.
10.¿Qué limitaciones tiene esta neurona para representar el riego de una planta real?: La tierra, la cantidad de agua, si hay nieve o si al lado de esa planta hay mas plantas que podrían llegar a comerse toda su agua.
