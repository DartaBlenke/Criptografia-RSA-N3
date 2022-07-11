# Criptografia-RSA-N3

<h3>Alunos: D'Artagnan Blenke e Eduardo Effting</h3>
<h3>Professor: Rodrigo Mello Mattos Habib</h3>

<h2 align="center">Planejamento e Operação</h2>
Utilizamos da linguagem Phyton, por ser uma linguágem de mais fácil entendimento, e por termos uma breve experiência de utilização,
como trabalhamos com Front-end, não costumamos utilizar linguágens de Back-end, encontramos diversos problemas para a criação do código,
por não dominarmos a tecnologia, não conseguimos fazer a leitura de outro arquivo, para que o mesmo fosse criptografado e depois descriptografado,
e também para a utilização do módulo junto das chaves.

Para utilização da chave utilizamos de uma função que pega numeros aleatórios para serem utilizados nos cálculos. E então temos a função que encripta a
mensagem, pegando a mensagem e de letra em letra fazneod a ordenação e multiplicando pelos valores de e(chave pública),e dividindo pelo valor de n, 
então trazendo a mensagem. Para decriptar, temos a função que recebe a mensagem cirpografada e de letra em letra faz a multiplicação por d(chave privada) 
e dividida pelo valor de n, então retorna a mensagem descriptografada. Então temos a função onde passamos os valores de cada uma das nossas variáveis 
para serem usadas no código, e os prints das chaves e mensagens.

Testamos o códiugo passando diversos tipos de mensagens e alterando os valores das chaves para conferir se efetivamente estavam calculando
independente do valor utilizado e da mensagem apresentada, no início encontramos erros no nossos cálculos e por isso não conseguíamos trazer a mensagem
cirptografada de forma correta, por falta de tempo e conhecimento não conseguimos nos aprofundar como gostaríamos para que o código ficasse no seu 100%,
o único problema mesmo foi por não conseguirmos efetivamente criar 100% da aplicação como solicitado.

Aprendemos diversas coisas sobre a utililzação da criptografia RSA, e como ela é utilizada em diversas aplicações, também tivemos a oportunidade de parar 
para estudar Phyton o que era uma vontade da dupla, mas por toda a correria acabamos deixando de lado, aprendemos muito sobre outros tipos de criptografia
durante nossos estudos sobre e pesquisas, encontramos diversas ferramentas disponíveis no Phyton para a realização dessa atividade, pretendemos estender
nossos estudos tando em criptografia como em phyton.

<h2 align="center">Comandos</h2>


Para clonar o repositório
```sh
git clone https://github.com/DartaBlenke/Criptografia-RSA-N3.git
```

Para rodar o script
```sh
py app.py
```
