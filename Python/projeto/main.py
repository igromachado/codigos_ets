Bulbasaur = ({"Nome Pokemon" : 'Bulbasaur',
              "HP": 45,
              "Ataque": 49,
              "Defesa": 49,
              "Velocidade": 45,
              "Tipo": ['Grass', 'Poison'],
              "Ataques": ['Tackle', 'Vine Whip', 'Take Down', 'Toxic']})

Charmander = ({"Nome Pokemon" : 'Charmander',
               "HP": 39,
               "Ataque": 52,
               "Defesa": 43,
               "Velocidade": 65,
               "Tipo": 'Fire',
               "Ataques": ['Tackle', 'Ember', 'Smokescreen', 'Dragon Breath']})

Squirtle = ({"Nome Pokemon" : 'Squirtle',
             "HP": 44,
             "Ataque": 48,
             "Defesa": 65,
             "Velocidade": 43,
             "Tipo": 'Water',
             "Ataques": ['Tackle', 'Water Gun', 'Bite', 'Headbutt']})

def hp_pokemon(level, pokemon_HP_Base):
    formula_hp_lvl = int(((2 * pokemon_HP_Base + 31) * level / 100) + level + 10)
    return formula_hp_lvl

def stats_pokemon(level, pokemon_stat_Base):
    formula_stat_lvl = int(((2 * pokemon_stat_Base + 31) * level / 100) + 5)
    return formula_stat_lvl



def printar_status(status_pokemon,level):

    hp = status_pokemon['HP']
    ataque = status_pokemon['Ataque']
    defesa = status_pokemon['Defesa']
    velocidade = status_pokemon['Velocidade']
    print("-=-="*4, " -STATUS- ", "-=-="*4)
    print(f"HP: {hp_pokemon(level, hp)}")
    print(F"ATQ: {stats_pokemon(level, ataque)}")
    print(F"DEF: {stats_pokemon(level, defesa)}")
    print(F"SPEED: {stats_pokemon(level, velocidade)}")
    return hp, ataque, defesa, velocidade
        


Ataques = ({"Tackle": {"Tipo": 'Normal',
                       "Poder": 40,
                       "Precisão": 100,
                       "PP" : 10,
                       "Descrição": "Ataque físico básico usando o corpo."},

            "Vine Whip": {"Tipo": 'Grass',
                          "Poder": 45,
                          "Precisão": 100,
                          "PP" : 10,
                          "Descrição": 'Bulbasaur chicoteia o oponente com vinhas finas, causando dano do tipo Grama.'},

            "Take Down": {"Tipo": 'Normal',
                          "Poder": 90,
                          "Precisão": 85,
                          "PP" : 5,
                          "Descrição": 'Um ataque físico forte em que o usuário se joga contra o oponente.',
                          "Efeito adicional": 'O usuário sofre recuo (recoil) equivalente a ¼ do dano causado.'},

            "Toxic": {"Tipo": 'Poison',
                      "Poder": None,
                      "Precisão": 90,
                      "PP" : 4,
                      "Descrição": 'Envenena gravemente o alvo. O dano de veneno aumenta a cada turno, tornando-se cada vez mais perigoso.'},

            "Ember": {"Tipo": 'Fire',
                      "Poder": 40,
                      "Precisão": 100,
                      "PP" : 10,
                      "Descrição": 'Charmander dispara pequenas chamas contra o inimigo.',
                      "Efeito adicional": '10% de chance de queimar o alvo.'},

            "Smokescreen": {"Tipo": 'Normal',
                            "Poder": None,
                            "Precisão": 100,
                            "PP" : 6,
                            "Descrição": 'Lança fumaça no oponente, reduzindo sua precisão.'},

            "Dragon Breath": {"Tipo": 'Dragon',
                              "Poder": 60,
                              "Precisão": 100,
                              "PP" : 8,
                              "Descrição": 'Um sopro dracônico que causa dano.',
                              "Efeito adicional": '30% de chance de paralisar o alvo.'},

            "Water Gun": {"Tipo": 'Water',
                          "Poder": 40,
                          "Precisão": 100,
                          "PP" : 10,
                          "Descrição": 'Dispara um jato de água no inimigo.'},
            
            "Bite": {"Tipo": 'Dark',
                     "Poder": 60,
                     "Precisão": 100,
                     "PP" : 8,
                     "Descrição": 'Mordida feroz.',
                     "Efeito adicional": '30% de chance de fazer o alvo recuar (flinch).'},

            "Headbutt": {"Tipo": 'Normal',
                         "Poder": 70,
                         "Precisão": 100,
                         "PP" : 6,
                         "Descrição": 'Golpe de cabeçada.',
                         "Efeito adicional": '30% de chance de flinch.'}
                      })