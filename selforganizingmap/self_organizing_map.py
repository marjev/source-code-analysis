import os

import pickle
from minisom import MiniSom

from sourcecodeanalysis.settings import BASE_DIR


SOM_PATH = os.path.join(BASE_DIR, './selforganizingmap/som.p')


class SomGenerator(object):
    week_size = 15
    semester_size = 10
    som_shape = (semester_size, week_size)

    def __new__(cls, _):
      if not hasattr(cls, 'instance'):
        cls.instance = super(SomGenerator, cls).__new__(cls)
      return cls.instance

    def __init__(self, ast_nodes):
        if not hasattr(self, 'som'):
          self.som = MiniSom(
              self.week_size,
              self.semester_size,
              len(ast_nodes),
              neighborhood_function='gaussian',
              sigma=1.5
          )

          self.initialize_som()

    def initialize_som(self):
        with open(SOM_PATH, 'rb') as infile:
            self.som = pickle.load(infile)
