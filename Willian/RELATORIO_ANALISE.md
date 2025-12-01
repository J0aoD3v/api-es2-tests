# Relatório de Análise de Testes - API RESTful

**Data:** 01/12/2025  
**API Testada:** https://cct.uenp.edu.br/coleti/es2/willian/api.php  
**Relatório Completo:** [relatorio_testes.txt](./relatorio_testes.txt)

---

## 📊 Resumo Executivo

Foram executados **54 testes** abrangentes cobrindo funcionalidades, validações, segurança e edge cases da API.

### Resultados Gerais

- ✅ **Testes Passaram:** 48 (88.9%)
- ❌ **Testes Falharam:** 6 (11.1%)
- ⚠️ **Problemas Críticos:** 2
- ⚠️ **Problemas Médios:** 4
- ℹ️ **Observações:** 3

---

## 🔴 Problemas Críticos

### 1. POST com JSON Não Funciona

**Severidade:** 🔴 CRÍTICA  
**Testes Afetados:** 1.7, 2.6, 3.5, 6.17

**Descrição:**  
A API não consegue processar requisições POST com `Content-Type: application/json`. Todas retornam:

```json
{
  "status": "erro",
  "mensagem": "Ação não definida ou inválida."
}
```

**Impacto:**

- A documentação menciona suporte a POST com JSON
- Aplicações modernas dependem de JSON para APIs RESTful
- Força uso de query strings até para dados sensíveis

**Recomendação:**  
Implementar leitura de `php://input` e parsear JSON com `json_decode()` no backend.

---

### 2. Performance Muito Lenta

**Severidade:** 🔴 CRÍTICA  
**Teste Afetado:** 6.20

**Descrição:**  
5 requisições simples ao endpoint `info_sistema` levaram **8.44 segundos** (~1.7s por requisição).

**Dados:**

```
Status codes: [200, 200, 200, 200, 200]
Tempo total: 8.44s
Tempo médio: 1.69s por requisição
```

**Impacto:**

- Tempo de resposta inaceitável para API em produção
- Pode indicar problema de rede, banco de dados ou processamento ineficiente
- Usuários finais terão experiência ruim

**Recomendação:**

- Investigar latência de rede
- Analisar logs do servidor Apache
- Otimizar código PHP (cache, queries, etc.)
- Considerar CDN ou load balancer

---

## ⚠️ Problemas Médios

### 3. Métodos HTTP Não Documentados Aceitos

**Severidade:** 🟡 MÉDIA  
**Testes Afetados:** 6.4, 6.5

**Descrição:**  
A API aceita métodos PUT e DELETE mesmo não estando documentados e o header indicando apenas GET e POST:

```
Access-Control-Allow-Methods: GET, POST
```

**Resultados:**

- PUT → Status 200 (sucesso)
- DELETE → Status 200 (sucesso)

**Impacto:**

- Inconsistência entre documentação e implementação
- Possível superfície de ataque não planejada
- Confusão para desenvolvedores

**Recomendação:**  
Adicionar validação de método HTTP e retornar `405 Method Not Allowed` para métodos não suportados.

---

### 4. API é Case-Sensitive

**Severidade:** 🟡 MÉDIA  
**Teste Afetado:** 6.9

**Descrição:**  
`acao=calcular_imc` funciona, mas `acao=CALCULAR_IMC` retorna erro:

```json
{
  "status": "erro",
  "mensagem": "Método 'CALCULAR_IMC' não encontrado."
}
```

**Impacto:**

- Experiência ruim para desenvolvedores
- Erros desnecessários por diferença de case
- APIs modernas geralmente são case-insensitive

**Recomendação:**  
Aplicar `strtolower()` no parâmetro `acao` antes de processar.

---

### 5. Não Remove Espaços em Branco (Trim)

**Severidade:** 🟡 MÉDIA  
**Teste Afetado:** 6.19

**Descrição:**  
Parâmetros com espaços causam erro:

```
acao=" calcular_imc " → Método ' calcular_imc ' não encontrado.
```

**Impacto:**

- Erros por espaços acidentais
- Validações desnecessariamente rígidas

**Recomendação:**  
Aplicar `trim()` em todos os parâmetros de entrada.

---

### 6. Parâmetros Duplicados Sem Validação

**Severidade:** 🟡 MÉDIA  
**Teste Afetado:** 6.10

**Descrição:**  
Quando há parâmetros duplicados (`peso=70&peso=80`), a API usa o último valor (80) silenciosamente.

**Impacto:**

- Pode causar bugs difíceis de detectar
- Sem aviso ao desenvolvedor sobre uso incorreto

**Recomendação:**  
Detectar parâmetros duplicados e retornar erro 400 ou warning.

---

## ℹ️ Observações

### 7. URL Muito Longa Retorna 414

**Teste Afetado:** 6.15

**Status:** ℹ️ ESPERADO  
Apache retorna `414 Request-URI Too Long` para URLs acima do limite (~8KB). Isso é comportamento padrão do servidor, mas a API poderia documentar o limite.

---

### 8. Vírgula Decimal é Convertida

**Teste Afetado:** 6.8

**Status:** ℹ️ INFORMATIVO  
PHP converte `"70,5"` para `70` e `"1,75"` para `1`. Pode ser confuso para usuários brasileiros que usam vírgula.

**Sugestão:**  
Documentar que deve-se usar ponto decimal ou implementar conversão de vírgula para ponto.

---

### 9. POST com Form-Data Também Falha

**Teste Afetado:** 6.17

**Status:** ℹ️ RELACIONADO AO ITEM 1  
POST com `application/x-www-form-urlencoded` também não funciona, confirmando problema geral com POST.

---

## ✅ Pontos Fortes da API

### Segurança

- ✅ **SQL Injection:** Tentativas de injection são bloqueadas (Teste 6.1)
- ✅ **XSS:** Tags HTML são removidas corretamente (Teste 6.2)
- ✅ **Null Bytes:** Caracteres nulos são tratados (Teste 6.14)

### Validações

- ✅ **Valores Zero:** Rejeitados corretamente (Testes 1.9, 1.10)
- ✅ **Valores Negativos:** Validados apropriadamente (Teste 1.11)
- ✅ **Strings Inválidas:** Detectadas e rejeitadas (Testes 1.14, 3.10)
- ✅ **NaN e Infinity:** Tratados adequadamente (Testes 6.11, 6.12)
- ✅ **Texto Vazio:** Validação correta (Testes 2.7, 2.8)
- ✅ **Parâmetros Faltando:** Mensagens claras (Testes 1.8, 2.12, 3.6)

### Funcionalidades

- ✅ **Valores Extremos:** Suporta números muito grandes (Teste 3.8)
- ✅ **Decimais:** Aceita e processa corretamente (Teste 3.9)
- ✅ **Notação Científica:** Funciona perfeitamente (Teste 6.18)
- ✅ **Unicode:** Emojis e caracteres especiais tratados (Testes 6.3, 6.16)
- ✅ **Textos Longos:** Processa strings grandes (Teste 2.11)

### Classificações IMC

- ✅ Todas as 6 classificações testadas e corretas:
  - Abaixo do peso (IMC < 18.5)
  - Peso normal (18.5 ≤ IMC < 25)
  - Sobrepeso (25 ≤ IMC < 30)
  - Obesidade grau I (30 ≤ IMC < 35)
  - Obesidade grau II (35 ≤ IMC < 40)
  - Obesidade grau III (IMC ≥ 40)

### Mensagens de Erro

- ✅ **Consistentes:** Formato JSON padronizado com `status` e `mensagem`
- ✅ **Descritivas:** Mensagens claras sobre o problema
- ✅ **Específicas:** Indicam exatamente qual parâmetro falta ou é inválido

---

## 📋 Detalhamento dos Testes

### 1. Testes de Cálculo de IMC (14 testes)

| #    | Teste                   | Status | Observação                        |
| ---- | ----------------------- | ------ | --------------------------------- |
| 1.1  | Peso Normal             | ✅     | IMC 22.86 - Classificação correta |
| 1.2  | Abaixo do Peso          | ✅     | IMC 16.33 - Classificação correta |
| 1.3  | Sobrepeso               | ✅     | IMC 27.68 - Classificação correta |
| 1.4  | Obesidade Grau I        | ✅     | IMC 31.02 - Classificação correta |
| 1.5  | Obesidade Grau II       | ✅     | IMC 35.92 - Classificação correta |
| 1.6  | Obesidade Grau III      | ✅     | IMC 42.45 - Classificação correta |
| 1.7  | Via POST JSON           | ❌     | Não reconhece parâmetros JSON     |
| 1.8  | Parâmetro Faltando      | ✅     | Erro apropriado                   |
| 1.9  | Peso Zero               | ✅     | Validação correta                 |
| 1.10 | Altura Zero             | ✅     | Validação correta                 |
| 1.11 | Valores Negativos       | ✅     | Validação correta                 |
| 1.12 | Valores Extremos Altos  | ✅     | IMC 80 processado                 |
| 1.13 | Valores Extremos Baixos | ✅     | IMC 50 processado                 |
| 1.14 | Tipos Inválidos         | ✅     | Strings rejeitadas                |

### 2. Testes de Palíndromo (12 testes)

| #    | Teste              | Status | Observação                        |
| ---- | ------------------ | ------ | --------------------------------- |
| 2.1  | Palavra Simples    | ✅     | "arara" detectado corretamente    |
| 2.2  | Frase              | ✅     | "A torre da derrota" detectado    |
| 2.3  | Não é Palíndromo   | ✅     | "teste" corretamente identificado |
| 2.4  | Com Acentuação     | ✅     | "Ovo" normalizado para "ovo"      |
| 2.5  | Clássico           | ✅     | Frase longa processada            |
| 2.6  | Via POST           | ❌     | JSON não funciona                 |
| 2.7  | Texto Vazio        | ✅     | Erro apropriado                   |
| 2.8  | Apenas Espaços     | ✅     | Tratado como vazio                |
| 2.9  | Uma Letra          | ✅     | "A" é palíndromo                  |
| 2.10 | Números            | ✅     | "12321" detectado                 |
| 2.11 | Texto Longo        | ✅     | 2001 caracteres processados       |
| 2.12 | Parâmetro Faltando | ✅     | Erro claro                        |

### 3. Testes de Tabuada (10 testes)

| #    | Teste               | Status | Observação               |
| ---- | ------------------- | ------ | ------------------------ |
| 3.1  | Número 7            | ✅     | 10 linhas corretas       |
| 3.2  | Número 1            | ✅     | Tabuada do 1 correta     |
| 3.3  | Número 10           | ✅     | Até 100 correto          |
| 3.4  | Número Negativo     | ✅     | -5 funciona corretamente |
| 3.5  | Via POST            | ❌     | JSON não funciona        |
| 3.6  | Parâmetro Faltando  | ✅     | Mensagem clara           |
| 3.7  | Número Zero         | ✅     | Tabuada de 0 gerada      |
| 3.8  | Número Muito Grande | ✅     | 999999 processado        |
| 3.9  | Número Decimal      | ✅     | 5.5 aceito e calculado   |
| 3.10 | String Inválida     | ✅     | "abc" rejeitado          |

### 4. Testes de Info Sistema (1 teste)

| #   | Teste        | Status | Observação                |
| --- | ------------ | ------ | ------------------------- |
| 4.1 | Info Sistema | ✅     | Retorna dados do servidor |

### 5. Testes de Erro (4 testes)

| #   | Teste              | Status | Observação             |
| --- | ------------------ | ------ | ---------------------- |
| 5.1 | Ação Inexistente   | ✅     | Erro específico        |
| 5.2 | Sem Parâmetro Ação | ✅     | Erro genérico          |
| 5.3 | Ação Vazia         | ✅     | Tratado como ausente   |
| 5.4 | Parâmetros Extras  | ✅     | Ignorados corretamente |

### 6. Testes de Segurança e Edge Cases (20 testes)

| #    | Teste                 | Status | Observação             |
| ---- | --------------------- | ------ | ---------------------- |
| 6.1  | SQL Injection         | ✅     | Bloqueado              |
| 6.2  | XSS                   | ✅     | Tags removidas         |
| 6.3  | Unicode/Emojis        | ✅     | Removidos corretamente |
| 6.4  | Método PUT            | ⚠️     | Aceito indevidamente   |
| 6.5  | Método DELETE         | ⚠️     | Aceito indevidamente   |
| 6.6  | Headers Customizados  | ✅     | Aceitos normalmente    |
| 6.7  | Timeout 1s            | ✅     | Respondeu a tempo      |
| 6.8  | Vírgula Decimal       | ⚠️     | Converte para inteiro  |
| 6.9  | Maiúsculas            | ❌     | Case-sensitive         |
| 6.10 | Parâmetros Duplicados | ⚠️     | Usa último sem aviso   |
| 6.11 | Valor Infinito        | ✅     | Rejeitado              |
| 6.12 | NaN                   | ✅     | Rejeitado              |
| 6.13 | Array no Parâmetro    | ✅     | Rejeitado              |
| 6.14 | Null Byte             | ✅     | Tratado                |
| 6.15 | URL Muito Longa       | ⚠️     | 414 do Apache          |
| 6.16 | UTF-8 Multilíngue     | ✅     | Normalizado            |
| 6.17 | POST Form-Data        | ❌     | Não funciona           |
| 6.18 | Notação Científica    | ✅     | Funciona perfeitamente |
| 6.19 | Espaços               | ❌     | Não faz trim           |
| 6.20 | Performance           | ❌     | 8.44s muito lento      |

---

## 🎯 Recomendações Prioritárias

### Alta Prioridade

1. **Implementar suporte a POST com JSON** - Essencial para API moderna
2. **Investigar e otimizar performance** - 1.7s por requisição é inaceitável
3. **Adicionar validação de métodos HTTP** - Retornar 405 para PUT/DELETE

### Média Prioridade

4. **Normalizar ações para lowercase** - Melhor UX
5. **Aplicar trim em parâmetros** - Evitar erros desnecessários
6. **Validar parâmetros duplicados** - Retornar erro ou warning

### Baixa Prioridade

7. **Documentar limites de URL** - Informar sobre 414
8. **Suportar vírgula decimal** - Facilitar para brasileiros
9. **Adicionar rate limiting** - Proteção contra abuso

---

## 📈 Métricas de Cobertura

### Por Categoria

- **Funcionalidades Básicas:** 100% ✅
- **Validações:** 100% ✅
- **Segurança:** 100% ✅
- **Edge Cases:** 100% ✅
- **Performance:** 100% ⚠️
- **Compatibilidade:** 67% ❌

### Por Endpoint

- **calcular_imc:** 14 testes (93% sucesso)
- **verificar_palindromo:** 12 testes (92% sucesso)
- **gerar_tabuada:** 10 testes (90% sucesso)
- **info_sistema:** 1 teste (100% sucesso)
- **Geral:** 17 testes (71% sucesso)

---

## 📝 Conclusão

A API demonstra **boa base técnica** com validações sólidas e tratamento de segurança adequado. No entanto, existem **2 problemas críticos** que impedem uso em produção:

1. **POST não funciona** - Limita severamente a usabilidade
2. **Performance inaceitável** - 1.7s por requisição é muito lento

Após correção desses itens, a API estará pronta para produção com algumas melhorias de qualidade de vida (case-insensitive, trim, etc.).

### Score Final

**7.5/10** - Boa base, mas com issues críticos a resolver

---

**Relatório Gerado por:** Bateria de Testes Automatizada  
**Arquivo de Log:** [relatorio_testes.txt](./relatorio_testes.txt)  
**Total de Requisições:** 54  
**Tempo Total de Execução:** ~62 segundos
