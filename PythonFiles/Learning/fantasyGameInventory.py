inventory = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def printInv(inv):
    print('Inventory:')
    total = 0
    for k in inv:
        print(str(inv[k]) + ' ' + k)
        total += inv[k]
    print('Total number of items: ' + str(total))

def addToInv(inv, add):
    for i in add:
        inv.setdefault(i, 0)
        inv[i] += 1

printInv(inventory)
addToInv(inventory, dragonLoot)
printInv(inventory)
