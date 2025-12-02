"""
Testes de Caixa Preta para API de Análise e Paletas de Cores
API desenvolvida por Ana
URL Base: https://api-cores-node-bu6d.onrender.com
"""

import requests

BASE_URL = "https://api-cores-node-bu6d.onrender.com"

def test_docs():
    """Testa o endpoint de documentação"""
    print("\n=== Testando GET /docs ===")
    response = requests.get(f"{BASE_URL}/docs")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200, "Erro ao acessar documentação"

def test_hex_para_rgb():
    """Testa conversão de HEX para RGB"""
    print("\n=== Testando GET /hex_para_rgb ===")
    
    # Teste com cor válida
    response = requests.get(f"{BASE_URL}/hex_para_rgb", params={"hex": "1E90FF"})
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {data}")
    
    assert response.status_code == 200, "Erro na conversão HEX para RGB"
    assert data["success"] == True, "Conversão não foi bem-sucedida"
    assert "data" in data, "Resposta não contém campo 'data'"
    assert data["data"]["hex"] == "#1E90FF", "HEX retornado incorreto"
    assert data["data"]["rgb"] == "30, 144, 255", "RGB retornado incorreto"
    assert data["data"]["rgb_array"] == [30, 144, 255], "RGB array incorreto"

def test_calcular_complementar():
    """Testa cálculo de cor complementar"""
    print("\n=== Testando GET /calcular_complementar ===")
    
    response = requests.get(f"{BASE_URL}/calcular_complementar", params={"hex": "FF0000"})
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {data}")
    
    assert response.status_code == 200, "Erro ao calcular complementar"
    assert data["success"] == True, "Cálculo não foi bem-sucedido"
    assert "data" in data, "Resposta não contém campo 'data'"
    assert data["data"]["original_hex"] == "#FF0000", "HEX original incorreto"
    assert data["data"]["complementar_hex"] == "#00FFFF", "Complementar incorreto"

def test_gerar_paleta_triadica():
    """Testa geração de paleta triádica"""
    print("\n=== Testando GET /gerar_paleta_triadica ===")
    
    response = requests.get(f"{BASE_URL}/gerar_paleta_triadica", params={"hex": "00FF00"})
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {data}")
    
    assert response.status_code == 200, "Erro ao gerar paleta triádica"
    assert data["success"] == True, "Geração não foi bem-sucedida"
    assert "data" in data, "Resposta não contém campo 'data'"
    assert data["data"]["base_hex"] == "#00FF00", "Base HEX incorreta"
    assert len(data["data"]["paleta"]) == 3, "Paleta deve conter 3 cores"

def test_obter_nome_cor():
    """Testa obtenção de nome da cor"""
    print("\n=== Testando GET /obter_nome_cor ===")
    
    response = requests.get(f"{BASE_URL}/obter_nome_cor", params={"hex": "4682B4"})
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {data}")
    
    assert response.status_code == 200, "Erro ao obter nome da cor"
    assert data["success"] == True, "Obtenção não foi bem-sucedida"
    assert "data" in data, "Resposta não contém campo 'data'"
    assert data["data"]["hex"] == "#4682B4", "HEX retornado incorreto"
    assert "name" in data["data"], "Nome da cor não retornado"

if __name__ == "__main__":
    print("Iniciando testes da API de Cores (Ana)...")
    
    try:
        test_docs()
        test_hex_para_rgb()
        test_calcular_complementar()
        test_gerar_paleta_triadica()
        test_obter_nome_cor()
        
        print("\n" + "="*50)
        print("[OK] TODOS OS TESTES PASSARAM!")
        print("="*50)
    except AssertionError as e:
        print(f"\n[FALHA] TESTE FALHOU: {e}")
    except Exception as e:
        print(f"\n[ERRO] ERRO: {e}")
