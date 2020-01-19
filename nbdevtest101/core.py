# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['say_hello', 'HelloSayer', 'bubble_scatter']

# Cell
def say_hello(to):
    "Say hello to somebody"
    return f'Hello {to}!'

# Cell
class HelloSayer:
    "Say hello to `to` using `say_hello`"
    def __init__(self, to): self.to = to
    def say(self): return say_hello(self.to)

# Cell
def bubble_scatter(n):
  "Create a scatter plot of n different sized bubbles"
  np.random.seed(19680801)
  x = np.random.rand(n)
  y = np.random.rand(n)
  colors = np.random.rand(n)
  area = (30 * np.random.rand(n))**2  # 0 to 15 point radii

  plt.scatter(x, y, s=area, c=colors, alpha=0.5)
  plt.show()