import os
import pandas as pd
from gerar_mapa import gerar_mapa

def test_geracao_de_mapa_com_sucesso():
    """Testa se o sistema gera o arquivo HTML corretamente com dados válidos."""
    # 1. Prepara dados falsos para o teste
    df = pd.DataFrame({
        'latitude': [-25.7000], 
        'longitude': [-51.7000], 
        'intensidade': [1]
    })
    df.to_csv('teste_valido.csv', index=False)

    # 2. Roda a nossa função principal
    gerar_mapa('teste_valido.csv', 'mapa_teste.html')

    # 3. Verifica se o mapa nasceu na pasta
    assert os.path.exists('mapa_teste.html') == True

    # 4. Limpa a sujeira do teste
    os.remove('teste_valido.csv')
    os.remove('mapa_teste.html')

def test_erro_coluna_faltando(capsys):
    """Testa se o sistema avisa o usuário quando falta a coluna latitude."""
    # 1. Prepara dados errados (sem latitude)
    df = pd.DataFrame({'longitude': [-51.7000]})
    df.to_csv('teste_invalido.csv', index=False)

    # 2. Roda a função
    gerar_mapa('teste_invalido.csv', 'mapa_erro.html')

    # 3. Captura o que o sistema "printou" na tela e verifica se tem a mensagem de erro
    texto_tela = capsys.readouterr().out
    assert "A planilha deve conter as colunas 'latitude' e 'longitude'" in texto_tela

    # 4. Limpeza
    os.remove('teste_invalido.csv')