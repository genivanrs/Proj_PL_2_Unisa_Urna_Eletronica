# Projeto Integrador II - Laboratório de Programação: Urna Eletrônica

## 1. Introdução

O projeto integrador visa sistematizar os conhecimentos adquiridos pelos estudantes durante o curso, oferecendo vivência prática-profissional mediante aplicação dos conhecimentos em situações reais.

Tem por objetivo integrar os conhecimentos nas áreas específicas dos cursos e a prática organizacional, promovendo o desenvolvimento de competências, ou seja, a capacidade pessoal de mobilizar, articular e colocar em ação conhecimentos, habilidades, atitudes e valores necessários para o desempenho eficiente e eficaz de atividades requeridas pela natureza do trabalho e pelo desenvolvimento tecnológico.

## 2. Proposta do Projeto

**Projeto Integrador II - Laboratório de Programação – Urna Eletrônica:** deverá ser criado uma urna eletrônica utilizando a linguagem Python. A aplicação deve apresentar as seguintes características:

### Requisitos do Projeto

- A urna deve apurar os votos para **prefeito** e **vereadores** de um município. 
  - Deve haver ao menos **três candidatos** para prefeito e **dez candidatos** para a câmara de vereadores.

- Ao iniciar a urna, deve ser apresentado um **menu** com as seguintes opções:
  - **Imprimir Zerésima:** mostra que todos os candidatos estão com zero votos computados.
  - **Iniciar Votação:** o programa fica pronto para receber os votos.

- O candidato deve ser selecionado pelo eleitor com a inserção de seu **número**:
  - **Prefeito:** dois dígitos.
  - **Vereador:** cinco dígitos.
  - Ao digitar um número válido, o nome e o partido do candidato devem ser exibidos.
  - Caso o número não exista, o programa deve informar que o voto será computado como **nulo**.
  - Deve haver uma **confirmação da escolha** e a opção de votar em **branco**.

- Após a votação de cada eleitor, o programa deve exibir a mensagem:
  - "**Finalizar a votação ou continuar?**"
  - Se **continuar** for selecionado, a urna fica pronta para o próximo voto.
  - Se **finalizar** for selecionado, a urna realiza a **totalização dos votos**, indicando o total de votos de cada candidato.

- Com base na totalização dos votos, o sistema deve:
  - Indicar o **vencedor para prefeito**.
  - Indicar os **três melhores colocados para o cargo de vereador**.
  - Caso haja empate para o cargo de prefeito, deve indicar que ocorrerá um **segundo turno**.
  - Nenhum vereador pode ser eleito sem receber votos.

---

Este projeto foi desenvolvido para o curso de **Laboratório de Programação**, utilizando a linguagem **Python**.
