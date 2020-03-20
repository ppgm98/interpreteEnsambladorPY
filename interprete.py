
variables={}
stack=[]

def buebos():
    print("feature1")

def checkOpcode(linea):
    if linea[0]=="mov":
       linea[1]=linea[1].split(',')
       variables[linea[1][0]]=linea[1][1]

    elif linea[0]=="add":
        linea[1]=linea[1].split(',')
        operando1=int(variables[linea[1][0]])
        operando2=int(variables[linea[1][1]])
        suma=operando1+operando2
        variables[linea[1][0]]=suma
    
    elif linea[0]=="push":
        stack.append(variables[linea[1]])

    elif linea[0]=="cmp":
        linea[1]=linea[1].split(',')
        compare1=int()


def runCode(archivo):
    for linea in archivo:
        linea=linea.replace('\r','').replace('\n','')
        linea=linea.split(" ")
        checkOpcode(linea)

def main():
    archivo=open('ensamblador.txt')
    runCode(archivo)
    print(variables)
    print(stack)

main()