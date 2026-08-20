def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts,
                  key=lambda artifact: artifact["power"],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda mage: mage["power"])
    min_power = min(mages, key=lambda mage: mage["power"])
    avg_power = sum([mages['power'] for mages in mages]) / len(mages)
    return {'max_power': max_power['power'],
            'min_power': min_power['power'],
            'avg_power': round(avg_power, 2)}


if __name__ == "__main__":
    artifacts = [{'name': 'Storm Crown', 'power': 89, 'type': 'accessory'},
                 {'name': 'Crystal Orb', 'power': 88, 'type': 'relic'},
                 {'name': 'Earth Shield', 'power': 102, 'type': 'focus'},
                 {'name': 'Shadow Blade', 'power': 93, 'type': 'focus'}]
    mages = [{'name': 'Riley', 'power': 89, 'element': 'fire'},
             {'name': 'Sage', 'power': 62, 'element': 'water'},
             {'name': 'Ash', 'power': 63, 'element': 'fire'},
             {'name': 'Luna', 'power': 55, 'element': 'wind'},
             {'name': 'Casey', 'power': 67, 'element': 'ice'}]
    spells = ['freeze', 'shield', 'earthquake', 'heal']

    print("\nTesting artifact sorter...")
    sorted_art = artifact_sorter(artifacts)
    print(f"{sorted_art[0]['name']} ({sorted_art[0]['power']} power) "
          "comes before "
          f"{sorted_art[1]['name']} ({sorted_art[1]['power']} power) ")

    # print("\nTesting power filter...")
    # filted_mag = power_filter(mages, 60)
    # print(f"mage power over 60: \n{filted_mag}")

    print("\nTesting spell transformer...")
    trans_spl = spell_transformer(spells)
    print(f"{' '.join(trans_spl)}")

    # print("\nTesting mage stats")
    # mag_stat = mage_stats(mages)
    # print(f"mage stats: \n{mag_stat}")
