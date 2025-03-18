import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np


st.set_page_config(
    page_title="Análise de Dados",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

pages = st.sidebar.radio(
        "Escolha o tópico 👇",
        ["1-Apresentação", "2-Análises Iniciais", "3-Análises Finais"]
        )
st.sidebar.markdown("Desenvolvido por Gustavo Gouvêa Soares *ggsgustavoggs@gmail.com*")

def plot_distribution(x, y, title, xlabel, ylabel):
    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel)
    st.plotly_chart(fig)

if "df_puro" not in st.session_state:
    df = pd.read_csv("Geral/CP4-Banco.csv", index_col=False)
    st.session_state["df_puro"] = df

if "df_diretoriasXPerguntas" not in st.session_state:
    df = st.session_state["df_puro"][:]
    df.drop(columns=["total de pessoas por diretoria"], inplace=True)
    df.drop(columns=["reclamacoes totais"], inplace=True)
    df.drop(index=8, inplace=True)
    df.drop(index=9, inplace=True)
    for coluna in df.columns:
        if coluna != "diretorias":
            df[coluna]= pd.to_numeric(df[coluna], errors="coerce")
    st.session_state["df_diretoriasXPerguntas"] = df

if "df_diretoriasXTotal" not in st.session_state:
    df_apoio = st.session_state["df_puro"][:]
    df = df_apoio[["diretorias", "total de pessoas por diretoria", "reclamacoes totais"]]
    df.drop(index=8, inplace=True)
    df.drop(index=9, inplace=True)
    df["total de pessoas por diretoria"]= pd.to_numeric(df["total de pessoas por diretoria"], errors="coerce")
    df["reclamacoes totais"]= pd.to_numeric(df["reclamacoes totais"], errors="coerce")
    df["proporcao de reclamacoes totais"] = round(df["reclamacoes totais"] / df["total de pessoas por diretoria"], 2)
    st.session_state["df_diretoriasXTotal"] = df

if "df_diretoriasXTotal_reduzido" not in st.session_state:
    df = st.session_state["df_diretoriasXTotal"][:]
    df = df[["diretorias", "proporcao de reclamacoes totais"]]
    st.session_state["df_diretoriasXTotal_reduzido"] = df

if "df_perguntas" not in st.session_state:
    df = st.session_state["df_puro"][:]
    df.drop(columns=["total de pessoas por diretoria"], inplace=True)
    df.drop(columns=["reclamacoes totais"], inplace=True)
    for linha in range(8):
        df.drop(index=linha, inplace=True)
    df.rename(columns={"diretorias": " "}, inplace=True)
    df = df.T
    df.rename(columns={8: "reclamacoes totais"}, inplace=True)
    df.rename(columns={9: "pergunta"}, inplace=True)
    df.drop(index=" ", inplace=True)
    df["reclamacoes totais"]= pd.to_numeric(df["reclamacoes totais"], errors="coerce")
    st.session_state["df_perguntas"] = df

if "df_perguntas_reduzido" not in st.session_state:
    df = st.session_state["df_perguntas"][:]
    df.drop(columns=["pergunta"], inplace=True)
    st.session_state["df_perguntas_reduzido"] = df


if pages == "1-Apresentação":
    st.write("# 1-Apresentação dos dados e tipos de variáveis")
    col1, col2 = st.columns(2)
    col1.divider()

    st.write(" ")
    st.write(" ")
    st.write("## Conjunto de dados utilizados")
    st.divider()
    st.write("De acordo com o resultado obtido pela Pesquisa de Satisfação dos funcionários da Empresa, será feita uma análise do resultado a fim de perceber algum problema em alguma questão pontual ou em algum setor da empresa.")
    
    st.write("Tabela 1 (registro de Insatisfação por Diretoria e Pergunta):")
    st.dataframe(st.session_state["df_diretoriasXPerguntas"])

    st.write("Tabela 2 (comparação e Proporção entre Tamanho e Reclamações de cada Diretoria):")
    st.dataframe(st.session_state["df_diretoriasXTotal"])

    st.write("Tabela 3 (descrição e total de Reclamações de cada Pergunta):")
    st.dataframe(st.session_state["df_perguntas"])


    st.write(" ")
    st.write(" ")
    st.write("## Tipo de variáveis")
    st.divider()
    st.write("- Tabela 1\n\t- Registro de Insatisfação por Diretoria e Pergunta\n\t\t- Dado Quantitativo e Discreto")
    st.write("- Tabela 2\n\t- Total de pessoa por Diretoria\n\t\t- Dado Quantitativo e Discreto\n\t- Reclamações Totais por Diretoria\n\t\t- Dado Quantitativo e Discreto\n\t- Proporção de Reclamações por Diretoria\n\t\t- Dado Quantitativo e Contínuo")
    st.write("- Tabela 3\n\t- Reclamações Totais por Pergunta\n\t\t- Dado Quantitativo e Discreto\n\t- Descrição da Pergunta\n\t\t- Dado Qualitativo Nominal")


    st.write(" ")
    st.write(" ")
    st.write("## Principais perguntas de análise")
    st.divider()
    st.write("- A quantidade de Reclamações é proporcional ao tamanho da Diretoria e se não for como ela está distribuída?")
    st.write("- Todas as reclamações de cada pergunta seguem uma média ou existem problemas dentro da empresa a serem resolvidos de forma mais urgente?")
elif pages == "2-Análises Iniciais":
    st.write("# 2-Análise inicial sobre Medidas centrais, de Dispersão e sobre Correlação")
    col1, col2 = st.columns(2)
    col1.divider()

    st.write(" ")
    st.write(" ")
    st.write("## Média, Quartis, Desvio Padrão e Gráficos")
    st.divider()

    st.write("### Diretoria X Reclamações")
    cor_pearson, p_pearson = stats.pearsonr(st.session_state["df_diretoriasXTotal"]["total de pessoas por diretoria"], st.session_state["df_diretoriasXTotal"]["proporcao de reclamacoes totais"])
    fig = px.scatter(st.session_state["df_diretoriasXTotal"], x="total de pessoas por diretoria", y="proporcao de reclamacoes totais", text="diretorias", size="proporcao de reclamacoes totais", color="proporcao de reclamacoes totais", trendline="ols", title=f"Correlação entre Reclamações e Tamanho de uma Diretoria(Coeficiente de Correlação de Pearson: {cor_pearson:.2f})", color_continuous_scale="reds")
    fig.update_traces(textposition="top center", marker=dict(opacity=0.7, line=dict(width=1, color="black")))
    st.plotly_chart(fig)
    col1, col2 = st.columns([4, 6])
    col1.write(" ")
    col1.write(" ")
    col1.write("Média, Mediana e outros Quartis e Desvio Padrão")
    col1.dataframe((st.session_state["df_diretoriasXTotal_reduzido"]).describe())
    df_boxplot = st.session_state["df_diretoriasXTotal"][:]
    fig = px.box(st.session_state["df_diretoriasXTotal_reduzido"], y="proporcao de reclamacoes totais", points="all", title="Boxplot da proporção", hover_data={"diretorias": True})
    fig.update_traces(marker=dict(size=10, color="red", opacity=0.7), jitter=0.3)
    col2.plotly_chart(fig)

    st.write(" ")
    st.write(" ")
    st.write("### Perguntas X Reclamações")
    fig = px.line(st.session_state["df_perguntas_reduzido"], x=st.session_state["df_perguntas_reduzido"].index, y="reclamacoes totais", title="Gráfico Linear de Reclamações Totais por Pergunta", markers=True)
    st.plotly_chart(fig)
    col1, col2 = st.columns([4, 6])
    col1.write(" ")
    col1.write(" ")
    col1.write("Média, Mediana e outros Quartis e Desvio Padrão")
    col1.dataframe(st.session_state["df_perguntas"].describe())
    fig = px.box(st.session_state["df_perguntas"], y="reclamacoes totais", points="all", title="Boxplot de Totais de Reclamações", hover_data={"pergunta": True})
    fig.update_traces(marker=dict(size=10, color="red", opacity=0.7), jitter=0.3)
    col2.plotly_chart(fig)


    st.write(" ")
    st.write(" ")
    st.write("## Discussão sobre Distribuição dos Dados")
    st.divider()
    st.write("### Diretoria X Reclamações")
    st.write("Elaborando o Gráfico de Correlação entre Reclamações e Tamanho de uma Diretoria, obtivemos um Coeficiente de Correlação de Pearson próximo à 0.2, atestando uma correlação desprezível e evidenciando a necessidade de um maior cuidado a alguns setores em específico.")

    st.write(" ")
    st.write(" ")
    st.write("### Perguntas X Reclamações")
    st.write("Analisando o gráfico linear simples é possível notar 2 pontos em específico que se destacam dos outros dados. Ao elaborar o gráfico Boxplot, é possível comprovar que esses dois valores, agora classificados como outliers, estão acima de qualquer desvio esperado para eles possuírem.")
    st.write("Dessa forma, evidencia-se uma urgência na resolução desses problemas em específico ou a execução de outro Questionário para garantir a veracidade desses e de outros dados antes da tomada de qualquer medida.")
elif pages == "3-Análises Finais":
    st.write("# 3-Aplicação de Distribuições Probabilísticas")
    col1, col2 = st.columns(2)
    col1.divider()

    st.write(" ")
    st.write(" ")
    st.write("## Binomial e Poisson")
    st.divider()
    st.write("### Distribuição Binomial (Diretoria X Reclamações)")
    st.write("Considerando as 8 diretorias e as proporções de reclamação obtidas na pesquisa de Satisfação, é possível calcular uma expectativa de resultado para um próximo questionário.")
    st.write("Os gráficos a seguir permitem visualizar a probabilidade de sucesso, única e acumulada, de um determinado número de diretorias obter uma Proporção de Reclamações menor que o valor definido pelo slider abaixo:")
    n = 8
    pro = st.slider("Proporção de reclamações máxima", min_value=0.5, max_value=2.4, value=1.4, step=0.1)
    p = (st.session_state["df_diretoriasXTotal_reduzido"]['proporcao de reclamacoes totais'] < pro).sum() / 8
    st.write(f"Probabilidade de sucesso: {p}")
    x = np.arange(0, n + 1)
    y = stats.binom.pmf(x, n, p)
    df_binomial = pd.DataFrame({"Número de Sucessos": x, "Probabilidade de Ocorrência": y, "Probabilidade de Ocorrência Acumulada": np.cumsum(y)})
    col1, col2 = st.columns([7, 3])
    col1.write("Tabela de probabilidades:")
    col1.write(df_binomial)
    y_cdf = stats.binom.cdf(x, n, p)
    fig, ax = plt.subplots()
    ax.plot(x, y_cdf, marker="o", linestyle="-", color="red", label="CDF")
    ax.set_xlabel("Número de sucessos")
    ax.set_ylabel("Probabilidade Acumulada")
    ax.set_title("Distribuição Binomial Acumulada")
    ax.legend()
    col2.write(" ")
    col2.write(" ")
    col2.write(" ")
    col2.write(" ")
    col2.write(" ")
    col2.write(" ")
    col2.write(" ")
    col2.write(" ")
    col2.pyplot(fig)
    fig = plot_distribution(x, y, "Distribuição Binomial", "Número de sucessos", "Probabilidade")


    st.write(" ")
    st.write(" ")
    st.write("###  Distribuição de Poisson (Perguntas X Reclamações)")
    st.write("Através do gráfico de Poisson se torna possível evidenciar o número de reclamações geradas por um determinado número de perguntas, de forma única ou acumulada, ao considerar a média de 8.5 obtida pelo questionário de Satisfação.")
    st.write("Dessa forma é possível se programar para uma determinada quantidade de reclamações de acordo com uma quantidade de problemas(representado pela pergunta) não resolvidos dentro da empresa.")
    st.write("")
    lambda_por_pergunta = 8.5
    n_perguntas = st.slider("Quantidades de problemas(perguntas) não resolvidos:", min_value=1, max_value=21, value=10, step=1)
    lambda_total = lambda_por_pergunta * n_perguntas
    x = np.arange(0, lambda_total*1.2)
    y = stats.poisson.pmf(x, lambda_total)
    df_poisson = pd.DataFrame({
        "Número de Reclamações": x,
        "Probabilidade de Ocorrência": y,
        "Probabilidade de Ocorrência Acumulada": np.cumsum(y)
    })
    st.write("Tabela de probabilidades:")
    st.write(df_poisson)
    y_cdf = stats.poisson.cdf(x, lambda_total)
    plot_distribution(x, y_cdf, "Distribuição Acumulada de Poisson", "Número de Reclamações", "Probabilidade acumulada")
    plot_distribution(x, y, "Distribuição de Poisson", "Número de Reclamações", "Probabilidade")


    st.write(" ")
    st.write(" ")
    st.write("## Visualizações e Interpretações Finais dos resultados")
    st.divider()
    st.write("- Além de não der possível evidenciar uma correlação entre o número total de reclamações de diretoria e a proporção de suas reclamações, não existem diretorias que demonstram uma urgência(outlier) na resolução de problemas em relação a outras. Dessa forma, não é possível prever o número de reclamações de uma diretoria através de seu tamanho e cada uma deve ser estudada individualmente, dando prioridade às de maior proporção de reclamações ou impacto na empresa.")
    st.write("- A maioria dos problemas se mantém dentro do desvio padrão de reclamações, mas 2 em específico se destacam por estarem no limite superior do gráfico e outros 2 se destacam mais ainda por se evidenciarem como outliers. Dessa forma é possível atestar que existem problemas tanto de maior importância como de maior urgência dentro da realidade dos trabalhadores da empresa.")
else:
    st.write("# Rota Inválida!")
    st.write("## Algo de errado ocorreu com a página")
