
import matplotlib.pyplot as plt
import numpy as np
import yaml  # Pour charger le fichier de configuration YAML
import time

# Charger la configuration à partir du fichier config.yaml
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Extraire les pièces (rooms) à partir du fichier de config
rooms = {room: [coord['position_x'], coord['position_y'], coord['position_z']] for room, coord in config['rooms'].items()}

# Fonction pour dessiner les pièces
def draw_rooms(ax):
    for room, coord in rooms.items():
        ax.scatter(coord[0], coord[1], coord[2], c='k', s=100)  # Points noirs pour symboliser une pièce
        ax.text(coord[0], coord[1], coord[2] + 0.3, room, fontsize=12, ha='center')

# Classe pour gérer les groupes
class Group:
    def __init__(self, group_id, num_people, color, path, room_times, travel_times):
        self.group_id = group_id
        self.num_people = num_people
        self.color = color
        self.path = path
        self.room_times = room_times  # Temps passé dans chaque pièce
        self.travel_times = travel_times  # Liste des temps de déplacement
        self.positions = self.generate_positions()
        self.current_step = 0
        self.time_in_room = 0
        self.is_moving = False
        self.step_fraction = 0  # Fraction de la distance à parcourir
        self.completed = False  # Indicateur si le groupe a fini son chemin

    # Génère des positions de départ pour chaque personne dans le groupe
    def generate_positions(self):
        start_room = self.path[0]
        start_pos = rooms[start_room]
        positions = np.array([start_pos + 0.1 * np.random.randn(3) for _ in range(self.num_people)])
        return positions

    # Déplacement fluide du groupe d'une pièce à l'autre
    def move_to_next_room(self):
        current_room = rooms[self.path[self.current_step]]
        next_room = rooms[self.path[self.current_step + 1]]
        travel_time = self.travel_times[self.current_step]  # Temps de déplacement
        self.positions += (np.array(next_room) - np.array(current_room)) / travel_time
        self.step_fraction += 1

        # Si on a atteint la prochaine pièce, on arrête le mouvement
        if self.step_fraction >= travel_time:
            self.is_moving = False
            self.current_step += 1
            self.step_fraction = 0

    # Gérer le temps passé dans les pièces et le déplacement
    def update(self):
        if self.current_step < len(self.path) - 1:  # S'assurer de ne pas dépasser le chemin
            if self.is_moving:
                self.move_to_next_room()
            else:
                if self.time_in_room < self.room_times[self.current_step]:  # Accès direct
                    self.time_in_room += 1
                else:
                    self.is_moving = True
                    self.time_in_room = 0
        else:
            # Si le groupe a terminé son chemin, le marquer comme "complété"
            self.completed = True

# Charger les groupes depuis le fichier de configuration
groups = [
    Group(group_id=group['group_id'],
          num_people=group['num_people'],
          color=group['color'],
          path=group['path'],
          room_times=[list(room_time.values())[0] for room_time in group['room_times']],  # Extraire les temps
          travel_times=[list(travel_time.values())[0] for travel_time in group['travel_times']])  # Extraire les temps de déplacement
    for group in config['groups']
]

# Animation des déplacements
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)

draw_rooms(ax)

# Délai de fermeture configurable depuis le fichier de config
close_delay = config.get('close_delay', 5)  # Par défaut 5 secondes

while True:  # Boucle d'animation continue
    ax.cla()  # Nettoyer l'axe
    draw_rooms(ax)

    # Mettre à jour chaque groupe
    for group in groups:
        group.update()
        ax.scatter(group.positions[:, 0], group.positions[:, 1], group.positions[:, 2],
                   color=group.color, label=f'Group {group.group_id}')

    # Vérifier si tous les groupes ont complété leur parcours
    if all(group.completed for group in groups):
        print(f"Tous les groupes ont terminé leur parcours. Arrêt de l'animation. Fermeture dans {close_delay} secondes.")
        break  # Sortir de la boucle et arrêter l'animation

    plt.pause(0.01)  # Pause très courte pour une animation plus fluide (presque en temps réel)

# Pause pour montrer la fenêtre pendant le délai configuré
plt.pause(close_delay)

# Fermeture de la fenêtre
plt.close()
