from datetime import date
today = date.today()
todaybr = today.strftime('%d/%m/%Y')
print(todaybr)
derbyazul = int(input('Digite quantos \033[44mDERBY AZUL\033[m existe em estoque: '))
derbyprata = int(input('Digite quantos \033[41mDERBY VERMELHO\033[m existe em estoque: '))
derbyverm = int(input('Digite quantos \033[47;30mDERBY PRATA\033[m existe em estoque: '))
hollverm = int(input('Digite quantos \033[44mHOLLYWOOD AZUL\033[m existe em estoque: '))
hollazul = int(input('Digite quantos \033[41mHOLLYWOOD VERMELHO\033[m existe em estoque: '))
hollmenta = int(input('Digite quantos \033[42;30mHOLLYWOOD MENTA\033[m existe em estoque: '))
kentvermmaco = int(input('Digite quantos \033[41mKENT VERMELHO MAÇO\033[m existe em estoque: '))
kentvermbox = int(input('Digite quantos \033[1;41mKENT VERMELHO BOX\033[m existe em estoque: '))
kentazulmaco = int(input('Digite quantos \033[44mKENT AZUL MAÇO\033[m existe em estoque: '))
kentazulbox = int(input('Digite quantos \033[1;44mKENT AZUL BOX\033[m existe em estoque: '))
carlton = int(input('Digite quantos \033[7;41mCARLTON\033[m existe em estoque: '))
rothazul = int(input('Digite quantos \033[44mROTHMANS AZUL\033[m existe em estoque: '))
rothverm = int(input('Digite quantos \033[41mROTHMANS VERMELHO\033[m existe em estoque: '))
rothprata = int(input('Digite quantos \033[47;30mROTHMANS PRATA\033[m existe em estoque: '))
lustazul = int(input('Digite quantos \033[44mLUCKY STRIKE AZUL\033[m existe em estoque: '))
lustdb = int(input('Digite quantos \033[7mLUCKY STRIKE \033[m\033[30;44mDOUBLE\033[m\033[42;30mCLICK\033[m existe em estoque: '))
ritz = int(input('Digite quantos \033[7mRITZ\033[m existe em estoque: '))
plazac = int(input('Digite quantos \033[7mPLAZA CURTO\033[m existe em estoque: '))
plazal = int(input('Digite quantos \033[7mPLAZA LONGO\033[m existe em estoque: '))
luxor = int(input('Digite quantos \033[43;30mLUXOR\033[m existe em estoque: '))
chestazul = int(input('Digite quantos \033[44mCHESTERFIELD AZUL\033[m existe em estoque: '))
chestverm = int(input('Digite quantos \033[41mCHESTERFIELD VERMELHO\033[m existe em estoque: '))
malbmazul = int(input('Digite quantos \033[1;41mMALBORO BOX VERMELHO\033[m existe em estoque: '))
malbbg = int(input('Digite quantos \033[1;30;43mMALBORO BOX GOLD\033[m existe em estoque: '))
    #Daqui pra baixo cigarros sobraram
derbyazuls = int(input('Digite quantos \033[44mDERBY AZUL\033[m restaram?: '))
derbypratas = int(input('Digite quantos \033[41mDERBY VERMELHO\033[m restaram?: '))
derbyverms = int(input('Digite quantos \033[47;30mDERBY PRATA\033[m restaram?: '))
hollverms = int(input('Digite quantos \033[44mHOLLYWOOD AZUL\033[m restaram?: '))
hollazuls = int(input('Digite quantos \033[41mHOLLYWOOD VERMELHO\033[m restaram?: '))
hollmentas = int(input('Digite quantos \033[42;30mHOLLYWOOD MENTA\033[m restaram?: '))
kentvermmacos = int(input('Digite quantos \033[41mKENT VERMELHO MAÇO\033[m restaram?: '))
kentvermboxs = int(input('Digite quantos \033[1;41mKENT VERMELHO BOX\033[m restaram?: '))
kentazulmacos = int(input('Digite quantos \033[44mKENT AZUL MAÇO\033[m restaram?: '))
kentazulboxs = int(input('Digite quantos \033[1;44mKENT AZUL BOX\033[m restaram?: '))
carltons = int(input('Digite quantos \033[7;41mCARLTON\033[m restaram?: '))
rothazuls = int(input('Digite quantos \033[44mROTHMANS AZUL\033[m restaram?: '))
rothverms = int(input('Digite quantos \033[41mROTHMANS VERMELHO\033[m restaram?: '))
rothpratas = int(input('Digite quantos \033[47;30mROTHMANS PRATA\033[m restaram?: '))
lustazuls = int(input('Digite quantos \033[44mLUCKY STRIKE AZUL\033[m restaram?: '))
lustdbs = int(input('Digite quantos \033[7mLUCKY STRIKE \033[m\033[30;44mDOUBLE\033[m\033[42;30mCLICK\033[m restaram?: '))
ritzs = int(input('Digite quantos \033[7mRITZ\033[m restaram?: '))
plazacs = int(input('Digite quantos \033[7mPLAZA CURTO\033[m restaram?: '))
plazals = int(input('Digite quantos \033[7mPLAZA LONGO\033[m restaram?: '))
luxors = int(input('Digite quantos \033[43;30mLUXOR\033[m restaram?: '))
chestazuls = int(input('Digite quantos \033[44mCHESTERFIELD AZUL\033[m restaram?: '))
chestverms = int(input('Digite quantos \033[41mCHESTERFIELD VERMELHO\033[m restaram?: '))
malbmazuls = int(input('Digite quantos \033[1;41mMALBORO BOX VERMELHO\033[m restaram?: '))
malbbgs = int(input('Digite quantos \033[1;30;43mMALBORO BOX GOLD\033[m restaram?: '))

#Aqui nós iremos mostrar o resultado
vend = derbyazul - derbyazuls
vend1 = derbyverm - derbyverms
vend2 = derbyprata - derbypratas
vend3 = hollazul - hollazuls
vend4 = hollverm - hollverms
vend5 = hollmenta - hollmentas
vend6 = kentvermmaco - kentvermmacos
vend7 = kentvermbox - kentvermboxs
vend8 = kentazulmaco - kentazulmacos
vend9= kentazulbox - kentazulboxs
vend10 = carlton - carltons
vend11 = rothazul - rothazuls
vend12 = rothverm - rothverms
vend13 = rothprata - rothpratas
vend14 = lustazul - lustazuls
vend15 = lustdb - lustdbs
vend16 = ritz - ritzs
vend17 = plazac - plazacs
vend18 = plazal - plazals
vend19 = luxor - luxors
vend20 = chestazul - chestazuls
vend21 = chestverm - chestverms
malb