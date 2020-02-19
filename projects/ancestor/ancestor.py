def earliest_ancestor(ancestors, starting_node):

    relationships = {}
    for parent_child in ancestors:
        parent = parent_child[0]
        child = parent_child[1]
        if parent not in relationships:
            relationships[parent] = set()
        if child not in relationships:
            relationships[child] = set()
        relationships[child].add(parent)

    previous_generation = set([starting_node])
    while True:
        next_generation = set()
        for member in previous_generation:
            if len(relationships[member]) > 0:
                for parent in relationships[member]:
                    next_generation.add(parent)
        if len(next_generation) > 0:
            previous_generation = next_generation
        elif min(previous_generation) == starting_node:
            return -1
        else:
            return min(previous_generation)