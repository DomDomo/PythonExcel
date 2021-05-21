import json

def compare_with_previous_top():

    print("Comparing with the previous top 50...")

    old_holders = []
    new_holders = []

    with open('old_holders.txt', 'r') as f:
        old_holders = json.loads(f.read())
    with open('holders.txt', 'r') as f:
        new_holders = json.loads(f.read())

    

    num = 1
    for new_holder in new_holders:
        new_address = new_holder["address"]
        for old_holder in old_holders:
            if new_address == old_holder["address"]:
                new_holder["old_quantity"] = old_holder["quantity"]
                num += 1
                break

    with open('holders.txt', 'w') as f:
        f.write(json.dumps(new_holders))
    with open('old_holders.txt', 'w') as f:
        f.write(json.dumps(new_holders))


    new_addresses = [holder["address"] for holder in new_holders]
    old_adresses = [holder["address"] for holder in old_holders]

    new_whale_addresses = list(set(new_addresses) ^ set(old_adresses))
    old_whales = []

    for whale in new_whale_addresses:
        for holder in old_holders:
            if whale == holder["address"]:
                holder["old_quantity"] = holder["quantity"]

                old_whales.append(holder)
    
    print("Done.")





