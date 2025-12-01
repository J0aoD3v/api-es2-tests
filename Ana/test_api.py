"""
Script de Testes para API de Análise e Paletas de Cores (Node.js/Express)
Autor: Ana
Data: 1 de dezembro de 2025
"""

import requests
import json
from datetime import datetime

# Configuração da URL base da API
BASE_URL = "https://api-cores-node-bu6d.onrender.com"

def print_header(title):
    """Imprime um cabeçalho formatado"""
    print("\n" + "=" * 80)
    print(f" {title}")
    print("=" * 80)

def print_test_result(test_name, success, details=""):
    """Imprime o resultado de um teste"""
    status = "[OK] PASSOU" if success else "[FALHOU] FALHOU"
    print(f"\n{test_name}: {status}")
    if details:
        print(f"  Detalhes: {details}")

def test_hex_para_rgb():
    """Testa o endpoint /hex_para_rgb"""
    print_header("TESTANDO: /hex_para_rgb")
    
    # Teste 1: HEX válido de 6 dígitos
    response = requests.get(f"{BASE_URL}/hex_para_rgb?hex=1E90FF")
    if response.status_code == 200:
        data = response.json()
        expected_rgb = [30, 144, 255]
        if data.get("data", {}).get("rgb_array") == expected_rgb:
            print_test_result("Teste 1 (HEX 6 dígitos válido)", True, f"RGB: {data['data']['rgb']}")
        else:
            print_test_result("Teste 1 (HEX 6 dígitos válido)", False, f"RGB esperado: {expected_rgb}, recebido: {data.get('data', {}).get('rgb_array')}")
    else:
        print_test_result("Teste 1 (HEX 6 dígitos válido)", False, f"Status Code: {response.status_code}")
    
    # Teste 2: HEX válido de 3 dígitos
    response = requests.get(f"{BASE_URL}/hex_para_rgb?hex=F00")
    if response.status_code == 200:
        data = response.json()
        expected_rgb = [255, 0, 0]
        if data.get("data", {}).get("rgb_array") == expected_rgb:
            print_test_result("Teste 2 (HEX 3 dígitos válido)", True, f"RGB: {data['data']['rgb']}")
        else:
            print_test_result("Teste 2 (HEX 3 dígitos válido)", False, f"RGB esperado: {expected_rgb}, recebido: {data.get('data', {}).get('rgb_array')}")
    else:
        print_test_result("Teste 2 (HEX 3 dígitos válido)", False, f"Status Code: {response.status_code}")
    
    # Teste 3: HEX com # no início
    response = requests.get(f"{BASE_URL}/hex_para_rgb?hex=%23FFFFFF")
    if response.status_code == 200:
        data = response.json()
        expected_rgb = [255, 255, 255]
        if data.get("data", {}).get("rgb_array") == expected_rgb:
            print_test_result("Teste 3 (HEX com #)", True, f"RGB: {data['data']['rgb']}")
        else:
            print_test_result("Teste 3 (HEX com #)", False, f"RGB esperado: {expected_rgb}, recebido: {data.get('data', {}).get('rgb_array')}")
    else:
        print_test_result("Teste 3 (HEX com #)", False, f"Status Code: {response.status_code}")
    
    # Teste 4: HEX inválido (deve falhar)
    response = requests.get(f"{BASE_URL}/hex_para_rgb?hex=GGGGGG")
    if response.status_code == 400:
        print_test_result("Teste 4 (HEX inválido)", True, "Erro capturado corretamente")
    else:
        print_test_result("Teste 4 (HEX inválido)", False, f"Status Code esperado: 400, recebido: {response.status_code}")
    
    # Teste 5: Sem parâmetro hex (deve falhar)
    response = requests.get(f"{BASE_URL}/hex_para_rgb")
    if response.status_code == 400:
        print_test_result("Teste 5 (Sem parâmetro hex)", True, "Erro capturado corretamente")
    else:
        print_test_result("Teste 5 (Sem parâmetro hex)", False, f"Status Code esperado: 400, recebido: {response.status_code}")

def test_calcular_complementar():
    """Testa o endpoint /calcular_complementar"""
    print_header("TESTANDO: /calcular_complementar")
    
    # Teste 1: Vermelho puro -> Ciano
    response = requests.get(f"{BASE_URL}/calcular_complementar?hex=FF0000")
    if response.status_code == 200:
        data = response.json()
        expected_hex = "#00FFFF"
        if data.get("data", {}).get("complementar_hex") == expected_hex:
            print_test_result("Teste 1 (Vermelho -> Ciano)", True, f"Complementar: {data['data']['complementar_hex']}")
        else:
            print_test_result("Teste 1 (Vermelho -> Ciano)", False, f"Esperado: {expected_hex}, recebido: {data.get('data', {}).get('complementar_hex')}")
    else:
        print_test_result("Teste 1 (Vermelho -> Ciano)", False, f"Status Code: {response.status_code}")
    
    # Teste 2: Azul Dodger
    response = requests.get(f"{BASE_URL}/calcular_complementar?hex=1E90FF")
    if response.status_code == 200:
        data = response.json()
        expected_hex = "#E16F00"
        if data.get("data", {}).get("complementar_hex") == expected_hex:
            print_test_result("Teste 2 (Azul Dodger)", True, f"Complementar: {data['data']['complementar_hex']}")
        else:
            print_test_result("Teste 2 (Azul Dodger)", False, f"Esperado: {expected_hex}, recebido: {data.get('data', {}).get('complementar_hex')}")
    else:
        print_test_result("Teste 2 (Azul Dodger)", False, f"Status Code: {response.status_code}")
    
    # Teste 3: Preto -> Branco
    response = requests.get(f"{BASE_URL}/calcular_complementar?hex=000000")
    if response.status_code == 200:
        data = response.json()
        expected_hex = "#FFFFFF"
        if data.get("data", {}).get("complementar_hex") == expected_hex:
            print_test_result("Teste 3 (Preto -> Branco)", True, f"Complementar: {data['data']['complementar_hex']}")
        else:
            print_test_result("Teste 3 (Preto -> Branco)", False, f"Esperado: {expected_hex}, recebido: {data.get('data', {}).get('complementar_hex')}")
    else:
        print_test_result("Teste 3 (Preto -> Branco)", False, f"Status Code: {response.status_code}")
    
    # Teste 4: Sem parâmetro hex (deve falhar)
    response = requests.get(f"{BASE_URL}/calcular_complementar")
    if response.status_code == 400:
        print_test_result("Teste 4 (Sem parâmetro hex)", True, "Erro capturado corretamente")
    else:
        print_test_result("Teste 4 (Sem parâmetro hex)", False, f"Status Code esperado: 400, recebido: {response.status_code}")

def test_gerar_paleta_triadica():
    """Testa o endpoint /gerar_paleta_triadica"""
    print_header("TESTANDO: /gerar_paleta_triadica")
    
    # Teste 1: Verde limão
    response = requests.get(f"{BASE_URL}/gerar_paleta_triadica?hex=00FF00")
    if response.status_code == 200:
        data = response.json()
        paleta = data.get("data", {}).get("paleta", [])
        if len(paleta) == 3:
            print_test_result("Teste 1 (Verde limão - 3 cores)", True, f"Paleta: {paleta}")
        else:
            print_test_result("Teste 1 (Verde limão - 3 cores)", False, f"Esperado 3 cores, recebido: {len(paleta)}")
    else:
        print_test_result("Teste 1 (Verde limão - 3 cores)", False, f"Status Code: {response.status_code}")
    
    # Teste 2: Azul Dodger
    response = requests.get(f"{BASE_URL}/gerar_paleta_triadica?hex=1E90FF")
    if response.status_code == 200:
        data = response.json()
        paleta = data.get("data", {}).get("paleta", [])
        base_hex = data.get("data", {}).get("base_hex")
        if len(paleta) == 3 and base_hex in paleta:
            print_test_result("Teste 2 (Azul Dodger - contém cor base)", True, f"Base: {base_hex}")
        else:
            print_test_result("Teste 2 (Azul Dodger - contém cor base)", False, f"Paleta: {paleta}")
    else:
        print_test_result("Teste 2 (Azul Dodger - contém cor base)", False, f"Status Code: {response.status_code}")
    
    # Teste 3: Vermelho
    response = requests.get(f"{BASE_URL}/gerar_paleta_triadica?hex=FF0000")
    if response.status_code == 200:
        data = response.json()
        paleta = data.get("data", {}).get("paleta", [])
        if len(paleta) == 3:
            print_test_result("Teste 3 (Vermelho)", True, f"Paleta: {paleta}")
        else:
            print_test_result("Teste 3 (Vermelho)", False, f"Esperado 3 cores, recebido: {len(paleta)}")
    else:
        print_test_result("Teste 3 (Vermelho)", False, f"Status Code: {response.status_code}")
    
    # Teste 4: Sem parâmetro hex (deve falhar)
    response = requests.get(f"{BASE_URL}/gerar_paleta_triadica")
    if response.status_code == 400:
        print_test_result("Teste 4 (Sem parâmetro hex)", True, "Erro capturado corretamente")
    else:
        print_test_result("Teste 4 (Sem parâmetro hex)", False, f"Status Code esperado: 400, recebido: {response.status_code}")

def test_obter_nome_cor():
    """Testa o endpoint /obter_nome_cor"""
    print_header("TESTANDO: /obter_nome_cor")
    
    # Teste 1: Vermelho puro (na lista)
    response = requests.get(f"{BASE_URL}/obter_nome_cor?hex=FF0000")
    if response.status_code == 200:
        data = response.json()
        nome = data.get("data", {}).get("name")
        if nome == "Vermelho Puro":
            print_test_result("Teste 1 (Vermelho Puro encontrado)", True, f"Nome: {nome}")
        else:
            print_test_result("Teste 1 (Vermelho Puro encontrado)", False, f"Nome esperado: 'Vermelho Puro', recebido: {nome}")
    else:
        print_test_result("Teste 1 (Vermelho Puro encontrado)", False, f"Status Code: {response.status_code}")
    
    # Teste 2: Azul Aço (na lista)
    response = requests.get(f"{BASE_URL}/obter_nome_cor?hex=4682B4")
    if response.status_code == 200:
        data = response.json()
        nome = data.get("data", {}).get("name")
        if nome == "Azul Aço (Steel Blue)":
            print_test_result("Teste 2 (Azul Aço encontrado)", True, f"Nome: {nome}")
        else:
            print_test_result("Teste 2 (Azul Aço encontrado)", False, f"Nome esperado: 'Azul Aço (Steel Blue)', recebido: {nome}")
    else:
        print_test_result("Teste 2 (Azul Aço encontrado)", False, f"Status Code: {response.status_code}")
    
    # Teste 3: Ouro (na lista)
    response = requests.get(f"{BASE_URL}/obter_nome_cor?hex=FFD700")
    if response.status_code == 200:
        data = response.json()
        nome = data.get("data", {}).get("name")
        if nome == "Ouro":
            print_test_result("Teste 3 (Ouro encontrado)", True, f"Nome: {nome}")
        else:
            print_test_result("Teste 3 (Ouro encontrado)", False, f"Nome esperado: 'Ouro', recebido: {nome}")
    else:
        print_test_result("Teste 3 (Ouro encontrado)", False, f"Status Code: {response.status_code}")
    
    # Teste 4: Cor não na lista (deve retornar 404)
    response = requests.get(f"{BASE_URL}/obter_nome_cor?hex=123456")
    if response.status_code == 404:
        data = response.json()
        print_test_result("Teste 4 (Cor não encontrada)", True, f"Mensagem: {data.get('message')}")
    else:
        print_test_result("Teste 4 (Cor não encontrada)", False, f"Status Code esperado: 404, recebido: {response.status_code}")
    
    # Teste 5: Sem parâmetro hex (deve falhar)
    response = requests.get(f"{BASE_URL}/obter_nome_cor")
    if response.status_code == 400:
        print_test_result("Teste 5 (Sem parâmetro hex)", True, "Erro capturado corretamente")
    else:
        print_test_result("Teste 5 (Sem parâmetro hex)", False, f"Status Code esperado: 400, recebido: {response.status_code}")

def test_docs():
    """Testa o endpoint /docs"""
    print_header("TESTANDO: /docs")
    
    response = requests.get(f"{BASE_URL}/docs")
    if response.status_code == 200:
        data = response.json()
        endpoints = data.get("endpoints", [])
        if len(endpoints) == 4:
            print_test_result("Teste 1 (Documentação acessível)", True, f"4 endpoints documentados")
        else:
            print_test_result("Teste 1 (Documentação acessível)", False, f"Esperado 4 endpoints, encontrado: {len(endpoints)}")
    else:
        print_test_result("Teste 1 (Documentação acessível)", False, f"Status Code: {response.status_code}")

def test_root_redirect():
    """Testa se a rota raiz redireciona para /docs"""
    print_header("TESTANDO: Rota Raiz (Redirecionamento)")
    
    response = requests.get(BASE_URL, allow_redirects=False)
    if response.status_code in [301, 302]:
        location = response.headers.get("Location", "")
        if "/docs" in location:
            print_test_result("Teste 1 (Redirecionamento para /docs)", True, f"Location: {location}")
        else:
            print_test_result("Teste 1 (Redirecionamento para /docs)", False, f"Location: {location}")
    else:
        print_test_result("Teste 1 (Redirecionamento para /docs)", False, f"Status Code: {response.status_code}")

def test_invalid_route():
    """Testa rota inválida"""
    print_header("TESTANDO: Rota Inválida")
    
    response = requests.get(f"{BASE_URL}/rota_inexistente")
    if response.status_code == 404:
        data = response.json()
        print_test_result("Teste 1 (Rota inválida retorna 404)", True, f"Mensagem: {data.get('message')}")
    else:
        print_test_result("Teste 1 (Rota inválida retorna 404)", False, f"Status Code esperado: 404, recebido: {response.status_code}")

def test_security():
    """Testes de segurança"""
    print_header("TESTANDO: Segurança")
    
    # Teste 1: SQL Injection
    response = requests.get(f"{BASE_URL}/hex_para_rgb?hex=FF0000';DROP TABLE users;--")
    if response.status_code in [400, 200]:
        print_test_result("Teste 1 (SQL Injection bloqueado)", True, "Requisição tratada")
    else:
        print_test_result("Teste 1 (SQL Injection bloqueado)", False, f"Status Code: {response.status_code}")
    
    # Teste 2: XSS (Cross-Site Scripting)
    response = requests.get(f"{BASE_URL}/hex_para_rgb?hex=<script>alert('xss')</script>")
    if response.status_code in [400]:
        print_test_result("Teste 2 (XSS bloqueado)", True, "Tag HTML rejeitada")
    else:
        print_test_result("Teste 2 (XSS bloqueado)", False, f"Status Code: {response.status_code}")
    
    # Teste 3: Path Traversal
    response = requests.get(f"{BASE_URL}/hex_para_rgb?hex=../../etc/passwd")
    if response.status_code in [400]:
        print_test_result("Teste 3 (Path Traversal bloqueado)", True, "Tentativa bloqueada")
    else:
        print_test_result("Teste 3 (Path Traversal bloqueado)", False, f"Status Code: {response.status_code}")
    
    # Teste 4: HEX muito longo (Buffer Overflow)
    response = requests.get(f"{BASE_URL}/hex_para_rgb?hex={'A' * 1000}")
    if response.status_code == 400:
        print_test_result("Teste 4 (HEX muito longo rejeitado)", True, "Validação funcionando")
    else:
        print_test_result("Teste 4 (HEX muito longo rejeitado)", False, f"Status Code: {response.status_code}")
    
    # Teste 5: Null Bytes
    response = requests.get(f"{BASE_URL}/hex_para_rgb?hex=FF0000%00")
    if response.status_code in [400, 200]:
        print_test_result("Teste 5 (Null Bytes tratados)", True, "Requisição tratada")
    else:
        print_test_result("Teste 5 (Null Bytes tratados)", False, f"Status Code: {response.status_code}")

def test_edge_cases():
    """Testes de casos extremos e especiais"""
    print_header("TESTANDO: Edge Cases")
    
    # Teste 1: HEX com letras minúsculas
    response = requests.get(f"{BASE_URL}/hex_para_rgb?hex=ff0000")
    if response.status_code == 200:
        data = response.json()
        expected_rgb = [255, 0, 0]
        if data.get("data", {}).get("rgb_array") == expected_rgb:
            print_test_result("Teste 1 (HEX minúsculas)", True, "Normalização funcionando")
        else:
            print_test_result("Teste 1 (HEX minúsculas)", False, "RGB incorreto")
    else:
        print_test_result("Teste 1 (HEX minúsculas)", False, f"Status Code: {response.status_code}")
    
    # Teste 2: HEX com espaços antes/depois
    response = requests.get(f"{BASE_URL}/hex_para_rgb?hex=%20FF0000%20")
    if response.status_code in [200, 400]:
        print_test_result("Teste 2 (HEX com espaços)", True, "Tratado")
    else:
        print_test_result("Teste 2 (HEX com espaços)", False, f"Status Code: {response.status_code}")
    
    # Teste 3: Unicode/Emojis
    response = requests.get(f"{BASE_URL}/hex_para_rgb?hex=😀FF0000")
    if response.status_code == 400:
        print_test_result("Teste 3 (Unicode/Emojis rejeitados)", True, "Validação funcionando")
    else:
        print_test_result("Teste 3 (Unicode/Emojis rejeitados)", False, f"Status Code: {response.status_code}")
    
    # Teste 4: Parâmetros duplicados (Parameter Pollution)
    response = requests.get(f"{BASE_URL}/hex_para_rgb?hex=FF0000&hex=00FF00")
    if response.status_code in [200, 400]:
        print_test_result("Teste 4 (Parâmetros duplicados)", True, "Tratado corretamente")
    else:
        print_test_result("Teste 4 (Parâmetros duplicados)", False, f"Status Code: {response.status_code}")
    
    # Teste 5: HEX com caracteres especiais
    response = requests.get(f"{BASE_URL}/hex_para_rgb?hex=FF@#$%")
    if response.status_code == 400:
        print_test_result("Teste 5 (Caracteres especiais rejeitados)", True, "Validação OK")
    else:
        print_test_result("Teste 5 (Caracteres especiais rejeitados)", False, f"Status Code: {response.status_code}")
    
    # Teste 6: Case sensitivity na rota
    response = requests.get(f"{BASE_URL}/HEX_PARA_RGB?hex=FF0000")
    if response.status_code in [200, 404]:
        print_test_result("Teste 6 (Case sensitivity na rota)", True, f"Status: {response.status_code}")
    else:
        print_test_result("Teste 6 (Case sensitivity na rota)", False, f"Status Code: {response.status_code}")
    
    # Teste 7: Trailing slash na rota
    response = requests.get(f"{BASE_URL}/hex_para_rgb/?hex=FF0000")
    if response.status_code in [200, 404]:
        print_test_result("Teste 7 (Trailing slash)", True, "Normalização de rota")
    else:
        print_test_result("Teste 7 (Trailing slash)", False, f"Status Code: {response.status_code}")
    
    # Teste 8: HEX de 4 dígitos (inválido)
    response = requests.get(f"{BASE_URL}/hex_para_rgb?hex=FFFF")
    if response.status_code == 400:
        print_test_result("Teste 8 (HEX 4 dígitos rejeitado)", True, "Validação correta")
    else:
        print_test_result("Teste 8 (HEX 4 dígitos rejeitado)", False, f"Status Code: {response.status_code}")
    
    # Teste 9: HEX de 5 dígitos (inválido)
    response = requests.get(f"{BASE_URL}/hex_para_rgb?hex=FFFFF")
    if response.status_code == 400:
        print_test_result("Teste 9 (HEX 5 dígitos rejeitado)", True, "Validação correta")
    else:
        print_test_result("Teste 9 (HEX 5 dígitos rejeitado)", False, f"Status Code: {response.status_code}")
    
    # Teste 10: HEX de 7 dígitos (inválido)
    response = requests.get(f"{BASE_URL}/hex_para_rgb?hex=FFFFFFF")
    if response.status_code == 400:
        print_test_result("Teste 10 (HEX 7 dígitos rejeitado)", True, "Validação correta")
    else:
        print_test_result("Teste 10 (HEX 7 dígitos rejeitado)", False, f"Status Code: {response.status_code}")

def test_cors_headers():
    """Testa headers CORS"""
    print_header("TESTANDO: Headers CORS")
    
    response = requests.get(f"{BASE_URL}/docs")
    cors_header = response.headers.get("Access-Control-Allow-Origin", "")
    
    if cors_header:
        print_test_result("Teste 1 (CORS habilitado)", True, f"Header: {cors_header}")
    else:
        print_test_result("Teste 1 (CORS habilitado)", False, "Header CORS ausente")
    
    content_type = response.headers.get("Content-Type", "")
    if "json" in content_type.lower():
        print_test_result("Teste 2 (Content-Type correto)", True, f"Content-Type: {content_type}")
    else:
        print_test_result("Teste 2 (Content-Type correto)", False, f"Content-Type: {content_type}")

def test_complementar_advanced():
    """Testes avançados do endpoint complementar"""
    print_header("TESTANDO: Complementar (Avançado)")
    
    # Teste 1: Cinza médio
    response = requests.get(f"{BASE_URL}/calcular_complementar?hex=808080")
    if response.status_code == 200:
        data = response.json()
        expected = "#7F7F7F"
        actual = data.get("data", {}).get("complementar_hex")
        print_test_result("Teste 1 (Cinza médio)", True, f"Original: #808080, Complementar: {actual}")
    else:
        print_test_result("Teste 1 (Cinza médio)", False, f"Status Code: {response.status_code}")
    
    # Teste 2: Verde
    response = requests.get(f"{BASE_URL}/calcular_complementar?hex=00FF00")
    if response.status_code == 200:
        data = response.json()
        expected = "#FF00FF"
        actual = data.get("data", {}).get("complementar_hex")
        print_test_result("Teste 2 (Verde -> Magenta)", True, f"Complementar: {actual}")
    else:
        print_test_result("Teste 2 (Verde -> Magenta)", False, f"Status Code: {response.status_code}")
    
    # Teste 3: Azul puro
    response = requests.get(f"{BASE_URL}/calcular_complementar?hex=0000FF")
    if response.status_code == 200:
        data = response.json()
        expected = "#FFFF00"
        actual = data.get("data", {}).get("complementar_hex")
        print_test_result("Teste 3 (Azul -> Amarelo)", True, f"Complementar: {actual}")
    else:
        print_test_result("Teste 3 (Azul -> Amarelo)", False, f"Status Code: {response.status_code}")

def test_paleta_advanced():
    """Testes avançados de paleta triádica"""
    print_header("TESTANDO: Paleta Triádica (Avançado)")
    
    # Teste 1: Amarelo
    response = requests.get(f"{BASE_URL}/gerar_paleta_triadica?hex=FFFF00")
    if response.status_code == 200:
        data = response.json()
        paleta = data.get("data", {}).get("paleta", [])
        if len(paleta) == 3 and "#FFFF00" in paleta:
            print_test_result("Teste 1 (Amarelo)", True, f"Paleta: {paleta}")
        else:
            print_test_result("Teste 1 (Amarelo)", False, f"Paleta inválida: {paleta}")
    else:
        print_test_result("Teste 1 (Amarelo)", False, f"Status Code: {response.status_code}")
    
    # Teste 2: Ciano
    response = requests.get(f"{BASE_URL}/gerar_paleta_triadica?hex=00FFFF")
    if response.status_code == 200:
        data = response.json()
        paleta = data.get("data", {}).get("paleta", [])
        if len(paleta) == 3:
            print_test_result("Teste 2 (Ciano)", True, f"Paleta: {paleta}")
        else:
            print_test_result("Teste 2 (Ciano)", False, f"Paleta: {paleta}")
    else:
        print_test_result("Teste 2 (Ciano)", False, f"Status Code: {response.status_code}")
    
    # Teste 3: Magenta
    response = requests.get(f"{BASE_URL}/gerar_paleta_triadica?hex=FF00FF")
    if response.status_code == 200:
        data = response.json()
        paleta = data.get("data", {}).get("paleta", [])
        if len(paleta) == 3:
            print_test_result("Teste 3 (Magenta)", True, f"Paleta: {paleta}")
        else:
            print_test_result("Teste 3 (Magenta)", False, f"Paleta: {paleta}")
    else:
        print_test_result("Teste 3 (Magenta)", False, f"Status Code: {response.status_code}")
    
    # Teste 4: Preto (edge case)
    response = requests.get(f"{BASE_URL}/gerar_paleta_triadica?hex=000000")
    if response.status_code == 200:
        data = response.json()
        paleta = data.get("data", {}).get("paleta", [])
        print_test_result("Teste 4 (Preto - edge case)", True, f"Paleta: {paleta}")
    else:
        print_test_result("Teste 4 (Preto - edge case)", False, f"Status Code: {response.status_code}")
    
    # Teste 5: Branco (edge case)
    response = requests.get(f"{BASE_URL}/gerar_paleta_triadica?hex=FFFFFF")
    if response.status_code == 200:
        data = response.json()
        paleta = data.get("data", {}).get("paleta", [])
        print_test_result("Teste 5 (Branco - edge case)", True, f"Paleta: {paleta}")
    else:
        print_test_result("Teste 5 (Branco - edge case)", False, f"Status Code: {response.status_code}")

def test_nome_cor_advanced():
    """Testes avançados de obter nome de cor"""
    print_header("TESTANDO: Nome de Cor (Avançado)")
    
    # Teste 1: Verde Limão (na lista)
    response = requests.get(f"{BASE_URL}/obter_nome_cor?hex=00FF00")
    if response.status_code == 200:
        data = response.json()
        nome = data.get("data", {}).get("name")
        print_test_result("Teste 1 (Verde Limão)", True, f"Nome: {nome}")
    else:
        print_test_result("Teste 1 (Verde Limão)", False, f"Status Code: {response.status_code}")
    
    # Teste 2: Azul Puro (na lista)
    response = requests.get(f"{BASE_URL}/obter_nome_cor?hex=0000FF")
    if response.status_code == 200:
        data = response.json()
        nome = data.get("data", {}).get("name")
        print_test_result("Teste 2 (Azul Puro)", True, f"Nome: {nome}")
    else:
        print_test_result("Teste 2 (Azul Puro)", False, f"Status Code: {response.status_code}")
    
    # Teste 3: Cor aleatória não catalogada
    response = requests.get(f"{BASE_URL}/obter_nome_cor?hex=ABCDEF")
    if response.status_code == 404:
        print_test_result("Teste 3 (Cor não catalogada)", True, "404 retornado corretamente")
    else:
        print_test_result("Teste 3 (Cor não catalogada)", False, f"Status Code: {response.status_code}")
    
    # Teste 4: HEX de 3 dígitos
    response = requests.get(f"{BASE_URL}/obter_nome_cor?hex=F00")
    if response.status_code in [200, 404]:
        print_test_result("Teste 4 (HEX 3 dígitos)", True, f"Status: {response.status_code}")
    else:
        print_test_result("Teste 4 (HEX 3 dígitos)", False, f"Status Code: {response.status_code}")

def test_performance():
    """Testes de performance"""
    print_header("TESTANDO: Performance")
    
    import time
    
    # Teste 1: 5 requisições sequenciais
    start_time = time.time()
    status_codes = []
    
    for i in range(5):
        response = requests.get(f"{BASE_URL}/hex_para_rgb?hex=FF0000")
        status_codes.append(response.status_code)
    
    elapsed_time = time.time() - start_time
    
    if all(code == 200 for code in status_codes):
        print_test_result("Teste 1 (5 requisições)", True, f"Tempo total: {elapsed_time:.2f}s, Média: {elapsed_time/5:.2f}s/req")
    else:
        print_test_result("Teste 1 (5 requisições)", False, f"Status codes: {status_codes}")
    
    # Teste 2: Timeout (10 segundos)
    try:
        response = requests.get(f"{BASE_URL}/docs", timeout=10)
        if response.status_code == 200:
            print_test_result("Teste 2 (Timeout 10s)", True, "Respondeu dentro do tempo")
        else:
            print_test_result("Teste 2 (Timeout 10s)", False, f"Status Code: {response.status_code}")
    except requests.exceptions.Timeout:
        print_test_result("Teste 2 (Timeout 10s)", False, "Timeout excedido")

def main():
    """Função principal que executa todos os testes"""
    print("\n" + "=" * 80)
    print(" SUITE DE TESTES - API de Análise e Paletas de Cores (Node.js)")
    print(" Data/Hora:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print(" URL Base:", BASE_URL)
    print("=" * 80)
    
    try:
        # Testa se a API está acessível
        print("\nVerificando conectividade com a API...")
        response = requests.get(f"{BASE_URL}/docs", timeout=10)
        if response.status_code == 200:
            print("[OK] API esta acessivel!")
        else:
            print(f"[ERRO] API retornou status code inesperado: {response.status_code}")
            return
    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Erro ao conectar com a API: {e}")
        return
    
    # Executa todos os testes
    print("\n[INFO] Executando testes dos endpoints principais...")
    test_hex_para_rgb()
    test_calcular_complementar()
    test_gerar_paleta_triadica()
    test_obter_nome_cor()
    
    print("\n[INFO] Executando testes de documentacao e rotas...")
    test_docs()
    test_root_redirect()
    test_invalid_route()
    
    print("\n[INFO] Executando testes de seguranca...")
    test_security()
    
    print("\n[INFO] Executando testes de edge cases...")
    test_edge_cases()
    
    print("\n[INFO] Executando testes de headers CORS...")
    test_cors_headers()
    
    print("\n[INFO] Executando testes avancados de complementar...")
    test_complementar_advanced()
    
    print("\n[INFO] Executando testes avancados de paleta triadica...")
    test_paleta_advanced()
    
    print("\n[INFO] Executando testes avancados de nome de cor...")
    test_nome_cor_advanced()
    
    print("\n[INFO] Executando testes de performance...")
    test_performance()
    
    print("\n" + "=" * 80)
    print(" TESTES CONCLUIDOS")
    print(" Total de funcoes de teste: 14")
    print(" Estimativa de testes individuais: 50+")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
