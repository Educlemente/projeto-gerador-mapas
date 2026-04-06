import argparse
import os

import folium
import pandas as pd
from folium.plugins import HeatMap

# REQUISITO DA ATIVIDADE: Versionamento Semântico
__version__ = "1.0.0"


def gerar_mapa(arquivo_entrada, arquivo_saida):
    """Lê os dados e gera o mapa de calor em HTML."""
    if not os.path.exists(arquivo_entrada):
        print(f"❌ ERRO: O arquivo '{arquivo_entrada}' não foi encontrado.")
        return

    print(f"🔄 Lendo dados de '{arquivo_entrada}'...")
    try:
        planilha = pd.read_csv(arquivo_entrada)
    except Exception as e:
        print(f"❌ ERRO ao ler a planilha: {e}")
        return

    # Validação de colunas
    colunas = planilha.columns
    if 'latitude' not in colunas or 'longitude' not in colunas:
        print(
            "❌ ERRO: A planilha deve conter as colunas 'latitude' e "
            "'longitude' escritas em minúsculo."
        )
        return

    # Se não tiver a coluna intensidade, o sistema cria com peso 1
    if 'intensidade' not in planilha.columns:
        planilha['intensidade'] = 1

    centro_lat = planilha['latitude'].mean()
    centro_lon = planilha['longitude'].mean()

    print("🗺️ Gerando o mapa espacial (KDE)...")
    mapa = folium.Map(location=[centro_lat, centro_lon], zoom_start=12)
    coordenadas = planilha[
        ['latitude', 'longitude', 'intensidade']
    ].values.tolist()

    HeatMap(coordenadas, radius=15, blur=5, min_opacity=0.5).add_to(mapa)

    mapa.save(arquivo_saida)
    print(f"✅ SUCESSO! Mapa salvo como '{arquivo_saida}'.")


def main():
    # Configurando a interface de linha de comando (CLI)
    parser = argparse.ArgumentParser(
        description="Gerador de Mapas de Densidade (KDE)."
    )

    parser.add_argument(
        '--entrada',
        required=True,
        help="Caminho para o arquivo CSV com os dados (ex: dados.csv)"
    )
    parser.add_argument(
        '--saida',
        default="mapa_pronto.html",
        help="Nome do arquivo final (ex: mapa_icmbio.html)"
    )
    parser.add_argument(
        '--versao',
        action='version',
        version=f'%(prog)s {__version__}',
        help="Mostra a versão do sistema"
    )

    args = parser.parse_args()
    gerar_mapa(args.entrada, args.saida)


if __name__ == "__main__":
    main()
