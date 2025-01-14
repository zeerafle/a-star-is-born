graph_neighbours = {}

# Labirin 12x12
def generate_graph():
    add_neighbours(1,   [2,13]       )
    add_neighbours(2,   [1,3]        )
    add_neighbours(3,   [2,4]        )
    add_neighbours(4,   [3,5]        )
    add_neighbours(5,   [4,6]        )
    add_neighbours(6,   [5,18]       )
    add_neighbours(7,   [8,19]       )
    add_neighbours(8,   [7,9]        )
    add_neighbours(9,   [8,10]       )
    add_neighbours(10,  [9,22]       )
    add_neighbours(11,  [12,23]      )
    add_neighbours(12,  [11]         )

    add_neighbours(13,  [1,25]       )
    add_neighbours(14,  [15,26]      )
    add_neighbours(15,  [14,16]      )
    add_neighbours(16,  [15,28]      )
    add_neighbours(17,  [18,29]      )
    add_neighbours(18,  [6,17]       )
    add_neighbours(19,  [7,20]       )
    add_neighbours(20,  [19,32]      )
    add_neighbours(21,  [22]         )
    add_neighbours(22,  [10,21]      )
    add_neighbours(23,  [11,24,35]   )
    add_neighbours(24,  [23,36]      )

    add_neighbours(25,  [13]         )
    add_neighbours(26,  [14,38]      )
    add_neighbours(27,  [28,39]      )
    add_neighbours(28,  [16,27]      )
    add_neighbours(29,  [17,41]      )
    add_neighbours(30,  [31,42]      )
    add_neighbours(31,  [30,32,43]   )
    add_neighbours(32,  [20,31,33]   ) 
    add_neighbours(33,  [32,34]      )
    add_neighbours(34,  [33,46]      )
    add_neighbours(35,  [23,47]      )
    add_neighbours(36,  [24]         )

    add_neighbours(37,  [38,49]      )
    add_neighbours(38,  [26,37]      )
    add_neighbours(39,  [27,40]      )
    add_neighbours(40,  [39,41]      )
    add_neighbours(41,  [29,40]      )
    add_neighbours(42,  [30,54]      )
    add_neighbours(43,  [31]         )
    add_neighbours(44,  [45,56]      )
    add_neighbours(45,  [44,46]      )
    add_neighbours(46,  [34,45]      )
    add_neighbours(47,  [35,48]      )
    add_neighbours(48,  [47,60]      )

    add_neighbours(49,  [37,50,61]   )
    add_neighbours(50,  [49,51]      )
    add_neighbours(51,  [50,52]      )
    add_neighbours(52,  [51,53]      )
    add_neighbours(53,  [52,54]      )
    add_neighbours(54,  [42,53]      )
    add_neighbours(55,  [56,67]      ) 
    add_neighbours(56,  [44,55]      )
    add_neighbours(57,  [58,69]      )
    add_neighbours(58,  [57,70,59]   )
    add_neighbours(59,  [58,71]      )
    add_neighbours(60,  [48,72]      )

    add_neighbours(61,  [49,73]      )
    add_neighbours(62,  [63,74]      )
    add_neighbours(63,  [62,64]      )
    add_neighbours(64,  [63,76]      )
    add_neighbours(65,  [66,77]      )
    add_neighbours(66,  [65,78]      )
    add_neighbours(67,  [55,68]      )
    add_neighbours(68,  [67,69]      )
    add_neighbours(69,  [57,68]      )
    add_neighbours(70,  [58,82]      )
    add_neighbours(71,  [59,72,83]   )
    add_neighbours(72,  [60,71]      )

    add_neighbours(73,  [61]         )
    add_neighbours(74,  [62,86]      )
    add_neighbours(75,  [76,87]      )
    add_neighbours(76,  [64,75]      )
    add_neighbours(77,  [65]         )
    add_neighbours(78,  [66,79]      )
    add_neighbours(79,  [78,80]      )
    add_neighbours(80,  [79,92]      )
    add_neighbours(81,  [82]         )
    add_neighbours(82,  [70,81,94]   ) 
    add_neighbours(83,  [71,95]      )
    add_neighbours(84,  [96]         )

    add_neighbours(85,  [86,97]      )
    add_neighbours(86,  [74,85]      ) 
    add_neighbours(87,  [75,99]      )
    add_neighbours(88,  [89]         )
    add_neighbours(89,  [88,90,101]  )
    add_neighbours(90,  [89,91]      )
    add_neighbours(91,  [90,92]      )
    add_neighbours(92,  [91,80,93]   )
    add_neighbours(93,  [92,94]      )
    add_neighbours(94,  [82,93]      )
    add_neighbours(95,  [83]         )
    add_neighbours(96,  [84,108]     )

    add_neighbours(97,  [85,98,109]  )
    add_neighbours(98,  [97,110]     )
    add_neighbours(99,  [87,100]     )
    add_neighbours(100, [99,101]     )
    add_neighbours(101, [100,89,102] )
    add_neighbours(102, [101]        )
    add_neighbours(103, [104,115]    )
    add_neighbours(104, [103,116]    ) 
    add_neighbours(105, [106,117]    )
    add_neighbours(106, [105,118]    )
    add_neighbours(107, [108,119]    )
    add_neighbours(108, [107,96]     )

    add_neighbours(109, [97,121]     )
    add_neighbours(110, [98]         )
    add_neighbours(111, [112,123]    )
    add_neighbours(112, [111,113]    )
    add_neighbours(113, [112,114]    )
    add_neighbours(114, [113,126]    )
    add_neighbours(115, [103,127]    )
    add_neighbours(116, [104,128]    )
    add_neighbours(117, [105,129]    )
    add_neighbours(118, [106,119]    )
    add_neighbours(119, [118,107]    )
    add_neighbours(120, [132]        )
    
    add_neighbours(121, [109,122,133])
    add_neighbours(122, [121,123]    )
    add_neighbours(123, [122,111]    )
    add_neighbours(124, [125,136]    )
    add_neighbours(125, [124]        )
    add_neighbours(126, [114,127]    )     
    add_neighbours(127, [115,126,139])
    add_neighbours(128, [116,129]    )
    add_neighbours(129, [128,117]    )
    add_neighbours(130, [131]        )
    add_neighbours(131, [130,143,132])
    add_neighbours(132, [131,120,144])

    add_neighbours(133, [121,134]    )
    add_neighbours(134, [133,135]    )
    add_neighbours(135, [134,136]    )
    add_neighbours(136, [135,124,137])
    add_neighbours(137, [136,138]    )
    add_neighbours(138, [137]        )
    add_neighbours(139, [127,140]    )
    add_neighbours(140, [139,141]    )
    add_neighbours(141, [140,142]    )
    add_neighbours(142, [141,143]    )
    add_neighbours(143, [142,131]    )
    add_neighbours(144, [132]        )
    
    return graph_neighbours


def add_neighbours(node, neighbours):
    new_list = []
    for val in neighbours:
        if val is not None and not val == '':
            new_list.append(str(val))
    graph_neighbours[str(node)] = new_list