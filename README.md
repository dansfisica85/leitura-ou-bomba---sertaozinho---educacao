# 🎯 Leitura ou Bomba

Aplicação web de reconhecimento de voz para teste de leitura com palavras reais e pseudopalavras.

## 👨‍🏫 Autor

### Profº Davi Antonino Nunes da Silva

- 📞 Contato: (16) 99260-4315
- 📧 E-mail: <davi.silva@educacao.sp.gov.br>
- 📧 E-mail alternativo: <professordavi85@gmail.com>

**Uso gratuito — exclusivo para a Secretaria de Educação do Município de Sertãozinho**

---

## 📋 Funcionalidades

- ✅ Cronômetro de 60 segundos
- ✅ Contagem regressiva 3, 2, 1, VAI! antes de iniciar
- ✅ Gravação de voz automática
- ✅ Alternância entre palavras reais e pseudopalavras
- ✅ Cadastro do nome do jogador
- ✅ Ranking dos melhores resultados
- ✅ Reconhecimento de voz em português (pt-BR)
- ✅ Interface moderna e responsiva
- ✅ Comparação inteligente com tolerância a erros

## 🚀 Deploy no Vercel

### Opção 1: Via Vercel CLI

1. Instale o Vercel CLI:

```bash
npm install -g vercel
```

2. Faça login no Vercel:

```bash
vercel login
```

3. Na pasta do projeto, execute:

```bash
vercel
```

4. Siga as instruções e faça deploy!

### Opção 2: Via GitHub

1. Crie um repositório no GitHub
2. Faça upload dos arquivos
3. Acesse [vercel.com](https://vercel.com)
4. Clique em "Import Project"
5. Selecione seu repositório
6. Clique em "Deploy"

### Configurar Ranking no GitHub (Opcional)

Para que o ranking seja persistido no repositório do GitHub:

1. Crie um **Personal Access Token** no GitHub:
   - Acesse: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Gere um novo token com permissão `repo`

2. No Vercel, adicione as variáveis de ambiente:
   - `GITHUB_TOKEN`: Seu token pessoal do GitHub
   - `GITHUB_REPO`: Nome do repositório (formato: `usuario/repositorio`)

3. Faça redeploy do projeto

**Obs:** Sem essa configuração, o ranking funciona apenas localmente no navegador.

## 🔐 Área Administrativa

Para resetar o ranking:

1. Clique no botão "⚙️ Admin" discreto no rodapé
2. Digite a senha de administrador
3. Confirme para limpar todo o ranking

## 🎮 Como Usar

1. Digite seu nome no campo de cadastro
2. Clique no botão "INICIAR"
3. Aguarde a contagem regressiva (3, 2, 1, VAI!)
4. Leia as palavras que aparecem na tela em voz alta
5. O sistema reconhece automaticamente sua voz
6. Tente acertar o máximo de palavras em 1:00
7. Ao final, veja sua pontuação e o ranking!

## 🔧 Tecnologias Utilizadas

- **Frontend**: HTML5, CSS3, JavaScript (Web Speech API)
- **Backend**: Python (Serverless Functions para ranking)
- **Hospedagem**: Vercel
- **Armazenamento**: GitHub API (ranking persistente)
- **Reconhecimento de Voz**: Web Speech API

## ⚠️ Requisitos

- Navegador moderno (Chrome ou Edge recomendados)
- Permissão de microfone
- Conexão com internet

## 📝 Notas

- O reconhecimento de voz funciona melhor no Chrome e Edge
- É necessário permitir o acesso ao microfone quando solicitado
- O ranking é salvo no navegador (localStorage)
- A similaridade mínima para acerto é de 75%

## 🎓 Objetivo Pedagógico

Este aplicativo foi desenvolvido para auxiliar no desenvolvimento de habilidades de leitura em crianças, permitindo que educadores e alunos pratiquem a pronúncia correta de palavras reais e pseudopalavras de diferentes níveis de complexidade.

---

© 2025 - Profº Davi Antonino Nunes da Silva | Secretaria de Educação do Município de Sertãozinho
