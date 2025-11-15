def romantic_dinner_sharing(dishes, skip_dishes):
    # Step 0: Validate same length
    if len(dishes) != len(skip_dishes):
        return []

    shared = []

    # Step 1 & 2: Iterate and filter
    for dish, skip in zip(dishes, skip_dishes):
        if not skip:     # skip == False → share this dish
            shared.append(dish)

    # Step 3: Return reversed list
    return shared[::-1]
