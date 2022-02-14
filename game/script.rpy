###########################
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
    #Fin Declariacion de variables  #

    show bg main with dissolve #muestra el fondo
    show doc neutral at diabox #muestra la imagen doc neutra en diabox 
    
    ######### PRIMER LINEA DE DIALOGO #########
    doc "¡Bienvenido!"
    "..."

    #Inicio de la primera pregunta
    menu:
        
        doc "¿Hay algo así como un fundamento último y permanente de la realidad?"

        "1) Sí, hay un ser o seres así (Como Dios).":
            $ pregunta1_respuestaA = True

        "2) Sí, hay estructuras así (Como la no-contradicción, que algo no puede ser y no ser al mismo tiempo).":
            $ pregunta1_respuestaB = True
            
        "3) No creo, todo parece estar, o está en cambio.":
            $ pregunta1_respuestaC = True
        "4) No lo sé, o no se puede saber.":
            $ pregunta1_respuestaD = True
            

    #Inicio de la segunda pregunta
    menu:

        doc "¿Crees que existe un ser supremo? Un ser absoluto , primero que cualquier otro."

        "1) Sí, y ese ser es Dios.":
            $ pregunta2_respuestaA = True

        "2) Sí, pero considero a ese 'ser' un principio o sustancia absoluta.":
            $ pregunta2_respuestaB = True

        "3) No, la realidad no tiene principio tal que haya un ser 'primario'.":
            $ pregunta2_respuestaC = True
            
        "4) No lo sé, o no se puede saber.":
            $ pregunta2_respuestaD = True
    
    #Evaluacion de contradicción
    if pregunta1_respuestaA == True and pregunta2_respuestaC == True:
        show doc giggle at diabox
        "tensión detectada XD"

    
    #FIN DEL JUEGO
return