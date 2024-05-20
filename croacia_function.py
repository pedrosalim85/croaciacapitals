croacia = [
            {
                "cidade": "Zagreb",
                "regiao": "Croácia Central",
                "populacao": 767000,
                "area": 641,
                "densidade_populacional": 1197
            },
            {
                "cidade": "Split",
                "regiao": "Dalmácia",
                "populacao": 178000,
                "area": 79.2,
                "densidade_populacional": 2246
            },
            {
                "cidade": "Rijeka",
                "regiao": "Kvarner",
                "populacao": 129000,
                "area": 128,
                "densidade_populacional": 1008
            },
            {
                "cidade": "Osijek",
                "regiao": "Eslavônia",
                "populacao": 108000,
                "area": 114.21,
                "densidade_populacional": 945
            },
            {
                "cidade": "Šibenik",
                "regiao": "Dalmácia",
                "populacao": 35000,
                "area": 38,
                "densidade_populacional": 921
            },
            {
                "cidade": "Dubrovnik",
                "regiao": "Dalmácia",
                "populacao": 43000,
                "area": 152,
                "densidade_populacional": 283
            },
            {
                "cidade": "Zadar",
                "regiao": "Dalmácia",
                "populacao": 72000,
                "area": 72.93,
                "densidade_populacional": 986
            },
            {
                "cidade": "Pula",
                "regiao": "Ístria",
                "populacao": 58000,
                "area": 52,
                "densidade_populacional": 1115
            },
            {
                "cidade": "Karlovac",
                "regiao": "Croácia Central",
                "populacao": 55000,
                "area": 128,
                "densidade_populacional": 429
            },
            {
                "cidade": "Varaždin",
                "regiao": "Norte da Croácia",
                "populacao": 47000,
                "area": 37.6,
                "densidade_populacional": 1250
            }
            ]


resposta = int(input('qual cidade croata você quer conhecer? digite um número de 1 a 10 para escolher uma cidade: 1 - Zagreb; 2 - Split; 3 - Rijeka; 4 - Osijek; 5 - Šibenik; 6 - Dubrovnik; 7 - Zadar; 8 - Pula; 9 - Karlovac; 10 - Varaždin: '))

def escolha(x):
    cidade = croacia[int(x)-1]
    print(cidade)

escolha(resposta)

continua = True

while continua:
    resposta2 = int(input('você quer conhecer outra cidade? Digite 1 para sim e 2 para não: '))
    if (resposta2 == 1):
        resposta = (input('qual cidade croata você quer conhecer? digite um número de 1 a 10 para escolher uma cidade: 1 - Zagreb; 2 - Split; 3 - Rijeka; 4 - Osijek; 5 - Šibenik; 6 - Dubrovnik; 7 - Zadar; 8 - Pula; 9 - Karlovac; 10 - Varaždin: '))
        escolha(resposta)
    else:
        print('Até a próxima!')
        break


