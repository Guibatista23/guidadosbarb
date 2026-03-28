import pandas as pd
import random
from datetime import datetime, timedelta


barbeiros = ['Guilherme', 'Paulo Sergio', 'Alex']
servicos = {
    'Corte': 35.00,
    'Barba': 25.00,
    'Combo': 55.00,
    'Sobrancelha': 15.00,
    'Progressiva': 120.00
}

data_lista = []

for i in range(1, 101):
    dias_atras = random.randint(0, 60)
    data_venda = datetime.now() - timedelta(days=dias_atras)
    
    servico = random.choice(list(servicos.keys()))
    valor = servicos[servico]
    
    
    final_cartao = random.randint(1000, 9999) 
    
    data_lista.append({
        'id_transacao': 1000 + i,
        'data_hora': data_venda.strftime('%Y-%m-%d %H:%M:%S'),
        'vendedor': random.choice(barbeiros),
        'servico': servico,
        'valor_venda': valor,
        'final_cartao': str(final_cartao)
    })

df = pd.DataFrame(data_lista)
df.to_csv('faturamento_barbearia.csv', index=False)
print("✅ Arquivo 'faturamento_barbearia.csv' gerado com sucesso!")