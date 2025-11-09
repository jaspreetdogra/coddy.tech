def filter_properties_by_district(property_addresses, district_name):
    """
    Filters property addresses to include only those containing a given district name.
    
    Parameters:
        property_addresses (list): List of property address strings.
        district_name (str): The district name to filter by.
        
    Returns:
        list: Addresses that contain the district name.
    """
    filtered_addresses = []  # Step 1: Start with an empty list

    for address in property_addresses:  # Step 2: Go through each address
        if district_name in address:     # Step 3: Check if district name appears in the address
            filtered_addresses.append(address)  # Step 4: Add matching address to the list

    return filtered_addresses  # Step 5: Return all filtered results
