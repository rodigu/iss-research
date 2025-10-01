# Lightstreamer Reader

Este projeto contém um script Python que se conecta a um servidor Lightstreamer para receber dados em tempo real.

## Funcionalidades
- Conexão com o servidor Lightstreamer demo.
- Assinatura de um item específico (`NODE3000005`) e captura de campos (`Value`, `Status`, `TimeStamp`).
- Exibição das atualizações recebidas em tempo real no console.
- Tratamento de desconexão segura com `KeyboardInterrupt`.

## Requisitos
- Python 3.x
- Biblioteca `lightstreamer` (`pip install lightstreamer-client-lib` ou equivalente)
