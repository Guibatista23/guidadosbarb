# ✂️ Data Pipeline Serverless: Inteligência de Negócio para Barbearia

Este projeto implementa uma arquitetura de **Data Lakehouse** de baixo custo para transformar dados transacionais brutos de uma barbearia em insights de retenção de clientes (**Churn Analysis**). 

O foco principal foi a criação de um ecossistema **Serverless** na AWS, priorizando segurança (IAM) e custo operacional próximo a zero.

---

## 🎯 O Problema de Negócio
A barbearia operava com dados isolados em máquinas de cartão (POS), sem visibilidade sobre a recorrência dos clientes. O objetivo foi identificar clientes **"Ouro", "Prata" e "Bronze"** que não retornavam há mais de 20 dias, permitindo ações de marketing direcionadas para recuperação de faturamento.

## 🏗️ Arquitetura e Stack Tecnológica
A solução foi desenhada para ser escalável e econômica (Pay-as-you-go):

* **Armazenamento (Data Lake):** **Amazon S3** (Camada Bronze) para armazenamento de arquivos CSV brutos.
* **Motor de Consulta:** **Amazon Athena** para processamento SQL direto no S3 (Arquitetura Schema-on-Read).
* **Visualização (BI):** **Streamlit (Python)** conectado via `PyAthena` para dashboards em tempo real.
* **Segurança & Governança:** **AWS IAM** com políticas de "Menor Privilégio" e configuração via AWS CLI.
* **Lógica de Dados:** **SQL (CTEs)** para segmentação RFM (Recência, Frequência e Valor).

## 🛠️ Destaques de Engenharia
* **Otimização de Custos:** Ao utilizar Athena em vez de um banco de dados RDS (PostgreSQL/MySQL) ligado 24/7, o custo operacional foi reduzido em quase 100%, pagando apenas frações de centavos por query.
* **Tratamento de Dados Anônimos:** Como a maquininha não fornece nomes, utilizei o **Final do Cartão** como chave primária para rastrear o comportamento de consumo (LTV - Lifetime Value).
* **Segurança de Dados:** Implementação de um pipeline seguro, tratando erros de `AccessDenied` e garantindo que nenhuma credencial fosse exposta no código (uso de `.gitignore` e AWS CLI).

## 📊 Visualização dos Insights
O dashboard final no Streamlit apresenta:
1.  **Métrica de Churn:** Lista de clientes fiéis em risco de abandono.
2.  **Faturamento por Categoria:** Visão clara de quanto os clientes "Ouro" representam no caixa.
3.  **Ranking de Fidelidade:** Identificação dos cartões com maior frequência de visitas.

---

## 🎥 Demonstração
> [COLE AQUI O LINK DO SEU VÍDEO DO YOUTUBE OU LINKEDIN]

## 🚀 Como Executar
1. Configure suas credenciais AWS via `aws configure`.
2. Certifique-se de que o bucket no S3 e a tabela no Athena estejam criados.
3. Instale as dependências: `pip install streamlit pyathena pandas`.
4. Rode a aplicação: `streamlit run app_athena.py`.
