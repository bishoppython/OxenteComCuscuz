# Nutrição Nordestina - Chatbot Especializado em Nutrição com Receitas Nordestinas

Este projeto é um chatbot especializado em nutrição esportiva com foco em ganho de massa magra e perda de peso, utilizando receitas típicas da culinária nordestina brasileira. Utiliza tecnologias como Langchain, RAG (Retrieval-Augmented Generation) e o modelo Gemini para fornecer respostas nutricionais precisas e contextualizadas.

## Funcionalidades

- Respostas nutricionais especializadas em ganho de massa magra e perda de peso
- Recomendação de receitas nordestinas adaptadas para objetivos nutricionais
- Sistema de RAG para recuperação de informações relevantes de receitas nordestinas
- Interface web intuitiva para interação com o chatbot

## Tecnologias Utilizadas

- **Backend**: Python, Flask, Langchain, Google Generative AI (Gemini)
- **Frontend**: React com TypeScript
- **Banco de dados vetorial**: ChromaDB
- **Modelo de linguagem**: Google Gemini Pro

## Pré-requisitos

- Python 3.8+
- Node.js e npm
- Chave de API do Google AI Studio (para Gemini)

## Instalação e Configuração

### Backend

1. Navegue até o diretório do backend:
   ```bash
   cd /mnt/Dados/ALUNOS/nutricao_nordestina/backend
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure sua chave de API do Google:
   - Edite o arquivo `.env` e adicione sua chave:
     ```
     GOOGLE_API_KEY=sua_chave_aqui
     ```

5. Inicie o servidor backend:
   ```bash
   python app.py
   ```
   O servidor será iniciado em `http://localhost:5000`

### Frontend

1. Navegue até o diretório do frontend:
   ```bash
   cd /mnt/Dados/ALUNOS/nutricao_nordestina/frontend
   ```

2. Instale as dependências:
   ```bash
   npm install
   ```

3. Inicie o servidor de desenvolvimento:
   ```bash
   npm start
   ```
   O aplicativo será iniciado em `http://localhost:3000`

## Uso

1. Certifique-se de que o backend está em execução em `http://localhost:5000`
2. Acesse o frontend em `http://localhost:3000`
3. Faça perguntas relacionadas à nutrição, nutrição esportiva, dietas ou receitas nordestinas
4. O chatbot responderá com informações nutricionais e sugestões de receitas nordestinas adequadas ao seu objetivo

## Limitações

- O chatbot responderá apenas a perguntas relacionadas à nutrição, nutrição esportiva, dietas, alimentos e receitas nordestinas
- Para perguntas fora desse escopo, o sistema informará que só pode responder perguntas relevantes à nutrição

## Estrutura do Projeto

```
nutricao_nordestina/
├── backend/
│   ├── app.py              # Servidor Flask
│   ├── nutrition_rag.py    # Sistema RAG para nutrição
│   ├── prompt_template.py  # Template de prompt nutricional
│   ├── recipes_nordestinas.txt  # Dataset de receitas nordestinas
│   ├── requirements.txt    # Dependências do Python
│   └── .env               # Variáveis de ambiente
└── frontend/
    ├── src/
    │   ├── App.tsx
    │   ├── components/
    │   │   └── Chatbot.tsx # Componente do chatbot
    │   └── ...
    └── package.json
```

## Personalização

Para adicionar mais receitas nordestinas ao sistema RAG:
1. Edite o arquivo `backend/recipes_nordestinas.txt`
2. Adicione novas receitas com informações nutricionais detalhadas
3. Reinicie o servidor backend para que as novas receitas sejam indexadas

## Contribuição

Sinta-se à vontade para contribuir com este projeto:
1. Faça um fork do repositório
2. Crie uma branch para sua feature: `git checkout -b feature/nova-feature`
3. Commit suas mudanças: `git commit -m 'Adiciona nova feature'`
4. Push para a branch: `git push origin feature/nova-feature`
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.