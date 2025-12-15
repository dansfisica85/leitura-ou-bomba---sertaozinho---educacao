# 💣 Leitura ou Bomba

Aplicação web gamificada de reconhecimento de voz para avaliação de fluência leitora, organizada em **3 fases progressivas**: palavras reais, pseudopalavras e leitura de texto completo.

## 👨‍🏫 Autor

### Profº Davi Antonino Nunes da Silva

- 📞 Contato: (16) 99260-4315
- 📧 E-mail: <davi.silva@educacao.sp.gov.br>
- 📧 E-mail alternativo: <professordavi85@gmail.com>

**Uso gratuito — exclusivo para a Secretaria de Educação do Município de Sertãozinho**

---

## 🎮 Como Funciona

O jogo possui **3 fases**. O jogador precisa acertar **10 palavras em cada fase** para avançar. Se o tempo esgotar antes de atingir a meta, a bomba explode!

### 📖 Fase 1 — Palavras Reais
- Palavras do vocabulário comum são exibidas uma por vez
- O jogador deve ler em voz alta
- Meta: 10 acertos em 60 segundos

### 🔤 Fase 2 — Pseudopalavras
- Palavras inventadas (sem significado) são exibidas
- Avalia a decodificação fonológica
- Meta: 10 acertos em 60 segundos

### 📄 Fase 3 — Texto Completo
- Um texto inteiro aparece formatado na tela
- O jogador lê sequencialmente
- Palavras corretas ficam **verdes**, erradas ficam **vermelhas**
- Validação em tempo real conforme a leitura
- Meta: 10 acertos em 60 segundos

---

## 📋 Funcionalidades

- ✅ **3 fases progressivas** com dificuldade crescente
- ✅ Cronômetro de **60 segundos por fase**
- ✅ Contagem regressiva 3, 2, 1, VAI! antes de iniciar
- ✅ Reconhecimento de voz em tempo real (pt-BR)
- ✅ Validação visual instantânea (verde/vermelho)
- ✅ Cadastro do nome do jogador
- ✅ Ranking dos melhores resultados (Top 10)
- ✅ Animação de explosão quando perde
- ✅ Interface moderna e responsiva
- ✅ Comparação inteligente com tolerância fonética

---

## 🚀 Deploy no Vercel

### Opção 1: Via Vercel CLI

```bash
npm install -g vercel
vercel login
vercel
```

### Opção 2: Via GitHub

1. Crie um repositório no GitHub
2. Faça upload dos arquivos
3. Acesse [vercel.com](https://vercel.com)
4. Clique em "Import Project"
5. Selecione seu repositório
6. Clique em "Deploy"

### Configurar Ranking no GitHub (Opcional)

Para persistir o ranking no repositório:

1. Crie um **Personal Access Token** no GitHub com permissão `repo`
2. No Vercel, adicione as variáveis de ambiente:
   - `GITHUB_TOKEN`: Seu token pessoal
   - `GITHUB_REPO`: `usuario/repositorio`
3. Faça redeploy

**Obs:** Sem essa configuração, o ranking funciona apenas localmente (localStorage).

---

## 🔐 Área Administrativa

Para resetar o ranking:

1. Clique no botão "⚙️ Admin" no rodapé
2. Digite a senha de administrador
3. Confirme para limpar o ranking

---

## 🔧 Tecnologias Utilizadas

- **Frontend**: HTML5, CSS3, JavaScript
- **Reconhecimento de Voz**: Web Speech API
- **Backend**: Python (Serverless Functions)
- **Hospedagem**: Vercel
- **Armazenamento**: localStorage + GitHub API

---

## ⚠️ Requisitos

- Navegador moderno (Chrome ou Edge recomendados)
- Permissão de microfone
- Conexão com internet

## 📝 Notas Técnicas

- Reconhecimento de voz otimizado para português brasileiro
- Similaridade mínima para acerto: 65%
- Normalização fonética para maior tolerância
- 20 alternativas de reconhecimento para melhor precisão

---

## 🎓 Objetivo Pedagógico

Este aplicativo foi desenvolvido para auxiliar no desenvolvimento de habilidades de leitura em crianças, permitindo que educadores avaliem:

- **Fluência leitora** com palavras conhecidas
- **Decodificação fonológica** com pseudopalavras
- **Leitura contextualizada** com textos completos

---

© 2025 - Profº Davi Antonino Nunes da Silva | Secretaria de Educação do Município de Sertãozinho
