﻿##########################################
#    SUPER CONSULTORIA FILOSFICA VIRTUAL #
#    TURBO EX EDICION DE CAMPEONATO      #
##########################################

#definición de la imagen de carga
image splash = "splash loading.png"
image bg main = "images/bg main.png"

#definición de personajes
define doc = Character("Dra. Aurora", color="#ff0000")

#definición de las imagenes de la Dra Aurora
images doc neutral = "images/doc neutral.png"
images doc thinking = "images/doc thinking.png"
images doc giggle = "images/doc giggle.png"

#¿Intro del juego?
scene black
with with Pause(1)

#caja de dialogo
transform diabox:
        pos(566, 32)

#Inicio del splashscreen
label splashscreen:
        scene black
        with Pause(1)

        show splash with dissolve
        with Pause(2)

        return 

#Inicio del juego
label start:
        #Inicia declaración de variables
        #TODO: Declarar el resto de variables que faltan
        $ pregunta1_respuestaA = False 
        $ pregunta1_respuestaB = False
        $ pregunta1_respuestaC = False
        $ pregunta1_respuestaD = False
        $ pregunta2_respuestaA = False
        $ pregunta2_respuestaB = False
        $ pregunta2_respuestaC = False
        $ pregunta2_respuestaD = False
        $ pregunta3_respuestaA = False
        $ pregunta3_respuestaB = False
        $ pregunta3_respuestaC = False
        $ pregunta3_respuestaD = False
        $ pregunta4_respuestaA = False
        $ pregunta4_respuestaB = False
        $ pregunta4_respuestaC = False
        $ pregunta5_respuestaA = False
        $ pregunta5_respuestaB = False
        $ pregunta5_respuestaC = False
        #$ pregunta6 = False#placeholder
        #$ pregunta7 = False#placeholder
        #$ pregunta8# placeholder
        #$ pregunta9# placeholder
        #$ pregunta10#placeholder
        #$ pregunta11#placeholder
        #$ pregunta12#placeholder
        #$ pregunta13#placeholder
        #$ pregunta#placeholder
        
        #Fin declaración de variables
        
        #Muestra el fondo
        show bg main with fade
        show bg main with dissolve

        #Muestra Doc Neutral.png en diabox
        show doc neutral at diabox

        #Primera línea de dialogo
        doc "¡Bienvenido!"
        ...

        #Inicio de la primera pregunta
        menu:
                doc "¿Hay algo así como un fundamento último y permamente de la realidad? Ya sea un ser Creador, Omnipotente como Dios, o una estructura como algo que no puede ser y no ser al mismo tiempo."

                "1) Sí, hay un ser o seres así":
                        $pregunta1_respuestaA = True
                "2) Sí, hay estructuras así":
                        $pregunta1_respuestaB = True
                "3) No creo, todo parece estar, o está en cambio":
                        $pregunta1_respuestaC = True
                "4) No lo sé, o no se puede saber":
                        $pregunta1_respuestaD
        
        #Inicio de la segunda pregunta
        menu:
                doc "¿Crees que existe un ser supremo? Un ser absoluto, primero que cualquier otro"

                "1) Sí, y ese ser es dios":
                        $ pregunta2_respuestaA = True
                
                "2) Sí, pero considero a ese 'ser' un principio o sustancia absoluta":
                        $ pregunta2_respuestaB = True
                
                "3) No, la realidad no tiene principio tal que haya un ser 'primario'":
                        $ pregunta2_respuestaC = True
                
                "4) No lo sé, o no se puede saber":
                        $ pregunta2_respuestaD = True
        
        #Inicio de la terecera pregunta
        menu:
                doc "Vamos a usar 'objeto' de manera muy general aquí, cualquier tipo de cosa, incluso si no es tangible. Para ti, la realidad está compuesta de... ¿Qué tipo de objetos?"

                "1) Fundamentalmente de objetos abstractos que no podemos percibir con los sentidos como ideas, formas o estructuras profundas":
                        $ pregunta3_respuestaA = True
                
                "2) De varios tipos de objetos, abstractos como ideas, números o almas, pero también de los objetos que podemos percibir e interactuar físicamente":
                        $ pregunta3_respuestaB = True
                
                "3) Sólo hay objetos y fuerzas materiales. Todo con lo que podemos interactuar causalmente":
                        $ pregunta3_respuestaC = True
                
                "4) No lo sé, o no se puede saber":
                        $ pregunta3_respuestaD = True
        
        #Inicio de la cuarta pregunta
        menu:
                doc "¿Crees que después de morir, las personas siguen existiendo de forma no corporal?"

                "1) Sí, las personas existimos como almas, o similar":
                        $ pregunta4_respuestaA = True

                "2) No, las personas están ligadas a los cuerpos y al momento de la muerte cesa de existir la persona":
                        $pregunta4_respuestaB = True
                
                "3) No lo sé, o no se puede saber":
                        $ pregunta4_respuestaC = True
        
        #Inicio de la quinta pregunta
        menu:
                doc "Si uno quiere estudiar la realidad en el sentido más general, es mejor…"

                "1) Buscar leyes o estructuras universales. Intentar llegar a una perspectiva de lo más general y abstracta. Alcanzar respuestas absolutas":
                        $ pregunta5_respuestaA = True
                
                "2) Estudiar las cosas en su conexión con otras, incorporando las contradicciones u oposiciones de fuerzas presentes en un entendimiento que crece constantemente": 
                        $ pregunta5_respuestaB = True

                "3) Ninguna de las anteriores, o no creo que tal cosa sea posible":
                        $ pregunta5_respuestaC = True

        #Inicio de la sexta pregunta
        menu:
                doc "¿Es posible cosas, en el sentido más general? Es decir, ¿Es el conocimiento posible?"

                "1) Sí, el conocimiento es posible":
                        $ pregunta6_respuestaA = True
                
                "2) No, no hay fenómenos tales como hechos, o creencias justificadas verdaderas, o cualquier intento similar":
                        $ pregunta6_respuestaB = True
        
        #Inicio de la septima pregunta
        menu:
                doc "adfadfadfadfa"

                "1) placeholder": 
                        $ pregunta7_respuestaA = True
                
                "2) placeholder":
                        $ pregunta7_respuestaB = True



        

        #TODO: TRABAJAR EN LAS EVALUACIONES
        #      O sea, en los "eventos de contradicción"
        #FIN DEL JUEGO
        return