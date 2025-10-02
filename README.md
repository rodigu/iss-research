# Lightstreamer Reader

Este projeto contém um script Python que captura dados em tempo real da Estação Espacial Internacional (ISS), com foco no **nível do tanque de urina** (`NODE3000005`).

## Funcionalidades

- Captura do valor atual do tanque de urina da ISS a partir da página demo do Lightstreamer (`https://demos.lightstreamer.com/ISSLive/`).  
- Extração apenas do valor relevante, ignorando dados de atualização de taxa ou outras colunas.  
- Exibição das atualizações recebidas em tempo real no console.  
- Tratamento de desconexão segura com `KeyboardInterrupt`.  

## Motivo da mudança da captura dos dados

Inicialmente, o projeto utilizava **conexão direta ao feed Lightstreamer** para capturar telemetria (`NODE3000005`).  
Durante os testes, identificamos algumas limitações:

- O feed direto nem sempre estava disponível de forma estável.  
- Alguns itens de telemetria específicos podiam não aparecer ou ter formatos complicados para leitura direta.  

Para contornar isso, a abordagem foi alterada para **scraping do site demo do Lightstreamer**. Essa solução garante:

- Captura confiável do valor do tanque de urina para fins de estudo.  
- Estabilidade na execução do script, sem depender de endpoints privados ou instáveis.  

> Nota: A captura via scraping é **apenas para fins educacionais**. O feed original da ISS continua sendo público.

## Requisitos

- Python 3.x  
- Biblioteca `selenium` (`pip install selenium webdriver-manager`)  
- Google Chrome instalado (compatível com ChromeDriver)  

## Como executar

1. Instale as dependências:

```bash
pip install selenium webdriver-manager
