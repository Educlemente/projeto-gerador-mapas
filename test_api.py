from unittest.mock import patch
from api_clima import obter_temperatura

# O @patch vai "sequestrar" a biblioteca requests apenas durante este teste
@patch('api_clima.requests.get')
def test_obter_temperatura_sucesso(mock_get):
    # 1. Configura a simulação (Mock): fingimos que a API devolveu 28.5 graus
    mock_resposta = mock_get.return_value
    mock_resposta.json.return_value = {
        "current_weather": {"temperature": 28.5}
    }
    
    # 2. Executa a tua função passando coordenadas quaisquer
    resultado = obter_temperatura(-15.78, -47.93)
    
    # 3. Verifica se a função extraiu corretamente o 28.5 do "json" falso
    assert resultado == 28.5
    