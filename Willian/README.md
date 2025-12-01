# Documentação API

Esta é uma API RESTful simplificada, desenvolvida em PHP, destinada a fornecer utilitários matemáticos e de manipulação de texto. O projeto foi desenhado para ser leve, sem dependências externas e de fácil implementação.

**URL Base:** `http://[SEU_DOMINIO]/api.php`  
**Formato de Resposta:** JSON (`application/json`)

---

## Métodos Disponíveis

A API utiliza o parâmetro `acao` (via Query String `GET` ou corpo `JSON`) para rotear a requisição.

### 1. Calcular IMC
Calcula o Índice de Massa Corporal com base no peso e altura fornecidos e retorna a classificação oficial detalhada.

- **Endpoint:** `?acao=calcular_imc`
- **Método HTTP:** GET ou POST
- **Parâmetros:**
  - `peso` (float): Peso em quilogramas (ex: `70.5`).
  - `altura` (float): Altura em metros (ex: `1.75`). **Atenção:** Utilize ponto para decimais.

**Classificações de Retorno:**
A API retornará uma das seguintes strings no campo `classificacao`:
* `Abaixo do peso`
* `Peso normal`
* `Sobrepeso`
* `Obesidade grau I`
* `Obesidade grau II`
* `Obesidade grau III`

**Exemplo de Requisição:**
`GET /api.php?acao=calcular_imc&peso=95&altura=1.75`

**Exemplo de Resposta:**
```json
{
  "status": "sucesso",
  "dados": {
    "imc": 31.02,
    "classificacao": "Obesidade grau I"
  }
}
```

### 2. Verificar Palíndromo
Verifica se uma palavra ou frase é um palíndromo (se a leitura é idêntica de trás para frente), ignorando espaços, acentuação básica e diferenciação de maiúsculas/minúsculas.

- **Endpoint:** `?acao=verificar_palindromo`
- **Método HTTP:** GET ou POST
- **Parâmetros:**
  - `texto` (string): A palavra ou frase a ser verificada.

**Exemplo de Requisição:**
`GET /api.php?acao=verificar_palindromo&texto=A+torre+da+derrota`

**Exemplo de Resposta:**
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

### 3. Gerar Tabuada
Gera uma lista contendo a tabuada de multiplicação (de 1 a 10) para um número inteiro fornecido.

- **Endpoint:** `?acao=gerar_tabuada`
- **Método HTTP:** GET ou POST
- **Parâmetros:**
  - `numero` (int): O número base para a geração da tabuada.

**Exemplo de Requisição:**
`GET /api.php?acao=gerar_tabuada&numero=7`

**Exemplo de Resposta:**
```json
{
  "status": "sucesso",
  "dados": [
    "7 x 1 = 7",
    "7 x 2 = 14",
    "7 x 3 = 21",
    "...",
    "7 x 10 = 70"
  ]
}
```

### 4. Info Sistema
Retorna informações de diagnóstico sobre o servidor onde a API está hospedada. Útil para validação de deploy e verificação de ambiente.

- **Endpoint:** `?acao=info_sistema`
- **Método HTTP:** GET
- **Parâmetros:** Nenhum.

**Exemplo de Requisição:**
`GET /api.php?acao=info_sistema`

**Exemplo de Resposta:**
```json
{
  "status": "sucesso",
  "dados": {
    "data_hora": "2025-11-19 15:30:00",
    "versao_php": "8.2.4",
    "servidor": "Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.2.4"
  }
}
```

## Tratamento de Erros

Caso a ação não seja informada, o método não exista ou os parâmetros obrigatórios sejam omitidos, a API retornará uma estrutura de erro padronizada.

**Exemplo de Erro:**
```json
{
  "status": "erro",
  "mensagem": "Ação não definida ou inválida."
}
```
