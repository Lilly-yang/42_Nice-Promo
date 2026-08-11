import random


ACHIEVEMENTS = {'Crafting Genius', 'Strategist', 'World Savior',
                'Speed Runner', 'Survivor', 'Master Explorer',
                'Treasure Hunter', 'Unstoppable', 'First Steps',
                'Collector Supreme', 'Untouchable', 'Sharp Mind',
                'Boss Slayer'}


def gen_player_achievements() -> set:
    achieve_number = random.randint(1, 12)
    all_achieves = ACHIEVEMENTS
    achieve = set(random.sample(list(all_achieves), achieve_number))
    return achieve


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice_achieve = gen_player_achievements()
    print(f"Player Alice: {alice_achieve}")

    bob_achieve = gen_player_achievements()
    print(f"Player Bob: {bob_achieve}")

    charlie_achieve = gen_player_achievements()
    print(f"Player Charlie: {charlie_achieve}")

    dylan_achieve = gen_player_achievements()
    print(f"Player Dylan: {dylan_achieve}")

    all_achieve = alice_achieve.union(bob_achieve, charlie_achieve,
                                      dylan_achieve)
    print(f"\nAll distinct achievements: {all_achieve}")

    common_achieve = alice_achieve & bob_achieve \
        & charlie_achieve & dylan_achieve
    print(f"\nCommon achievements: {common_achieve}\n")

    alice_only = alice_achieve - bob_achieve - charlie_achieve - dylan_achieve
    bob_only = bob_achieve - alice_achieve - charlie_achieve - dylan_achieve
    charlie_only = charlie_achieve - alice_achieve \
        - bob_achieve - dylan_achieve
    dylan_only = dylan_achieve - alice_achieve - bob_achieve - charlie_achieve
    print(f"Only Alice has: {alice_only}")
    print(f"Only Bob has: {bob_only}")
    print(f"Only Charlie has: {charlie_only}")
    print(f"Only Dylan has: {dylan_only}\n")

    print(f"Alice is missing: {all_achieve - alice_achieve}")
    print(f"Bob is missing: {all_achieve - bob_achieve}")
    print(f"Charlie is missing: {all_achieve - charlie_achieve}")
    print(f"Dylan is missing: {all_achieve - dylan_achieve}")
