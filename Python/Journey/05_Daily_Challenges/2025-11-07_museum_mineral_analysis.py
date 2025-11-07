def analyze_museum_exhibit(mineral_names, mineral_descriptions):
    """
    Museum Mineral Analysis: Cerulean and Conductive 🏛️🔬
    
    Objective:
    Analyze a museum's mineral exhibit and classify minerals based on their
    descriptions — identifying which ones are cerulean-colored and which ones
    are conductive.
    
    Parameters:
        mineral_names (list of str): Names of the minerals in the exhibit.
        mineral_descriptions (list of str): Descriptions of each mineral's properties.
    
    Returns:
        dict: {
            'cerulean_minerals': [list of minerals with cerulean color],
            'conductive_minerals': [list of conductive minerals]
        }
    """

    # Step 1️⃣ — Initialize empty lists to store results
    cerulean_minerals = []
    conductive_minerals = []

    # Step 2️⃣ — Loop through both lists simultaneously
    for name, description in zip(mineral_names, mineral_descriptions):

        # Convert description to lowercase for case-insensitive search
        desc_lower = description.lower()

        # Step 3️⃣ — Check if mineral is cerulean-colored
        if "cerulean" in desc_lower:
            cerulean_minerals.append(name)

        # Step 4️⃣ — Check if mineral is conductive
        if "conductive" in desc_lower:
            conductive_minerals.append(name)

    # Step 5️⃣ — Return organized dictionary
    return {
        "cerulean_minerals": cerulean_minerals,
        "conductive_minerals": conductive_minerals
    }
