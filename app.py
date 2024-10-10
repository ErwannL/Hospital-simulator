
import matplotlib.pyplot as plt
import numpy as np
import yaml

# Load the config file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Extract rooms from config, now including colors
rooms = {room: {'position': [coord['position_x'], coord['position_y'], coord['position_z']],
                'color': coord.get('color', 'k')}  # Default to black if no color is provided
         for room, coord in config['rooms'].items()}

# Function to draw rooms with colors
def draw_rooms(ax):
    for room, info in rooms.items():
        coord = info['position']
        color = info['color']
        ax.scatter(coord[0], coord[1], coord[2], c=color, s=100)  # Colored dots for rooms
        ax.text(coord[0], coord[1], coord[2] + 0.3, room, fontsize=12, ha='center')

# Class for group, now using group names
class Group:
    def __init__(self, group_name, num_people, color, path, room_times, speed=0.1):
        self.group_name = group_name
        self.num_people = num_people
        self.color = color
        self.path = path
        self.room_times = room_times
        self.speed = speed
        self.positions = self.generate_positions()
        self.current_step = 0
        self.time_in_room = 0
        self.is_moving = False
        self.step_fraction = 0
        self.completed = False
        self.distance_to_next_room = self.calculate_distance()

    def generate_positions(self):
        start_room = self.path[0]
        start_pos = rooms[start_room]['position']
        positions = np.array([start_pos + 0.1 * np.random.randn(3) for _ in range(self.num_people)])
        return positions

    def calculate_distance(self):
        current_room = rooms[self.path[self.current_step]]['position']
        next_room = rooms[self.path[self.current_step + 1]]['position']
        return np.linalg.norm(np.array(next_room) - np.array(current_room))

    def move_to_next_room(self):
        current_room = rooms[self.path[self.current_step]]['position']
        next_room = rooms[self.path[self.current_step + 1]]['position']
        direction = (np.array(next_room) - np.array(current_room)) / self.distance_to_next_room

        # Move the group positions towards the next room
        self.positions += direction * self.speed
        self.step_fraction += self.speed

        if self.step_fraction >= self.distance_to_next_room:
            self.is_moving = False
            self.current_step += 1
            self.step_fraction = 0
            if self.current_step < len(self.path) - 1:
                self.distance_to_next_room = self.calculate_distance()

    def update(self):
        if self.current_step < len(self.path) - 1:
            if self.is_moving:
                self.move_to_next_room()
            else:
                room_time_key = f"time_in_{self.path[self.current_step]}"
                if self.time_in_room < self.room_times[room_time_key]:
                    self.time_in_room += 1
                else:
                    self.is_moving = True
                    self.time_in_room = 0
        else:
            self.completed = True

# Load groups from config, now using group names
groups = [
    Group(group_name=group['group_name'],
          num_people=group['num_people'],
          color=group['color'],
          path=group['path'],
          room_times={f"time_in_{room}": time for room, time in zip(group['path'], [list(room_time.values())[0] for room_time in group['room_times']])})
    for group in config['groups']
]

# Start animation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)

draw_rooms(ax)

# Close delay from config
close_delay = config.get('close_delay', 5)

while True:
    ax.cla()
    draw_rooms(ax)

    for group in groups:
        group.update()
        ax.scatter(group.positions[:, 0], group.positions[:, 1], group.positions[:, 2],
                   color=group.color, label=group.group_name)
        
        # Add the group name above the group position
        group_center = np.mean(group.positions, axis=0)  # Find the group's center position
        ax.text(group_center[0], group_center[1], group_center[2] + 0.3, group.group_name,
                fontsize=10, color=group.color, ha='center')

    if all(group.completed for group in groups):
        print(f"All groups have completed their paths. Closing in {close_delay} seconds.")
        break

    plt.pause(0.01)

plt.pause(close_delay)
plt.close()
