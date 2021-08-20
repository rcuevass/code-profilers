from pyinstrument import Profiler
from matrix_product import generate_matrices, product_numpy, product_loop


profiler = Profiler()
a, b = generate_matrices()
profiler.start()
profiler.stop()
profiler.print()


profiler = Profiler()
c_np = product_numpy(a, b)
profiler.start()
profiler.stop()
profiler.print()


profiler = Profiler()
c_loop = product_loop(a, b)
profiler.start()
profiler.stop()
profiler.print()
