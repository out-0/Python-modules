def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort magical artifacts"""
    sorted(artifacts, key=lambda artifacts: artifacts.level)


#def power_filter(mages: list[dict], min_power: int) -> list[dict]
#def spell_transformer(spells: list[str]) -> list[str]
#def mage_stats(mages: list[dict]) -> dict

