import random
class NPS:
   def __init__(self, base_resist, armor_resist, health):
      self.resist = base_resist + armor_resist
      self.fire_resist = random.randrange(0,30)
      self.cold_resist = random.randrange(0,30)
      self.health = health


      isDead = False


      def getDamage(self, damage_d):
         self.health -= damage_d
         if self.health <= 0:
            self.isDead = True
            return damage_d


def damage(NPC, damage_type, base_damage = 0, fire_damage = 0, cold_damage = 0,):
   if damage_type == 0:
      d = (base_damage - NPC.resis) + (fire_damage - NPC.fire_resist) + (cold_damage - NPC.fire_resist)
      return d if d > 0 else 0
   else:
      d =  (fire_damage - NPC.fire_resist) + (cold_damage - NPC.fire_resist)
      return d if d > 0 else 0

oleg = NPS(30,60,190)

while True:
   action = input("Тип урона: ")
   if action.upper() == "Огонь" .upper():
      d = int(input("Количество урона огнём: "))
      df = oleg.getDamage(damage(oleg, 1, 0, d))
      print("Нанесено урона: ", df)
      print("Осталось здоровья:", oleg.health)
      if oleg.health <= 0:
         print("Чел подох")


   elif action.upper() == "Оружие" .upper:
      d = int(input("кол-во урона оружием:"))
      v = int(input("кол во урона холодом"))
      с =






































