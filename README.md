# Rocket League Utils
Este é um pacote python com o intuito de facilitar operações com dados de Rocket League.

## Demonstrações:

### Trabalhando com atributos:
Por exemplo, imagine que voce tem duas strings que se referem a cor Titanium White, uma é ‘white’ e a outra é ‘tw’, com 
o nosso pacote voce consegue facilmente compara-las:

```py
from rl_data_utils.item.color.color import Color

Color("tw").compare("white")
```

Com esse pacote voce poderá comparar cores, tipos, raridades e certificados

### Trabalhando com items:
Com este pacote você pode criar items aleatorios, comparar items, criar items apartir de strings
e muito mais...
```py
from rl_data_utils.item.item.item import Item

# Criando um item aleatorio
random_item = Item.create_random()
# Comparando dois items
result = Item(color='tw').compare(Item(color='white'))
# Criando um item apartir de uma string
item_from_string = Item.from_attribute_string('tw dingo')
```
##Instalação:
```
pip install rocket-league-utils
```
ou
```
pip install git+https://github.com/TheVicio/Rocket-League-Utils
```
## Implementações futuras:

- Suporte a Data Prices.
- Uma função para comparação apenas de atributos indenficadores.
- Site com documentação para o projeto.
- Um readme em inglês.

Caso tenha uma sugestão de implementação, entre em contato.