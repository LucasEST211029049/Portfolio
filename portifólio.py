import streamlit as st

st.set_page_config(page_title="Portfólio - Lucas Matheus", layout="wide")

# Seletor de idioma
language = st.sidebar.selectbox("Choose language / Escolha o idioma", ["Português", "English"])
lang_code = "pt" if language == "Português" else "en"

# Dicionário de textos bilíngues
texts = {
    "pt": {
        "menu": {
            "about": "ℹ️ Sobre mim",
            "projects": "📂 Projetos",
            "dashboards": "📊 Dashboards",
            "reports": "📑 Relatórios",
            "certificates": "👨‍🎓 Certificados",
        },
        "about_text": """
Sou Lucas Matheus Oliveira de Brito, estudante de Estatística na UnB, com experiência em 
Python, R, SQL, Power BI e automações de dados.
""",
        "linkedin": "💼 LinkedIn",
        "github": "💻 GitHub",
        "projects_title": "Projetos em Python, R e SQL",
        "projects_intro": "Aqui estão alguns exemplos de projetos que desenvolvi. O código completo está disponível no GitHub.",
        "project_1_title": "1. Automação Web com Selenium",
        "project_1_code": """
from selenium import webdriver
navegador = webdriver.Chrome()
navegador.get("https://exemplo.com")
# Código de automação...
""",
        "project_1_link": "[🔗 Ver código no GitHub](https://github.com/seuusuario/seurepositorio)",
        "project_2_title": "2. Análise Estatística em R",
        "project_2_code": """
dados <- read.csv("dados.csv")
summary(dados)
""",
        "project_2_link": "[🔗 Ver código no GitHub](https://github.com/seuusuario/seurepositorio)",
        "project_3_title": "3. Consultas SQL",
        "project_3_code": """
SELECT cliente, SUM(valor) AS total_compras
FROM vendas
GROUP BY cliente;
""",
        "dashboards_title": "Dashboards em Power BI",
        "dashboards_intro": "A seguir, prints e links para dashboards (com dados fictícios).",
        "dashboard_image_caption": "Exemplo de Dashboard Power BI",
        "dashboard_link_text": "🔗 Ver Dashboard Público",
        "reports_title": "Relatórios Técnicos e Acadêmicos",
        "reports_intro": "Relatórios desenvolvidos no Overleaf (PDFs com dados fictícios).",
        "report_1_link_text": "📄 Baixar Relatório 1",
        "report_2_link_text": "📄 Baixar Relatório 2",
        "certificates_title": "Certificados",
        "english_course": "Curso de Inglês",
        "sql_server": "SQL Server",
        "project_management": "Gestão de projetos e produtos",
        "view_link": "🔗 Ver Dashboard Público",
    },
    "en": {
        "menu": {
            "about": "ℹ️ About me",
            "projects": "📂 Projects",
            "dashboards": "📊 Dashboards",
            "reports": "📑 Reports",
            "certificates": "👨‍🎓 Certificates",
        },
        "about_text": """
I am Lucas Matheus Oliveira de Brito, a Statistics student at UnB, experienced in 
Python, R, SQL, Power BI, and data automation.
""",
        "linkedin": "💼 LinkedIn",
        "github": "💻 GitHub",
        "projects_title": "Projects in Python, R, and SQL",
        "projects_intro": "Here are some project examples I developed. Full code is available on GitHub.",
        "project_1_title": "1. Web Automation with Selenium",
        "project_1_code": """
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://example.com")
# Automation code...
""",
        "project_1_link": "[🔗 See code on GitHub](https://github.com/seuusuario/seurepositorio)",
        "project_2_title": "2. Statistical Analysis in R",
        "project_2_code": """
data <- read.csv("data.csv")
summary(data)
""",
        "project_2_link": "[🔗 See code on GitHub](https://github.com/seuusuario/seurepositorio)",
        "project_3_title": "3. SQL Queries",
        "project_3_code": """
SELECT client, SUM(amount) AS total_purchases
FROM sales
GROUP BY client;
""",
        "dashboards_title": "Power BI Dashboards",
        "dashboards_intro": "Below, screenshots and links to dashboards (with fictitious data).",
        "dashboard_image_caption": "Power BI Dashboard Example",
        "dashboard_link_text": "🔗 See Public Dashboard",
        "reports_title": "Technical and Academic Reports",
        "reports_intro": "Reports developed in Overleaf (PDFs with fictitious data).",
        "report_1_link_text": "📄 Download Report 1",
        "report_2_link_text": "📄 Download Report 2",
        "certificates_title": "Certificates",
        "english_course": "English Course",
        "sql_server": "SQL Server",
        "project_management": "Project and Product Management",
        "view_link": "🔗 See Public Dashboard",
    }
}

menu = st.sidebar.radio("Navigation / Navegação", [
    texts[lang_code]["menu"]["about"],
    texts[lang_code]["menu"]["projects"],
    texts[lang_code]["menu"]["dashboards"],
    texts[lang_code]["menu"]["reports"],
    texts[lang_code]["menu"]["certificates"],
])

if menu == texts[lang_code]["menu"]["about"]:
    st.title(texts[lang_code]["menu"]["about"])
    st.write(texts[lang_code]["about_text"])
    st.markdown(f"[{texts[lang_code]['linkedin']}](https://linkedin.com/in/SEULINK)")
    st.markdown(f"[{texts[lang_code]['github']}](https://github.com/SEUUSUARIO)")

elif menu == texts[lang_code]["menu"]["projects"]:
    st.title(texts[lang_code]["projects_title"])
    st.write(texts[lang_code]["projects_intro"])

    st.subheader(texts[lang_code]["project_1_title"])
    st.code(texts[lang_code]["project_1_code"], language="python")
    st.markdown(texts[lang_code]["project_1_link"])

    st.subheader(texts[lang_code]["project_2_title"])
    st.code(texts[lang_code]["project_2_code"], language="r")
    st.markdown(texts[lang_code]["project_2_link"])

    st.subheader(texts[lang_code]["project_3_title"])
    st.code(texts[lang_code]["project_3_code"], language="sql")

elif menu == texts[lang_code]["menu"]["dashboards"]:
    st.title(texts[lang_code]["dashboards_title"])
    st.write(texts[lang_code]["dashboards_intro"])

    st.image("painel1.png", caption=texts[lang_code]["dashboard_image_caption"])
    st.markdown(f"[{texts[lang_code]['dashboard_link_text']}](https://app.powerbi.com/view?r=eyJrIjoiMGNjM2MyY2ItODQ1Zi00ODk1LWE2NzItOWU4NjhhZThkNTZlIiwidCI6ImVjMzU5YmExLTYzMGItNGQyYi1iODMzLWM4ZTZkNDhmODA1OSJ9)")

elif menu == texts[lang_code]["menu"]["reports"]:
    st.title(texts[lang_code]["reports_title"])
    st.write(texts[lang_code]["reports_intro"])

    st.markdown(f"[{texts[lang_code]['report_1_link_text']}](https://drive.google.com/SEU_LINK_AQUI)")
    st.markdown(f"[{texts[lang_code]['report_2_link_text']}](https://drive.google.com/SEU_LINK_AQUI)")

elif menu == texts[lang_code]["menu"]["certificates"]:
    st.title(texts[lang_code]["certificates_title"])

    st.subheader(texts[lang_code]["english_course"])
    st.image("Certificados/certificado_ingles.png", width=300)

    st.subheader(texts[lang_code]["sql_server"])
    images = [
        {
            "file": "Certificados/Microsoft SQL Server 2022 - getting to know SQL.png",
            "caption_pt": "Microsoft SQL Server 2022: conhecendo SQL",
            "caption_en": "Microsoft SQL Server 2022: getting to know SQL",
            "link": "https://cursos.alura.com.br/certificate/lucasmoliveirabrito2003/microsoft-sql-server-conhecendo-sql?lang=en"
        },
        {
            "file": "Certificados/Microsoft SQL Server 2022 - consultas avançadas.png",
            "caption_pt": "Microsoft SQL Server 2022 - consultas avançadas",
            "caption_en": "Microsoft SQL Server 2022 - advanced queries",
            "link": "https://cursos.alura.com.br/certificate/lucasmoliveirabrito2003/microsoft-sql-server-2022-consultas-avancadas?lang=en"
        },
        {
            "file": "Certificados/Microsoft SQL Server 2022 - manipulando dados.png",
            "caption_pt": "Microsoft SQL Server 2022 - manipulando dados",
            "caption_en": "Microsoft SQL Server 2022 - data manipulation",
            "link": "https://cursos.alura.com.br/certificate/lucasmoliveirabrito2003/microsoft-sql-server-2022-manipulando-dados?lang=en"
        },
        {
            "file": "Certificados/Microsoft SQL Server 2022 - conhecendo o T-SQL.png",
            "caption_pt": "Microsoft SQL Server 2022 - conhecendo o T-SQL",
            "caption_en": "Microsoft SQL Server 2022 - getting to know T-SQL",
            "link": "https://cursos.alura.com.br/certificate/lucasmoliveirabrito2003/microsoft-sql-server-2022-conhecendo-t-sql?lang=en"
        },
        {
            "file": "Certificados/Microsoft SQL Server 2022 - aprofundando em procedures e funções.png",
            "caption_pt": "Microsoft SQL Server 2022 - aprofundando em procedures e funções",
            "caption_en": "Microsoft SQL Server 2022 - deep dive in procedures and functions",
            "link": "https://cursos.alura.com.br/user/lucasmoliveirabrito2003/course/microsoft-sql-server-2022-procedures-funcoes/certificate?lang=en"
        },
    ]

    for i in range(0, len(images), 3):
        cols = st.columns(3)
        for idx, col in enumerate(cols):
            if i + idx < len(images):
                cert = images[i + idx]
                caption = cert["caption_pt"] if lang_code == "pt" else cert["caption_en"]
                with col:
                    st.image(cert["file"], caption=caption, width=250)
                    st.markdown(f"[{texts[lang_code]['view_link']}]({cert['link']})")

    st.subheader(texts[lang_code]["project_management"])
    # Aqui você pode adicionar mais certificados ou outras seções conforme quiser
