# 🏆 Pokémon Album - Coleção Lendária

Um álbum de figurinhas virtual, interativo e nostálgico dedicado às criaturas mais famosas do universo Pokémon. O projeto traz uma experiência imersiva de folhear páginas em um ambiente com tema de cores elétricas e douradas em tom neon.

---

## 🎯 Objetivo do Projeto

O **Pokémon Album** visa recriar a clássica experiência de colecionar figurinhas no ambiente digital. O usuário pode folhear o álbum de forma fluida e tátil, escutar o som físico tridimensional das folhas de papel e ver as imagens dos Pokémon surgirem de forma dinâmica a partir de dados alimentados por um servidor local (API).

---

## 📁 Estrutura do Projeto e Funcionalidades

O projeto é dividido em três arquivos principais:

### 1. 📄 [index.html](index.html)
* **Objetivo:** Define a estrutura do álbum de figurinhas.
* **Principais Funcionalidades:**
  * **Configuração Inicial:** Carrega metadados, fontes do Google Fonts (Inter e Outfit) e os links de dependências.
  * **Controles Interativos:** Botão de silenciar som e setas para folhear as páginas nas bordas.
  * **Estrutura das Páginas (`#book`):**
    * Capa com design 3D cintilante em estilo *glitch*.
    * Páginas temáticas de figurinhas categorizadas por tipos: **Elétrico**, **Fogo**, **Água**, **Planta** e **Lendários**.
    * Contracapa com código de barras decorativo e créditos finais do projeto.
  * **Dependências Externas:** Importação do script da biblioteca `St.PageFlip` via CDN para simular a dobra realista das folhas.

### 2. 🎨 [style.css](style.css)
* **Objetivo:** Controla a estética visual, cores, animações e o design responsivo.
* **Principais Funcionalidades:**
  * **Paleta de Cores de Alta Fidelidade (Amarelo/Ouro):** Configurado no bloco `:root` com variações de amarelo elétrico, ouro metálico e marrom-dourado profundo em contraste com fundo preto/grafite.
  * **Micro-animações:** Efeito de *glitch* nos títulos principais e de flutuação dinâmica em mini-cards colecionáveis na capa (Pikachu, Charizard e Mewtwo).
  * **Efeito Tridimensional:** Sombreamento gradiente na dobra das páginas para emular o relevo de um livro físico aberto.

### 3. ⚡ [app.js](app.js)
* **Objetivo:** Controla a interatividade de folhear páginas, áudio dinâmico e integração com a API.
* **Principais Funcionalidades:**
  * **Integração com Backend:** Busca dinamicamente os metadados das figurinhas (`GET http://localhost:8000/figurinhas`) para preencher os 30 slots do álbum.
  * **Efeito Sonoro Dinâmico (Web Audio API):** Sintetiza em tempo real um som de papel sendo folheado baseado na fricção física.
  * **Controle de Gestos:** Permite a transição das páginas arrastando com o mouse ou toques na tela (mobile).

---

## 🚀 Como Executar o Projeto

1. **Visualizar o Álbum (Frontend):**
   * Abra o arquivo `index.html` em qualquer navegador ou utilize uma extensão como a *Live Server* do VS Code.

2. **Servir as Figurinhas Dinamicamente (Backend - Opcional):**
   * Se você possuir a API local estruturada, inicie o servidor Python FastAPI:
     ```bash
     cd backend/dia-3
     uvicorn main:app --reload
     ```
   * O frontend se conectará a `http://localhost:8000` para colar as fotos dos Pokémon nos slots de #01 a #30.
