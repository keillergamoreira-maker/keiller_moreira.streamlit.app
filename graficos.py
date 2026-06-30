#---Importar as bibliotecas
import seaborn as sns
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.figure_factory as ff


class Graficos:
    """Classe responsável por criar os gráficos (estaticos e interativos)"""
    def __init__(self,df, coluna, email):
        """Função resposável por inicializar a clase."""
        self.df = df
        self.coluna = coluna
        self.email = email
    def histograma_estatico(self):
        """Função responsável por criar o histpgrama."""
        #---Criar o histograma

        fig, ax = plt.subplots()
        sns.histplot(
            data=self.df,
            x=self.coluna,
            ax=ax,
            edgecolor='white',
            linewidth=1.5
        )

        for container in ax.containers:
            ax.bar_label(container, fmt='%.0f', padding=3)

        #---Título do grafico e dos eixos
        ax.set_title(f'Histograma: {self.coluna}')
        ax.set_ylabel('Quantidade')

        fig.tight_layout()

        if self.email:
            return fig
        else:
            #---Mostrar o grafico
            st.pyplot(fig, width='stretch')



    def pizza_estatico(self):
        """Função responsável por criar o gráfico de pizza"""
        #---Saber a quantidade de cada item na tabela
        quantidade = self.df[self.coluna].value_counts()

        #---Criar o gráfico de pizza
        fig, ax = plt.subplots()
        ax.pie(
            x=quantidade,
            labels=quantidade.index,
            autopct='%1.1f%%'
        )

        #---Título do gráfico
        ax.set_title(f'Pizza: {self.coluna}')

        fig.tight_layout()

        if self.email:
            return fig
        else:
            st.pyplot(fig, width=1000)

    def histograma_interativo(self):
        """Função responsável por criar o histograma interativo """
        #---Criar o histograma
        grafico = px.histogram(
            data_frame=self.df,
            x=self.coluna,
            title=f'Histograma: {self.coluna}',
            nbins=20

        )

        grafico.update_layout(bargap=0.1)

        #---Mostrar o gráfico
        st.plotly_chart(grafico)



    def pizza_interativo(self):
        """Função responsável por criar o grafico de pizza interativo"""
        #---Criar o grafico de pizza
        grafico = px.pie(
            data_frame=self.df,
            names=self.coluna,
            title=f'Gráfico de pizza: {self.coluna}'
        )

        st.plotly_chart(grafico)