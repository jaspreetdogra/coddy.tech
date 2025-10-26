# Challenge: Sunny Afternoon Picnic Basket Sharing Simulation
# Difficulty: Hard
#
# 🧺 Story / Guided Material:
# You’re spending a sunny afternoon sharing a picnic basket with friends! ☀️
# Each friend takes turns picking items from a shared basket across multiple rounds.
# Everyone wants their favorite snack — something that starts with the first letter
# of their name — but if that’s not available, they’ll just pick the next available
# item alphabetically. Let’s simulate this fair (but slightly greedy) sharing system!
#
# 🧠 Problem Description:
# Create a function named `share_picnic_basket` that receives:
#   - friends (list of str): names of friends attending the picnic.
#   - basket (dict): keys = item names (str), values = quantities (int).
#   - rounds (int): number of rounds of sharing.
#
# ✅ Rules to Implement:
# 1️⃣ In each round, every friend takes one turn in the same order as given.
# 2️⃣ A friend tries to take their favorite item first (starting with the same first letter as their name).
# 3️⃣ If unavailable, they take the alphabetically next available item.
# 4️⃣ If no items are left, they skip that turn.
# 5️⃣ Continue until all rounds are done OR the basket is empty.
#
# 🧮 Output:
# Return a dictionary where:
#   - Keys: friend names
#   - Values: list of items they collected
#
# 🧱 Constraints:
# - 1 ≤ len(friends) ≤ 10
# - 1 ≤ len(basket) ≤ 20
# - 1 ≤ rounds ≤ 100
# - All names and items are lowercase alphabetic strings.
# - Basket quantities are positive integers.
#
# 💡 Hint:
# You’ll need nested loops:
#   - Outer loop → rounds
#   - Inner loop → friends
#   - Inner logic → choosing item from basket
#
# 🧪 Example (not exact input, just conceptual):
# friends = ["alice", "bob", "carol"]
# basket = {"apple": 2, "bread": 1, "banana": 2, "carrot": 1}
# rounds = 3
#
# Expected structure of return value:
# {
#   "alice": ["apple", "apple", ...],
#   "bob": ["banana", "bread", ...],
#   "carol": ["carrot", ...]
# }

def share_picnic_basket(friends, basket, rounds):
    # Initialize the result dictionary with each friend’s name as key and empty list as value
    shared_items = {friend: [] for friend in friends}

    # Loop through each round
    for _ in range(rounds):
        # If basket becomes empty, stop the sharing early
        if not basket:
            break

        # Each friend takes their turn
        for friend in friends:
            if not basket:
                break  # stop if basket is empty mid-round

            favorite_letter = friend[0]  # friend’s favorite item starts with this letter
            chosen_item = None

            # 1️⃣ Try to find favorite item
            for item in sorted(basket.keys()):
                if item.startswith(favorite_letter):
                    chosen_item = item
                    break

            # 2️⃣ If favorite item not available, pick alphabetically smallest available item
            if not chosen_item:
                chosen_item = sorted(basket.keys())[0] if basket else None

            # 3️⃣ Take the chosen item (if exists)
            if chosen_item:
                shared_items[friend].append(chosen_item)
                basket[chosen_item] -= 1

                # If item quantity hits zero, remove it from basket
                if basket[chosen_item] == 0:
                    del basket[chosen_item]

    return shared_items


# 🧪 Example Test:
friends = ["alice", "bob", "carol"]
basket = {"apple": 2, "bread": 1, "banana": 2, "carrot": 1}
rounds = 3

print(share_picnic_basket(friends, basket, rounds))
# Expected Output Example:
# {
#   'alice': ['apple', 'apple'],
#   'bob': ['banana', 'bread'],
#   'carol': ['carrot', 'banana']
# }
