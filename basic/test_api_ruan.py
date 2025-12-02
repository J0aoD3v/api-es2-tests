"""
Testes de Caixa Preta para API de Validação de Dados
API desenvolvida por Ruan
URL Base: http://atividadeengenharia2.infinityfree.me
"""

import requests

BASE_URL = "http://atividadeengenharia2.infinityfree.me/API.php"

def test_validar_email_valido():
    """Testa validação de e-mail válido"""
    print("\n=== Testando Validar E-mail (Válido) ===")
    
    response = requests.get(BASE_URL, params={
        "action": "validar_email",
        "email": "teste@dominio.com"
    })
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {data}")
    
    assert response.status_code == 200, "Erro na requisição"
    assert data["acao"] == "validar_email", "Ação incorreta"
    assert data["valido"] == True, "E-mail válido não foi reconhecido"
    assert "mensagem" in data, "Mensagem não retornada"

def test_validar_email_invalido():
    """Testa validação de e-mail inválido"""
    print("\n=== Testando Validar E-mail (Inválido) ===")
    
    response = requests.get(BASE_URL, params={
        "action": "validar_email",
        "email": "teste@dominio"
    })
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {data}")
    
    assert response.status_code == 200, "Erro na requisição"
    assert data["acao"] == "validar_email", "Ação incorreta"
    assert data["valido"] == False, "E-mail inválido foi aceito"

def test_validar_telefone_valido():
    """Testa validação de telefone válido"""
    print("\n=== Testando Validar Telefone (Válido) ===")
    
    response = requests.get(BASE_URL, params={
        "action": "validar_telefone",
        "telefone": "999999999"
    })
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {data}")
    
    assert response.status_code == 200, "Erro na requisição"
    assert data["acao"] == "validar_telefone", "Ação incorreta"
    assert data["valido"] == True, "Telefone válido não foi reconhecido"
    assert "mensagem" in data, "Mensagem não retornada"

def test_validar_telefone_invalido():
    """Testa validação de telefone inválido"""
    print("\n=== Testando Validar Telefone (Inválido) ===")
    
    response = requests.get(BASE_URL, params={
        "action": "validar_telefone",
        "telefone": "123"
    })
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {data}")
    
    assert response.status_code == 200, "Erro na requisição"
    assert data["acao"] == "validar_telefone", "Ação incorreta"
    assert data["valido"] == False, "Telefone inválido foi aceito"

def test_validar_cpf_valido():
    """Testa validação de CPF válido"""
    print("\n=== Testando Validar CPF (Válido) ===")
    
    response = requests.get(BASE_URL, params={
        "action": "validar_cpf",
        "cpf": "12345678909"
    })
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {data}")
    
    assert response.status_code == 200, "Erro na requisição"
    assert data["acao"] == "validar_cpf", "Ação incorreta"
    assert "valido" in data, "Campo valido não retornado"
    assert "mensagem" in data, "Mensagem não retornada"

def test_validar_cpf_invalido():
    """Testa validação de CPF inválido"""
    print("\n=== Testando Validar CPF (Inválido) ===")
    
    response = requests.get(BASE_URL, params={
        "action": "validar_cpf",
        "cpf": "123"
    })
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {data}")
    
    assert response.status_code == 200, "Erro na requisição"
    assert data["acao"] == "validar_cpf", "Ação incorreta"
    assert data["valido"] == False, "CPF inválido foi aceito"

def test_numero_positivo():
    """Testa verificação de número positivo"""
    print("\n=== Testando Número Positivo ===")
    
    response = requests.get(BASE_URL, params={
        "action": "numero_positivo",
        "numero": "5"
    })
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {data}")
    
    assert response.status_code == 200, "Erro na requisição"
    assert data["acao"] == "numero_positivo", "Ação incorreta"
    assert data["valido"] == True, "Número positivo não foi reconhecido"
    assert "mensagem" in data, "Mensagem não retornada"

def test_numero_negativo():
    """Testa verificação de número negativo"""
    print("\n=== Testando Número Negativo ===")
    
    response = requests.get(BASE_URL, params={
        "action": "numero_positivo",
        "numero": "-5"
    })
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {data}")
    
    assert response.status_code == 200, "Erro na requisição"
    assert data["acao"] == "numero_positivo", "Ação incorreta"
    assert data["valido"] == False, "Número negativo foi aceito como positivo"

if __name__ == "__main__":
    print("Iniciando testes da API de Validação (Ruan)...")
    
    try:
        test_validar_email_valido()
        test_validar_email_invalido()
        test_validar_telefone_valido()
        test_validar_telefone_invalido()
        test_validar_cpf_valido()
        test_validar_cpf_invalido()
        test_numero_positivo()
        test_numero_negativo()
        
        print("\n" + "="*50)
        print("[OK] TODOS OS TESTES PASSARAM!")
        print("="*50)
    except AssertionError as e:
        print(f"\n[FALHA] TESTE FALHOU: {e}")
    except Exception as e:
        print(f"\n[ERRO] ERRO: {e}")
