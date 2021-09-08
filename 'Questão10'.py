'Questão10'
compras=list()
feijão= float (8.00)
arroz= float (4.30)
macarrão= float (2.30)
while True:
    pro= input('Mecione um produto: ')
    Quant1= int(input('quantidade: '))
    if pro == 'feijão':
        feijão=Quant1*feijão
    if pro == 'arroz':
        arroz=Quant1*arroz
    if pro == macarrão:
        macarrão=Quant1*macarrão
    total=feijão+macarrão+arroz
    compras.append([pro, Quant1])
    fim= input('quer adcionar mais:s/n? ')
    if fim in 'n' and 'não':
        break
print ('<--'*30,'>')
print (total)
for i, a in enumerate (compras):
    print(a)
