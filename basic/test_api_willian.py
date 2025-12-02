"""
Testes de Caixa Preta para API de Utilitários Matemáticos e Texto
API desenvolvida por Willian
URL Base: http://[SEU_DOMINIO]/api.php
"""

import requests

# NOTA: Substitua pela URL real da API
BASE_URL = "https://cct.uenp.edu.br/coleti/es2/willian/api.php"  # Ajuste conforme necessário

def test_calcular_imc():
    """Testa cálculo de IMC"""
    print("\n=== Testando Calcular IMC ===")
    
    response = requests.get(BASE_URL, params={
        "acao": "calcular_imc",
        "peso": "95",
        "altura": "1.75"
    })
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {data}")
    
    assert response.status_code == 200, "Erro na requisição"
    assert data["status"] == "sucesso", "Status não é sucesso"
    assert "dados" in data, "Campo dados não retornado"
    assert "imc" in data["dados"], "IMC não retornado"
    assert "classificacao" in data["dados"], "Classificação não retornada"
    assert data["dados"]["imc"] == 31.02, "IMC calculado incorretamente"
    assert data["dados"]["classificacao"] == "Obesidade grau I", "Classificação incorreta"

def test_calcular_imc_peso_normal():
    """Testa cálculo de IMC com peso normal"""
    print("\n=== Testando Calcular IMC (Peso Normal) ===")
    
    response = requests.get(BASE_URL, params={
        "acao": "calcular_imc",
        "peso": "70",
        "altura": "1.75"
    })
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {data}")
    
    assert response.status_code == 200, "Erro na requisição"
    assert data["status"] == "sucesso", "Status não é sucesso"
    assert "dados" in data, "Campo dados não retornado"

def test_verificar_palindromo_verdadeiro():
    """Testa verificação de palíndromo verdadeiro"""
    print("\n=== Testando Verificar Palíndromo (Verdadeiro) ===")
    
    response = requests.get(BASE_URL, params={
        "acao": "verificar_palindromo",
        "texto": "A torre da derrota"
    })
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {data}")
    
    assert response.status_code == 200, "Erro na requisição"
    assert data["status"] == "sucesso", "Status não é sucesso"
    assert "dados" in data, "Campo dados não retornado"
    assert data["dados"]["eh_palindromo"] == True, "Palíndromo não foi reconhecido"
    assert "texto_original" in data["dados"], "Texto original não retornado"
    assert "texto_tratado" in data["dados"], "Texto tratado não retornado"

def test_verificar_palindromo_falso():
    """Testa verificação de palíndromo falso"""
    print("\n=== Testando Verificar Palíndromo (Falso) ===")
    
    response = requests.get(BASE_URL, params={
        "acao": "verificar_palindromo",
        "texto": "teste"
    })
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {data}")
    
    assert response.status_code == 200, "Erro na requisição"
    assert data["status"] == "sucesso", "Status não é sucesso"
    assert data["dados"]["eh_palindromo"] == False, "Texto não palíndromo foi aceito"

def test_gerar_tabuada():
    """Testa geração de tabuada"""
    print("\n=== Testando Gerar Tabuada ===")
    
    response = requests.get(BASE_URL, params={
        "acao": "gerar_tabuada",
        "numero": "7"
    })
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {data}")
    
    assert response.status_code == 200, "Erro na requisição"
    assert data["status"] == "sucesso", "Status não é sucesso"
    assert "dados" in data, "Campo dados não retornado"
    assert len(data["dados"]) == 10, "Tabuada deve ter 10 linhas"
    assert "7 x 1 = 7" in data["dados"], "Primeira linha da tabuada incorreta"
    assert "7 x 10 = 70" in data["dados"], "Última linha da tabuada incorreta"

def test_info_sistema():
    """Testa informações do sistema"""
    print("\n=== Testando Info Sistema ===")
    
    response = requests.get(BASE_URL, params={
        "acao": "info_sistema"
    })
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {data}")
    
    assert response.status_code == 200, "Erro na requisição"
    assert data["status"] == "sucesso", "Status não é sucesso"
    assert "dados" in data, "Campo dados não retornado"
    assert "data_hora" in data["dados"], "Data/hora não retornada"
    assert "versao_php" in data["dados"], "Versão PHP não retornada"
    assert "servidor" in data["dados"], "Servidor não retornado"

def test_acao_invalida():
    """Testa ação inválida"""
    print("\n=== Testando Ação Inválida ===")
    
    response = requests.get(BASE_URL, params={
        "acao": "acao_inexistente"
    })
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {data}")
    
    assert response.status_code == 200, "Erro na requisição"
    assert data["status"] == "erro", "Status deveria ser erro"
    assert "mensagem" in data, "Mensagem de erro não retornada"

if __name__ == "__main__":
    print("Iniciando testes da API de Utilitarios (Willian)...")
    print("\n[AVISO] ATENCAO: Certifique-se de configurar a BASE_URL correta!")
    
    try:
        test_calcular_imc()
        test_calcular_imc_peso_normal()
        test_verificar_palindromo_verdadeiro()
        test_verificar_palindromo_falso()
        test_gerar_tabuada()
        test_info_sistema()
        test_acao_invalida()
        
        print("\n" + "="*50)
        print("[OK] TODOS OS TESTES PASSARAM!")
        print("="*50)
    except AssertionError as e:
        print(f"\n[FALHA] TESTE FALHOU: {e}")
    except Exception as e:
        print(f"\n[ERRO] ERRO: {e}")
