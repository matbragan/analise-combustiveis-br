import pandas as pd

# leitura dos arquivos csv's
 
files_path = '/home/matbragan/Documents'

df1 = pd.read_csv('files_path/combustivel_automotivo_2020_01.csv', on_bad_lines='skip', sep=';', encoding='utf-8')
df2 = pd.read_csv('files_path/combustivel_automotivo_2020_02.csv', on_bad_lines='skip', sep=';', encoding='utf-8')
df3 = pd.read_csv('files_path/combustivel_automotivo_2021_01.csv', on_bad_lines='skip', sep=';', encoding='utf-8')
df4 = pd.read_csv('files_path/combustivel_automotivo_2021_02.csv', on_bad_lines='skip', sep=';', encoding='iso8859-1')

# criação dos dataframes

frames_2020 = [df1, df2]
frames_2021 = [df3, df4]

df_2020 = pd.concat(frames_2020)
df_2021 = pd.concat(frames_2021)

# renomeação das colunas

df_2020_treatment = df_2020.rename(
    columns=
    {'Regiao - Sigla': 'regiao_sigla'
    , 'Estado - Sigla': 'uf'
    , 'Municipio': 'municipio'
    , 'Revenda': 'nome_posto'
    , 'CNPJ da Revenda': 'cnpj_posto'
    , 'Bairro': 'bairro'
    , 'Produto': 'produto'
    , 'Data da Coleta': 'data_coleta'
    , 'Valor de Venda': 'valor_venda'
    , 'Unidade de Medida': 'unidade_medida'
    , 'Bandeira': 'bandeira'
    })

df_2021_treatment = df_2021.rename(
    columns=
    {'Regiao - Sigla': 'regiao_sigla'
    , 'Estado - Sigla': 'uf'
    , 'Municipio': 'municipio'
    , 'Revenda': 'nome_posto'
    , 'CNPJ da Revenda': 'cnpj_posto'
    , 'Bairro': 'bairro'
    , 'Produto': 'produto'
    , 'Data da Coleta': 'data_coleta'
    , 'Valor de Venda': 'valor_venda'
    , 'Unidade de Medida': 'unidade_medida'
    , 'Bandeira': 'bandeira'
    })

# filtro das colunas à serem usadas

columns_list = ['regiao_sigla', 'uf', 'municipio', 'nome_posto', 'cnpj_posto', 'bairro', 'produto', 'data_coleta', 'valor_venda', 'unidade_medida', 'bandeira']

df_2020_treatment = df_2020_treatment[columns_list]
df_2021_treatment = df_2021_treatment[columns_list]

# tratamento da coluna cnpj_posto

df_2020_treatment['cnpj_posto'] = df_2020_treatment['cnpj_posto'].str.replace('.', '')
df_2020_treatment['cnpj_posto'] = df_2020_treatment['cnpj_posto'].str.replace('/', '')
df_2020_treatment['cnpj_posto'] = df_2020_treatment['cnpj_posto'].str.replace('-', '')
df_2020_treatment['cnpj_posto'] = df_2020_treatment['cnpj_posto'].str.replace('^\s+', '')

df_2021_treatment['cnpj_posto'] = df_2021_treatment['cnpj_posto'].str.replace('.', '')
df_2021_treatment['cnpj_posto'] = df_2021_treatment['cnpj_posto'].str.replace('/', '')
df_2021_treatment['cnpj_posto'] = df_2021_treatment['cnpj_posto'].str.replace('-', '')
df_2021_treatment['cnpj_posto'] = df_2021_treatment['cnpj_posto'].str.replace('^\s+', '')

# tratamento da coluna data_coleta

df_2020_treatment['data_coleta'] = pd.to_datetime(df_2020_treatment['data_coleta'])

df_2021_treatment['data_coleta'] = pd.to_datetime(df_2021_treatment['data_coleta'])

# tratamento da coluna valor_venda

df_2020_treatment['valor_venda'] = df_2020_treatment['valor_venda'].str.replace(',', '.')
df_2020_treatment['valor_venda'] = df_2020_treatment['valor_venda'].astype(float)

df_2021_treatment['valor_venda'] = df_2021_treatment['valor_venda'].str.replace(',', '.')
df_2021_treatment['valor_venda'] = df_2021_treatment['valor_venda'].astype(float)

# tratamento das colunas com ,

df_2020_treatment['nome_posto'] = df_2020_treatment['nome_posto'].str.replace(',', '')
df_2020_treatment['municipio'] = df_2020_treatment['municipio'].str.replace(',', '')
df_2020_treatment['bairro'] = df_2020_treatment['bairro'].str.replace(',', '')

df_2021_treatment['nome_posto'] = df_2021_treatment['nome_posto'].str.replace(',', '')
df_2021_treatment['municipio'] = df_2021_treatment['municipio'].str.replace(',', '')
df_2021_treatment['bairro'] = df_2021_treatment['bairro'].str.replace(',', '')

# escrita dos arquivos csv's

df_2020_treatment.to_csv(path_or_buf='files_path/combustivel_automotivo_2020.csv', sep=',', index=False)
df_2021_treatment.to_csv(path_or_buf='files_path/combustivel_automotivo_2021.csv', sep=',', index=False)