﻿###########################
#PRUEBA CHEQUEO FILOSOFICO#
#PROPOSITO:               #
#PROBAR SI EL SCRIPT      #
#CUMPLE LOS REQUISITOS    #
#PARA LLEVAR ACABO LA VN  #
###########################

image splash = "splash loading.png" #imagen de carga
image bg main = "images/bg main.png" #imagen de menú principal


#Definición de un personaje
define mc = Character ("Yo", color="#f1c9ee")
define doc = Character("Dra. ", color="#ff0000")


#imagenes de la Dra.
image doc neutral = "images/doc neutral.png"
image doc thinking = "images/doc thinking.png"
image doc giggle = "images/doc giggle.png"

#opciones graficas
scene black
with Pause(1)
    

##Caja de dialogo
transform diabox:
    pos(566, 32)

#inicio del splashscreen
label splashscreen: 
    scene black
    with Pause(1)

    show splash with dissolve
    with Pause(2)

    return

    show bg main with fade
    
#inicio del juego
label start:
    #Inicia Declaración de variables#
$ pregunta1_respuestaA = False  #
$ pregunta1_respuestaB = False  #
$ pregunta1_respuestaC = False  #
$ pregunta1_respuestaD = False  #
$ pregunta2_respuestaA = False  #
$ pregunta2_respuestaB = False  #
$ pregunta2_respuestaC = False  #
$ pregunta2_respuestaD = False  #
$ pregunta3_respuestaA = False  #
$ pregunta3_respuestaB = False  #
$ pregunta3_respuestaC = False  #
$ pregunta3_respuestaD = False  #
$ pregunta4_respuestaA = False  #
$ pregunta4_respuestaB = False  #
$ pregunta4_respuestaC = False  #
$ pregunta5_respuestaA = False  #
$ pregunta5_respuestaB = False  #
$ pregunta5_respuestaC = False  #
$ pregunta6_respuestaA = False  #
$ pregunta6_respuestaB = False  #
$ pregunta7_respuestaA = False  #
$ pregunta7_respuestaB = False  #
$ pregunta7_respuestaC = False  #
$ pregunta7_respuestaD = False  #
$ pregunta8_respuestaA = False  #
$ pregunta8_respuestaB = False  #
$ pregunta8_respuestaC = False  #
$ pregunta8_respuestaD = False  #
$ pregunta9_respuestaA = False  #
$ pregunta9_respuestaB = False  #
$ pregunta9_respuestaC = False  #
$ pregunta9_respuestaD = False  #
$ pregunta10_respuestaA = False  #
$ pregunta10_respuestaB = False  #
$ pregunta10_respuestaC = False  #
$ pregunta10_respuestaD = False  #
#Fin Declariacion de variables  #

show bg main with dissolve #muestra el fondo
show doc neutral at diabox #muestra la imagen doc neutra en diabox 
doc "¡Bienvenido!"
"..."

    #Inicio de la primera pregunta
menu:
    doc "¿Hay algo así como un fundamento último y permanente de la realidad? Ya sea un ser Creador, Omnipotente como Dios, o una estructura como que algo no puede ser y no ser al mismo tiempo."

    "1) Sí, hay un ser o seres así.":
            $ pregunta1_respuestaA = True

    "2) Sí, hay estructuras así":
            $ pregunta1_respuestaB = True
            
    "3) No creo, todo parece estar, o está en cambio.":
            $ pregunta1_respuestaC = True

    "4) No lo sé, o no se puede saber":
            $ pregunta1_respuestaD = True
            

    #Inicio de la segunda pregunta
menu:
    doc "¿Crees que existe un ser supremo? Un ser absoluto, primero que cualquier otro."

    "1) Sí, y ese ser es Dios.":
            $ pregunta2_respuestaA = True

    "2) Sí, pero considero a ese 'ser' un principio o sustancia absoluta.":
            $ pregunta2_respuestaB = True

    "3) No, la realidad no tiene principio tal que haya un ser 'primario'.":
            $ pregunta2_respuestaC = True
            
    "4) No lo sé, o no se puede saber.":
            $ pregunta2_respuestaD = True
    
    #Inicio de la tercera pregunta
menu:
    doc "Vamos a usar 'objeto' de manera muy general aquí, cualquier tipo de cosa, incluso si no es tangible. Para ti, la realidad está compuesta de… ¿qué tipo de objetos?"

    "1) Fundamentalmente de objetos abstractos que no podemos percibir con los sentidos como ideas, formas o estructuras profundas.":
            $ pregunta3_respuestaA = True

    "2) De varios tipos de objetos, abstractos como ideas, números, o almas, pero también de los objetos que podemos percibir e interactuar físicamente":
            $ pregunta3_respuestaB = True

    "3) Sólo hay objetos y fuerzas materiales. Todo con lo que podemos interactuar causalmente.":
            $ pregunta3_respuestaC = True
            
    "4) No lo sé, o no se puede saber.":
            $ pregunta3_respuestaD = True
    
    #Inicio de la cuarta pregunta
menu:
    doc "¿Crees que después de morir, las personas siguen existiendo de forma no corporal?"

    "1) Sí, las personas existimos como almas, o similar.":
            $ pregunta4_respuestaA = True

    "2) No, las personas están ligadas a los cuerpos y al momento de la muerte cesa de existir la persona":
            $ pregunta4_respuestaB = True

    "3) No lo sé, o no se puede saber.":
            $ pregunta4_respuestaC = True

    #Inicio de la quinta pregunta
menu:
    doc "Si uno quiere estudiar la realidad en el sentido más general, es mejor…"

    "1) Buscar leyes o estructuras universales. Intentar llegar a una perspectiva de lo más general y abstracta. Alcanzar respuestas absolutas.":
            $ pregunta5_respuestaA = True

    "2) Estudiar las cosas en su conexión con otras, incorporando las contradicciones u oposiciones de fuerzas presentes en un entendimiento que crece constantemente":
            $ pregunta5_respuestaB = True

    "3) Ninguna de las anteriores, o no creo que tal cosa sea posible.":
            $ pregunta5_respuestaC = True
    
    #Inicio de la sexta pregunta
menu:
    doc "¿Es posible conocer cosas, en el sentido más general? Es decir, ¿es el conocimiento posible?"

    "1) Sí, el conocimiento es posible.":
            $ pregunta6_respuestaA = True

    "2) No, no hay fenómenos tales como hechos, o creencias justificadas verdaderas, o cualquier intento similar":
            $ pregunta6_respuestaB = True
    
    #Inicio de la septima pregunta
menu:
    doc "¿Es posible obtener conocimiento último y permanente sobre la realidad? Ejemplos: Conocer o formular 'Leyes de la Naturaleza' o 'Conocimiento de las Primeras Causas'?"

    "1) Sí, se pueden conocer objetivamente tales cosas.":
            $ pregunta7_respuestaA = True

    "2) Sí, podemos tener conocimiento tan preciso que es para fines prácticos inmutable.":
            $ pregunta7_respuestaB = True

    "3) No como tal, pero podemos tener teorías con un enorme poder predictivo en ciertas áreas.":
            $ pregunta7_respuestaC = True

    "4) No, el conocimiento que es posible es muy limitado, o temporal.":
            $ pregunta7_respuestaD = True
    
    #Inicio de la Octava pregunta
menu:
    doc "El conocimiento que adquirimos depende principalmente de…"

    "1) El ejercicio de la razón. Uno puede adquirir conocimiento desde la meditación racional.":
            $ pregunta8_respuestaA = True

    "2) La percepción y los sentidos. Uno conoce el mundo externo a partir de percibirlo.":
            $ pregunta8_respuestaB = True

    "3) Formas inherentes en el pensamiento, que proyectamos al mundo para hacerlo entendible":
            $ pregunta8_respuestaC = True

    "4) Ser miembro de una sociedad en la que se intercambian creencias y se piden justificaciones.":
            $ pregunta8_respuestaD = True
    
    #Inicio de la Novena pregunta
menu:
    doc "Cuando conocemos algo, ¿es necesario que nuestra creencia sea verdadera?"

    "1) Sí, nuestras creencias deben corresponder con la realidad para ser consideradas conocimiento. Decir de lo que es, lo que es, y de lo que no, no.":
            $ pregunta9_respuestaA = True

    "2) Sí, pero la verdad no es una correspondencia con el estado de las cosas, sino con otras ideas.":
            $ pregunta9_respuestaB = True

    "3) No, el conocimiento se trata más bien de formar teorías coherentes que sobrevivan rondas de refutación.":
            $ pregunta9_respuestaC = True

    "4) No, el conocimiento se valida por como nos permite lograr nuestros fines prácticos, por la utilidad de las creencias.":
            $ pregunta9_respuestaD = True
    
    #Inicio de la Decima pregunta
menu:
    doc "Si una ciencia exitosa hace predicciones o teorías, ¿debemos aceptar que aquello de lo que habla existe? Por ejemplo, la física nos compromete a aceptar la existencia de cosas como electrones, la biología predica la existencia de genes, etc."

    "1) Sí, para que una teoría científica sea exitosa, tiene que ser verdadera.":
            $ pregunta10_respuestaA = True

    "2) No en su totalidad, hay términos que son más bien lenguaje figurado.":
            $ pregunta10_respuestaB = True

    "3) No es necesario, las ciencias son exitosas por su uso instrumental.":
            $ pregunta10_respuestaC = True

    "4) No, no hay una demarcación aceptable de 'ciencia exitosa'.":
            $ pregunta10_respuestaD = True
return


    

            




    
    #Evaluacion de contradicción
    #if pregunta1_respuestaA == True and pregunta2_respuestaC == True:
    #   show doc giggle at diabox
    #   "tensión detectada XD"

    
    #FIN DEL JUEGO
return
