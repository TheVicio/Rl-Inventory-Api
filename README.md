Para você usar essa Api é necessário:
- Transferir todos os dados do seu inventário para um csv usando o BakkesMod.
- Baixar esse pacote pelo pip.

```
pip install bakkes_mod_inventory
ou
pip install git+https://github.com/gustavopedrosob/bakkes_mod_inventory
```

Essa Api tem como função principal facilitar obtenção de dados específicos de seu inventário de maneira simples,
por exemplo, imagine poder descobrir quantos itens non crate você tem:

```py
import bakkes_mod_inventory
from rocket_league_utils import serie_utils
import rocket_league_utils as rl_utils

inventory = bakkes_mod_inventory.read_inventory()
my_non_crate_filter = filter(lambda item: serie_utils.is_exactly(rl_utils.NON_CRATE, item.serie), inventory)
my_non_crate_items = list(my_non_crate_filter)
amount_of_non_crate = len(my_non_crate_items)
```
Pronto, com apenas 4 linhas de código você conseguiu obter todos os dados dos seus itens non crate e também a quantidade
de itens non-crate que você tem.