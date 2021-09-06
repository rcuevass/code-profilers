from utilities.matrix_operations import generate_matrices, product_numpy, product_loop
from viztracer import VizTracer
tracer = VizTracer()


tracer.start()
a_, b_ = generate_matrices()
c_1 = product_numpy(a_, b_)
c_2 = product_loop(a_, b_)
tracer.stop()
tracer.save()
