# djan-crud-auth
* user.is_authenticated //verifica si guardo sesion
* login(request,user) //guarda sesion
* logout(request) //cierra sesion 
* admin.site.register(\<name_model\>) //registra un modelo en la ventana de administrador
* \<name_Model\>.objects.filter() // devuelve objetos con los campos requeridos
* \<name_Model\>.objects.get() // devuelve un unico objeto si es que existe si no devuleve un error
* from django.contrib.auth.decorators import login_required //no permite el acceso a las funciones a menos que inicie sesion el usuario
* main.content //crea un main con clase content

## Generar requeriments.txt
* pip freeze > requeriments.txt //generar texto con las versiones de los modulos que necesitas
* pip install -r requetiments.txt //instala los modulos con las versiones que necesitas
