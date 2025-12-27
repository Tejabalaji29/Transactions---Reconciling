import csv

pos_file = "data/pos_transactions.csv"
bank_file = "data/bank_settlements.csv"

pos_data = {}
bank_data = {}

# Read POS data
with open(pos_file, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        pos_data[row['txn_id']] = float(row['amount'])

# Read Bank data
with open(bank_file, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        bank_data[row['txn_id']] = float(row['amount'])

matched = []
amount_mismatch = []
missing_settlement = []

for txn_id, pos_amount in pos_data.items():
    if txn_id in bank_data:
        if pos_amount == bank_data[txn_id]:
            matched.append(txn_id)
        else:
            amount_mismatch.append(txn_id)
    else:
        missing_settlement.append(txn_id)

# Write report
with open("report.txt", "w") as report:
    report.write("TRANSACTION RECONCILIATION REPORT\n")
    report.write("--------------------------------\n\n")
    report.write(f"Matched Transactions: {matched}\n")
    report.write(f"Amount Mismatch: {amount_mismatch}\n")
    report.write(f"Missing Settlements: {missing_settlement}\n")

print("Done! Check report.txt")
