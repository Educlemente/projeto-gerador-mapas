# 🗺️ Gerador de Mapas de Densidade (KDE) para Análise Espacial

## 🛑 Descrição do Problema Real
A gestão e proteção de recursos hídricos, como nascentes e bacias hidrográficas, é um desafio constante para órgãos de conservação ambiental (ex: ICMBio). Muitas vezes, os analistas possuem planilhas com milhares de coordenadas de ocorrências, mas perdem horas configurando softwares pesados de SIG (Sistemas de Informação Geográfica) apenas para visualizar a concentração espacial (clusters) desses dados para uma tomada de decisão rápida.

## 💡 Proposta da Solução
Esta aplicação automatiza a geração de mapas de calor focados em Densidade de Kernel (KDE) para dados discretos. Através de uma Interface de Linha de Comando (CLI), o usuário insere uma planilha bruta e o sistema retorna instantaneamente um mapa interativo em HTML, focado na concentração real dos fenômenos espaciais, poupando tempo operacional.

## 🎯 Público-Alvo
- Analistas Ambientais e Fiscais (ICMBio, IBAMA).
- Engenheiros Florestais e Gestores de Unidades de Conservação.
- Pesquisadores de Planejamento Territorial.

## ⚙️ Funcionalidades Principais
- Leitura automatizada de coordenadas espaciais via CSV.
- Centralização inteligente do mapa baseada na média dos dados.
- Geração de modelo KDE (Kernel Density Estimation) próprio para dados discretos.
- Output em HTML interativo com renderização rápida.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.10+
- **Bibliotecas Base:** `pandas` (manipulação de dados) e `folium` (renderização espacial).
- **Testes e Qualidade:** `pytest` e `flake8`.

## 🚀 Instruções de Instalação
1. Clone este repositório:
   `git clone [COLOQUE O LINK DO SEU GITHUB AQUI]`
2. Acesse a pasta do projeto:
   `cd projeto-gerador-mapas`
3. Instale as dependências:
   `pip install -r requirements.txt`

## ▶️ Instruções de Execução
Para gerar um mapa, execute o comando via terminal apontando para a sua base de dados:
`python gerar_mapa.py --entrada dados.csv --saida mapa_pronto.html`

## 🧪 Instruções para rodar os Testes
Este projeto possui testes automatizados. Para executá-los, digite no terminal:
`pytest tests/`

## 🧹 Instruções para rodar o Lint (Qualidade de Código)
Para verificar a formatação do código segundo as normas PEP8:
`flake8 gerar_mapa.py`

---
**Versão Atual:** 1.0.0 (MAJOR.MINOR.PATCH)
**Autor:** Eduardo Clemenete
**Link do Repositório Público:** https://github.com/Educlemente/projeto-gerador-mapas