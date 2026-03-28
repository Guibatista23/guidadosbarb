import streamlit as st
import pandas as pd
from pyathena import connect


AWS_REGION = "us-east-1"  
S3_STAGING_DIR = "s3://guidadosbarb3/resultados/"

st.set_page_config(page_title="Barbearia Intelligence - AWS Athena", layout="wide")
st.title("✂️ Dashboard Conectado à AWS (Data Lakehouse)")

@st.cache_data
def carregar_dados_athena():
    conn = connect(s3_staging_dir=S3_STAGING_DIR, region_name=AWS_REGION)
    query = """
    WITH resumo_clientes AS (
        SELECT 
            final_cartao,
            COUNT(id_transacao) AS frequencia,
            SUM(valor_venda) AS gasto_total
        FROM faturamento_barbearia
        GROUP BY final_cartao
    )
    SELECT 
        final_cartao,
        gasto_total,
        frequencia,
        CASE 
            WHEN gasto_total > 150 THEN '🏆 OURO'
            WHEN gasto_total BETWEEN 70 AND 150 THEN '🥈 PRATA'
            ELSE '🥉 BRONZE'
        END AS categoria
    FROM resumo_clientes
    ORDER BY gasto_total DESC;
    """
    return pd.read_sql(query, conn)

try:
    df = carregar_dados_athena()

    
    c1, c2, c3 = st.columns(3)
    c1.metric("Total de Clientes", len(df))
    c2.metric("Clientes 🏆 OURO", len(df[df['categoria'] == '🏆 OURO']))
    c3.metric("Faturamento Total", f"R$ {df['gasto_total'].sum():,.2f}")

    
    st.subheader("Distribuição por Categoria")
    st.bar_chart(df['categoria'].value_counts())

    
    st.subheader("Lista de Fidelidade (Dados do S3)")
    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"Erro ao conectar na AWS: {e}")
    st.info("Dica: Verifique se suas credenciais AWS estão configuradas no computador.")