#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1: Importar base de dados
import pandas as pd

tabela_clientes = pd.read_csv("telecom_users.csv")

#2: Visualizar a base de dados
tabela_clientes = tabela_clientes.drop("Unnamed: 0", axis =1) #exclui coluna Unnamed: 0
tabela_clientes = tabela_clientes.drop("IDCliente", axis =1) #exclui coluna IDCliente
display(tabela_clientes) #exibe a tabela formatada
display(tabela_clientes.columns) #mostra o nome de todas as colunas



# In[7]:


#3: Tratar dados
#retirar valores vazios
tabela_clientes["TotalGasto"] = pd.to_numeric(tabela_clientes["TotalGasto"], errors="coerce")#transforma texto para numeros, erros transforma para campos vazios
print(tabela_clientes.info())#exibe informacoes da tabela, exibe quantidade de campos vazios

#problema de valores vazios
tabela_clientes = tabela_clientes.dropna(how="all", axis =1) #excluiu todas as colunas com valores vazios
tabela_clientes = tabela_clientes.dropna(how="any", axis =0)#excluiu linhas com pelomenos um valor vazio


# In[ ]:





# In[8]:


#4: Olhar a distribuicaso de "Churns"(cancelamentos)
display(tabela_clientes["Churn"].value_counts()) #exibe a quantidade de cancelamentos
display(tabela_clientes["Churn"].value_counts(normalize=True).map('{:.1%}'.format))#exibe a porcentagem de cancelamentos,com 1 casa decimal
#5: Analizar os possiveis motivos para os cancelamentos
#instalar plotly comando no anaconta pip install plotly
import plotly.express as px
#cria todos os graficos da tavela
for coluna in tabela_clientes:
    grafico = px.histogram(tabela_clientes,x=coluna, color="Churn" )
    grafico.show()




# In[ ]:





# In[ ]:




