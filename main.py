from Drivers.displaylayout import DisplayLayout
import paper
from Drivers.displaysimdriver import * 



wallpapersystem = paper.Paper(
    driver = DisplaySimDriver(
        layout=DisplayLayout(
            200,
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 1, 1]
        )
        )
    )


input()