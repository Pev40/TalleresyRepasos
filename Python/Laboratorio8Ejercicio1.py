# [["Piero",977336451,[],[]] ]

def CrearNuevoChatParaUsuario():
    Lista = []
    NombreContacto=input("Nombre de su contacto: ")
    Chat = "No tiene ninguna conversación"
    Lista.append(NombreContacto)
    Lista.append(Chat)
    return Lista

def CrearUsuario():
    Usuario = []
    Nombre = input("Ingrese su nombre: ")
    Numero = int(input("Ingrese su numero: "))
    NuevoChat = CrearNuevoChatParaUsuario()
    Usuario.append(Nombre)
    Usuario.append(Numero)
    Usuario.append(NuevoChat)
    return Usuario

def CrearNUsuariosEnLaMatriz(Usuarios):
    CantidadDeUsuarios = int(input("Cuantos deseas crear: "))
    for i in range (CantidadDeUsuarios):
        Usuarios.append(CrearUsuario())    

def MostrarUsuarios(Usuarios):
    print("################# USUARIOS #####################")
    j = 0
    for i in range(0,len(Usuarios),1):
        print(type(i))
        print("Usuario [",i,"]",Usuarios[j][0])
        j=j+1
# (0Inicio,Final,salto) 
 
def eleccionDeUsuario(Usuarios):
    MostrarUsuarios(Usuarios)
    eleccion = int(input("Elija su usuario: "))
    return eleccion

def MostrarContactos(Usuarios,User):
    print("################# TUS CONTACTOS #####################")
    j = 2
    for i in range(2,len(Usuarios[User]),1):
        print("Contacto [",i,"]",Usuarios[User][i][0])
        j=j+1

def eleccionDeContacto(Usuarios,User):
    MostrarContactos(Usuarios,User)
    eleccion = int(input("Elija su usuario: "))
    return eleccion

def ImprimirUnChat(Usuarios,User,Contact):
    j=0
    for i in range(0,len(Usuarios[User][Contact]),1):
        print(Usuarios[User][Contact][i],"\n")
        j=j+1

def run():
    Matriz = []
    MatrizPrueba = [["Piero",95959595,["Luciana","No hay mensajes","Hello","Wenas"],["Paul","No hay Mensajes"]],["Luciana",9595959,["Piero","No hay mensajes","Hello"]]]
    CrearNUsuariosEnLaMatriz(Matriz)
    #MostrarUsuarios(MatrizPrueba)
    User = eleccionDeUsuario(Matriz)
    Contact = eleccionDeContacto(Matriz,User)
    ImprimirUnChat(Matriz,User,Contact)
    #ImprimirUnChat(MatrizPrueba,0,2)
    
run()


