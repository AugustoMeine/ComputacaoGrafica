# Computação Gráfica - Sistema Solar

Este projeto é uma simulação gráfica de um sistema solar utilizando Python com as bibliotecas Pygame e PyOpenGL. O objetivo é demonstrar conceitos de computação gráfica, como modelagem, texturização e transformações geométricas.

## Funcionalidades

- Renderização de esferas texturizadas representando o Sol e vários planetas.
- Movimentação da câmera utilizando as teclas W, A, S, D, Q e E.
- Animação contínua dos planetas orbitando ao redor do Sol.

## Requisitos

- Python 3
- Pygame
- PyOpenGL
- NumPy

## Como Executar

1. Certifique-se de ter todos os requisitos instalados.
2. Execute o script `main.py`:
   ```bash
   python main.py
   ```

## Controles

- `W` / `S`: Mover a câmera para cima / baixo.
- `A` / `D`: Mover a câmera para a esquerda / direita.
- `Q` / `E`: Aproximar / afastar a câmera.
- Setas do teclado: Rotacionar a cena.

## Estrutura do Projeto

- `main.py`: Script principal que inicializa a janela, carrega texturas e desenha os objetos.
- `objetos/texturas/`: Diretório contendo as texturas utilizadas para os planetas e o Sol.

## Capturas de Tela

![Sistema Solar](screenshots/sistema_solar.png)

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
