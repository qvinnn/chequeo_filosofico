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
    show bg main with dissolve
    show doc neutral at diabox #muestra la imagen doc neutra en diabox 
    doc "¡Bienvenido!"
    "..."

    #Inicio de la primera pregunta
    menu:
        
        doc "¿Eres comunista?"

        "Sí.":
            $ comunista = True #Creo que esto viene siendo muy redundante
            $ respuesta_pregunta1 = 1

        "No.":
            $comunista = False
            $respuesta_pregunta1 = 2
    
    #Inicio de la segunda pregunta
    menu:

        doc "¿Eres anarquista?"

        "Sí.":
            $ anarquista = True 
            $ respuesta_pregunta2 = 2
        
        "No.":
            $ anarquista = False
            $ respuesta_pregunta2 = 2
    
    if comunista == True or anarquista == True:
        $jugador_chairo = True
    
    #Inicio de la tercera pregunta
    show doc thinking at diabox
    menu:
        
        
        doc "¿Eres chairo?"
        
        "Sí.":
            $jugador_chairo = True #HMMMMMMMMMMM ¿LES PARECE MEJOR TRABAJAR CON SOLO VALORES BOOLEANOS?????????????
            $respuesta_pregunta3 = 1
            
        "No.":
            $jugador_chairo = False #Aquí la variable cambia a false al ser declarada previamente como true automaticamente al ser comunista o anarquista
            $respuesta_pregunta3 = 2
    
    #Evaluacion de contradicción
    if jugador_chairo == False  and (anarquista == True or comunista == True):
        show doc giggle at diabox
        doc "Puede que de hecho SÍ seas chairo...."
    
    if jugador_chairo == True and (anarquista == True or comunista == True):
        show doc giggle at diabox
        doc "Sabes que eres chairo lol"
    
    if jugador_chairo == False and (anarquista == False and comunista == False):
        doc "No eres chairo..."
    
    #FIN DEL JUEGO
    return
    
    