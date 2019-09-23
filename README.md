# OrthoDEGFinder
Find correspondent genes between species based on DEG data, functional annotation and orthology

OrthoDEGFinder é uma aplicação Web desenvolvida em Python/Django, na qual são correlacionadas informações de genes em diferentes espécies com base em dados de expressão diferencial, anotação funcional e ortologia.

Abaixo, estão todas as informações necessárias para instalação local e inserção dos dados.

## Manual

1. Instalação
2. Inserção dos dados

------------------------

### 1. Instalação

1. Instalar Python3 e pip:

```
$ sudo apt-get install python3
$ sudo apt-get install python3-pip
```

2. Criar uma pasta e colocar o código-fonte da aplicação, que está hospedado no GitHub, dentro dela:

```
$ mkdir <nome_pasta> 
$ cd <nome_pasta>
$ git clone https://github.com/vinibfranc/OrthoDEGFinder
```

3. Com o código-fonte, podemos navegar para a pasta que o contém:

```
$ cd OrthoDEGFinder/
```

4. Agora, iremos instalar e configurar uma virtual environment (virtualenv) para a aplicação:

```
$ pip3 install virtualenv
```

Com isso, podemos verificar onde a virtualenv e o Python foram instalados:

```
$ which virtualenv
/usr/bin/virtualenv
$ which python3
/usr/bin/python3
```

Então podemos criar o diretório da virtualenv dentro do nosso projeto:

```
$ mkdir venv/
$ cd venv
```

Finalmente, podemos criar a nossa virtualenv para o projeto:

```
virtualenv . -p /usr/bin/python3
```

O último passo agora, e sempre que formos trabalhar no projeto, é voltar para a pasta ```OrthoDEGFinder/``` e ativar a virtualenv:
```
$ cd ..
$ source venv/bin/activate
```

5. Instalando as dependências:

```
(venv) $ pip3 install -r requirements.txt
```

6. Instalar da biblioteca MySQL que conecta com a API de banco de dados do Django (mysqlclient):

```
(venv) $ sudo apt-get install python3-dev
(venv) $ sudo apt-get install python3-dev libmysqlclient-dev
(venv) $ pip3 install mysqlclient
```

7. Instalar o MySQL server:

```
(venv) $ sudo apt-get install mysql-server
```

8. Criar o usuário administrador dentro do MySQL:

```
(venv) $ sudo mysql
mysql> GRANT ALL PRIVILEGES ON *.* TO 'usuario'@'localhost' IDENTIFIED BY 'senha';
mysql> quit
```

9. Acesse o usuário e crie o banco de dados:

```
(venv) $ mysql -u usuario -p
mysql> CREATE DATABASE ortho_deg_finder;
```

10. Abrir o arquivo gerenciador do banco de dados:

```
(venv) $ sudo nano /etc/mysql/my.cnf
```

11. Adicionar as seguintes linhas ao arquivo ```my.cnf```:

```
[client]
database = ortho_deg_finder
user = usuario
password = senha
default-character-set = utf8
```

12. Aplicar as migrações do banco de dados:

```
(venv) $ cd project
(venv) $ python3 manage.py makemigrations
(venv) $ python3 manage.py migrate
```

13. Coletar arquivos estáticos:

```
(venv) $ python3 manage.py collectstatic
```

14. Testar a aplicação:

```
(venv) $ python3 manage.py runserver
```

Pronto! Todas as configurações foram feitas e o sistema já pode ser acessado.

13. Caso queira acessar a página admin basta criar um usuário:

```
(venv) $ python3 manage.py createsuperuser
```

Após, basta logar com as credenciais na página ```http://127.0.0.1:8000/admin``.

-------------------------------

### 2. Inserção dos dados

Como estamos em ambiente de desenvolvimento, possivelmente o sistema ainda não terá dados populados, ou precisará de atualização. Desse modo, é importante prestar atenção em como fazer esse processo para que tenhamos o resultado desejado.

#### Como inserir as informações?

Algumas informações são inseridas manualmente na página admin (necessário ter superusuário criado), outras por planilhas e outras por scripts. O fluxo de inserção deve seguir a seguinte ordem:

1. **Inserção de Organisms**: Acessar a página ```http://127.0.0.1:8000/admin/app/organism/``` e ir em ```Add organism```. Abaixo um exemplo da adição do fungo Metarhizium anisopliae E6. É muito importante que seja adicionado o ID taxonômico do organismo, que pode ser encontrado no [NCBI Taxonomy Browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi). Também deverá ser inserido o organismo ao qual a expressão diferencial será inferida com base na ortologia, podendo deixar o ExperimentalDesign em branco.

![Adição de organismos](https://drive.google.com/drive/folders/1ZVSSfrqcUwhJDmH-iuhKdyW5WvCdIi0y)


2. **Carregamento de planilhas**: A organização das informações de expressão diferencial e anotação funcional é feita através de planilhas geradas pelos programas utilizados em: [https://github.com/vinibfranc/InternshipDEAnalysis](https://github.com/vinibfranc/InternshipDEAnalysis), algumas delas modificadas para atenderem às nossas necessidades. Os arquivos exemplo também se encontram em ```OrthoDEGFinder/project/app/files_to_upload```.

    2.1. **Analysis Annotated Genes**: Arquivo CSV com genes diferencialmente expressos gerados pelo [edgeR](https://bioconductor.org/packages/release/bioc/html/edgeR.html). Esse arquivo pode ser gerado pelo [pipeline](https://github.com/vinibfranc/InternshipDEAnalysis) e deve ser modificado para ficar igual ao [exemplo](https://docs.google.com/spreadsheets/d/1becN_2aQjFlYFa4kuTLfdw8WsuufuTCpGdZtX7jREFE/edit#gid=1182937593), com o ID taxonômico do organismo e com a descrição do design experimental adicionados anteriormente, e com a mudança na penúltima e última colunas. Para adicionar esses dados basta entrar em ```http://127.0.0.1:8000/admin/app/analysisannotatedgene/``` -> ```Import``` -> Selecione o arquivo -> Selecione o formato CSV -> Submit -> Confirm import. O processo de importação deve levar alguns minutos.

    2.2. **Pannzer2 Functional annotations**: Arquivo TSV com anotações funcionais geradas pelo [Pannzer 2](http://ekhidna2.biocenter.helsinki.fi/sanspanz/). Esse arquivo corresponde ao arquivo ```GO.out``` gerado no web server do Pannzer2 após a submissão da sequência de proteínas e o recebimento dos resultados por e-mail. Ele deve ser modificado para ficar igual ao [exemplo1](https://docs.google.com/spreadsheets/d/1QphqjliTIOuA4vpy0m5HeVjyzGrKk4K3N1Edkfo1ztY/edit#gid=1479770010) e [exemplo2](https://docs.google.com/spreadsheets/d/1-_AtCoVQVnaIz9T-OhG9WK1RSVg6nZc9_g1NqgM4SqM/edit#gid=1080685024), com o ID taxonômico do organismo, a coluna de id em branco e alterando a ordem dos campos go_id e ontology. Para adicionar o ```GO:``` basta rodar o seguinte comando e remover ```GO:``` da primeira linha da coluna go_id (Os arquivos da pasta files_to_upload já foram convertidos e estão prontos para serem inseridos):

    ```
    $ awk -F'\t' -vOFS='\t' '{ $4 = "GO:" $4 }1' anotacao_anisopliae_arsef_549.tsv > anotacao_anisopliae_arsef_549_formatted.tsv
    $ awk -F'\t' -vOFS='\t' '{ $4 = "GO:" $4 }1' anotacao_robertsii_arsef_23.tsv > anotacao_robertsii_arsef_23_formatted.tsv
    ```
    
    Agora, adicionamos esses dados, um para cada organismo, entrando em ```http://127.0.0.1:8000/admin/app/pannzer2annotation/``` -> ```Import``` -> Selecione o arquivo -> Selecione o formato TSV -> Submit -> Confirm import. O processo de importação deve levar alguns minutos pois são muitas linhas de dados.

3. **Execução de scripts**: Os dados de ortologia e correspondência de genes e proteínas entre as espécies são inseridos via script. Os arquivos exemplo também se encontram em ```OrthoDEGFinder/project/app/orthologs```.

    3.1. **Orthologs**: Arquivo TSV com dados de ortologia gerados pelo [OrthoFinder](https://github.com/davidemms/OrthoFinder). Esse arquivo pode ser gerado pelo [pipeline](https://github.com/vinibfranc/InternshipDEAnalysis) e corresponde ao arquivo ```proteins/OrthoFinder/Results/Orthogroups/Orthogroups_SingleCopyOrthologues.txt``` gerado no OrthoFinder. Após, podem ser rodados os seguintes comandos para extrair os ortólogos Single_copy: 
    
    ```
    $ cd proteins/OrthoFinder/Results/Orthogroups
    $ grep -Fwf Orthogroups_SingleCopyOrthologues.txt Orthogroups.txt > OrthologsIDS.txt
    $ sed 's/://' OrthologsIDS.txt > OrthologsIDS_2.txt
    $ awk -v OFS="\t" '$1=$1' OrthologsIDS_2.txt > OrthologsIDS_done.txt
    ```

    Com isso, devem ser adicionados os IDs taxonômicos dos dois organismos na primeira e segunda linha, sendo que o organismo da coluna 1 corresponde à proteína da coluna 4 e o organismo da coluna 2 corresponde ao organismo da coluna 5. O arquivo resultante deverá possuir a seguinte estrutura: [arquivo](https://docs.google.com/spreadsheets/d/1s52zQ-uXLLxDFo3SsByvX4Tam6goyZCpPQ1nZb28ubY/edit#gid=1745020920).

    Caso queira mudar o arquivo a ser lido pelo programa basta alterar a linha 14 do script ```map_orthologs.py``` contido na pasta ```OrthoDEGFinder/project/app/management/commands```.
    
    Com o arquivo configurado, podemos rodar o script (dentro de ```OrthoDEGFinder/project```) que popula os ortólogos:

    ```
    (venv) $ python3 manage.py map_orthologs
    ```

    3.2. **Gene Correspondences**: Essa tabela irá conter todas as informações relacionadas, utilizando o [Biopython](https://biopython.org/) para extrair os genes que codificam as proteínas ortólogas, mapear as anotações funcionais e as expressões diferenciais.

    Esse script não lê nenhum arquivo, mas sim compara os registros no banco de dados para encontrar as correspondências, de modo que é muito importante que todos os demais passos tenham sido feitos antes deste. Podemos rodar o script (dentro de ```OrthoDEGFinder/project```), que está contido em ```OrthoDEGFinder/project/app/management/commands```, assim:

    ```
    (venv) $ python3 manage.py map_genes_to_annotation
    ```

    Esse script também irá demorar, pois o NCBI limita a quantidade de requisições por segundo pelo mesmo IP.

#### Como consultar as informações?

Existem 5 tipos de filtragens (com várias opções de campos de filtragem), sendo 4 delas sem as informações correlacionadas e uma delas com as correlações:

* Por [organismos](http://127.0.0.1:8000/search_organism/);
* Por [genes](http://127.0.0.1:8000/search_gene/);
* Por [anotação funcional](http://127.0.0.1:8000/search_annotation/);
* Por [ortólogos](http://127.0.0.1:8000/search_orthologs/);
* [Busca unificada](http://127.0.0.1:8000/search_unified/): mostra todas as informações de organismo, design experimental, genes e anotações funcionais para uma mesma entrada em ```GeneCorrespondences```.

---------------------

Desenvolvido por Vinícius Franceschi em [UBTEC](https://www.facebook.com/ubtec.ufrgs/) - [CBiot](http://www.cbiot.ufrgs.br/) - UFRGS.

Dúvidas, problemas ou sugestões de melhorias podem ser enviadas para: vinibfranc@gmail.com