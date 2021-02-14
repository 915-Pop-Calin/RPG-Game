from Characters.Character import Character
from Characters.FinalBoss import FinalBoss
from Combat.Combat import Combat
from CombatSystem.LastBossCombat import LastBossCombat
from Items.Armors.Bandage import WornBandage
from Items.Weapons.Words import Words

ceva = Character("Pula", 100, 1000000000000, Words(), WornBandage(), 100000000)
yogg = FinalBoss()
combat = Combat(ceva, yogg)
combat.fight()