from tkinter import *
from tkinter import messagebox


denom=[50000,20000,10000,5000,2000,1000,500,200,100,50]
exist=[0,0,0,0,0,0,0,0,0,0]


v=Tk()

#Aspecto de la ventana
v.title("EXAMEN FINAL")
v.minsize(300,350)


#Variables
n0 = StringVar(); n1 = StringVar()
n2 = StringVar(); n3 = StringVar()
n4 = StringVar(); n5 = StringVar()
n6 = StringVar(); n7 = StringVar()
n8 = StringVar(); n9 = StringVar()


def actualizar():
    exist[0]=int(n0.get()); exist[1]=int(n1.get())
    exist[2]=int(n2.get()); exist[3]=int(n3.get())
    exist[4]=int(n4.get()); exist[5]=int(n5.get())
    exist[6]=int(n6.get()); exist[7]=int(n7.get())
    exist[8]=int(n8.get()); exist[9]=int(n9.get())

#Función para actualizar valores existentes
def actualizar2():
    n0.set(exist[0]); n1.set(exist[1])
    n2.set(exist[2]); n3.set(exist[3])
    n4.set(exist[4]); n5.set(exist[5])
    n6.set(exist[6]); n7.set(exist[7])
    n8.set(exist[8]); n9.set(exist[9])
    

def devuelve():
    devolver=[]
    valor=int(entrada.get())
    for i in range(len(denom)):
        if(exist[i]==0):
            devolver.append(0)
        else:
            r1=valor//denom[i]    
            if(r1>exist[i]):
                r1=exist[i]
                devolver.append(r1)
                restar=r1*denom[i]
                valor=valor-restar
                exist[i]=0
            else:
                devolver.append(r1)
                restar=r1*denom[i]
                valor=valor-restar
                exist[i]=exist[i]-r1
    actualizar2()
    
    print("\nLa devuelta se compone de: ")
    for i in range(len(devolver)):
        if (devolver[i]==0):
            None
        elif(denom[i]>=1000 and devolver[i]==1):
            print(devolver[i]," billete de $",denom[i],sep="")
        elif(denom[i]>=1000 and devolver[i]>1):
            print(devolver[i]," billetes de $",denom[i],sep="")
        elif(denom[i]<1000 and devolver[i]<=1):
            print(devolver[i]," moneda de $",denom[i],sep="")
        else:
            print(devolver[i]," monedas de $",denom[i],sep="")
    if(valor>0):
        messagebox.showwarning(title="Alerta", message="La devuelta es incompleta. Por favor llene y actualice la caja")


#Valor a devolver
entrada=Entry(v,width=10)

#Botones
boton1=Button(v,text="Devolver",command=devuelve)
actual=Button(v,text="Actualizar",command=actualizar)

#Labels de los títulos
titulo1=Label(v,text="Denominación")
titulo2=Label(v,text="Existencia")

#Labels de denominaciones de moneda
valor0=Label(v,text="50.000")
valor1=Label(v,text="20.000")
valor2=Label(v,text="10.000")
valor3=Label(v,text="5.000")
valor4=Label(v,text="2.000")
valor5=Label(v,text="1.000")
valor6=Label(v,text="500")
valor7=Label(v,text="200")
valor8=Label(v,text="100")
valor9=Label(v,text="50")

#Existencia de las denominaciones
entrada0=Entry(v, textvariable=n0, width=8)
entrada1=Entry(v, textvariable=n1, width=8)
entrada2=Entry(v, textvariable=n2, width=8)
entrada3=Entry(v, textvariable=n3, width=8)
entrada4=Entry(v, textvariable=n4, width=8)
entrada5=Entry(v, textvariable=n5, width=8)
entrada6=Entry(v, textvariable=n6, width=8)
entrada7=Entry(v, textvariable=n7, width=8)
entrada8=Entry(v, textvariable=n8, width=8)
entrada9=Entry(v, textvariable=n9, width=8)


#Grilla
titulo1.grid(row=0,column=0); titulo2.grid(row=0,column=1)
valor0.grid(row=1,column=0); entrada0.grid(row=1,column=1)
valor1.grid(row=2,column=0); entrada1.grid(row=2,column=1)
valor2.grid(row=3,column=0); entrada2.grid(row=3,column=1)
valor3.grid(row=4,column=0); entrada3.grid(row=4,column=1)
valor4.grid(row=5,column=0); entrada4.grid(row=5,column=1)
valor5.grid(row=6,column=0); entrada5.grid(row=6,column=1)
valor6.grid(row=7,column=0); entrada6.grid(row=7,column=1)
valor7.grid(row=8,column=0); entrada7.grid(row=8,column=1)
valor8.grid(row=9,column=0); entrada8.grid(row=9,column=1)
valor9.grid(row=10,column=0); entrada9.grid(row=10,column=1)
actual.grid(row=11,column=1)
boton1.grid(row=12, column=0); entrada.grid(row=12, column=1)

v.mainloop()




