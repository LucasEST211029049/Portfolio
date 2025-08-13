import streamlit as st

st.set_page_config(page_title="Portfólio - Lucas Matheus", layout="wide")

# Seletor de idioma no sidebar
language = st.sidebar.selectbox("Choose language / Escolha o idioma", ["Português", "English"])
lang_code = "pt" if language == "Português" else "en"

# Dicionário de textos para cada idioma
texts = {
    "pt": {
        "menu": {
            "about": "ℹ️ Sobre mim",
            "projects": "📂 Projetos",
            "dashboards": "📊 Dashboards",
            "reports": "📑 Relatórios",
            "certificates": "👨‍🎓 Certificados",
        },
        "certificates_title": "Certificados",
        "english_course": "Curso de Inglês",
        "sql_server": "SQL Server",
        "project_management": "Gestão de projetos e produtos",
        "view_link": "🔗 Ver Dashboard Público",
        # outros textos que precisar
    },
    "en": {
        "menu": {
            "about": "ℹ️ About me",
            "projects": "📂 Projects",
            "dashboards": "📊 Dashboards",
            "reports": "📑 Reports",
            "certificates": "👨‍🎓 Certificates",
        },
        "certificates_title": "Certificates",
        "english_course": "English Course",
        "sql_server": "SQL Server",
        "project_management": "Project and Product Management",
        "view_link": "🔗 See Public Dashboard",
    },
}

menu = st.sidebar.radio("Navigation / Navegação", [
    texts[lang_code]["menu"]["about"],
    texts[lang_code]["menu"]["projects"],
    texts[lang_code]["menu"]["dashboards"],
    texts[lang_code]["menu"]["reports"],
    texts[lang_code]["menu"]["certificates"],
])

# Agora seu menu vai trocar de idioma automaticamente

if menu == texts[lang_code]["menu"]["certificates"]:
    st.subheader(texts[lang_code]["english_course"])
    st.image("Certificados/certificado_ingles.png", width=300)
    st.subheader(texts[lang_code]["sql_server"])

    images = [
        ("Certificados/Microsoft SQL Server 2022 - getting to know SQL.png", "Microsoft SQL Server 2022: conhecendo SQL", "https://cursos.alura.com.br/certificate/lucasmoliveirabrito2003/microsoft-sql-server-conhecendo-sql?lang=en"),
        ("Certificados/Microsoft SQL Server 2022 - consultas avançadas.png", "Microsoft SQL Server 2022 - consultas avançadas", "https://cursos.alura.com.br/certificate/lucasmoliveirabrito2003/microsoft-sql-server-2022-consultas-avancadas?lang=en"),
        ("Certificados/Microsoft SQL Server 2022 - manipulando dados.png", "Microsoft SQL Server 2022 - manipulando dados", "https://cursos.alura.com.br/certificate/lucasmoliveirabrito2003/microsoft-sql-server-2022-manipulando-dados?lang=en"),
        ("Certificados/Microsoft SQL Server 2022 - conhecendo o T-SQL.png", "Microsoft SQL Server 2022 - conhecendo o T-SQL", "https://cursos.alura.com.br/certificate/lucasmoliveirabrito2003/microsoft-sql-server-2022-conhecendo-t-sql?lang=en"),
        ("Certificados/Microsoft SQL Server 2022 - aprofundando em procedures e funções.png", "Microsoft SQL Server 2022 - aprofundando em procedures e funções", "https://cursos.alura.com.br/user/lucasmoliveirabrito2003/course/microsoft-sql-server-2022-procedures-funcoes/certificate?lang=en"),
    ]

    for i in range(0, len(images), 3):
        cols = st.columns(3)
        for idx, col in enumerate(cols):
            if i + idx < len(images):
                img, caption, link = images[i + idx]
                with col:
                    st.image(img, caption=caption, width=250)
                    st.markdown(f"[{texts[lang_code]['view_link']}]({link})")

    st.subheader(texts[lang_code]["project_management"])
    # Continue adicionando os conteúdos e traduções conforme quiser...

# Continue adaptando o resto do seu app usando essa lógica para trocar os textos e legendas
