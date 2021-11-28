graph_neighbours = {}

def generate_graph():
    add_neighbours(1, [2, 11])
    add_neighbours(2, [1, 12])
    add_neighbours(3, [4, 13])
    add_neighbours(4, [3])
    add_neighbours(5, [6, 15])
    add_neighbours(6, [5, 16])
    add_neighbours(7, [17])
    add_neighbours(8, [9, 18])
    add_neighbours(9, [8, 19])
    add_neighbours(10, [9, 20])

    add_neighbours(11, [1, 21])
    add_neighbours(12, [2])
    add_neighbours(13, [3, 12])
    add_neighbours(14, [15, 24])
    add_neighbours(15, [5, 14, 25])
    add_neighbours(16, [6, 26])
    add_neighbours(17, [7, 18])
    add_neighbours(18, [8, 17])
    add_neighbours(19, [9, 29])
    add_neighbours(20, [10, 30])

    add_neighbours(21, [11, 22])
    add_neighbours(22, [21, 23])
    add_neighbours(23, [22, 24])
    add_neighbours(24, [14, 23])
    add_neighbours(25, [15])
    add_neighbours(26, [16, 36])
    add_neighbours(27, [28, 37])
    add_neighbours(28, [27, 29])
    add_neighbours(29, [19, 28])
    add_neighbours(30, [20, 40])

    add_neighbours(31, [32, 41])
    add_neighbours(32, [31, 33])
    add_neighbours(33, [32])
    add_neighbours(34, [35, 44])
    add_neighbours(35, [34, 45])
    add_neighbours(36, [26, 37])
    add_neighbours(37, [27, 36, 47])
    add_neighbours(38, [39, 48])
    add_neighbours(39, [38, 40])
    add_neighbours(40, [30, 39])

    add_neighbours(41, [31, 51])
    add_neighbours(42, [43, 52])
    add_neighbours(43, [42, 44])
    add_neighbours(44, [34, 43, 54])
    add_neighbours(45, [35, 55])
    add_neighbours(46, [56])
    add_neighbours(47, [37, 57])
    add_neighbours(48, [38, 49])
    add_neighbours(49, [48, 50])
    add_neighbours(50, [49])

    add_neighbours(51, [41, 61])
    add_neighbours(52, [42, 53, 62])
    add_neighbours(53, [52, 63])
    add_neighbours(54, [44])
    add_neighbours(55, [45, 65])
    add_neighbours(56, [46, 57])
    add_neighbours(57, [47, 56, 58])
    add_neighbours(58, [57, 59])
    add_neighbours(59, [58, 69])
    add_neighbours(60, [70])

    add_neighbours(61, [51, 62, 71])
    add_neighbours(62, [52, 61])
    add_neighbours(63, [53])
    add_neighbours(64, [65, 74])
    add_neighbours(65, [55, 64, 66, 75])
    add_neighbours(66, [65, 67])
    add_neighbours(67, [66, 68, 77])
    add_neighbours(68, [67, 78])
    add_neighbours(69, [59, 79])
    add_neighbours(70, [60, 80])

    add_neighbours(71, [61, 81])
    add_neighbours(72, [73, 82])
    add_neighbours(73, [72, 74])
    add_neighbours(74, [64, 73])
    add_neighbours(75, [65, 76])
    add_neighbours(76, [75])
    add_neighbours(77, [67, 87])
    add_neighbours(78, [68, 88])
    add_neighbours(79, [69, 89])
    add_neighbours(80, [70, 90])

    add_neighbours(81, [71, 91])
    add_neighbours(82, [72, 83])
    add_neighbours(83, [82, 84])
    add_neighbours(84, [83, 94])
    add_neighbours(85, [86, 95])
    add_neighbours(86, [85, 96])
    add_neighbours(87, [77])
    add_neighbours(88, [78, 89])
    add_neighbours(89, [79, 88])
    add_neighbours(90, [80, 100])

    add_neighbours(91, [81, 92])
    add_neighbours(92, [91, 93])
    add_neighbours(93, [92])
    add_neighbours(94, [84, 95])
    add_neighbours(95, [85, 94])
    add_neighbours(96, [86, 97])
    add_neighbours(97, [96, 98])
    add_neighbours(98, [97, 99])
    add_neighbours(99, [98, 100])
    add_neighbours(100, [90, 99])
    return graph_neighbours

def add_neighbours(node, neighbours):
    new_list = []
    for val in neighbours:
        if val is not None and not val == '':
            new_list.append(str(val))
    graph_neighbours[str(node)] = new_list
