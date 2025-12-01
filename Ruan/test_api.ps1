# Script PowerShell para Testar API do Ruan
# API URL: http://atividadeengenharia2.infinityfree.me/API.php

$API_BASE_URL = "http://atividadeengenharia2.infinityfree.me/API.php"
$REPORT_FILE = "relatorio_testes_powershell.txt"
$results = @()

function Write-TestHeader {
    param($testName)
    $header = "`n" + ("=" * 70) + "`nTESTE: $testName`n" + ("=" * 70)
    Write-Host $header -ForegroundColor Cyan
    $script:results += $header
}

function Extract-JsonFromHtml {
    param($htmlContent)
    
    if ($htmlContent -match '<pre>([\s\S]*?)</pre>') {
        $jsonText = $matches[1]
        # Decodificar entidades HTML
        $jsonText = [System.Web.HttpUtility]::HtmlDecode($jsonText)
        return $jsonText
    }
    return $null
}

function Test-APIEndpoint {
    param(
        [string]$TestName,
        [hashtable]$Params
    )
    
    Write-TestHeader $TestName
    
    try {
        # Construir URL com parametros
        $queryString = ($Params.GetEnumerator() | ForEach-Object { "$($_.Key)=$([System.Uri]::EscapeDataString($_.Value))" }) -join '&'
        $url = $API_BASE_URL + '?' + $queryString
        
        Start-Sleep -Milliseconds 300
        
        $response = Invoke-WebRequest -Uri $url -TimeoutSec 15 -ErrorAction Stop
        
        $result = "`nStatus Code: $($response.StatusCode)"
        $result += "`nContent-Type: $($response.Headers['Content-Type'])"
        
        $jsonData = Extract-JsonFromHtml $response.Content
        if ($jsonData) {
            $result += "`nResponse JSON (extraido do HTML):`n$jsonData"
        } else {
            $result += "`nResponse (primeiros 300 chars):`n$($response.Content.Substring(0, [Math]::Min(300, $response.Content.Length)))"
        }
        
        Write-Host $result -ForegroundColor Green
        $script:results += $result
        
    } catch {
        $errorMsg = "`nERRO: $($_.Exception.Message)"
        Write-Host $errorMsg -ForegroundColor Red
        $script:results += $errorMsg
    }
}

# Carregar assembly System.Web para HtmlDecode
Add-Type -AssemblyName System.Web

# Inicio dos testes
$timestamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
$script:results += "`n"
$script:results += "######################################################################`n"
$script:results += "# INICIANDO BATERIA DE TESTES DA API (PowerShell)`n"
$script:results += "# URL: $API_BASE_URL`n"
$script:results += "# Data/Hora: $timestamp`n"
$script:results += "######################################################################`n"

Write-Host "`n######################################################################" -ForegroundColor Yellow
Write-Host "# INICIANDO BATERIA DE TESTES DA API (PowerShell)" -ForegroundColor Yellow
Write-Host "# URL: $API_BASE_URL" -ForegroundColor Yellow
Write-Host "######################################################################`n" -ForegroundColor Yellow

# Testes de Validacao de E-mail
Test-APIEndpoint "1.1 - Validar E-mail - E-mail Valido Simples" @{ action = "validar_email"; email = "teste@dominio.com" }
Test-APIEndpoint "1.2 - Validar E-mail - Com Subdominio" @{ action = "validar_email"; email = "usuario@mail.empresa.com.br" }
Test-APIEndpoint "1.3 - Validar E-mail - Com Numeros" @{ action = "validar_email"; email = "user123@test456.com" }
Test-APIEndpoint "1.4 - Validar E-mail - Caracteres Especiais" @{ action = "validar_email"; email = "user.name+tag@example.com" }
Test-APIEndpoint "1.5 - Validar E-mail - Erro: Sem @" @{ action = "validar_email"; email = "testedominio.com" }
Test-APIEndpoint "1.6 - Validar E-mail - Erro: Sem Dominio" @{ action = "validar_email"; email = "teste@" }
Test-APIEndpoint "1.7 - Validar E-mail - Erro: Sem TLD" @{ action = "validar_email"; email = "teste@dominio" }
Test-APIEndpoint "1.8 - Validar E-mail - Erro: E-mail Vazio" @{ action = "validar_email"; email = "" }
Test-APIEndpoint "1.9 - Validar E-mail - Erro: Com Espacos" @{ action = "validar_email"; email = "teste @dominio.com" }

# Testes de Validacao de Telefone
Test-APIEndpoint "2.1 - Validar Telefone - 9 Digitos Validos" @{ action = "validar_telefone"; telefone = "999999999" }
Test-APIEndpoint "2.2 - Validar Telefone - 11 Digitos (com DDD)" @{ action = "validar_telefone"; telefone = "11999999999" }
Test-APIEndpoint "2.3 - Validar Telefone - 10 Digitos (Fixo)" @{ action = "validar_telefone"; telefone = "1133334444" }
Test-APIEndpoint "2.4 - Validar Telefone - 8 Digitos" @{ action = "validar_telefone"; telefone = "99999999" }
Test-APIEndpoint "2.5 - Validar Telefone - Erro: Menos de 8" @{ action = "validar_telefone"; telefone = "1234567" }
Test-APIEndpoint "2.6 - Validar Telefone - Erro: Mais de 11" @{ action = "validar_telefone"; telefone = "119999999999" }
Test-APIEndpoint "2.7 - Validar Telefone - Erro: Com Letras" @{ action = "validar_telefone"; telefone = "99999abcd" }
Test-APIEndpoint "2.8 - Validar Telefone - Erro: Vazio" @{ action = "validar_telefone"; telefone = "" }
Test-APIEndpoint "2.9 - Validar Telefone - Com Caracteres Especiais" @{ action = "validar_telefone"; telefone = "(11)99999-9999" }

# Testes de Validacao de CPF
Test-APIEndpoint "3.1 - Validar CPF - CPF Valido" @{ action = "validar_cpf"; cpf = "12345678909" }
Test-APIEndpoint "3.2 - Validar CPF - CPF Conhecido Valido" @{ action = "validar_cpf"; cpf = "11144477735" }
Test-APIEndpoint "3.3 - Validar CPF - Com Formatacao" @{ action = "validar_cpf"; cpf = "123.456.789-09" }
Test-APIEndpoint "3.4 - Validar CPF - Erro: Menos de 11 Digitos" @{ action = "validar_cpf"; cpf = "123456789" }
Test-APIEndpoint "3.5 - Validar CPF - Erro: Mais de 11 Digitos" @{ action = "validar_cpf"; cpf = "123456789012" }
Test-APIEndpoint "3.6 - Validar CPF - Erro: Digitos Repetidos (11111111111)" @{ action = "validar_cpf"; cpf = "11111111111" }
Test-APIEndpoint "3.7 - Validar CPF - Erro: Digitos Repetidos (00000000000)" @{ action = "validar_cpf"; cpf = "00000000000" }
Test-APIEndpoint "3.8 - Validar CPF - Erro: Com Letras" @{ action = "validar_cpf"; cpf = "123abc78909" }
Test-APIEndpoint "3.9 - Validar CPF - Erro: Vazio" @{ action = "validar_cpf"; cpf = "" }

# Testes de Numero Positivo
Test-APIEndpoint "4.1 - Numero Positivo - Inteiro Positivo" @{ action = "numero_positivo"; numero = "5" }
Test-APIEndpoint "4.2 - Numero Positivo - Numero Grande" @{ action = "numero_positivo"; numero = "999999" }
Test-APIEndpoint "4.3 - Numero Positivo - Decimal" @{ action = "numero_positivo"; numero = "5.5" }
Test-APIEndpoint "4.4 - Numero Positivo - Zero" @{ action = "numero_positivo"; numero = "0" }
Test-APIEndpoint "4.5 - Numero Positivo - Erro: Negativo" @{ action = "numero_positivo"; numero = "-5" }
Test-APIEndpoint "4.6 - Numero Positivo - Erro: Negativo Decimal" @{ action = "numero_positivo"; numero = "-10.5" }
Test-APIEndpoint "4.7 - Numero Positivo - Erro: String" @{ action = "numero_positivo"; numero = "abc" }
Test-APIEndpoint "4.8 - Numero Positivo - Erro: Vazio" @{ action = "numero_positivo"; numero = "" }

# Testes de Erro
Test-APIEndpoint "5.1 - Erro - Action Inexistente" @{ action = "action_inexistente" }
Test-APIEndpoint "5.2 - Erro - Action Vazia" @{ action = "" }
Test-APIEndpoint "5.3 - Erro - Sem Parametro Action" @{ email = "teste@test.com" }

# Testes de Seguranca e Edge Cases
Test-APIEndpoint "6.1 - Seguranca - SQL Injection no Email" @{ action = "validar_email"; email = "admin' OR '1'='1" }
Test-APIEndpoint "6.2 - Seguranca - XSS no Email" @{ action = "validar_email"; email = "<script>alert('xss')</script>@test.com" }
Test-APIEndpoint "6.3 - Unicode - Emojis no Telefone" @{ action = "validar_telefone"; telefone = "999999😀😀😀" }
Test-APIEndpoint "6.4 - Email - Case Sensitivity" @{ action = "validar_email"; email = "TESTE@DOMINIO.COM" }
Test-APIEndpoint "6.5 - CPF - Todos Zeros Exceto Ultimo" @{ action = "validar_cpf"; cpf = "00000000001" }
Test-APIEndpoint "6.6 - CPF - Digitos Repetidos 22222222222" @{ action = "validar_cpf"; cpf = "22222222222" }
Test-APIEndpoint "6.7 - CPF - Digitos Repetidos 99999999999" @{ action = "validar_cpf"; cpf = "99999999999" }
Test-APIEndpoint "6.8 - Numero - Virgula Decimal" @{ action = "numero_positivo"; numero = "5,5" }
Test-APIEndpoint "6.9 - Action - Case Sensitivity" @{ action = "VALIDAR_EMAIL"; email = "teste@test.com" }
Test-APIEndpoint "6.10 - Email - Muito Longo" @{ action = "validar_email"; email = ("a" * 200) + "@test.com" }
Test-APIEndpoint "6.11 - Telefone - Espacos no Meio" @{ action = "validar_telefone"; telefone = "999 999 999" }
Test-APIEndpoint "6.12 - CPF - Espacos" @{ action = "validar_cpf"; cpf = "111 444 777 35" }
Test-APIEndpoint "6.13 - Numero - String Vazia com Espacos" @{ action = "numero_positivo"; numero = "   " }
Test-APIEndpoint "6.14 - Email - Unicode Multiligue" @{ action = "validar_email"; email = "тест@тест.com" }

# Salvar relatorio
$timestamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
$script:results += "`n"
$script:results += "######################################################################`n"
$script:results += "# BATERIA DE TESTES CONCLUIDA`n"
$script:results += "# Data/Hora: $timestamp`n"
$script:results += "######################################################################`n"
$script:results += "`n"

$script:results | Out-File -FilePath $REPORT_FILE -Encoding UTF8

Write-Host "`n######################################################################" -ForegroundColor Yellow
Write-Host "# BATERIA DE TESTES CONCLUIDA" -ForegroundColor Yellow
Write-Host "######################################################################" -ForegroundColor Yellow
Write-Host "`n[OK] Relatorio salvo em: $(Resolve-Path $REPORT_FILE)" -ForegroundColor Green
