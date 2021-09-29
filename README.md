Para você usar essa Api é necessário você utilizar o BakkesMod para transferir todos os dados do seu inventário para um
csv.

Essa Api tem como função principal facilitar obtenção de dados específicos de seu inventário de maneira simples,
por exemplo, imagine poder descobrir quantos itens non crate você tem:
```py
from inventory import Inventory
# A linha abaixo ira ler os dados do seu inventario presente no csv que você conseguiu com o Bakkesmod e transfoma-lo em
# em um objeto Inventory.
inv = Inventory.read()
my_non_crate_items = inv.filter_non_crate().items
amount_of_non_crate = len(my_non_crate_items)
```
Pronto, com apenas 4 linhas de código você conseguiu obter todos os dados dos seus itens non crate e também a quantidade
de itens non-crate que você tem.