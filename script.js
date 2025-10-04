// ----- 1. Pegando os Elementos da Página -----
const botao = document.getElementById('botao-descomplicar');
const textoOriginal = document.getElementById('texto-original');
const areaResultado = document.getElementById('resultado');

// ----- 2. Adicionando o "Ouvinte" de Evento-----
botao.addEventListener('click', () => {
    gerarExplicacao();
});

// ----- 3. A Função Principal (AGORA COM A CONEXÃO REAL!) -----
async function gerarExplicacao() {
    const duvidaDoUsuario = textoOriginal.value.trim();

    if (duvidaDoUsuario === "") {
        alert("Por favor, digite um tópico ou cole um texto para que eu possa explicar!");
        return;
    }

    // Mostra a mensagem de "carregando"
    areaResultado.innerHTML = '<p>Ok, acionando a IA para criar a melhor explicação... 🚀</p>';


    try {
        const response = await fetch('http://127.0.0.1:5000/descomplicar', {
            method: 'POST', // Estamos enviando dados
            headers: {
                'Content-Type': 'application/json', // Avisando que estamos enviando no formato JSON
            },
            body: JSON.stringify({ texto: duvidaDoUsuario }) // Convertendo nosso texto para o formato JSON
        });

        // Pega a resposta do servidor
        const data = await response.json();

        if (response.ok) {
            // Se tudo deu certo, mostra a explicação formatada em HTML
            const htmlFormatado = marked.parse(data.explicacao);
            areaResultado.innerHTML = `<h3>Explicação Descomplicada:</h3>${htmlFormatado}`;
        } else {
            // Se o servidor retornou um erro, mostra a mensagem de erro
            areaResultado.innerHTML = `<p><strong>Opa, algo deu errado!</strong><br>${data.error}</p>`;
        }

    } catch (error) {
        // Se não conseguir nem conectar ao servidor, mostra este erro
        console.error("Erro na comunicação:", error);
        areaResultado.innerHTML = `<p><strong>Erro de conexão!</strong><br>Não consegui falar com o servidor local. Verifique se o arquivo 'app.py' está rodando no terminal.</p>`;
    }
}