import runpy

if __name__ == "__main__":
    # Run the hescan package as a module (runs __main__.py inside hescan)
    runpy.run_module('hescan', run_name='__main__')
