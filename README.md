# CaptchaPortalRJ
Este projeto esta sendo desenvolvido pois quero realizar webscrapping nos dados do portal de transparencia do governo do rio de janeiro.
("https://www.consultaremuneracao.rj.gov.br/ConsultaRemuneracao")

Para isso eu preciso quebrar um captcha simples feito em base64

Importante que este codigo está sendo desenvolvido em um computador windows, portanto tenha cuidado ao utilizar.

## Requisitos:
from PIL import Image

import pytesseract

import cv2

import numpy as np

Destes o que mais requer atencção é o pytesseract, ele deve ser adicionado ao path do sistema para o funcionamento, contudo eu preferi não realizar

Caso queira seguir pelo mesmo caminho, deve-se atentar a linha:
pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\joao.martinelli\\AppData\\Local\\Programs\\Tesseract-OCR\\Tesseract.exe"

Ponha ali o caminho do .exe, que deve ser baixado do site oficial para computadores em windows.

utilize pip install para instalar as dependencias faltantes.

## Funcionamento
Eu sei que o captcha vai ter 5 caracteres podendo conter numeros e letras da seguinte forma:

![image](https://github.com/joao-martinelli/CaptchaPortalRJ/assets/139559927/a3d1b691-3bd3-4d57-b8b1-c5464fba0c99)

Portanto eu vou trata-lo para que fique mais legivel, realizando a inversão de cores para diminuir o ruido, 
ficando após as transformações com:

![image](https://github.com/joao-martinelli/CaptchaPortalRJ/assets/139559927/13cffded-16b5-4980-8e4e-382c613c353a)

Posso restringir a possibilidade da barra ao final ser reconhecida com o tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVXWYZ1234567890

presente nas configs

Após fazer as transformações, faço a leitura pelo tesseract

## Resultados
Resgatando os resultados, removo os espaços em branco e limito o tamanho a 5 caracteres

Sei que caso o resultado seja menor que 5, sei que esta errado, então posso resetar o captcha e tentar um mais facil, atualmente tenho 50% de chance de sucesso,

contando com os fracassos <5 caracteres, que não vao ser testados no site.

Existem alguns problemas com a letra G e 8 que são reconhecidos como E ou S e 1 que é reconhecido como T penso em toda vez que aparecer um E ou T mandar rodar para tentar outro mais facil

EX:

![image](https://github.com/joao-martinelli/CaptchaPortalRJ/assets/139559927/419bee4c-471c-467c-ab70-6faf5cae793e)
