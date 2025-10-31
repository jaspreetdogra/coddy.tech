def manage_hotel_checkin(hotel_rooms, new_guests, checkout_guests, max_guests_per_room):
    """
    Advanced Hotel Check-in System 🏨
    Handles guest arrivals, checkouts, VIP upgrades, and waiting list management.
    """

    # --------------------------------------------------------
    # Helper Functions
    # --------------------------------------------------------

    # Check if a room is empty (room number string)
    def is_room_available(room):
        return isinstance(room, str) and room.isdigit()

    # Check if a room (guest list) has space for more guests
    def room_has_space(room):
        return isinstance(room, list) and len(room) < max_guests_per_room

    # Find the next available room (lowest floor, lowest room index)
    def find_available_room():
        for floor_idx, floor in enumerate(hotel_rooms):
            for room_idx, room in enumerate(floor):
                if is_room_available(room) or room_has_space(room):
                    return floor_idx, room_idx
        return None

    # --------------------------------------------------------
    # Step 1: Handle Checkouts
    # --------------------------------------------------------
    for guest in checkout_guests:
        for floor in hotel_rooms:
            for i, room in enumerate(floor):
                # If guest is in a shared room (list)
                if isinstance(room, list) and guest in room:
                    room.remove(guest)
                    if len(room) == 0:  # If empty after checkout → mark room vacant
                        floor[i] = str(i + 1).zfill(3)
                # If guest occupied a solo room (direct string)
                elif room == guest:
                    floor[i] = str(i + 1).zfill(3)

    # --------------------------------------------------------
    # Step 2: Initialize Check-in Lists
    # --------------------------------------------------------
    checked_in_guests = []
    waiting_list = []
    upgraded_vips = []

    # --------------------------------------------------------
    # Step 3: Handle Check-ins
    # --------------------------------------------------------
    for guest in new_guests:
        is_vip = guest.startswith("VIP_")
        room_found = find_available_room()

        if room_found:
            floor_idx, room_idx = room_found
            room = hotel_rooms[floor_idx][room_idx]

            # Case 1: Room number → create new list with guest
            if is_room_available(room):
                hotel_rooms[floor_idx][room_idx] = [guest]

            # Case 2: Room already partially occupied → append guest
            else:
                hotel_rooms[floor_idx][room_idx].append(guest)

            checked_in_guests.append(guest)

            # --------------------------------------------------------
            # Step 4: Handle VIP Room Upgrades (move to higher floor)
            # --------------------------------------------------------
            if is_vip:
                for upgrade_floor_idx in range(floor_idx + 1, len(hotel_rooms)):
                    upgrade_room = find_available_room()
                    if upgrade_room and upgrade_room[0] > floor_idx:
                        # Remove from old room
                        hotel_rooms[floor_idx][room_idx].remove(guest)
                        if len(hotel_rooms[floor_idx][room_idx]) == 0:
                            hotel_rooms[floor_idx][room_idx] = str(room_idx + 1).zfill(3)

                        # Move to upgraded room
                        new_floor, new_room = upgrade_room
                        if is_room_available(hotel_rooms[new_floor][new_room]):
                            hotel_rooms[new_floor][new_room] = [guest]
                        else:
                            hotel_rooms[new_floor][new_room].append(guest)

                        upgraded_vips.append(guest)
                        break
        else:
            # Hotel full → add to waiting list
            waiting_list.append(guest)

    # --------------------------------------------------------
    # Step 5: Return Summary Dictionary
    # --------------------------------------------------------
    return {
        'updated_rooms': hotel_rooms,
        'checked_in_guests': checked_in_guests,
        'waiting_list': waiting_list,
        'upgraded_vips': upgraded_vips
    }
