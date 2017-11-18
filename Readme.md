# Description

This script is a pet script that finds recursively squares
to fill a square with a circle hole inside.

It is written in pure Python.

It requires matplotlib library to create images.

Gif animation also requires convert program from imagemagick

Get started by running `python square_filling.py --help`.

      _______________________________________________
     |               ,,ggddY""""Ybbgg,,              |
     | square    ,agd""'              `""bg,   square|
     |        ,gdP"                       "Ybg,      |
     |      ,dP"                             "Yb,    |
     |   ,dP"                                 "Yb,   |
     |  ,8"                                     "8,  |
     | ,8'                                       `8, |
     |,8'                                         `8,|
     |d'                                           `b|
     |8                                             8|
     |8                                             8|
     |8                                             8|
     |8                                             8|
     |Y,                                           ,P|
     |`8,                                         ,8'|
     | `8,                                       ,8' |
     |  `8a                                     a8'  |
     |   `Yba                                 adP'   |
     |     "Yba                             adY"     |
     |       `"Yba,                     ,adP"'       |
     |          `"Y8ba,             ,ad8P"'          |
     | square       ``""YYbaaadPP""''     square     |
     |------------------------------------------------


    python square_filling.py --help
    usage: square_filling.py [-h] [-n LEVEL] [-p] [-r RADIUS] [-s] [-c] [-f FILTER]
                             [-o OUTPUT] [--colormap COLORMAP]

    Create squares in the space between the bottom left quarter of a circle and
    the surrounding square. The algorithme is recursive: one defines the recursion
    level.

    optional arguments:
    -h, --help            show this help message and exit
    -n LEVEL, --level LEVEL
                            Number of recursion levels
    -p, --plot            Boolean used to display result. Require matplotlib
    -r RADIUS, --radius RADIUS
                            Circle radius
    -s, --symmetry        Boolean used to create the 4 quarters
    -c, --csv             Boolean used to display result as a CSV table
    -f FILTER, --filter FILTER
                            Relative tolerance under which squares are not
                            exported. Default will export all squares
    -o OUTPUT, --output OUTPUT
                            Name of the generated file. If not provided, result
                            will display on screen.
    --colormap COLORMAP   Name of the matplotlib colormap to use.

# Examples

    python square_filling.py -n 12  -f 0.005 -o pSet3.gif --colormap jet -s