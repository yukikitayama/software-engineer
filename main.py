from enum import Enum
import uuid


class DogSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Dog:
    def __init__(self, uid, size: DogSize):
        self.uid = uid
        self.size = size


class Hotel:
    def __init__(self, small, medium, large):
        # Capacity
        self.small_rooms_count = small
        self.medium_rooms_count = medium
        self.large_rooms_count = large
        # k: Room ID, v: Dog
        self.small_rooms = {}
        self.medium_rooms = {}
        self.large_rooms = {}

    def check_in(self, dog) -> uuid.uuid4:
        """Return room ID"""

        room_id = uuid.uuid4()

        # Small
        if dog.size == DogSize.SMALL and len(self.small_rooms) < self.small_rooms_count:
            self.small_rooms[room_id] = dog

        # Medium
        if dog.size == DogSize.MEDIUM and len(self.medium_rooms) < self.medium_rooms_count:
            self.medium_rooms[room_id] = dog

        # Large
        if dog.size == DogSize.LARGE and len(self.large_rooms) < self.large_rooms_count:
            self.large_rooms[room_id] = dog

        return room_id

    def check_out(self, dog_id, room_id) -> None:

        # Small
        if room_id in self.small_rooms:
            dog = self.small_rooms[room_id]
            if dog.uid == dog_id:
                del self.small_rooms[room_id]

        # Medium
        elif room_id in self.medium_rooms:
            dog = self.medium_rooms[room_id]
            if dog.uid == dog_id:
                del self.medium_rooms[room_id]

        # Large
        elif room_id in self.large_rooms:
            dog = self.large_rooms[room_id]
            if dog.uid == dog_id:
                del self.large_rooms[room_id]

# https://www.davidseek.com/object-oriented-design-amazon
# From the follow up questions