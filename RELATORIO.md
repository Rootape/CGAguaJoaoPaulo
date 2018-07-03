										Relatorio CG Agua João Paulo.

Este projeto tinha como objetivo simular a propagação de uma onda em um espelho d'água quando uma gota cai no mesmo.

Primeiramente fui buscar uma maneira de representar a ação da água de maneira matemática. Encontrei um site que demonstrava que era possível representar 
a água utilizando-se de vários pontos e atribuindo um círculo a cada um deles. Dessa forma, para um ponto X, sua coordenada seria dada como:

										X = ( X + cos(ang), sin(ang), Z )

Para deixar o codigo mais limpo, criei duas funções chamadas "handlerX" para cuidar dos valores de X, e "handlerY" para os valores de Y.

Com essas funções criadas, prossegui para a parte da movimentação propriamente dita.

Criei uma Lista onde inseria outras listas com valores de "-m" até "m" e um valor "0" na forma:
										[ posição, angulo ]
e uma variavel chamada crista, que me indica quantos pontos devem ter da parte inferior da onda até sua crista.

Criei então uma função chama "waterHit" que gerencia o evento da gota caindo na água. Essa função pegava o centro da lista, e ia espalhando para os 
dois lados mudando os valores dos ángulos. Imaginando que quando uma gota cai, ela gere uma depressão e um levante, o ángulo do centro deve ser o 
mais baixo (270), e entre 270 - 360 devem haver "crista" pontos, entre 360 e 90 outros "crista" pontos e entre 90 e 180 idem. Com isso temos 3 * crista
pontos que serão alterados de 270 até 180, logo a diferença entre essas alterações deve ser (270 / crista * 3).

Depois que o estado inicial foi colocado, é necessário um Handler para manter a onda se mexendo. Essa é a função do "wavHandler". O que esse handler 
fazia era pegar o valor do ponto anterior e transferir para o da frente, mantendo assim a onda sempre em movimento.

 --------------------------------------------------------------------------------------------------------------------------------------------------
 
Com as funções funcionando em 2D, passei então a trabalhar para fazê-las funcionar em 3D.

Como estava em um ambiente 3D, tive que trabalhar com uma Matriz, uma das minhas maiores dúvidas foi: a onda se propaga em um circulo, e esse circulo
precisará ser desenhado na Matriz. Como fazer isso? Pesquisando um pouco, cheguei em uma função chamada midPoint, que basicamente transforma as 
coordenadas quebradas em coordenadas inteiras. Com base nesse algoritmo, criei uma função que fazia esse trabalho para mim.

Mudando do 2D para o 3D, tive que fazer alterações nas funções antigas. "waterHit" e "wavHandler" tiveram alterações para ao invés de trataren uma 
lista, tratarem uma Matriz.

Fontes (Tambem estão contidas no arquivo do código.):

https://threejs.org/examples/#webgl_water
https://math.stackexchange.com/questions/2097503/what-mathematical-shape-is-the-surface-of-waves-on-water
https://pdfs.semanticscholar.org/b88a/c2e6b2cd4f72835e89209d8240615791f742.pdf
https://en.wikipedia.org/wiki/Midpoint_circle_algorithm

