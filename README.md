# **Boids Algortihm In Python**

![Vai assister a primeira temporada de True Detective](birds_true_detective.gif)

Estava procurando por algum projeto para fazer em Python achei alguns assuntos sobre Boids, e como recentemente tenho dado preferência por projetos visualmentes apelativos esse aqui não foi diferente. 

### **Referências:** 
[Just Boids | Useless Game Dev](https://www.youtube.com/watch?v=6dJlhv3hfQ0&t=102s). **Canal do YouTube:** Useless Game Dev

[Coding Adventure: Boids](https://www.youtube.com/watch?v=bqtqltqcQhw&t=151s). **Canal do YouTube:** Sebastian Lague

[Boids algorithm](https://vanhunteradams.com/Pico/Animal_Movement/Boids-algorithm.html). **Artigo:** V. Hunter Adams **(vha3@cornell.edu)**

### **Resultado**
![Resultado](result.gif)

Basicamente três regras são aplicadas para que um fluxo de boids aconteça de forma interessante. 

- Separação: Responsavel pela não-colisão de um boid em um certo raio;

- Alinhamento: Responsável pela direção geral de um boid

- Coesão: Responsável pela posição de um boid, que gera grupos em todos os boids.

**Minha explicação talvez tenha sido a pior de todas, se tu tem interesse em saber mais sobre o assunto vai ler o artigo citado ali em cima que tu vai entender melhor**

### **A fazer:**
- Melhorar cálculo de alinhamento e coesão pois o universo dos boids pode acabar indo sempre para uma mesma direção
- Criar obstáculos no universo dos boids;
- Melhorar cálculos feitos para garantir performance para um universo com mais de 150 boids;
- Refatorar código (Fiz o código em 1 dia, tem muito espaço para melhorias);
- Melhorar organização do código.