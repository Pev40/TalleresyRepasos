# [["Piero",977336451,[],[]] ]

def CrearNuevoChatParaUsuario():
    Lista = []
    NombreContacto=input("Nombre de su contacto: ")
    Chat = ["No tiene ninguna conversación"]
    Lista.append(NombreContacto)
    Lista.append(Chat)
    return Lista

def CrearUsuario():
    Usuario = []
    Nombre=input("Ingrese su nombre")
    Numero=int(input("Ingrese su nombre"))
    NuevoChat = CrearNuevoChatParaUsuario()
    Usuario.append(Nombre)
    Usuario.append(Numero)
    Usuario.append(NuevoChat)
    return Usuario

def CrearNUsuariosEnLaMatriz(Usuarios):
    CantidadDeUsuarios=int(input("Cuantos deseas crear: "))
    for i in range (CantidadDeUsuarios):
        Usuarios.append(CrearUsuario())    
    
def MostrarUsuarios(Usuarios):
    for i in (len(Usuarios)):
        print("Usuario [",i,"]",Usuarios[i][0])
        
def eleccionDeUsuario(Usuarios):
    MostrarUsuarios(Usuarios)
    eleccion = int(input("Elija su usuario: "))
    return eleccion

def MostrarContactos(Usuarios,User):
    for i in (len(Usuarios[User])-2):
        print("Contacto [",i,"]",Usuarios[User][i+2][0])

def eleccionDeContacto(Usuarios):
    MostrarContactos(Usuarios)
    eleccion = int(input("Elija su usuario: "))
    return eleccion

def ImprimirUnChat(Usuarios):
    User = eleccionDeUsuario()
    Contact = eleccionDeContacto(Usuarios,User)
    for i in (len(Usuarios[User][Contact])-1):
        print(Usuarios[User][Contact][i+1],".\n")

def run():
    Matriz = []
    CrearNUsuariosEnLaMatriz(Matriz)

run()


