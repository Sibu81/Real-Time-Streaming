import json, time, random, os
from datetime import datetime

output_dir = r"C:\Users\SARTHAK\streaming_orders"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

while True:
    order = {
        "order_id": random.randint(1000, 9999),
        "customer_id": random.randint(100, 999),
        "amount": round(random.uniform(10.0, 500.0), 2),
        "timestamp": datetime.now().isoformat()
    }

    filename = os.path.join(output_dir, f"order_{order['order_id']}.json")
    with open(filename, "w") as f:
        json.dump(order, f)

    print(f"✅ Generated: {order}")
    time.sleep(3)
