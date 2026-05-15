import requests

def obter_temperatura(latitude, longitude):
    """
    Vai até a API do Open-Meteo, entrega a latitude e longitude, 
    e devolve a temperatura atual no local.
    """
    # 1. Monta o link exato da API com as coordenadas
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

    try:
        # 2. Faz o pedido na internet
        resposta = requests.get(url)
        
        # 3. Transforma a resposta num dicionário que o Python consegue ler
        dados = resposta.json()
        
        # 4. Entra nos dados e pega apenas o número da temperatura
        temperatura = dados['current_weather']['temperature']
        
        return temperatura
        
    except Exception as erro:
        print(f"Erro ao buscar a temperatura na API: {erro}")
        return None

# --- TESTE RÁPIDO PARA VER SE FUNCIONOU ---
# O código abaixo só roda se você executar este arquivo diretamente
if __name__ == "__main__":
    print("Testando a conexão com a API...")
    lat_teste = -15.78 # Latitude de Brasília
    lon_teste = -47.93 # Longitude de Brasília
    
    temp = obter_temperatura(lat_teste, lon_teste)
    
    if temp is not None:
        print(f"✅ Sucesso! A temperatura na coordenada ({lat_teste}, {lon_teste}) é: {temp}°C")
    else:
        print("❌ Falha ao buscar os dados.")