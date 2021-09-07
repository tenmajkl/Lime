from Route import Route

@Route.get("/")
def cs():
    return "ahoj tady je to misto"

def parek():
    return "PAREK V ROHLIKU PRO VSECHNY"

Route.get("/parek", controller=parek)

Route.execute()
