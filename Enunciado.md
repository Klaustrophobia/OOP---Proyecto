## PROPUESTA 
    Una empresa requiere realizar un sistema de ventas este sistema tendrá 
    el manejo de personal, compras, productos, ventas, envíos, del personal 
    se manejan 4 diferentes cargos, administradores, vendedores, compradores 
    y un personal de consulta, de igual manera el sistema manejara 4 productos 
    principales(a criterio del estudiante), y también manejara un forma de 
    productos por combo, esta forma será un conjunto de productos que se venderán
    como uno solo, para que un producto tenga existencia es necesario que se 
    realicen compras de este producto, por lo cual se requiere poder realizar
    ordenes de compra que luego se darán como recibidas y de esta forma se 
    podrá ingresar la existencia al producto o crear un nuevo producto en el 
    caso de que no exista.

    Las ventas se realizaran como una facturación normal donde se tiene un
    encabezado y un detalle de la factura, ese detalle serian los producto
    o combos o ambos, así mismo una factura cuenta con un control de envio 
    ya que puede ser a domicilio o no, este control de envio identificaría 
    el estado en el que se encuentre por ejemplo puede estar en “enviado”, 
    “recibido”, “transito” etc.

## SOLUCION    
                                          CLASE I = Clase Padre ; Clase II = Clase Hijo I ; Clase III = Clase Hija II
    Persona {CLASE I}                           [Nombre, Apellido, Identidad, Telefono, Correo]
        - Personal {CLASE II}                   [Num_Empleado, Salario]
            - Vendedores {CLASE III}            []{Encargado de: Venta de Producto, Envio de Producto}
            - Compradores {CLASE III}           []{Encargado de: Compra de Producto}
            - Consultores {CLASE III}           []{Obser. de Producto}
            - Administradores {CLASE  IV}       []{Encargado de administrar : producto, personal, ganancias}  
    
        - Cliente {Clase II}
        
    Producto {CLASE I}                          [Costo, Existencia]
        -Hamburguesa {Clase II}                 []
        -Pizza   {Clase II}                     []
        -Pastel {Clase II}                      []
        -Spaguetti {Clase II}                   []

    Factura {CLASE I} 
        - id: int        
        - fecha: Date    
        - estado: Str 
        - Domicilio: Boolean
     
    Compra {CLASE I}
        - id: int
        - fecha: Date
        - estado: Str
      
             
        
    Structure of Class
    Personal {Nombre: Str, Apellido: Str, Num_Empleado: Int, Telefono:Int, Correo:Str, Salario:Double}
        Administradores {Departamento: Str}
        Vendedores {Area_Venta: Str, Metas_Ventas: Double}
        Compradores {proveedores: List} [Abastecen]
        Consultores {Area_Consultoria: Str}
    
    Productos {Codigo: Int, Marca: Str, Modelo: Str, Costo: Double, Existencia: Int}
        Metodo Abstracto -> Combo de compra

        Celulares {Ram, Cantidad_Camaras, Megapixeles, Almacenamiento}
        Lavadoras {Secadora, Capacidad, Consumo_Energia}
        Televisores {Tamano, Resolucion, Smart}
        Refrigeradores {Tipo, Cantidad_Puertas, Dispensador_Agua, Consumo_Energia}
    
    


    


    

