"""
Bateria de Testes para API RESTful
API Base URL: https://cct.uenp.edu.br/coleti/es2/willian/api.php
"""

import requests
import json
from typing import Dict, Any
from datetime import datetime
import os

# Configuração
API_BASE_URL = "https://cct.uenp.edu.br/coleti/es2/willian/api.php"
REPORT_FILE = "relatorio_testes.txt"

# Variável global para armazenar o conteúdo do relatório
relatorio_content = []

def print_test_header(test_name: str):
    """Imprime cabeçalho do teste"""
    header = "\n" + "="*70 + "\n" + f"TESTE: {test_name}" + "\n" + "="*70
    print(header)
    relatorio_content.append(header)

def print_result(response: requests.Response):
    """Imprime resultado da requisição"""
    result = f"\nStatus Code: {response.status_code}\n"
    result += f"Headers: {dict(response.headers)}\n"
    try:
        result += f"Response JSON:\n{json.dumps(response.json(), indent=2, ensure_ascii=False)}"
    except:
        result += f"Response Text: {response.text}"
    
    print(result)
    relatorio_content.append(result)

def test_calcular_imc():
    """Testa o endpoint de cálculo de IMC"""
    
    # Teste 1: Peso normal
    print_test_header("1.1 - Calcular IMC - Peso Normal")
    params = {
        "acao": "calcular_imc",
        "peso": 70,
        "altura": 1.75
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 2: Abaixo do peso
    print_test_header("1.2 - Calcular IMC - Abaixo do Peso")
    params = {
        "acao": "calcular_imc",
        "peso": 50,
        "altura": 1.75
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 3: Sobrepeso
    print_test_header("1.3 - Calcular IMC - Sobrepeso")
    params = {
        "acao": "calcular_imc",
        "peso": 80,
        "altura": 1.70
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 4: Obesidade grau I
    print_test_header("1.4 - Calcular IMC - Obesidade Grau I")
    params = {
        "acao": "calcular_imc",
        "peso": 95,
        "altura": 1.75
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 5: Obesidade grau II
    print_test_header("1.5 - Calcular IMC - Obesidade Grau II")
    params = {
        "acao": "calcular_imc",
        "peso": 110,
        "altura": 1.75
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 6: Obesidade grau III
    print_test_header("1.6 - Calcular IMC - Obesidade Grau III")
    params = {
        "acao": "calcular_imc",
        "peso": 130,
        "altura": 1.75
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 7: Via POST com JSON
    print_test_header("1.7 - Calcular IMC - Via POST JSON")
    data = {
        "acao": "calcular_imc",
        "peso": 70.5,
        "altura": 1.75
    }
    response = requests.post(API_BASE_URL, json=data)
    print_result(response)
    
    # Teste 8: Parâmetro faltando (erro esperado)
    print_test_header("1.8 - Calcular IMC - Erro: Parâmetro Faltando")
    params = {
        "acao": "calcular_imc",
        "peso": 70
        # altura ausente
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 9: Peso zero
    print_test_header("1.9 - Calcular IMC - Erro: Peso Zero")
    params = {
        "acao": "calcular_imc",
        "peso": 0,
        "altura": 1.75
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 10: Altura zero
    print_test_header("1.10 - Calcular IMC - Erro: Altura Zero")
    params = {
        "acao": "calcular_imc",
        "peso": 70,
        "altura": 0
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 11: Valores negativos
    print_test_header("1.11 - Calcular IMC - Erro: Valores Negativos")
    params = {
        "acao": "calcular_imc",
        "peso": -70,
        "altura": 1.75
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 12: Valores muito altos (extremos)
    print_test_header("1.12 - Calcular IMC - Valores Extremos Altos")
    params = {
        "acao": "calcular_imc",
        "peso": 500,
        "altura": 2.50
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 13: Valores muito baixos (extremos)
    print_test_header("1.13 - Calcular IMC - Valores Extremos Baixos")
    params = {
        "acao": "calcular_imc",
        "peso": 0.5,
        "altura": 0.1
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 14: Tipos inválidos (string)
    print_test_header("1.14 - Calcular IMC - Erro: Tipos Inválidos")
    params = {
        "acao": "calcular_imc",
        "peso": "abc",
        "altura": "xyz"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)

def test_verificar_palindromo():
    """Testa o endpoint de verificação de palíndromo"""
    
    # Teste 1: Palíndromo simples
    print_test_header("2.1 - Verificar Palíndromo - Palavra Simples")
    params = {
        "acao": "verificar_palindromo",
        "texto": "arara"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 2: Palíndromo com frase
    print_test_header("2.2 - Verificar Palíndromo - Frase")
    params = {
        "acao": "verificar_palindromo",
        "texto": "A torre da derrota"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 3: Não é palíndromo
    print_test_header("2.3 - Verificar Palíndromo - Não é Palíndromo")
    params = {
        "acao": "verificar_palindromo",
        "texto": "teste"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 4: Palíndromo com acentuação
    print_test_header("2.4 - Verificar Palíndromo - Com Acentuação")
    params = {
        "acao": "verificar_palindromo",
        "texto": "Ovo"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 5: Palíndromo clássico
    print_test_header("2.5 - Verificar Palíndromo - Clássico")
    params = {
        "acao": "verificar_palindromo",
        "texto": "Socorram-me subi no onibus em Marrocos"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 6: Via POST
    print_test_header("2.6 - Verificar Palíndromo - Via POST")
    data = {
        "acao": "verificar_palindromo",
        "texto": "radar"
    }
    response = requests.post(API_BASE_URL, json=data)
    print_result(response)
    
    # Teste 7: Texto vazio
    print_test_header("2.7 - Verificar Palíndromo - Texto Vazio")
    params = {
        "acao": "verificar_palindromo",
        "texto": ""
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 8: Apenas espaços
    print_test_header("2.8 - Verificar Palíndromo - Apenas Espaços")
    params = {
        "acao": "verificar_palindromo",
        "texto": "     "
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 9: Uma única letra
    print_test_header("2.9 - Verificar Palíndromo - Uma Letra")
    params = {
        "acao": "verificar_palindromo",
        "texto": "A"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 10: Números e caracteres especiais
    print_test_header("2.10 - Verificar Palíndromo - Números e Especiais")
    params = {
        "acao": "verificar_palindromo",
        "texto": "12321"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 11: Texto muito longo
    print_test_header("2.11 - Verificar Palíndromo - Texto Longo")
    params = {
        "acao": "verificar_palindromo",
        "texto": "A" * 1000 + "B" + "A" * 1000
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 12: Parâmetro faltando
    print_test_header("2.12 - Verificar Palíndromo - Erro: Parâmetro Faltando")
    params = {
        "acao": "verificar_palindromo"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)

def test_gerar_tabuada():
    """Testa o endpoint de geração de tabuada"""
    
    # Teste 1: Tabuada do 7
    print_test_header("3.1 - Gerar Tabuada - Número 7")
    params = {
        "acao": "gerar_tabuada",
        "numero": 7
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 2: Tabuada do 1
    print_test_header("3.2 - Gerar Tabuada - Número 1")
    params = {
        "acao": "gerar_tabuada",
        "numero": 1
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 3: Tabuada do 10
    print_test_header("3.3 - Gerar Tabuada - Número 10")
    params = {
        "acao": "gerar_tabuada",
        "numero": 10
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 4: Número negativo
    print_test_header("3.4 - Gerar Tabuada - Número Negativo")
    params = {
        "acao": "gerar_tabuada",
        "numero": -5
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 5: Via POST
    print_test_header("3.5 - Gerar Tabuada - Via POST")
    data = {
        "acao": "gerar_tabuada",
        "numero": 12
    }
    response = requests.post(API_BASE_URL, json=data)
    print_result(response)
    
    # Teste 6: Parâmetro faltando
    print_test_header("3.6 - Gerar Tabuada - Erro: Parâmetro Faltando")
    params = {
        "acao": "gerar_tabuada"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 7: Número zero
    print_test_header("3.7 - Gerar Tabuada - Número Zero")
    params = {
        "acao": "gerar_tabuada",
        "numero": 0
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 8: Número muito grande
    print_test_header("3.8 - Gerar Tabuada - Número Muito Grande")
    params = {
        "acao": "gerar_tabuada",
        "numero": 999999
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 9: Número decimal
    print_test_header("3.9 - Gerar Tabuada - Número Decimal")
    params = {
        "acao": "gerar_tabuada",
        "numero": 5.5
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 10: String ao invés de número
    print_test_header("3.10 - Gerar Tabuada - Erro: String")
    params = {
        "acao": "gerar_tabuada",
        "numero": "abc"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)

def test_info_sistema():
    """Testa o endpoint de informações do sistema"""
    
    print_test_header("4.1 - Info Sistema")
    params = {
        "acao": "info_sistema"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)

def test_seguranca_e_edge_cases():
    """Testa casos de segurança e edge cases"""
    
    # Teste 1: Injeção SQL na ação (teste de segurança)
    print_test_header("6.1 - Segurança - SQL Injection na Ação")
    params = {
        "acao": "calcular_imc' OR '1'='1"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 2: XSS no texto do palíndromo
    print_test_header("6.2 - Segurança - XSS no Texto")
    params = {
        "acao": "verificar_palindromo",
        "texto": "<script>alert('xss')</script>"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 3: Caracteres especiais Unicode
    print_test_header("6.3 - Edge Case - Caracteres Unicode")
    params = {
        "acao": "verificar_palindromo",
        "texto": "😀radar😀"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 4: Requisição com método não suportado (se a API só aceita GET/POST)
    print_test_header("6.4 - Edge Case - Método PUT")
    params = {
        "acao": "info_sistema"
    }
    try:
        response = requests.put(API_BASE_URL, params=params)
        print_result(response)
    except Exception as e:
        print(f"Erro: {str(e)}")
        relatorio_content.append(f"Erro: {str(e)}")
    
    # Teste 5: Requisição com método DELETE
    print_test_header("6.5 - Edge Case - Método DELETE")
    params = {
        "acao": "info_sistema"
    }
    try:
        response = requests.delete(API_BASE_URL, params=params)
        print_result(response)
    except Exception as e:
        print(f"Erro: {str(e)}")
        relatorio_content.append(f"Erro: {str(e)}")
    
    # Teste 6: Headers customizados
    print_test_header("6.6 - Edge Case - Headers Customizados")
    params = {
        "acao": "info_sistema"
    }
    headers = {
        "User-Agent": "TestBot/1.0",
        "X-Custom-Header": "TestValue"
    }
    response = requests.get(API_BASE_URL, params=params, headers=headers)
    print_result(response)
    
    # Teste 7: Timeout (requisição rápida para verificar)
    print_test_header("6.7 - Performance - Timeout de 1 segundo")
    params = {
        "acao": "gerar_tabuada",
        "numero": 999
    }
    try:
        response = requests.get(API_BASE_URL, params=params, timeout=1)
        print_result(response)
    except requests.Timeout:
        msg = "Timeout: A requisição excedeu 1 segundo"
        print(msg)
        relatorio_content.append(msg)
    
    # Teste 8: Vírgula decimal (teste de locale)
    print_test_header("6.8 - Edge Case - Vírgula em Decimal")
    params = {
        "acao": "calcular_imc",
        "peso": "70,5",
        "altura": "1,75"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 9: Case sensitivity da ação
    print_test_header("6.9 - Edge Case - Ação com Maiúsculas")
    params = {
        "acao": "CALCULAR_IMC",
        "peso": 70,
        "altura": 1.75
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 10: Parâmetros duplicados
    print_test_header("6.10 - Edge Case - Parâmetros Duplicados")
    url = f"{API_BASE_URL}?acao=calcular_imc&peso=70&peso=80&altura=1.75"
    response = requests.get(url)
    print_result(response)
    
    # Teste 11: Infinity e valores especiais
    print_test_header("6.11 - Edge Case - Valor Infinito")
    params = {
        "acao": "calcular_imc",
        "peso": "inf",
        "altura": 1.75
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 12: NaN (Not a Number)
    print_test_header("6.12 - Edge Case - NaN")
    params = {
        "acao": "gerar_tabuada",
        "numero": "NaN"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 13: Array como parâmetro
    print_test_header("6.13 - Edge Case - Array no Parâmetro")
    url = f"{API_BASE_URL}?acao=gerar_tabuada&numero[]=7&numero[]=8"
    response = requests.get(url)
    print_result(response)
    
    # Teste 14: Null byte injection
    print_test_header("6.14 - Segurança - Null Byte")
    params = {
        "acao": "verificar_palindromo",
        "texto": "teste\x00injection"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 15: URL muito longa
    print_test_header("6.15 - Edge Case - URL Muito Longa")
    params = {
        "acao": "verificar_palindromo",
        "texto": "A" * 10000
    }
    try:
        response = requests.get(API_BASE_URL, params=params, timeout=5)
        print_result(response)
    except Exception as e:
        msg = f"Erro: {str(e)}"
        print(msg)
        relatorio_content.append(msg)
    
    # Teste 16: Encoding especial (UTF-8)
    print_test_header("6.16 - Edge Case - Caracteres UTF-8 Especiais")
    params = {
        "acao": "verificar_palindromo",
        "texto": "olá mundo 你好 مرحبا"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 17: POST com content-type incorreto
    print_test_header("6.17 - Edge Case - POST com Form Data")
    data = {
        "acao": "calcular_imc",
        "peso": 70,
        "altura": 1.75
    }
    response = requests.post(API_BASE_URL, data=data)
    print_result(response)
    
    # Teste 18: Números científicos
    print_test_header("6.18 - Edge Case - Notação Científica")
    params = {
        "acao": "calcular_imc",
        "peso": "7e1",  # 70
        "altura": "1.75e0"  # 1.75
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 19: Espaços no início/fim dos parâmetros
    print_test_header("6.19 - Edge Case - Espaços nos Parâmetros")
    params = {
        "acao": " calcular_imc ",
        "peso": " 70 ",
        "altura": " 1.75 "
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 20: Múltiplas requisições simultâneas (stress test básico)
    print_test_header("6.20 - Performance - Requisições Simultâneas")
    import time
    start_time = time.time()
    responses = []
    for i in range(5):
        params = {
            "acao": "info_sistema"
        }
        response = requests.get(API_BASE_URL, params=params)
        responses.append(response.status_code)
    end_time = time.time()
    msg = f"\n5 requisições completadas\nStatus codes: {responses}\nTempo total: {end_time - start_time:.2f}s"
    print(msg)
    relatorio_content.append(msg)

def test_erro_acao_invalida():
    """Testa o tratamento de erro para ações inválidas"""
    
    # Teste 1: Ação inexistente
    print_test_header("5.1 - Erro - Ação Inexistente")
    params = {
        "acao": "acao_inexistente"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 2: Sem parâmetro acao
    print_test_header("5.2 - Erro - Sem Parâmetro Ação")
    response = requests.get(API_BASE_URL)
    print_result(response)
    
    # Teste 3: Ação vazia
    print_test_header("5.3 - Erro - Ação Vazia")
    params = {
        "acao": ""
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)
    
    # Teste 4: Múltiplos parâmetros extras
    print_test_header("5.4 - Parâmetros Extras Ignorados")
    params = {
        "acao": "info_sistema",
        "extra1": "valor1",
        "extra2": "valor2"
    }
    response = requests.get(API_BASE_URL, params=params)
    print_result(response)

def save_report():
    """Salva o relatório em arquivo"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write("="*70 + "\n")
        f.write("RELATÓRIO DE TESTES DA API\n")
        f.write(f"Data/Hora: {timestamp}\n")
        f.write(f"URL: {API_BASE_URL}\n")
        f.write("="*70 + "\n")
        
        for content in relatorio_content:
            f.write(content + "\n")
        
        f.write("\n" + "="*70 + "\n")
        f.write("RELATÓRIO FINALIZADO\n")
        f.write("="*70 + "\n")
    
    print(f"\n✓ Relatório salvo em: {os.path.abspath(REPORT_FILE)}")

def run_all_tests():
    """Executa todos os testes"""
    inicio = "\n" + "#"*70 + "\n" + "# INICIANDO BATERIA DE TESTES DA API\n" + "# URL: " + API_BASE_URL + "\n" + "#"*70
    print(inicio)
    relatorio_content.append(inicio)
    
    try:
        # Testes de IMC
        test_calcular_imc()
        
        # Testes de Palíndromo
        test_verificar_palindromo()
        
        # Testes de Tabuada
        test_gerar_tabuada()
        
        # Testes de Info Sistema
        test_info_sistema()
        
        # Testes de Erro
        test_erro_acao_invalida()
        
        # Testes de Segurança e Edge Cases
        test_seguranca_e_edge_cases()
        
        fim = "\n" + "#"*70 + "\n" + "# BATERIA DE TESTES CONCLUÍDA\n" + "#"*70 + "\n"
        print(fim)
        relatorio_content.append(fim)
        
        # Salvar relatório
        save_report()
        
    except Exception as e:
        erro = f"\n\nERRO DURANTE EXECUÇÃO DOS TESTES: {str(e)}"
        print(erro)
        relatorio_content.append(erro)
        import traceback
        traceback.print_exc()
        
        # Salvar relatório mesmo com erro
        save_report()

if __name__ == "__main__":
    run_all_tests()
