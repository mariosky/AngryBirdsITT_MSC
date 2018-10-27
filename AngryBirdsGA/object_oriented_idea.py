


# pieceDic.append([[72, 72], ["Circle","wood",0,0,0]])


BLOCK_TYPE = { 'Circle':   {'height': 72, 'lenght': 72},
               'RectTiny': {'height': 22, 'lenght': 42},
               'RectSmall':{'height': 22, 'lenght': 82},
               'RectBig':{'height': 22, 'lenght':182},
               'RectMedium':{'height': 22, 'lenght': 162},

               }

BLOCK_MATERIAL = { 'Wood':0,
                   'Metal':1,
                   'Glass':2}

# This is only information for constructing blocks
BLOCKS = {
   0 : [ {'type': BLOCK_TYPE['Circle'],
          'material': BLOCK_MATERIAL['Wood'],
          'offset' : [0,0,0]  # x,y,y from center
          }],
   11:  [{'type': BLOCK_TYPE['RectBig'],
          'material': BLOCK_MATERIAL['Wood'],
          'offset' : [0,-91,0]  # x,y,y from center
          },
          {'type': BLOCK_TYPE['RectMedium'],
          'material': BLOCK_MATERIAL['Wood'],
          'offset' : [-90,0,90]  # x,y,y from center
          },
          {'type': BLOCK_TYPE['RectMedium'],
          'material': BLOCK_MATERIAL['Wood'],
          'offset' : [90,0,90]  # x,y,y from center
          },
          {'type': BLOCK_TYPE['RectBig'],
          'material': BLOCK_MATERIAL['Wood'],
          'offset' : [0,91,90]  # x,y,y from center
          }]
   }


class Composite:
    def __init__(self, blocks):
        # Blocks must be a list like above
        self.blocks = blocks

    def height(self):
        #TO DO: Calculate height for blocks
        return 0.0

    def width(self):
        return 0.0

    def top_center(self):
        return 0.0

    def as_dictionary(self):
        return {}

    def as_json(self):
        return {}


Composites = {
    0: Composite(BLOCKS[0]),
    1: Composite(BLOCKS[11])
}



# As a basic example a chromosome is a list of Connected Composites

chromosome = [0,1,0]

# when evaluating fitness or positioning in map

chromosome_objects = [ Composites[composite] for composite in chromosome]

for c in chromosome_objects:
    print(c.height())


class Individual:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.fitness = kwargs.get('fitness',{})
        self.chromosome = kwargs.get('chromosome',[])
        self.__dict__.update(kwargs)
        self.chromosome_objects = [ Composites[composite] for composite in chromosome]


    def position_chromosome(self):
        #To do
        # Here you can use the chromosome objects etc.
        pass
