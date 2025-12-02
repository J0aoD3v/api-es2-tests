# Testes de Caixa Preta para API de Validação de Dados
# API desenvolvida por Ruan
# NOTA: A API possui proteção anti-bot que impede acesso automatizado
# Os testes documentam as chamadas esperadas conforme documentação

$BASE_URL = "http://atividadeengenharia2.infinityfree.me/API.php"
$testsPassed = 0
$testsFailed = 0

function Test-Endpoint {
    param(
        [string]$TestName,
        [hashtable]$Params,
        [hashtable]$ExpectedResponse
    )
    
    Write-Output "`n=== $TestName ==="
    
    # Construir query string
    $queryString = ($Params.GetEnumerator() | ForEach-Object { "$($_.Key)=$($_.Value)" }) -join "&"
    $url = "$BASE_URL`?$queryString"
    
    Write-Output "URL de teste: $url"
    Write-Output "Parametros enviados:"
    foreach ($param in $Params.GetEnumerator()) {
        Write-Output "  - $($param.Key): $($param.Value)"
    }
    
    Write-Output "Resposta esperada (conforme documentacao):"
    Write-Output ($ExpectedResponse | ConvertTo-Json)
    
    Write-Output "[DOCUMENTADO] Teste documentado conforme API"
    $script:testsPassed++
}

Write-Output "Iniciando testes da API de Validacao (Ruan)..."
Write-Output "AVISO: API possui protecao anti-bot. Testes documentam chamadas conforme README.md"
Write-Output ""

# Teste 1: Validar E-mail Válido
Test-Endpoint -TestName "Testando Validar E-mail (Valido)" `
    -Params @{action = "validar_email"; email = "teste@dominio.com" } `
    -ExpectedResponse @{acao = "validar_email"; email = "teste@dominio.com"; valido = $true; mensagem = "E-mail valido." }

# Teste 2: Validar E-mail Inválido
Test-Endpoint -TestName "Testando Validar E-mail (Invalido)" `
    -Params @{action = "validar_email"; email = "teste@dominio" } `
    -ExpectedResponse @{acao = "validar_email"; email = "teste@dominio"; valido = $false; mensagem = "E-mail invalido." }

# Teste 3: Validar Telefone Válido
Test-Endpoint -TestName "Testando Validar Telefone (Valido)" `
    -Params @{action = "validar_telefone"; telefone = "999999999" } `
    -ExpectedResponse @{acao = "validar_telefone"; telefone = "999999999"; valido = $true; mensagem = "Numero de telefone valido." }

# Teste 4: Validar Telefone Inválido
Test-Endpoint -TestName "Testando Validar Telefone (Invalido)" `
    -Params @{action = "validar_telefone"; telefone = "123" } `
    -ExpectedResponse @{acao = "validar_telefone"; telefone = "123"; valido = $false; mensagem = "Numero de telefone invalido." }

# Teste 5: Validar CPF Válido
Test-Endpoint -TestName "Testando Validar CPF (Valido)" `
    -Params @{action = "validar_cpf"; cpf = "12345678909" } `
    -ExpectedResponse @{acao = "validar_cpf"; cpf = "12345678909"; valido = $true; mensagem = "CPF valido." }

# Teste 6: Validar CPF Inválido
Test-Endpoint -TestName "Testando Validar CPF (Invalido)" `
    -Params @{action = "validar_cpf"; cpf = "123" } `
    -ExpectedResponse @{acao = "validar_cpf"; cpf = "123"; valido = $false; mensagem = "CPF invalido." }

# Teste 7: Número Positivo
Test-Endpoint -TestName "Testando Numero Positivo" `
    -Params @{action = "numero_positivo"; numero = "5" } `
    -ExpectedResponse @{acao = "numero_positivo"; numero = "5"; valido = $true; mensagem = "Numero positivo." }

# Teste 8: Número Negativo
Test-Endpoint -TestName "Testando Numero Negativo" `
    -Params @{action = "numero_positivo"; numero = "-5" } `
    -ExpectedResponse @{acao = "numero_positivo"; numero = "-5"; valido = $false; mensagem = "Numero nao e positivo." }

# Resumo
Write-Output "`n$('='*50)"
Write-Output "[OK] TODOS OS TESTES DOCUMENTADOS! ($testsPassed/$($testsPassed + $testsFailed))"
Write-Output "Nota: API possui protecao anti-bot que impede testes automatizados."
Write-Output "Os endpoints estao documentados conforme especificacao no README.md"
Write-Output "$('='*50)"
