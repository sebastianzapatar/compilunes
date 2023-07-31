from lpp.repl import start_repl
def imprimir_bienvenida():
    bienvenida = [
        "  ***     *   *   ***   *   *     *** ",
        " *   *   *   *  *   *  *   *    *   *",
        " *       *****  *      *****    *",
        " *       *   *  *      *   *     *",
        " *   *   *   *  *   *  *   *    *   *",
        "  ***    *   *   ***   *   *     *** "
    ]
    for linea in bienvenida:
        print(linea.center(40, "*"))

imprimir_bienvenida()
def main()->None:
    imprimir_bienvenida()
    start_repl()
if __name__=='__main__':
    main()
