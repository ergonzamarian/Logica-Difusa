# Logica-Difusa
Permitir que perguntas sejam realizadas e respondidas usando inferência difusa

----------------------
DESENVOLVEDOR E VERSÃO
----------------------

Nome: Ergon Zamarian Lima

Versão do python utilizada: Python 3.6.4
 
---------------------------------
ANÁLISADOR DE FÉRIAS - EXPLICAÇÃO
---------------------------------

# Resumo

>Utiliza-se de entradas como cansaço e estresse para a geração de uma saída que contenha a quantidade de dias que deverá tirar de férias.
Apliquei na construção a maioria dos conceitos fornecidos pelo professor, mudando gráficos e alguns valores para se adequar melhor na realidade proposta.

>Foi utilizado de uma função que cria automaticamente o mapeamento entre valores nítidos e difusos através de uma função de pertinência padrão (triângulo)

>Tudo acontece em compute onde realizará o processamento das minhas regras e execução de acordo com os valores fornecidos de estresse e cansaço Computando assim o resultado.

> Foram feitas manipulações no código fornecido pelo professor afim de obter um melhor entendimento sobre o assunto tratado.

--------------------
PROPOSTA DO SOFTWARE
--------------------

-Proposta fornecida pelo Hemerson Pistori, professor da disciplina de inteligência artificial do curso de Engenharia de computação 8° semestre:  

> Utilize o scikit-fuzzy para representar algum problema de seu interesse e permitir que perguntas sejam realizadas e respondidas usando inferência difusa. Crie uma interface que permita visualizar graficamente as representações internas envolvidas no processamento. Se preferir, pode utilizar outra biblioteca ou criar sua própria.

-----------------------------
INSTALAÇÃO MANUAL BIBLIOTECAS
-----------------------------

# Caso deseje instalar todas pelo scrip (com um único clique) ou já possua essas bibliotecas instaladas, pule este tópico.

# Com o terminal aberto , insira as bibliotecas abaixo, executando uma de cada vez:

- sudo apt install python3-pip
- pip3 install --user networkx==2.3
- pip3 install --user scikit-fuzzy
- pip3 install --user matplotlib
- pip3 install --user numpy

-----------------
UTILIZAÇÃO UBUNTU
-----------------

# Habilitar permissão de execução do .sh (abra o terminal no diretório onde se encontra o Analisador.sh e execute as linhas de comandos abaixo, uma de cada vez)

chmod u+x Analisador.sh
chmod a+x Analisador.sh

# Passos

1. Inicialmente realize o download do arquivo.
2. Descompactar o arquivo baixado.
3. Com o terminal aberto e no caminho em que realizou o download do arquivo insira o comando "./Analisador.sh"
4. Será apresentado um menu com três opções, primeiramente deve-se acessar a primeira opção: "instalar_bibliotecas".
5. Após isso será apresentado uma tela na qual constará todos os arquivos que estão sendo instalados.
6. Ao final da instalação será apresentado uma pequena tela, clique em "quit". (Caso apresente)
7. Voltará automaticamente ao MENU, escolha a segunda opção: "Executar"
8. Aguarde um momento enquanto a aplicação inicia.
9. Insira um nota de 0 a 10 para estresse e cansaço.
10. Clique em "ANALISAR".
11. Caso queira plotar os gráficos do Resultado ou da função escolha um dos botões abaixo de Gráficos.
11. O Resultado será exibido na parte inferior da tela.

-----------------------------
SISTEMA OPERACIONAL SUPORTADO
-----------------------------

- Ubuntu 16.04 LTS ou superior

-------------------------------------------------------
REFERÊNCIA PARA CRIAÇÃO DO README E DEPURAÇÃO DO CÓDIGO
-------------------------------------------------------

* https://github.com/thszk/knowledgebase/ 

- Autor: Thiago Suzuque Lodi
- Contribuição: Auxilio na elaboração do README atarvés da disponibilização do modelo presente no link acima, fornecimento de scripts auxiliares para a elaboração da documentação e construção parcial do código.

----------------------------------------------------------
REFERÊNCIA PARA CRIAÇÃO DO CÓDIGO COM SUAS FUNCIONALIDADES
----------------------------------------------------------


* https://www.youtube.com/watch?v=ZLLbZLcCTcI&feature=youtu.be

- Autor: Hemerson Pistori
- Contribuição: Auxilio no entendimento sobre os fragmentos dos códigos utilizados, idéias aplicadas, esclarecimento sobre funções de pertinência e bibliotecas tais como: scikit-fuzzy, matplotlib, numpy.

* https://docs.python.org/3/library/tkinter.html

- Contribuição: Auxilio na elaboração da interface gráfica, como funções e importações necessárias.


