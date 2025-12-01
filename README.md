# 🧪 Projeto de Testes de APIs - Engenharia de Software 2

[![Status](https://img.shields.io/badge/Status-Completo-success)]()
[![Testes](https://img.shields.io/badge/Testes-160_executados-blue)]()
[![Taxa_de_Sucesso](https://img.shields.io/badge/Taxa_Sucesso-76.3%25-yellow)]()

Este projeto consolida a análise e testes automatizados de três APIs RESTful desenvolvidas como trabalho acadêmico de Engenharia de Software 2. Cada equipe implementou uma API com funcionalidades distintas, e este repositório contém a suíte completa de testes e relatórios de análise.

---

## 📁 Estrutura do Projeto

```
api-es2-tests/
│
├── README.md                              # Este arquivo - Documentação principal
├── RELATORIO_ANALISE_CONSOLIDADO.md       # Análise comparativa das 3 APIs
│
├── Ana/                                   # API de Análise e Paletas de Cores
│   ├── README.md                          # Documentação da API (Node.js/Express)
│   ├── RELATORIO_ANALISE.md               # Relatório de testes da Ana
│   ├── relatorio_testes.txt               # Output dos testes executados
│   ├── test_api.py                        # Suite de testes Python (52 testes)
│   └── api/
│       ├── server.js                      # Código fonte da API
│       ├── test_suite.js                  # Testes em JavaScript
│       ├── package.json                   # Dependências Node.js
│       └── RELATORIO_ERROS.md             # Documentação de bugs corrigidos
│
├── Ruan/                                  # API de Validação de Dados
│   ├── README.md                          # Documentação da API (PHP)
│   ├── RELATORIO_ANALISE.md               # Relatório de testes do Ruan
│   ├── relatorio_testes_powershell.txt    # Output dos testes executados
│   ├── test_api.ps1                       # Suite de testes PowerShell (54 testes)
│   └── API.php                            # Código fonte da API
│
└── Willian/                               # API RESTful Utilitária
    ├── README.md                          # Documentação da API (PHP)
    ├── RELATORIO_ANALISE.md               # Relatório de testes do Willian
    ├── relatorio_testes.txt               # Output dos testes executados
    ├── test_api.py                        # Suite de testes Python (54 testes)
    └── api.php                            # Código fonte da API
```

---

## 🎯 Visão Geral das APIs

### 1. 🎨 API de Análise e Paletas de Cores (Ana)

**Tecnologia:** Node.js + Express.js  
**Hosting:** Render.com  
**URL Base:** `https://api-cores-node-bu6d.onrender.com`

#### Funcionalidades:

- ✅ Conversão de cores HEX para RGB
- ✅ Cálculo de cor complementar
- ✅ Geração de paleta triádica
- ✅ Obtenção de nome descritivo de cores

#### Destaques:

- 🏆 Algoritmos complexos implementados manualmente
- 📚 Documentação integrada via endpoint `/docs`
- 🎯 Código limpo e bem estruturado com JSDoc

#### Estatísticas:

- **Testes:** 52
- **Aprovados:** 30 (57.7%)
- **Nota:** 5.5/10 (potencial 8.0/10 após correção de deploy)

---

### 2. ✔️ API de Validação de Dados (Ruan)

**Tecnologia:** PHP  
**Hosting:** InfinityFree  
**URL Base:** `http://atividadeengenharia2.infinityfree.me`

#### Funcionalidades:

- ✅ Validação de e-mail (100% acurácia)
- ✅ Validação de telefone
- ✅ Validação de CPF
- ✅ Verificação de números positivos

#### Destaques:

- ⚡ Melhor performance (300ms por requisição)
- 🎯 Validação de e-mail perfeita (9/9 testes)
- 🔒 Proteção contra SQL Injection e XSS

#### Estatísticas:

- **Testes:** 54
- **Aprovados:** 44 (81.5%)
- **Nota:** 6.2/10

---

### 3. 🧮 API RESTful Utilitária (Willian)

**Tecnologia:** PHP  
**Hosting:** UENP (Servidor Acadêmico)  
**URL Base:** `https://cct.uenp.edu.br/coleti/es2/willian`

#### Funcionalidades:

- ✅ Cálculo de IMC com classificação
- ✅ Verificação de palíndromo
- ✅ Geração de tabuada
- ✅ Informações do sistema

#### Destaques:

- 🔒 Segurança robusta (100%)
- ✅ Validações sólidas e consistentes
- 🎯 Funcionalidades avançadas (valores extremos, notação científica)

#### Estatísticas:

- **Testes:** 54
- **Aprovados:** 48 (88.9%)
- **Nota:** 7.5/10

---

## 📊 Resultados Consolidados

### Ranking Geral

| Posição | Equipe  | Tecnologia | Taxa de Sucesso | Nota Final | Status |
| ------- | ------- | ---------- | --------------- | ---------- | ------ |
| 🥇      | Willian | PHP        | 88.9%           | 7.5/10     | 🟢     |
| 🥈      | Ruan    | PHP        | 81.5%           | 6.2/10     | 🟡     |
| 🥉      | Ana     | Node.js    | 57.7%           | 5.5/10     | 🔴     |

### Comparação por Categoria

| Categoria        | Ana        | Ruan   | Willian  | Vencedor    |
| ---------------- | ---------- | ------ | -------- | ----------- |
| **Performance**  | ~1.88s     | ~300ms | ~1.69s   | Ruan ⚡     |
| **Segurança**    | 80%        | 67%    | 100%     | Willian 🔒  |
| **Validações**   | 60%        | 89%    | 93%      | Willian ✅  |
| **Documentação** | 100%       | 0%     | 50%      | Ana 📚      |
| **Padrões REST** | ✅         | ❌     | ✅       | Ana/Willian |
| **Código Limpo** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | Ana 🧹      |

### Estatísticas Totais

- **Total de Testes:** 160
- **Testes Aprovados:** 122 (76.3%)
- **Testes Falhados:** 38 (23.7%)
- **Problemas Críticos Identificados:** 7
- **Problemas Médios:** 11
- **Tempo Total de Execução:** ~4 minutos

---

## 🧪 Suítes de Testes

### Ana - test_api.py (Python)

```bash
cd Ana
python test_api.py
```

**Cobertura de Testes:**

- ✅ Conversão HEX para RGB (5 testes)
- ✅ Cálculo de cor complementar (4 testes)
- ✅ Geração de paleta triádica (4 testes)
- ✅ Obtenção de nome de cor (5 testes)
- ✅ Documentação (2 testes)
- ✅ Validações e segurança (32 testes)

**Requisitos:**

```bash
pip install requests colorama
```

---

### Ruan - test_api.ps1 (PowerShell)

```powershell
cd Ruan
.\test_api.ps1
```

**Cobertura de Testes:**

- ✅ Validação de e-mail (9 testes)
- ✅ Validação de telefone (9 testes)
- ✅ Validação de CPF (9 testes)
- ✅ Número positivo (8 testes)
- ✅ Tratamento de erros (3 testes)
- ✅ Segurança (14 testes)
- ✅ Funcionalidades especiais (2 testes)

**Requisitos:**

- PowerShell 5.1 ou superior

---

### Willian - test_api.py (Python)

```bash
cd Willian
python test_api.py
```

**Cobertura de Testes:**

- ✅ Cálculo de IMC (14 testes)
- ✅ Verificação de palíndromo (12 testes)
- ✅ Geração de tabuada (10 testes)
- ✅ Info sistema (1 teste)
- ✅ Testes gerais (17 testes)

**Requisitos:**

```bash
pip install requests
```

---

## 🚀 Como Executar os Testes

### Pré-requisitos Gerais

- **Python 3.8+** (para testes da Ana e Willian)
- **PowerShell 5.1+** (para testes do Ruan)
- **Conexão com internet** (APIs estão hospedadas remotamente)

### Execução Individual

#### Ana (Python)

```bash
cd Ana
pip install requests colorama
python test_api.py
```

#### Ruan (PowerShell)

```powershell
cd Ruan
.\test_api.ps1
```

#### Willian (Python)

```bash
cd Willian
pip install requests
python test_api.py
```

### Execução de Todos os Testes (PowerShell)

```powershell
# Ana
cd Ana
python test_api.py > relatorio_testes.txt

# Ruan
cd ..\Ruan
.\test_api.ps1 > relatorio_testes_powershell.txt

# Willian
cd ..\Willian
python test_api.py > relatorio_testes.txt
```

---

## 📝 Relatórios Disponíveis

### 1. RELATORIO_ANALISE_CONSOLIDADO.md

Análise comparativa completa das três APIs, incluindo:

- Resumo executivo e classificação final
- Análise detalhada de cada API
- Comparação lado a lado de todos os critérios
- Problemas críticos identificados
- Recomendações de correção

### 2. Relatórios Individuais

Cada pasta contém:

- **RELATORIO_ANALISE.md**: Análise técnica detalhada
- **relatorio_testes.txt**: Output bruto dos testes executados

---

## 🔧 Tecnologias Utilizadas

### APIs

- **Node.js** + Express.js (Ana)
- **PHP** (Ruan e Willian)

### Testes

- **Python 3** + requests + colorama
- **PowerShell 5.1**

### Hosting

- **Render.com** (Ana)
- **InfinityFree** (Ruan)
- **UENP** (Willian)

---

## 🐛 Problemas Críticos Identificados

### Ana

1. 🔴 Erro 500 com parâmetros duplicados (regressão de deploy)
2. 🔴 Header CORS ausente em produção
3. 🟡 Validação inconsistente de parâmetros ausentes

### Ruan

1. 🔴 Validação de CPF aceita dígitos repetidos (11111111111)
2. 🔴 Formato de resposta não-padrão (HTML + JSON)
3. 🟡 Validação de telefone muito restritiva

### Willian

1. 🔴 POST com JSON não funciona
2. 🔴 Performance inaceitável (~1.7s por requisição)
3. 🟡 Métodos HTTP não documentados aceitos (PUT/DELETE)

---

## 💡 Recomendações Gerais

### Alta Prioridade

1. ⚡ Implementar rate limiting (proteção contra DDoS)
2. 🔧 Normalizar inputs (lowercase em actions, trim em parâmetros)
3. 🧪 Adicionar testes unitários integrados

### Média Prioridade

4. 📊 Implementar logging estruturado
5. 📈 Adicionar monitoramento de performance
6. 🔖 Implementar versionamento de API (/v1/endpoint)

### Baixa Prioridade

7. 📦 Suporte a múltiplos formatos (JSON, XML)
8. 💾 Implementar cache de respostas
9. 📖 Documentação OpenAPI/Swagger

---

## 👥 Equipes

### Ana

- **API:** Análise e Paletas de Cores
- **Tecnologia:** Node.js/Express
- **Contato:** [Informação não disponível]

### Ruan

- **API:** Validação de Dados
- **Tecnologia:** PHP
- **Contato:** [Informação não disponível]

### Willian

- **API:** RESTful Utilitária
- **Tecnologia:** PHP
- **Contato:** [Informação não disponível]

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos como parte do curso de Engenharia de Software 2.

---

## 📞 Suporte

Para dúvidas sobre as APIs individuais, consulte o README.md específico de cada equipe em suas respectivas pastas.

Para questões sobre os testes ou relatórios consolidados, consulte o arquivo `RELATORIO_ANALISE_CONSOLIDADO.md`.

---

## 🏆 Conclusão

Este projeto demonstra a importância de testes automatizados abrangentes no desenvolvimento de APIs. Cada equipe apresentou pontos fortes únicos:

- **Ana**: Excelência em algoritmos e arquitetura de código
- **Ruan**: Performance excepcional e validações específicas
- **Willian**: Segurança robusta e funcionalidades completas

Com as correções recomendadas, todas as APIs têm potencial para se tornarem soluções profissionais de alta qualidade.

---

**Última Atualização:** 1 de dezembro de 2025  
**Versão do Documento:** 1.0
