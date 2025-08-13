# portfolio.py
import streamlit as st

st.set_page_config(page_title="Portfólio - Lucas Matheus", layout="wide")

# --- MENU ---
menu = st.sidebar.radio("Navegação", [ "ℹ️ Sobre mim","📂 Projetos", "📊 Dashboards", "📑 Relatórios"])

# --- PROJETOS ---
if menu == "📂 Projetos":
    st.title("Projetos em Python, R e SQL")
    st.write("Aqui estão alguns exemplos de projetos que desenvolvi. O código completo está disponível no GitHub.")

    st.subheader("1. Automação Web com Selenium")
    st.code("""
from selenium import webdriver
navegador = webdriver.Chrome()
navegador.get("https://exemplo.com")
# Código de automação...
    """, language="python")
    st.markdown("[🔗 Ver código no GitHub](https://github.com/seuusuario/seurepositorio)")

    st.subheader("2. Análise Estatística em R")
    st.code("""
dados <- read.csv("dados.csv")
summary(dados)
    """, language="r")
    st.markdown("[🔗 Ver código no GitHub](https://github.com/seuusuario/seurepositorio)")

    st.subheader("3. Consultas SQL")
    st.code("""
SELECT cliente, SUM(valor) AS total_compras
FROM vendas
GROUP BY cliente;
    """, language="sql")

# --- DASHBOARDS ---
elif menu == "📊 Dashboards":
    st.title("Dashboards em Power BI")
    st.write("A seguir, prints e links para dashboards (com dados fictícios).")

    st.image("painel1.png", caption="Exemplo de Dashboard Power BI")
    st.markdown("[🔗 Ver Dashboard Público](https://app.powerbi.com/view?r=eyJrIjoiMGNjM2MyY2ItODQ1Zi00ODk1LWE2NzItOWU4NjhhZThkNTZlIiwidCI6ImVjMzU5YmExLTYzMGItNGQyYi1iODMzLWM4ZTZkNDhmODA1OSJ9)")

# --- RELATÓRIOS ---
elif menu == "📑 Relatórios":
    st.title("Relatórios Técnicos e Acadêmicos")
    st.write("Relatórios desenvolvidos no Overleaf (PDFs com dados fictícios).")

    st.markdown("[📄 Baixar Relatório 1](https://drive.google.com/SEU_LINK_AQUI)")
    st.markdown("[📄 Baixar Relatório 2](https://drive.google.com/SEU_LINK_AQUI)")

# --- SOBRE ---
elif menu == "ℹ️ Sobre":
    st.title("Sobre mim")
    st.write("""
Sou Lucas Matheus Oliveira de Brito, estudante de Estatística na UnB, com experiência em 
Python, R, SQL, Power BI e automações de dados.
""")
    st.markdown("[💼 LinkedIn](https://linkedin.com/in/SEULINK)")
    st.markdown("[💻 GitHub](https://github.com/SEUUSUARIO)")
