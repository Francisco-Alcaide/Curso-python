ingreso_mensual = 72000
gasto_mensual = 80000

#if anidados y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("estas bien abro")
    else:
        print("estas gastando mucho, no te alcanza")
    
elif ingreso_mensual > 1000:
    print("estas bien economicamente")
    
elif ingreso_mensual > 500:
    print("estas bien en argentina")
    
elif ingreso_mensual > 200:
    print("estas bien venezuela")

else:
    print("eres pobre")