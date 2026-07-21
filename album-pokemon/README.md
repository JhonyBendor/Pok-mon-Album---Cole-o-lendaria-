# 🃏 Pokémon Album - Coleção Lendária

Um álbum de figurinhas digital e interativo de Pokémon, com efeito realista de virada de página (flip-book), integrado a uma API em FastAPI (Python) para carregar dinamicamente as figurinhas e imagens do servidor.

Este projeto foi desenvolvido durante a **Imersão Dev** (Alura) e aprimorado com recursos visuais premium, design responsivo e uma arquitetura limpa separando o Front-end e o Back-end.

---

## 🚀 Funcionalidades

- **Efeito Flip-Book Realista**: Navegação interativa imitando um álbum físico de papel usando a biblioteca `page-flip`.
- **Cores Temáticas Vibrantes**: Cada página possui gradientes personalizados de acordo com o tipo do Pokémon (Elétrico, Fogo, Água, Planta e Lendários).
- **Proporção Perfeita de Cartas**: Slots de figurinhas redesenhados no formato exato de cartas colecionáveis (proporção 240x330px), garantindo o preenchimento de 100% da imagem sem distorções ou cortes.
- **Capa Inteira Personalizada**: Uma arte de capa imersiva em tela cheia com colagem de vários Pokémons.
- **Carregamento Dinâmico (API)**: Integração via `fetch` assíncrono para buscar metadados e imagens do servidor FastAPI.
- **Efeitos de Som**: Efeito sonoro dinâmico e sintetizado (Web Audio API) que simula o barulho de papel virando ao passar as páginas.

---

## 🛠️ Tecnologias Utilizadas

### Front-end:
- **HTML5** (Estrutura semântica do álbum)
- **Vanilla CSS3** (Gradientes dinâmicos, efeitos hover e animações de colagem)
- **JavaScript ES6+** (Consumo da API e controle de som/navegação)
- **Page-Flip.js** (Efeito físico de virada de página)

### Back-end:
- **Python 3.x**
- **FastAPI** (Framework moderno de alta performance para criação da API)
- **Uvicorn** (Servidor ASGI para rodar a aplicação Python)

---

## 📁 Estrutura do Projeto

```text
album-pokemon/
├── backend/                  # API desenvolvida em Python/FastAPI
│   ├── figurinhas/          # Banco de imagens das figurinhas (.png e .jpeg)
│   ├── main.py              # Código principal e endpoints da API
│   └── ...
└── frontend/                 # Interface visual do Álbum (HTML/CSS/JS)
    ├── index.html           # Estrutura das páginas do álbum
    ├── style.css            # Estilização completa e responsiva
    ├── app.js               # Lógica de consumo da API e renderização
    ├── cover_illustration.jpg # Imagem em tela cheia da capa
    └── ...
```

---

## 🔧 Como Executar o Projeto Localmente

### 1. Iniciar o Back-end:
Entre na pasta `backend`, ative o seu ambiente virtual e inicie o servidor:
```bash
# Navegar até a pasta do backend
cd backend

# Iniciar o servidor com Uvicorn
python -m uvicorn main:app --reload
```
A API estará rodando em `http://localhost:8000`. Você pode conferir a documentação interativa em `http://localhost:8000/docs`.

### 2. Executar o Front-end:
1. Navegue até a pasta `frontend`.
2. Dê um duplo clique no arquivo `index.html` para abri-lo no seu navegador.
3. Divirta-se colecionando suas figurinhas favoritas!

---

## 📝 Autor e Agradecimentos

Projeto desenvolvido para fins de aprendizado e aprimoramento pessoal de desenvolvimento web Full-Stack durante a Imersão Dev da Alura.
