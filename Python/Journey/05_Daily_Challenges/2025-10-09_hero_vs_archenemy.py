def park_battle(hero_stats, enemy_stats, park_elements, max_turns):
    """
    Simulates a turn-based battle between a hero and an archenemy in a park.

    Parameters:
        hero_stats (list): [attack, defense, speed, health] for hero
        enemy_stats (list): [attack, defense, speed, health] for enemy
        park_elements (list): elements in the park for special attacks
        max_turns (int): maximum number of turns allowed

    Returns:
        list of strings: battle log for each turn and final result
    """

    battle_log = []  # Log to store actions of each turn
    turn = 0  # Initialize turn counter

    # Function to calculate damage for strong/balanced attacks
    def calculate_damage(attacker, defender):
        """
        Determines damage based on attack vs defense comparison.
        - Strong attack if attacker > defender: 20 damage
        - Balanced attack if attacker == defender: 10 damage
        - Base fallback (used in special move case too): 15
        """
        if attacker[0] > defender[1]:
            return 20
        elif attacker[0] < defender[1]:
            return 15
        else:
            return 10

    # Function to use a special move using a park element
    def use_special_move(attacker, park_elements):
        """
        Uses a park element for a special attack.
        - Rotates the element to the end of the list after use
        - Deals 25 damage
        - If no elements left, fallback to weaker move (5 damage)
        """
        if park_elements:
            element = park_elements[0]  # Pick first available element
            # Rotate used element to the end of the list using slicing + concatenation
            park_elements[:] = park_elements[1:] + [element]
            return f"uses {element} for a special attack", 25
        return "attempts a desperate move", 5

    # Main battle loop: continues until health reaches 0 or max_turns exceeded
    while hero_stats[3] > 0 and enemy_stats[3] > 0 and turn < max_turns:
        turn += 1  # Increment turn counter

        # Determine attacker based on speed stats (higher speed goes first)
        attacker, defender = (hero_stats, enemy_stats) if hero_stats[2] >= enemy_stats[2] else (enemy_stats, hero_stats)
        attacker_name = "Hero" if attacker == hero_stats else "Enemy"
        defender_name = "Enemy" if attacker == hero_stats else "Hero"

        # Determine attack type using game theory logic
        if attacker[0] > defender[1]:
            # Strong attack: attacker's attack > defender's defense
            action = "performs a strong attack"
            damage = calculate_damage(attacker, defender)
        elif attacker[0] < defender[1]:
            # Special move: attacker's attack < defender's defense
            action, damage = use_special_move(attacker, park_elements)
        else:
            # Balanced attack: attacker's attack == defender's defense
            action = "executes a balanced attack"
            damage = calculate_damage(attacker, defender)

        # Apply damage using array slicing and concatenation
        defender[3] = max(0, defender[3] - damage)

        # Log the action of this turn
        battle_log.append(f"Turn {turn}: {attacker_name} {action} dealing {damage} damage. {defender_name} health: {defender[3]}")

        # Swap stats for next turn (attacker and defender switch)
        hero_stats, enemy_stats = defender if attacker == hero_stats else hero_stats, defender if attacker == enemy_stats else enemy_stats

    # Determine final outcome
    if hero_stats[3] > enemy_stats[3]:
        battle_log.append("Hero wins the battle!")
    elif enemy_stats[3] > hero_stats[3]:
        battle_log.append("Enemy wins the battle!")
    else:
        battle_log.append("The battle ends in a draw!")

    return battle_log


# -------------------- EXAMPLE TEST CASE --------------------
hero_stats = [15, 10, 5, 100]
enemy_stats = [10, 15, 5, 100]
park_elements = ["bench", "fountain", "tree", "lamppost"]
max_turns = 10

result = park_battle(hero_stats, enemy_stats, park_elements, max_turns)
for line in result:
    print(line)
