# This script is a pet script that finds recursively squares
# to fill a square with a circle hole inside.
#
# It is written in pure Python.
#
# It requires matplotlib library to create images.
# Gif animation also requires convert program from imagemagick
#
# Get started by running `python `square_filling.py --help`
#
#       _______________________________________________
#      |               ,,ggddY""""Ybbgg,,              |
#      | square    ,agd""'              `""bg,   square|
#      |        ,gdP"                       "Ybg,      |
#      |      ,dP"                             "Yb,    |
#      |   ,dP"                                 "Yb,   |
#      |  ,8"                                     "8,  |
#      | ,8'                                       `8, |
#      |,8'                                         `8,|
#      |d'                                           `b|
#      |8                                             8|
#      |8                                             8|
#      |8                                             8|
#      |8                                             8|
#      |Y,                                           ,P|
#      |`8,                                         ,8'|
#      | `8,                                       ,8' |
#      |  `8a                                     a8'  |
#      |   `Yba                                 adP'   |
#      |     "Yba                             adY"     |
#      |       `"Yba,                     ,adP"'       |
#      |          `"Y8ba,             ,ad8P"'          |
#      | square       ``""YYbaaadPP""''     square     |
#      |------------------------------------------------

def intersect_quarter_circle_with_line(x=0,y=0,r=1):
    """
    evaluates the intersection point of:
    - the bottom left quater of circle whose center is in (r,r) with radius r
    - the line going through (x,y) with a slope of 1
    """
    xc = r + x/2 - y/2 - (2*r**2 - x**2 + 2*x*y - y**2)**0.5 / 2
    yc = xc  + (y - x)
    return (xc, yc)


def sympy_solve():
    """
    Evaluate with a CAS the intersection abscissa between:

    - the bottom left quater of circle whose center is in (r,r) with radius r
    - the line going through (x,y) with a slope of 1
    """
    import sympy
    from sympy.solvers import solve
    r = sympy.Symbol('r', real=True, positive=True)
    y = sympy.Symbol('y', real=True, positive=True)
    x = sympy.Symbol('x', real=True, positive=True)
    xc = sympy.Symbol('xc', real=True, positive=True)
    # (xc - r)**2+(xc + (y - x) - r)**2 - r**2
    return solve((xc - r)**2+(xc + (y - x) - r)**2 - r**2, xc)


def new_squares(square, r=1.0):
    """
    Generate the two children square from one square
    """
    s1_x, s1_y = intersect_quarter_circle_with_line(square[0], square[3], r=r)
    s2_x, s2_y = intersect_quarter_circle_with_line(square[2], square[1], r=r)
    return [square[0], square[3], s1_x, s1_y], \
           [square[2], square[1], s2_x, s2_y]


def main(n=10, radius=1, filter=None):
    """
    Create the squares
    Result is a dict where:
    - keys represent the level of recursion
    - values represent the list of squares of the corresponding level
    """
    xc, yc = intersect_quarter_circle_with_line(x=0,y=0,r=radius)
    res = {0: [[0, 0, xc, yc]]}
    for i in range(1, n):
        res[i] = []
        for s in res[i-1]:
            s1, s2 = new_squares(s, r=radius)
            res[i].append(s1)
            res[i].append(s2)
        if filter:
            (radius * filter) ** 2
            res[i] = [s for s in res[i] if ((s[0]-s[2])**2) + ((s[1]-s[3])**2) > (radius * filter) ** 2]
    return res


def plot_result(res, r=1, outputname='res.png', **kwargs):
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon
    import matplotlib.cm as cm
    def list_of_colormaps():
        # http://matplotlib.org/examples/color/colormaps_reference.html
        import matplotlib.pyplot as plt
        # Get a list of the colormaps in matplotlib.  Ignore the ones that end with
        # '_r' because these are simply reversed versions of ones that don't end
        # with '_r'
        return sorted(m for m in plt.cm.datad if not m.endswith("_r"))
    def plot_square(ax, x1=0, y1=0, x2=1, y2=1):
        ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], 'k-')
    def patch_square(ax, x1=0, y1=0, x2=1, y2=1, color='k'):
        x, y = [x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1]
        verts = list(zip(x, y))
        poly = Polygon(verts, facecolor=color, edgecolor='0.5')  # linewidth
        #poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
        ax.add_patch(poly)
    n = kwargs.get('n', 101)
    dpi = kwargs.get('dpi', 300)
    colormap = kwargs.get('colormap', 'hot')
    axis_off = kwargs.get('axis_off', True)
    symmetry = kwargs.get('symmetry', False)
    n_levels = kwargs.get('n_levels', float(max(list([k for k in res])) + 1) if res else 0)
    fig, ax = plt.subplots()
    if axis_off:
        ax.set_axis_off()
    X = [r * float(i)/(n-1) for i in range(n)]
    Y = [r - (r**2 - (x - r)**2)**0.5 for x in X]
    if symmetry:
        ax.plot(X, Y, 'k--')
        ax.plot([2 * r - x for x in X], Y, 'k--')
        ax.plot([2 * r - x for x in X], [2 * r - y for y in Y], 'k--')
        ax.plot(X, [2 * r - y for y in Y], 'k--')
        ax.plot([0, 2 * r], [0, 0], 'k-')
        ax.plot([0, 0], [0, 2 * r], 'k-')
        ax.plot([2 * r, 2 * r], [0, 2 * r], 'k-')
        ax.plot([0, 2 * r], [2 * r, 2 * r], 'k-')
    else:
        ax.plot(X, Y, 'k--')
        ax.plot([0, r], [0, 0], 'k-')
        ax.plot([0, 0], [0, r], 'k-')
    v = cm.get_cmap(colormap)
    for k in res:
        # color = v((k + 1) / (n_levels + 1))
        # color = v((k + 1) / (n_levels + 1)) if k%2==0 else v((n_levels - k - 1) / (n_levels + 1))
        if k%2==0:
            color = v((k + 1) / (n_levels + 1))
        elif k < n_levels//2:
            color = v((k + 1 + n_levels//2) / (n_levels + 1))
        else:
            color = v((k + 1 - n_levels//2) / (n_levels + 1))
        for s in res[k]:
            # plot_square(ax, *s)
            patch_square(ax, *s, color=color)
    # plt.set_cmap(colormap)
    plt.axis('equal')
    # ax.contourf(data)
    if outputname:
        plt.savefig(outputname, dpi=dpi)
        plt.close()
    else:
        plt.show()


def print_result(res):
    print('level,x1,y1,x2,y2')
    for k in res:
        for s in res[k]:
            print(', '.join([str(k + 1)] + [str(v) for v in s]))


def symmetry(res, r=1):
    m = 2 * r
    for k in res:
        res[k] = [[s, [m-s[0],s[1],m-s[2],s[3]], [m-s[0],m-s[1],m-s[2],m-s[3]], [s[0],m-s[1],s[2],m-s[3]]] for s in res[k]]
        res[k] = [s for ss in res[k] for s in ss]
    return res


def get_filename(colormap, level):
    return colormap + 'res_{0:02d}.png'.format(level)


def get_filenames(colormap, levels):
    return [get_filename(colormap, level) for level in range(levels + 1)]


def create_animated_gif(filename='square.gif', **kwargs):
    import subprocess
    pngs = kwargs.get('pngs', None)
    continuous = kwargs.get('continuous', False)
    if pngs is None:
        from glob import glob
        pngs = glob('*.png')
    if continuous:
        pngs += pngs[-2:0:-1]
    cmd = 'convert -antialias -density 100 -delay 120 '
    cmd += ' '.join(pngs)
    cmd += ' ' + filename
    subprocess.check_output(cmd.split(' '))


def save_to_file(args, res):
    if args.output.lower().endswith('.gif'):
        pngs = get_filenames(args.colormap, levels=args.level)
        for level, png in zip(list(range(args.level + 1)), pngs):
            plot_result({k: res[k] for k in range(level)} if level >= 1 else {}, r=args.radius, outputname=png, colormap=args.colormap, n_levels=args.level, symmetry=args.symmetry)
        create_animated_gif(filename=args.output, pngs=pngs, continuous=True)
    else:
        plot_result(res, r=args.radius, outputname=args.output, colormap=args.colormap, symmetry=args.symmetry)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Create squares in the space between the bottom left quarter of a circle and the surrounding square. The algorithme is recursive: one defines the recursion level.')
    pa = parser.add_argument
    pa('-n', '--level', default=6, type=int, help='Number of recursion levels')
    pa('-p', '--plot', action='store_true', help='Boolean used to display result. Require matplotlib')
    pa('-r', '--radius', default=1.0, type=float,  help='Circle radius')
    pa('-s', '--symmetry', action='store_true', help='Boolean used to create the 4 quarters')
    pa('-c', '--csv', action='store_true', help='Boolean used to display result as a CSV table')
    pa('-f', '--filter', default=None, type=float, help='Relative tolerance under which squares are not exported. Default will export all squares')
    pa('-o', '--output', default=None, help='Name of the generated file. If not provided, result will display on screen.')
    pa('--colormap', type=str, help='Name of the matplotlib colormap to use.', default='autumn')
    args = parser.parse_args()
    res = main(n=args.level, radius=args.radius, filter=args.filter)
    if args.symmetry:
        res = symmetry(res)
    if args.csv:
        print_result(res)
    if args.output:
        save_to_file(args, res)
    if args.plot:
        plot_result(res, r=args.radius, colormap=args.colormap, symmetry=args.symmetry)
