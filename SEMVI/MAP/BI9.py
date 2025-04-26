import csv
from itertools import combinations
from collections import defaultdict

def load_transactions_from_csv(filename):
    transactions = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            items = row[2:]  # Skip Order ID and Price
            cleaned_items = [item.strip() for item in items if item.strip()]
            if cleaned_items:
                transactions.append(cleaned_items)
    return transactions

def get_item_support(transactions, itemsets):
    item_support = defaultdict(int)
    for transaction in transactions:
        transaction_set = set(transaction)
        for itemset in itemsets:
            if set(itemset).issubset(transaction_set):
                item_support[itemset] += 1
    return item_support

def apriori(transactions, min_support):
    num_transactions = len(transactions)
    min_count = min_support * num_transactions

    # Frequent 1-itemsets
    item_counts = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            item_counts[(item,)] += 1

    current_itemsets = {itemset for itemset, count in item_counts.items() if count >= min_count}
    frequent_itemsets = dict()
    k = 1

    while current_itemsets:
        item_support = get_item_support(transactions, current_itemsets)
        frequent_itemsets.update({itemset: count for itemset, count in item_support.items() if count >= min_count})
        
        items = sorted(set(item for itemset in current_itemsets for item in itemset))
        next_itemsets = set(combinations(items, k + 1))

        current_itemsets = {itemset for itemset in next_itemsets
                            if get_item_support(transactions, [itemset])[itemset] >= min_count}
        k += 1

    return frequent_itemsets

# Main execution
if __name__ == "__main__":
    filename = "C:/Users/riyai/Downloads/resturant_trans.csv"  # Make sure the file is in the same directory
    min_support = 0.2  # Set your desired minimum support

    transactions = load_transactions_from_csv(filename)
    frequent_itemsets = apriori(transactions, min_support)

    print("Top 10 frequent itemsets:")
    for itemset, count in sorted(frequent_itemsets.items(), key=lambda x: -x[1])[:10]:
        print(f"{itemset}: {count}")

