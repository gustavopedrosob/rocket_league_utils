# Rocket League Utils
Este é um pacote python com o intuito de facilitar operações com dados de Rocket League.

Por exemplo, imagine que voce tem duas strings que se referem a cor Titanium White, uma é "white" e a outra é "tw", com 
o nosso pacote voce consegue facilmente compara-las:

```py
from rl_data_utils.color import compare_colors

print(compare_colors("tw", "white"))
```
Se executarmos o código de exemplo, o resultado sera:
```
True
```
Com esse pacote voce poderá comparar cores, tipos, raridades e certificados
##Instalação:
```
pip install rocket-league-utils
```