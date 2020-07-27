#!/bin/bash

clear
echo "=================================="                  
echo "    MENU DE EXECUCAO E INSTALCAO	 "
echo "=================================="
select i in instalar_bibliotecas executar_analisador sair
do

	case "$i" in

		instalar_bibliotecas)
			clear
			echo "Instalando bibliotecas..."
			sudo apt install python3-pip
			# python -m ensurepip --upgrade
			pip3 install --user networkx==2.3
			pip3 install --user scikit-fuzzy
			pip3 install --user matplotlib
			pip3 install --user numpy
			sudo apt install python3-tk
			clear
			echo "Bibliotecas instaladas com sucesso, execute o código!!"
			echo "              "
			echo "=================================="                  
			echo "    MENU DE EXECUCAO E INSTALCAO	"
			echo "=================================="
			echo "1) Instalar_bibliotecas       	" 
			echo "2) Executar         		"
			echo "3) Sair                        	"

			;;

		executar_analisador)
			clear
			echo "Executando - Aguarde um momento..."
			python3 prog_ferias.py
			clear
			echo "=================================="                  
			echo "    MENU DE EXECUCAO E INSTALCAO	"
			echo "=================================="
			echo "1) Instalar_bibliotecas       	" 
			echo "2) Executar         		"
			echo "3) Sair                        	"

			;;

		sair)
			clear
			break
			;;

		*)
			echo "opcao invalida, tente de novo"
			;;
		

	esac

done

exit 0

