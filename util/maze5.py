graph_neighbours = {}

# Labirin 5x5
def generate_graph():

    add_neighbours(1,  [2,  6])
    add_neighbours(2,  [1,  3])
    add_neighbours(3,  [2]    )
    add_neighbours(4,  [5,  9])
    add_neighbours(5,  [4, 10])

    add_neighbours(6,  [1,  7])
    add_neighbours(7,  [6,  8])
    add_neighbours(8,  [7,  9])
    add_neighbours(9,  [4,  8,  14])
    add_neighbours(10, [5, 15])

    add_neighbours(11, [12, 16])
    add_neighbours(12, [11, 13])
    add_neighbours(13, [12]    )
    add_neighbours(14, [9,  19])
    add_neighbours(15, [10]    )

    add_neighbours(16, [11, 21])
    add_neighbours(17, [18, 22])
    add_neighbours(18, [17, 23])
    add_neighbours(19, [14, 24])
    add_neighbours(20, [25]    )

    add_neighbours(21, [16, 22])
    add_neighbours(22, [17, 21])
    add_neighbours(23, [18, 24])
    add_neighbours(24, [19, 23, 25])
    add_neighbours(25, [24, 20])

    return graph_neighbours


def add_neighbours(node, neighbours):
    new_list = []
    for val in neighbours:
        if val is not None and not val == '':
            new_list.append(str(val))
    graph_neighbours[str(node)] = new_list

