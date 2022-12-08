-- criando o banco de dados
create database combustivel;

-- selecionando o banco de dados, para futuras interações
use combustivel;

-- criando as duas tabelas desnormalizadas do projeto
create table combustivel_automotivo_2020 (
    regiao_sigla char(2),
    uf char(2),
    municipio varchar(40),
    nome_posto varchar(150),
    cnpj_posto char(14),
    bairro varchar(100),
    produto varchar(40),
    data_coleta date,
    valor_venda float(10, 2),
    unidade_medida varchar(40),
    bandeira varchar(100)
);

create table combustivel_automotivo_2021 (
    regiao_sigla char(2),
    uf char(2),
    municipio varchar(40),
    nome_posto varchar(150),
    cnpj_posto char(14),
    bairro varchar(100),
    produto varchar(40),
    data_coleta date,
    valor_venda float(10, 2),
    unidade_medida varchar(40),
    bandeira varchar(100)
);

-- obtendo o path onde iremos colocar nossos arquivos csv's
show variables like 'secure_file_priv';

-- populando as duas tabelas criadas, com os dados dos arquivos csv's
load data infile '/var/lib/mysql-files/combustivel_automotivo_2020.csv'
into table combustivel_automotivo_2020
fields terminated by ','
lines terminated by '\n'
ignore 1 rows;

load data infile '/var/lib/mysql-files/combustivel_automotivo_2021.csv'
into table combustivel_automotivo_2021
fields terminated by ','
lines terminated by '\n'
ignore 1 rows;

-- certificando-se de que os dados foram populados nas tabelas
select * from combustivel_automotivo_2020 limit 10;

select * from combustivel_automotivo_2021 limit 10;