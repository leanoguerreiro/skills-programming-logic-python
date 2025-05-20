
# Lista de Exercícios de Python

### Operações aritméticas, lógicas e relacionais

1. Crie um programa em Python que solicite do usuário sua data de nascimento (dia, mês e ano) e calcule quantos anos, meses, dias, minutos e segundos de vida tem o usuário. Imprima na tela todas as informações calculadas.  
   **Obs.:** Considere que um ano tem 365 dias.
[resposta](aritmeticas_logicas_e_condicionais/q1.py)

2. Calcular a quantidade de dinheiro gasta por um alcoólatra. Dados: o número de anos que ele bebeu, a quantidade de latinhas bebidas por dia e o preço de uma latinha.  
   **Obs.:** Considere que um ano tem 365 dias. O usuário deve fornecer os dados necessários. Imprima os valores resultantes na tela.
[resposta](aritmeticas_logicas_e_condicionais/q2.py)

3. Faça um programa em Python que solicite do usuário 2 números inteiros e um número real. Calcule e mostre:  
   a. Produto do dobro do primeiro com metade do segundo;  
   b. A soma do triplo do primeiro com o terceiro;  
   c. O terceiro elevado ao cubo;  
   d. O valor absoluto da subtração entre o primeiro e o segundo (use abs());  
   e. O quadrado do segundo somado com o logaritmo natural do terceiro multiplicado pelo primeiro.  
   **Obs.:** Use o pacote math. Imprima os valores resultantes na tela.
[resposta](aritmeticas_logicas_e_condicionais/q3.py)

4. Faça um programa em Python, que solicite duas datas do usuário. Cada data deverá ser formada por dia, mês e ano. O programa deve imprimir a diferença em dias entre as datas.  
   **Obs.:** Considere que um ano tem 365 dias. Imprima os valores resultantes na tela.
[resposta](aritmeticas_logicas_e_condicionais/q4.py)

5. Crie um programa em Python que converta um valor em reais para dólar, euro e iene, considerando taxas de conversão fixas e a cobrança do imposto IOF (6,38%), sobre o valor. Solicite o valor em reais do usuário e as taxas de conversão das moedas constantes.  
   **Obs.:** Imprima os valores resultantes na tela.
[resposta](aritmeticas_logicas_e_condicionais/q5.py)
---

### Estruturas condicionais

6. A prefeitura de Manaus abriu uma linha de crédito para funcionários estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário bruto. Faça um algoritmo em Python que receba o valor do salário bruto do funcionário e o valor da prestação e informe se o empréstimo pode ser concedido.
[resposta](estruturas_condicionais/q6.py)

7. Crie um programa em Python para calcular o imposto de renda por faixas. Com base no salário anual informado pelo usuário, aplique as alíquotas por faixa:  
   - Até R$28.200 – isento  
   - Até R$40.000 – 15%  
   - Acima disso – 27.5%  
   Imprima os valores referentes ao imposto a ser pago.
[resposta](estruturas_condicionais/q7.py)

8. Crie um programa em Python que solicite do usuário o tempo de ligação (em minutos) e o tipo de ligação:  
   - Local: até 3 min custam R$0,50 + R$0,10/min adicional  
   - Nacional: até 3 min custam R$1,00 + R$0,25/min adicional  
   - Internacional: até 3 min custam R$2,00 + R$0,60/min adicional  
   Calcule e imprima na tela o valor da ligação.
[resposta](estruturas_condicionais/q8.py)

9. Crie um programa em Python que leia os lados de um triângulo. Verifique se formam um triângulo e classifique quanto aos lados (equilátero, isósceles ou escaleno) e aos ânglos (retângulo, obtusângulo ou acutângulo), utilizando o Teorema de Pitágoras.  
   **Obs.:** Pesquise sobre o problema.
[resposta](estruturas_condicionais/q9.py)

10. Faça um algoritmo em Python que solicite do usuário o tamanho do arquivo (em MB) e a velocidade da conexão. Verifique o plano:  
    - Plano básico (1MBps)  
    - Intermediário (5MBps)  
    - Avançado (10MBps)  
    Calcule e exiba o tempo de download, incluindo mensagens sobre lentidão ou velocidade excelente.
[resposta](estruturas_condicionais/q10.py)
    
11. Faça um programa em Python que leia um número inteiro e classifique o número nas faixas com múltiplos critérios abaixo:  
    - Faixa 1: Múltiplos de 3 e 5  
    - Faixa 2: Pares e múltiplos de 10  
    - Faixa 3: Números entre 100 e 1000  
    Exiba as classificações aplicáveis.
[resposta](estruturas_condicionais/q11.py)

12. Crie um programa em Python que leia a idade e mostre na tela o plano disponível:  
    - Até 18 anos: Plano Júnior  
    - 19 a 40 anos: Plano Adulto  
    - 41 a 60 anos: Plano Senior  
    - Acima de 60: Plano Master com Coparticipação
[resposta](estruturas_condicionais/q12.py)
---

### Estruturas de repetição

13. Desenvolva um algoritmo em Python que solicite um número N do usuário e gere todos os números primos até ele. Imprima os números primos na tela.  
    **Obs.:** Utilize a estrutura de repetição for.
[resposta](estruturas_de_repeticao/q13.py)

14. Faça um programa em Python que defina dois números inteiros: **inicio** e **fim** e imprima na tela todos os números múltiplos de 3 e múltiplos de 5 entre **inicio** e **fim** (incluindo os limites se forem múltiplos).  
    **Obs.:** Utilize a estrutura de repetição for.
[resposta](estruturas_de_repeticao/q14.py)
15. Implemente um algoritmo em Python que calcule o valor de H, sendo que ele é determinado pela série:  
    \[
    H = 1/1 + 3/2 + 5/3 + 7/4 + \ldots + 99/50
    \]
[resposta](estruturas_de_repeticao/q15.py)
16. Faça um programa em Python que imprima os 15 primeiros termos da série de Fibonacci. Os termos são: 1 1 2 3 5 8 13 ...
[resposta](estruturas_de_repeticao/q16.py)
17. Faça um programa em Python que imprima um losango simétrico para um valor ímpar **n** (altura total):

    ```
       *
      ***
     *****
    *******
     *****
      ***
       *
    ```
    **Obs.:** Solicite do usuário o valor **n**.
[resposta](estruturas_de_repeticao/q17.py)
18. Crie um algoritmo em Python que calcule o Mínimo Múltiplo Comum (MMC) entre dois números inteiros usando repetição. Solicite os dois números inteiros do usuário.
[resposta](estruturas_de_repeticao/q18.py)
19. Faça um algoritmo em Python que imprima todos os números de 3 dígitos que satisfazem a propriedade de Armstrong:  
    **Ex:** 153 → 1³ + 5³ + 3³ = 153
[resposta](estruturas_de_repeticao/q19.py)
20. Desenvolva um programa em Python para calcular a aproximação de **π** pela Série de Leibniz. Para isso, calcule os 20 primeiros termos da aproximação de π, conforme abaixo:  
     n ≅ 4 x (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)

    **Obs.:** Mostre na tela o valor final.
[resposta](estruturas_de_repeticao/q20.py)