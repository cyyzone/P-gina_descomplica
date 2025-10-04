# Descomplica 🚀

Um tradutor de "adultês" para a linguagem da Geração Z. Este projeto é uma aplicação web que utiliza a API do Google Gemini para explicar tópicos complexos de estudo de forma simples, divertida e didática, usando analogias e uma linguagem atual para adolescentes.

![Prévia do Descomplica](https://i.imgur.com/a9JNIKH.png) 
---

## 🎯 Sobre o Projeto

A ideia para o "Descomplica" nasceu da necessidade de criar uma ponte entre o conteúdo escolar tradicional e a forma como os jovens de hoje consomem informação. A ferramenta permite que usuários colem um texto ou digitem um tópico e recebam em troca uma explicação reformulada, rica em emojis, gírias e referências ao universo de games, filmes e redes sociais.

O objetivo é transformar o aprendizado em algo menos intimidador e mais engajante.

---

## ✨ Funcionalidades

* **Interface Simples:** Uma caixa de texto para inserir o tópico e um botão para a mágica acontecer.
* **Explicações via IA:** Utiliza o poder do Google Gemini para gerar explicações criativas e precisas.
* **Linguagem Adaptada:** O prompt da IA é instruído a focar em um público adolescente, garantindo que o tom seja sempre relevante.
* **Formatação Rica:** A resposta da IA é convertida de Markdown para HTML, exibindo títulos, listas e negrito corretamente.

---

## 🛠️ Tecnologias Utilizadas

Este projeto é uma aplicação full-stack que combina tecnologias de front-end e back-end.

**Front-End:**
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

**Back-End:**
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

**APIs e Bibliotecas:**
* **Google Gemini API:** O cérebro por trás das explicações.
* **Marked.js:** Biblioteca para converter a resposta em Markdown para HTML no front-end.
* **Python-dotenv:** Para gerenciar as variáveis de ambiente de forma segura.

---

## ⚙️ Configuração e Instalação

Para rodar este projeto localmente, siga os passos abaixo.

**Pré-requisitos:**
* Python 3.x instalado
* Uma chave de API do [Google AI Studio](https://aistudio.google.com/)

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
    cd nome-do-repositorio
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências do Python:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure sua chave de API:**
    * Crie um arquivo chamado `.env` na raiz do projeto.
    * Dentro dele, adicione sua chave secreta no seguinte formato:
        ```
        GOOGLE_API_KEY=SUA_CHAVE_SUPER_SECRETA_AQUI
        ```

5.  **Inicie o servidor back-end:**
    ```bash
    python app.py
    ```
    O servidor estará rodando em `http://127.0.0.1:5000`.

6.  **Abra o front-end:**
    * Navegue até a pasta do projeto e abra o arquivo `index.html` diretamente no seu navegador.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

Feito com ❤️ por [Cyyzone](https://github.com/cyyzone).
