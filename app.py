
import matplotlib.pyplot as plt
import numpy as np
import yaml
import time

# Load the config file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Extract rooms from config
rooms = {room: [coord['position_x'], coord['position_y'], coord['position_z']] for room, coord in config['rooms'].items()}

# Function to draw rooms
def draw_rooms(ax):
    for room, coord in rooms.items():
        ax.scatter(coord[0], coord[1], coord[2], c='k', s=100)  # Black dots for rooms
        ax.text(coord[0], coord[1], coord[2] + 0.3, room, fontsize=12, ha='center')

# Class for group
class Group:
    def __init__(self, group_id, num_people, color, path, room_times, speed=0.1):
        self.group_id = group_id
        self.num_people = num_people
        self.color = color
        self.path = path
        self.room_times = room_times  # Time spent in each room
        self.speed = speed  # Constant speed for moving between rooms
        self.positions = self.generate_positions()
        self.current_step = 0
        self.time_in_room = 0
        self.is_moving = False
        self.step_fraction = 0
        self.completed = False
        self.distance_to_next_room = self.calculate_distance()

    def generate_positions(self):
        start_room = self.path[0]
        start_pos = rooms[start_room]
        positions = np.array([start_pos + 0.1 * np.random.randn(3) for _ in range(self.num_people)])
        return positions

    def calculate_distance(self):
        """Calculate the distance between the current room and the next room."""
        current_room = rooms[self.path[self.current_step]]
        next_room = rooms[self.path[self.current_step + 1]]
        distance = np.linalg.norm(np.array(next_room) - np.array(current_room))
        return distance

    def move_to_next_room(self):
        """Move the group towards the next room at a constant speed."""
        current_room = rooms[self.path[self.current_step]]
        next_room = rooms[self.path[self.current_step + 1]]
        direction = (np.array(next_room) - np.array(current_room)) / self.distance_to_next_room

        # Move the group positions towards the next room
        self.positions += direction * self.speed
        self.step_fraction += self.speed

        if self.step_fraction >= self.distance_to_next_room:  # If the group reached the next room
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

# Load groups from config
groups = [
    Group(group_id=group['group_id'],
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
                   color=group.color, label=f'Group {group.group_id}')

    if all(group.completed for group in groups):
        print(f"All groups have completed their paths. Closing in {close_delay} seconds.")
        break

    plt.pause(0.01)

# Wait before closing the plot
plt.pause(close_delay)
plt.close()
