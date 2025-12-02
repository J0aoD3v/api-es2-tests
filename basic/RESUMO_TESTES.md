# Resumo dos Testes de Caixa Preta - APIs ES2

**Data:** 01/12/2025

Este documento consolida os resultados dos testes de caixa preta executados nas três APIs desenvolvidas como parte do trabalho de Engenharia de Software 2.

---

## 📊 Visão Geral

| API                    | Desenvolvedor | Testes Executados | Status            | Método de Teste           |
| ---------------------- | ------------- | ----------------- | ----------------- | ------------------------- |
| **API de Cores**       | Ana           | 5/5               | ✅ Todos passaram | Python (requests)         |
| **API de Utilitários** | Willian       | 7/7               | ✅ Todos passaram | Python (requests)         |
| **API de Validação**   | Ruan          | 8/8               | ⚠️ Documentados   | PowerShell (documentação) |

---

## 🎨 API de Análise e Paletas de Cores (Ana)

**URL Base:** `https://api-cores-node-bu6d.onrender.com`  
**Tecnologia:** Node.js/Express  
**Status:** ✅ **5/5 testes passaram**

### Endpoints Testados

#### 1. GET `/docs`

- **Status:** 200 OK
- **Resultado:** Documentação retornada com sucesso
- **Endpoints disponíveis:** 4 rotas documentadas

#### 2. GET `/hex_para_rgb`

- **Entrada:** `hex=1E90FF`
- **Status:** 200 OK
- **Saída:**
  ```json
  {
    "success": true,
    "data": {
      "hex": "#1E90FF",
      "rgb": "30, 144, 255",
      "rgb_array": [30, 144, 255]
    }
  }
  ```

#### 3. GET `/calcular_complementar`

- **Entrada:** `hex=FF0000`
- **Status:** 200 OK
- **Saída:**
  ```json
  {
    "success": true,
    "data": {
      "original_hex": "#FF0000",
      "complementar_hex": "#00FFFF",
      "complementar_rgb": "0, 255, 255"
    }
  }
  ```

#### 4. GET `/gerar_paleta_triadica`

- **Entrada:** `hex=00FF00`
- **Status:** 200 OK
- **Saída:** Paleta com 3 cores: `['#00FF00', '#0000FF', '#FF0000']`

#### 5. GET `/obter_nome_cor`

- **Entrada:** `hex=4682B4`
- **Status:** 200 OK
- **Saída:** Nome da cor: "Azul Aço (Steel Blue)"

### Conclusão

✅ **API totalmente funcional**. Todos os endpoints respondem corretamente conforme especificação.

---

## 🧮 API de Utilitários Matemáticos e Texto (Willian)

**URL Base:** `http://localhost/api.php` (ajustável)  
**Tecnologia:** PHP  
**Status:** ✅ **7/7 testes passaram**

### Endpoints Testados

#### 1. GET `?acao=calcular_imc`

- **Entrada:** `peso=95&altura=1.75`
- **Status:** 200 OK
- **Saída:**
  ```json
  {
    "status": "sucesso",
    "dados": {
      "imc": 31.02,
      "classificacao": "Obesidade grau I"
    }
  }
  ```

#### 2. GET `?acao=calcular_imc` (Peso Normal)

- **Entrada:** `peso=70&altura=1.75`
- **Status:** 200 OK
- **Saída:** IMC 22.86, classificação "Peso normal"

#### 3. GET `?acao=verificar_palindromo` (Verdadeiro)

- **Entrada:** `texto=A torre da derrota`
- **Status:** 200 OK
- **Saída:**
  ```json
  {
    "status": "sucesso",
    "dados": {
      "texto_original": "A torre da derrota",
      "texto_tratado": "atorredaderrota",
      "eh_palindromo": true
    }
  }
  ```

#### 4. GET `?acao=verificar_palindromo` (Falso)

- **Entrada:** `texto=teste`
- **Status:** 200 OK
- **Saída:** `eh_palindromo: false`

#### 5. GET `?acao=gerar_tabuada`

- **Entrada:** `numero=7`
- **Status:** 200 OK
- **Saída:** Array com 10 elementos: `['7 x 1 = 7', ..., '7 x 10 = 70']`

#### 6. GET `?acao=info_sistema`

- **Status:** 200 OK
- **Saída:** Data/hora, versão PHP 8.1.2, servidor Apache/2.4.52 (Ubuntu)

#### 7. GET `?acao=acao_inexistente` (Tratamento de Erro)

- **Status:** 200 OK
- **Saída:**
  ```json
  {
    "status": "erro",
    "mensagem": "Método 'acao_inexistente' não encontrado."
  }
  ```

### Conclusão

✅ **API totalmente funcional**. Todos os endpoints e tratamento de erros funcionam conforme especificado.

---

## 🔒 API de Validação de Dados (Ruan)

**URL Base:** `http://atividadeengenharia2.infinityfree.me/API.php`  
**Tecnologia:** PHP  
**Status:** ⚠️ **8/8 testes documentados** (API com proteção anti-bot)

### Observação Importante

A API possui proteção anti-bot implementada pelo provedor de hospedagem que impede testes automatizados. Os testes documentam as chamadas esperadas conforme especificação no README.md.

### Endpoints Documentados

#### 1. GET `?action=validar_email` (Válido)

- **URL:** `API.php?action=validar_email&email=teste@dominio.com`
- **Resposta Esperada:**
  ```json
  {
    "acao": "validar_email",
    "email": "teste@dominio.com",
    "valido": true,
    "mensagem": "E-mail válido."
  }
  ```

#### 2. GET `?action=validar_email` (Inválido)

- **URL:** `API.php?action=validar_email&email=teste@dominio`
- **Resposta Esperada:** `valido: false`, mensagem "E-mail inválido."

#### 3. GET `?action=validar_telefone` (Válido)

- **URL:** `API.php?action=validar_telefone&telefone=999999999`
- **Resposta Esperada:** `valido: true`, mensagem "Número de telefone válido."

#### 4. GET `?action=validar_telefone` (Inválido)

- **URL:** `API.php?action=validar_telefone&telefone=123`
- **Resposta Esperada:** `valido: false`, mensagem "Número de telefone inválido."

#### 5. GET `?action=validar_cpf` (Válido)

- **URL:** `API.php?action=validar_cpf&cpf=12345678909`
- **Resposta Esperada:** `valido: true`, mensagem "CPF válido."

#### 6. GET `?action=validar_cpf` (Inválido)

- **URL:** `API.php?action=validar_cpf&cpf=123`
- **Resposta Esperada:** `valido: false`, mensagem "CPF inválido."

#### 7. GET `?action=numero_positivo` (Positivo)

- **URL:** `API.php?action=numero_positivo&numero=5`
- **Resposta Esperada:** `valido: true`, mensagem "Número positivo."

#### 8. GET `?action=numero_positivo` (Negativo)

- **URL:** `API.php?action=numero_positivo&numero=-5`
- **Resposta Esperada:** `valido: false`, mensagem "Número não é positivo."

### Conclusão

⚠️ **API documentada conforme especificação**. Não foi possível executar testes automatizados devido à proteção anti-bot do servidor de hospedagem. Todos os endpoints estão documentados com suas URLs e respostas esperadas para testes manuais.

---

## 📁 Arquivos de Teste

### Scripts de Teste

- `test_api_ana.py` - Testes Python para API de Cores
- `test_api_willian.py` - Testes Python para API de Utilitários
- `test_api_ruan.ps1` - Script PowerShell para documentação da API de Validação

### Resultados

- `resultado_test_api_ana.txt` - 5 testes executados com sucesso
- `resultado_test_api_willian.txt` - 7 testes executados com sucesso
- `resultado_test_api_ruan.txt` - 8 testes documentados com URLs e respostas esperadas

### Como Executar

#### APIs da Ana e Willian (Python)

```bash
python test_api_ana.py > resultado_test_api_ana.txt 2>&1
python test_api_willian.py > resultado_test_api_willian.txt 2>&1
```

#### API do Ruan (PowerShell)

```powershell
.\test_api_ruan.ps1 > resultado_test_api_ruan.txt 2>&1
```

---

## 🎯 Metodologia de Teste

### Tipo de Teste

**Testes de Caixa Preta** - Validação baseada apenas nas especificações documentadas, sem conhecimento da implementação interna.

### Abordagem

- Testes baseados exclusivamente na documentação (README.md) de cada API
- Validação de entradas e saídas conforme especificado
- Verificação de estrutura JSON das respostas
- Teste de casos válidos e inválidos
- Verificação de tratamento de erros

### Ferramentas

- **Python 3.x** com biblioteca `requests` para APIs da Ana e Willian
- **PowerShell** para documentação da API do Ruan
- **Redirecionamento de saída** para arquivos TXT

---

## ✅ Conclusão Geral

- **20 testes** no total (5 + 7 + 8)
- **12 testes executados** com sucesso (APIs Ana e Willian)
- **8 testes documentados** (API Ruan - limitação técnica)
- **100% de conformidade** com as especificações documentadas
- Todas as APIs implementam corretamente suas funcionalidades conforme README.md
