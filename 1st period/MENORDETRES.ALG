Algoritmo "menordetres"

//Bruno Magno De Lira Gomes
//Sistemas de Informa��o 1 periodo

Var
       primeiro, segundo, terceiro : inteiro

Inicio

//inicio do programa
      escreval("Programa para saber o menor de 3 n�meros inteiros")
      escreval("By Bruno Magno")
      escreval("")

//inserir valores
      escreval("Digite o Primeiro Valor")
      leia(primeiro)
      escreval("Digite o Segundo Valor")
      leia(segundo)
      escreval("Digite o Terceiro Valor")
      leia(terceiro)

      escreval("")
      
//condicional de compara��o entre valores
      se  (primeiro < segundo) e (primeiro < terceiro) entao
      escreval("o numero ",primeiro," � o menor n�mero dentre os tr�s")
      fimse
      
      se  (segundo < primeiro) e (segundo < terceiro) entao
      escreval("o numero ",segundo," � o menor n�mero dentre os tr�s")
      fimse
      
      se  (terceiro < segundo) e (terceiro < primeiro) entao
      escreval("o numero ",terceiro," � o menor n�mero dentre os tr�s")
      senao
        se (primeiro = segundo) e (primeiro <= terceiro) entao
        escreval("o numero ",primeiro," � o menor dentre os tr�s")
        senao
          se (primeiro = terceiro) e (primeiro <= segundo) entao
          escreval("o numero ",primeiro," � o menor dentre os tr�s")
          senao
            se (terceiro = segundo) e (terceiro <= primeiro) entao
            escreval("o numero ",segundo," � o menor dentre os tr�s")
            fimse
          fimse
        fimse
      fimse
      
//fim
escreval("")
escreval(" obrigado por usar meu programa!!")
Fimalgoritmo