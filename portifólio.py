# portfolio.py
import streamlit as st
import base64
import os

st.set_page_config(page_title="Portfólio - Lucas Matheus", layout="wide")

# --- MENU ---
menu = st.sidebar.radio("Navegação", [ "ℹ️ Sobre mim","📂 Projetos", "📊 Dashboards", "📑 Relatórios","👨‍🎓 Certificados"])

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
elif menu == "ℹ️ Sobre mim":
    st.title("Sobre mim")
    st.write("""
Sou Lucas Matheus Oliveira de Brito, estudante de Estatística na UnB, com experiência em 
Python, R, SQL, Power BI e automações de dados.
""")
    st.markdown("[💼 LinkedIn](https://linkedin.com/in/SEULINK)")
    st.markdown("[💻 GitHub](https://github.com/SEUUSUARIO)")

elif menu == "👨‍🎓 Certificados":
    st.subheader("Curso de Inglês")
    st.image("Certificados/certificado_ingles.png", width=300)
    st.subheader("Cientista e de dados/Analista de dados")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_file = os.path.join(base_dir, "Certificados",
                            "Microsoft SQL Server 2022 - aprofundando em procedures e funções.pdf")

    if os.path.exists(pdf_file):
        with open(pdf_file, "rb") as f:
            pdf_bytes = f.read()
        base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="300" height="400" type="application/pdf"></iframe>'
        st.components.v1.html(pdf_display, height=400)
    else:
        st.error(f"Arquivo não encontrado: {pdf_file}")

    st.subheader("Gestão de projetos e produtos")


