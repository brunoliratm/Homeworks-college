Algoritmo "menordetres"

//Bruno Magno De Lira Gomes
//Sistemas de Informação 1 periodo

Var
       primeiro, segundo, terceiro : inteiro

Inicio

//inicio do programa
      escreval("Programa para saber o menor de 3 números inteiros")
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
      
//condicional de comparação entre valores
      se  (primeiro < segundo) e (primeiro < terceiro) entao
      escreval("o numero ",primeiro," é o menor número dentre os três")
      fimse
      
      se  (segundo < primeiro) e (segundo < terceiro) entao
      escreval("o numero ",segundo," é o menor número dentre os três")
      fimse
      
      se  (terceiro < segundo) e (terceiro < primeiro) entao
      escreval("o numero ",terceiro," é o menor número dentre os três")
      senao
        se (primeiro = segundo) e (primeiro <= terceiro) entao
        escreval("o numero ",primeiro," é o menor dentre os três")
        senao
          se (primeiro = terceiro) e (primeiro <= segundo) entao
          escreval("o numero ",primeiro," é o menor dentre os três")
          senao
            se (terceiro = segundo) e (terceiro <= primeiro) entao
            escreval("o numero ",segundo," é o menor dentre os três")
            fimse
          fimse
        fimse
      fimse
      
//fim
escreval("")
escreval(" obrigado por usar meu programa!!")
Fimalgoritmo