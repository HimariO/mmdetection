import json
import random
import mmcv
import numpy as np

from .builder import DATASETS
from .custom import CustomDataset


VG_CLASSES = [
    'yolk',
    'goal',
    'bathroom',
    'macaroni',
    'umpire',
    'toothpick',
    'alarm clock',
    'ceiling fan',
    'photos',
    'parrot',
    'tail fin',
    'birthday cake',
    'calculator',
    'catcher',
    'toilet',
    'batter',
    'stop sign',
    'cone',
    'microwave',
    'skateboard ramp',
    'tea',
    'dugout',
    'products',
    'halter',
    'kettle',
    'kitchen',
    'refrigerator',
    'ostrich',
    'bathtub',
    'blinds',
    'court',
    'urinal',
    'knee pads',
    'bed',
    'flamingo',
    'giraffe',
    'helmet',
    'giraffes',
    'tennis court',
    'motorcycle',
    'laptop',
    'tea pot',
    'horse',
    'television',
    'shorts',
    'manhole',
    'dishwasher',
    'jeans',
    'sail',
    'monitor',
    'man',
    'shirt',
    'car',
    'cat',
    'garage door',
    'bus',
    'radiator',
    'tights',
    'sailboat',
    'racket',
    'plate',
    'rock wall',
    'beach',
    'trolley',
    'ocean',
    'headboard',
    'tea kettle',
    'wetsuit',
    'tennis racket',
    'sink',
    'train',
    'keyboard',
    'sky',
    'match',
    'train station',
    'stereo',
    'bats',
    'tennis player',
    'toilet brush',
    'lighter',
    'pepper shaker',
    'gazebo',
    'hair dryer',
    'elephant',
    'toilet seat',
    'zebra',
    'skateboard',
    'zebras',
    'floor lamp',
    'french fries',
    'woman',
    'player',
    'tower',
    'bicycle',
    'magazines',
    'christmas tree',
    'umbrella',
    'cow',
    'pants',
    'bike',
    'field',
    'living room',
    'latch',
    'bedroom',
    'grape',
    'castle',
    'table',
    'swan',
    'blender',
    'orange',
    'teddy bear',
    'net',
    'meter',
    'baseball field',
    'runway',
    'screen',
    'ski boot',
    'dog',
    'clock',
    'hair',
    'avocado',
    'highway',
    'skirt',
    'frisbee',
    'parasail',
    'desk',
    'pizza',
    'mouse',
    'sign',
    'shower curtain',
    'polar bear',
    'airplane',
    'jersey',
    'reigns',
    'hot dog',
    'surfboard',
    'couch',
    'glass',
    'snowboard',
    'girl',
    'plane',
    'elephants',
    'oven',
    'dirt bike',
    'tail wing',
    'area rug',
    'bear',
    'washer',
    'date',
    'bow tie',
    'cows',
    'fire extinguisher',
    'bamboo',
    'wallet',
    'tail feathers',
    'truck',
    'beach chair',
    'boat',
    'tablet',
    'ceiling',
    'chandelier',
    'sheep',
    'glasses',
    'ram',
    'kite',
    'salad',
    'pillow',
    'fire hydrant',
    'mug',
    'tarmac',
    'computer',
    'swimsuit',
    'tomato',
    'tire',
    'cauliflower',
    'fireplace',
    'snow',
    'building',
    'sandwich',
    'weather vane',
    'bird',
    'jacket',
    'chair',
    'water',
    'cats',
    'soccer ball',
    'horses',
    'drapes',
    'barn',
    'engine',
    'cake',
    'head',
    'head band',
    'skier',
    'town',
    'bath tub',
    'bowl',
    'stove',
    'tongue',
    'coffee table',
    'floor',
    'uniform',
    'ottoman',
    'broccoli',
    'olive',
    'mound',
    'pitcher',
    'food',
    'paintings',
    'traffic light',
    'parking meter',
    'bananas',
    'mountain',
    'cage',
    'hedge',
    'motorcycles',
    'wet suit',
    'radish',
    'teddy bears',
    'monitors',
    'suitcase',
    'drawers',
    'grass',
    'apple',
    'lamp',
    'goggles',
    'boy',
    'armchair',
    'ramp',
    'burner',
    'lamb',
    'cup',
    'tank top',
    'boats',
    'hat',
    'soup',
    'fence',
    'necklace',
    'visor',
    'coffee',
    'bottle',
    'stool',
    'shoe',
    'surfer',
    'stop',
    'backpack',
    'shin guard',
    'wii remote',
    'wall',
    'pizza slice',
    'home plate',
    'van',
    'packet',
    'earrings',
    'wristband',
    'tracks',
    'mitt',
    'dome',
    'snowboarder',
    'faucet',
    'toiletries',
    'ski boots',
    'room',
    'fork',
    'snow suit',
    'banana slice',
    'bench',
    'tie',
    'burners',
    'stuffed animals',
    'zoo',
    'train platform',
    'cupcake',
    'curtain',
    'ear',
    'tissue box',
    'bread',
    'scissors',
    'vase',
    'herd',
    'smoke',
    'skylight',
    'cub',
    'tail',
    'cutting board',
    'wave',
    'hedges',
    'windshield',
    'apples',
    'mirror',
    'license plate',
    'tree',
    'wheel',
    'ski pole',
    'clock tower',
    'freezer',
    'luggage',
    'skateboarder',
    'mousepad',
    'road',
    'bat',
    'toilet tank',
    'vanity',
    'neck',
    'cliff',
    'tub',
    'sprinkles',
    'dresser',
    'street',
    'wing',
    'suit',
    'veggie',
    'palm trees',
    'urinals',
    'door',
    'propeller',
    'keys',
    'skate park',
    'platform',
    'pot',
    'towel',
    'computer monitor',
    'flip flop',
    'eggs',
    'shed',
    'moped',
    'sand',
    'face',
    'scissor',
    'carts',
    'squash',
    'pillows',
    'family',
    'glove',
    'rug',
    'watch',
    'grafitti',
    'dogs',
    'scoreboard',
    'basket',
    'poster',
    'duck',
    'horns',
    'bears',
    'jeep',
    'painting',
    'lighthouse',
    'remote control',
    'toaster',
    'vegetables',
    'surfboards',
    'ducks',
    'lane',
    'carrots',
    'market',
    'paper towels',
    'island',
    'blueberries',
    'smile',
    'balloons',
    'stroller',
    'napkin',
    'towels',
    'papers',
    'person',
    'train tracks',
    'child',
    'headband',
    'pool',
    'plant',
    'harbor',
    'counter',
    'hand',
    'house',
    'donut',
    'knot',
    'soccer player',
    'seagull',
    'bottles',
    'buses',
    'coat',
    'trees',
    'geese',
    'bun',
    'toilet bowl',
    'trunk',
    'station',
    'bikini',
    'goatee',
    'lounge chair',
    'breakfast',
    'nose',
    'moon',
    'river',
    'racer',
    'picture',
    'shaker',
    'sidewalk',
    'shutters',
    'stove top',
    'church',
    'lampshade',
    'map',
    'shop',
    'platter',
    'airport',
    'hoodie',
    'oranges',
    'woods',
    'enclosure',
    'skatepark',
    'vases',
    'city',
    'park',
    'mailbox',
    'balloon',
    'billboard',
    'pasture',
    'portrait',
    'forehead',
    'ship',
    'cookie',
    'seaweed',
    'sofa',
    'slats',
    'tomato slice',
    'tractor',
    'bull',
    'suitcases',
    'graffiti',
    'policeman',
    'remotes',
    'pens',
    'window sill',
    'suspenders',
    'easel',
    'tray',
    'straw',
    'collar',
    'shower',
    'bag',
    'scooter',
    'tails',
    'toilet lid',
    'panda',
    'comforter',
    'outlet',
    'stems',
    'valley',
    'flag',
    'jockey',
    'gravel',
    'mouth',
    'window',
    'bridge',
    'corn',
    'mountains',
    'beer',
    "pitcher's mound",
    'palm tree',
    'crowd',
    'skis',
    'phone',
    'banana bunch',
    'tennis shoe',
    'ground',
    'carpet',
    'eye',
    'urn',
    'beak',
    'giraffe head',
    'steeple',
    'mattress',
    'baseball player',
    'wine',
    'water bottle',
    'kitten',
    'archway',
    'candle',
    'croissant',
    'tennis ball',
    'dress',
    'column',
    'utensils',
    'cell phone',
    'computer mouse',
    'cap',
    'lawn',
    'airplanes',
    'carriage',
    'snout',
    'cabinets',
    'lemons',
    'grill',
    'umbrellas',
    'meat',
    'wagon',
    'ipod',
    'bookshelf',
    'cart',
    'roof',
    'hay',
    'ski pants',
    'seat',
    'mane',
    'bikes',
    'drawer',
    'game',
    'clock face',
    'boys',
    'rider',
    'fire escape',
    'slope',
    'iphone',
    'pumpkin',
    'pan',
    'chopsticks',
    'hill',
    'uniforms',
    'cleat',
    'costume',
    'cabin',
    'police officer',
    'ears',
    'egg',
    'trash can',
    'horn',
    'arrow',
    'toothbrush',
    'carrot',
    'banana',
    'planes',
    'garden',
    'forest',
    'brocolli',
    'aircraft',
    'front window',
    'dashboard',
    'statue',
    'saucer',
    'people',
    'silverware',
    'fruit',
    'drain',
    'jet',
    'speaker',
    'eyes',
    'railway',
    'lid',
    'soap',
    'rocks',
    'office chair',
    'door knob',
    'banana peel',
    'baseball game',
    'asparagus',
    'spoon',
    'cabinet door',
    'pineapple',
    'traffic cone',
    'nightstand',
    'teapot',
    'taxi',
    'chimney',
    'lake',
    'suit jacket',
    'train engine',
    'ball',
    'wrist band',
    'pickle',
    'fruits',
    'pad',
    'dispenser',
    'bridle',
    'breast',
    'cones',
    'headlight',
    'necktie',
    'skater',
    'toilet paper',
    'skyscraper',
    'telephone',
    'ox',
    'roadway',
    'sock',
    'paddle',
    'dishes',
    'hills',
    'street sign',
    'headlights',
    'benches',
    'fuselage',
    'card',
    'napkins',
    'bush',
    'rice',
    'computer screen',
    'spokes',
    'flowers',
    'bucket',
    'rock',
    'pole',
    'pear',
    'sauce',
    'store',
    'juice',
    'knobs',
    'mustard',
    'ski',
    'stands',
    'cabinet',
    'dirt',
    'goats',
    'wine glass',
    'spectators',
    'crate',
    'pancakes',
    'kids',
    'engines',
    'shade',
    'feeder',
    'cellphone',
    'pepper',
    'blanket',
    'sunglasses',
    'train car',
    'magnet',
    'donuts',
    'sweater',
    'signal',
    'advertisement',
    'log',
    'vent',
    'whiskers',
    'adult',
    'arch',
    'locomotive',
    'tennis match',
    'tent',
    'motorbike',
    'magnets',
    'night',
    'marina',
    'wool',
    'vest',
    'railroad tracks',
    'stuffed bear',
    'moustache',
    'bib',
    'frame',
    'snow pants',
    'tank',
    'undershirt',
    'icons',
    'neck tie',
    'beams',
    'baseball bat',
    'safety cone',
    'paper towel',
    'bedspread',
    'can',
    'container',
    'flower',
    'vehicle',
    'tomatoes',
    'back wheel',
    'soccer field',
    'nostril',
    'suv',
    'buildings',
    'canopy',
    'flame',
    'kid',
    'baseball',
    'throw pillow',
    'belt',
    'rainbow',
    'lemon',
    'oven door',
    'tag',
    'books',
    'monument',
    'men',
    'shadow',
    'bicycles',
    'cars',
    'lamp shade',
    'pine tree',
    'bouquet',
    'toothpaste',
    'potato',
    'sinks',
    'hook',
    'switch',
    'lamp post',
    'lapel',
    'desert',
    'knob',
    'chairs',
    'pasta',
    'feathers',
    'hole',
    'meal',
    'station wagon',
    'kites',
    'boots',
    'baby',
    'biker',
    'gate',
    'signal light',
    'headphones',
    'goat',
    'waves',
    'bumper',
    'bud',
    'logo',
    'curtains',
    'american flag',
    'yacht',
    'box',
    'baseball cap',
    'fries',
    'controller',
    'awning',
    'path',
    'front legs',
    'life jacket',
    'purse',
    'outfield',
    'pigeon',
    'toddler',
    'beard',
    'thumb',
    'water tank',
    'board',
    'parade',
    'robe',
    'newspaper',
    'wires',
    'camera',
    'pastries',
    'deck',
    'watermelon',
    'clouds',
    'deer',
    'motorcyclist',
    'kneepad',
    'sneakers',
    'women',
    'onions',
    'eyebrow',
    'gas station',
    'vane',
    'girls',
    'trash',
    'numerals',
    'knife',
    'tags',
    'light',
    'bunch',
    'outfit',
    'groom',
    'infield',
    'frosting',
    'forks',
    'entertainment center',
    'stuffed animal',
    'yard',
    'numeral',
    'ladder',
    'shoes',
    'bracelet',
    'teeth',
    'guy',
    'display case',
    'cushion',
    'post',
    'pathway',
    'tablecloth',
    'skiers',
    'trouser',
    'cloud',
    'hands',
    'produce',
    'beam',
    'ketchup',
    'paw',
    'dish',
    'raft',
    'crosswalk',
    'front wheel',
    'toast',
    'cattle',
    'players',
    'group',
    'coffee pot',
    'track',
    'cowboy hat',
    'petal',
    'eyeglasses',
    'handle',
    'table cloth',
    'jets',
    'shakers',
    'remote',
    'snowsuit',
    'bushes',
    'dessert',
    'leg',
    'eagle',
    'fire truck',
    'game controller',
    'smartphone',
    'backsplash',
    'trains',
    'shore',
    'signs',
    'bell',
    'cupboards',
    'sweat band',
    'sack',
    'ankle',
    'coin slot',
    'bagel',
    'masts',
    'police',
    'drawing',
    'biscuit',
    'toy',
    'legs',
    'pavement',
    'outside',
    'wheels',
    'driver',
    'numbers',
    'blazer',
    'pen',
    'cabbage',
    'trucks',
    'key',
    'saddle',
    'pillow case',
    'goose',
    'label',
    'boulder',
    'pajamas',
    'wrist',
    'shelf',
    'cross',
    'coffee cup',
    'foliage',
    'lot',
    'fry',
    'air',
    'officer',
    'pepperoni',
    'cheese',
    'lady',
    'kickstand',
    'counter top',
    'veggies',
    'baseball uniform',
    'book shelf',
    'bags',
    'pickles',
    'stand',
    'netting',
    'lettuce',
    'facial hair',
    'lime',
    'animals',
    'drape',
    'boot',
    'railing',
    'end table',
    'shin guards',
    'steps',
    'trashcan',
    'tusk',
    'head light',
    'walkway',
    'cockpit',
    'tennis net',
    'animal',
    'boardwalk',
    'keypad',
    'bookcase',
    'blueberry',
    'trash bag',
    'ski poles',
    'parking lot',
    'gas tank',
    'beds',
    'fan',
    'base',
    'soap dispenser',
    'banner',
    'life vest',
    'train front',
    'word',
    'cab',
    'liquid',
    'exhaust pipe',
    'sneaker',
    'light fixture',
    'power lines',
    'curb',
    'scene',
    'buttons',
    'roman numerals',
    'muzzle',
    'sticker',
    'bacon',
    'pizzas',
    'paper',
    'feet',
    'stairs',
    'triangle',
    'plants',
    'rope',
    'beans',
    'brim',
    'beverage',
    'letters',
    'soda',
    'menu',
    'finger',
    'dvds',
    'candles',
    'picnic table',
    'wine bottle',
    'pencil',
    'tree trunk',
    'nail',
    'mantle',
    'countertop',
    'view',
    'line',
    'motor bike',
    'audience',
    'traffic sign',
    'arm',
    'pedestrian',
    'stabilizer',
    'dock',
    'doorway',
    'bedding',
    'end',
    'worker',
    'canal',
    'crane',
    'grate',
    'little girl',
    'rims',
    'passenger car',
    'plates',
    'background',
    'peel',
    'brake light',
    'roman numeral',
    'string',
    'tines',
    'turf',
    'armrest',
    'shower head',
    'leash',
    'stones',
    'stoplight',
    'handle bars',
    'front',
    'scarf',
    'band',
    'jean',
    'tennis',
    'pile',
    'doorknob',
    'foot',
    'houses',
    'windows',
    'restaurant',
    'booth',
    'cardboard box',
    'fingers',
    'mountain range',
    'bleachers',
    'rail',
    'pastry',
    'canoe',
    'sun',
    'eye glasses',
    'salt shaker',
    'number',
    'fish',
    'knee pad',
    'fur',
    'she',
    'shower door',
    'rod',
    'branches',
    'birds',
    'printer',
    'sunset',
    'median',
    'shutter',
    'slice',
    'heater',
    'prongs',
    'bathing suit',
    'skiier',
    'rack',
    'book',
    'blade',
    'apartment',
    'manhole cover',
    'stools',
    'overhang',
    'door handle',
    'couple',
    'picture frame',
    'chicken',
    'planter',
    'seats',
    'hour hand',
    'dvd player',
    'ski slope',
    'french fry',
    'bowls',
    'top',
    'landing gear',
    'coffee maker',
    'melon',
    'computers',
    'light switch',
    'jar',
    'tv stand',
    'overalls',
    'garage',
    'tabletop',
    'writing',
    'doors',
    'stadium',
    'placemat',
    'air vent',
    'trick',
    'sled',
    'mast',
    'pond',
    'steering wheel',
    'baseball glove',
    'watermark',
    'pie',
    'sandwhich',
    'cpu',
    'mushroom',
    'power pole',
    'dirt road',
    'handles',
    'speakers',
    'fender',
    'telephone pole',
    'strawberry',
    'mask',
    'children',
    'crust',
    'art',
    'rim',
    'branch',
    'display',
    'grasses',
    'photo',
    'receipt',
    'instructions',
    'herbs',
    'toys',
    'handlebars',
    'trailer',
    'sandal',
    'skull',
    'hangar',
    'pipe',
    'office',
    'chest',
    'lamps',
    'horizon',
    'calendar',
    'foam',
    'stone',
    'bars',
    'button',
    'poles',
    'heart',
    'hose',
    'jet engine',
    'potatoes',
    'rain',
    'magazine',
    'chain',
    'footboard',
    'tee shirt',
    'design',
    'walls',
    'copyright',
    'pictures',
    'pillar',
    'drink',
    'barrier',
    'boxes',
    'chocolate',
    'chef',
    'slot',
    'sweatpants',
    'face mask',
    'icing',
    'wipers',
    'circle',
    'bin',
    'kitty',
    'electronics',
    'wild',
    'tiles',
    'steam',
    'lettering',
    'bathroom sink',
    'laptop computer',
    'cherry',
    'spire',
    'conductor',
    'sheet',
    'slab',
    'windshield wipers',
    'storefront',
    'hill side',
    'spatula',
    'tail light',
    'bean',
    'wire',
    'intersection',
    'pier',
    'snow board',
    'trunks',
    'website',
    'bolt',
    'kayak',
    'nuts',
    'holder',
    'turbine',
    'stop light',
    'olives',
    'ball cap',
    'burger',
    'barrel',
    'fans',
    'beanie',
    'stem',
    'lines',
    'traffic signal',
    'sweatshirt',
    'handbag',
    'mulch',
    'socks',
    'landscape',
    'soda can',
    'shelves',
    'ski lift',
    'cord',
    'vegetable',
    'apron',
    'blind',
    'bracelets',
    'stickers',
    'traffic',
    'strip',
    'tennis shoes',
    'swim trunks',
    'hillside',
    'sandals',
    'concrete',
    'lips',
    'butter knife',
    'words',
    'leaves',
    'train cars',
    'spoke',
    'cereal',
    'pine trees',
    'cooler',
    'bangs',
    'half',
    'sheets',
    'figurine',
    'park bench',
    'stack',
    'second floor',
    'motor',
    'hand towel',
    'wristwatch',
    'spectator',
    'tissues',
    'flip flops',
    'quilt',
    'floret',
    'calf',
    'back pack',
    'grapes',
    'ski tracks',
    'skin',
    'bow',
    'controls',
    'dinner',
    'baseball players',
    'ad',
    'ribbon',
    'hotel',
    'sea',
    'cover',
    'tarp',
    'weather',
    'notebook',
    'mustache',
    'stone wall',
    'closet',
    'statues',
    'bank',
    'skateboards',
    'butter',
    'dress shirt',
    'knee',
    'wood',
    'laptops',
    'cuff',
    'hubcap',
    'wings',
    'range',
    'structure',
    'balls',
    'tunnel',
    'globe',
    'utensil',
    'dumpster',
    'cd',
    'floors',
    'wrapper',
    'folder',
    'pocket',
    'mother',
    'ski goggles',
    'posts',
    'power line',
    'wake',
    'roses',
    'train track',
    'reflection',
    'air conditioner',
    'referee',
    'barricade',
    'baseball mitt',
    'mouse pad',
    'garbage can',
    'buckle',
    'footprints',
    'lights',
    'muffin',
    'bracket',
    'plug',
    'taxi cab',
    'drinks',
    'surfers',
    'arrows',
    'control panel',
    'ring',
    'twigs',
    'soil',
    'skies',
    'clock hand',
    'caboose',
    'playground',
    'mango',
    'stump',
    'brick wall',
    'screw',
    'minivan',
    'leaf',
    'fencing',
    'ledge',
    'clothes',
    'grass field',
    'plumbing',
    'blouse',
    'patch',
    'scaffolding',
    'hamburger',
    'utility pole',
    'teddy',
    'rose',
    'skillet',
    'cycle',
    'cable',
    'gloves',
    'bark',
    'decoration',
    'tables',
    'palm',
    'wii',
    'mountain top',
    'shrub',
    'hoof',
    'celery',
    'beads',
    'plaque',
    'flooring',
    'surf',
    'cloth',
    'passenger',
    'spot',
    'plastic',
    'knives',
    'case',
    'railroad',
    'pony',
    'muffler',
    'hot dogs',
    'stripe',
    'scale',
    'block',
    'recliner',
    'body',
    'shades',
    'tap',
    'tools',
    'cupboard',
    'wallpaper',
    'sculpture',
    'surface',
    'sedan',
    'distance',
    'shrubs',
    'skiis',
    'lift',
    'bottom',
    'cleats',
    'roll',
    'clothing',
    'bed frame',
    'slacks',
    'tail lights',
    'doll',
    'traffic lights',
    'symbol',
    'strings',
    'fixtures',
    'short',
    'paint',
    'candle holder',
    'guard rail',
    'cyclist',
    'tree branches',
    'ripples',
    'gear',
    'waist',
    'trash bin',
    'onion',
    'home',
    'side mirror',
    'brush',
    'sweatband',
    'handlebar',
    'light pole',
    'street lamp',
    'pads',
    'ham',
    'artwork',
    'reflector',
    'figure',
    'tile',
    'mountainside',
    'black',
    'bricks',
    'paper plate',
    'stick',
    'beef',
    'patio',
    'weeds',
    'back',
    'sausage',
    'paws',
    'farm',
    'decal',
    'harness',
    'monkey',
    'fence post',
    'door frame',
    'stripes',
    'clocks',
    'ponytail',
    'toppings',
    'strap',
    'carton',
    'greens',
    'chin',
    'lunch',
    'name',
    'earring',
    'area',
    'tshirt',
    'cream',
    'rails',
    'cushions',
    'lanyard',
    'brick',
    'hallway',
    'cucumber',
    'wire fence',
    'fern',
    'tangerine',
    'windowsill',
    'pipes',
    'package',
    'wheelchair',
    'chips',
    'driveway',
    'tattoo',
    'side window',
    'stairway',
    'basin',
    'machine',
    'table lamp',
    'radio',
    'pony tail',
    'ocean water',
    'inside',
    'cargo',
    'overpass',
    'mat',
    'socket',
    'flower pot',
    'tree line',
    'sign post',
    'tube',
    'dial',
    'splash',
    'male',
    'lantern',
    'lipstick',
    'lip',
    'tongs',
    'ski suit',
    'trail',
    'passenger train',
    'bandana',
    'antelope',
    'designs',
    'tents',
    'photograph',
    "catcher's mitt",
    'electrical outlet',
    'tires',
    'boulders',
    'mannequin',
    'plain',
    'layer',
    'mushrooms',
    'strawberries',
    'piece',
    'oar',
    'bike rack',
    'slices',
    'arms',
    'fin',
    'shadows',
    'hood',
    'windshield wiper',
    'letter',
    'dot',
    'bus stop',
    'railings',
    'pebbles',
    'mud',
    'claws',
    'police car',
    'crown',
    'meters',
    'name tag',
    'entrance',
    'staircase',
    'shrimp',
    'ladies',
    'peak',
    'vines',
    'computer keyboard',
    'glass door',
    'pears',
    'pant',
    'wine glasses',
    'stall',
    'asphalt',
    'columns',
    'sleeve',
    'pack',
    'cheek',
    'baskets',
    'land',
    'day',
    'blocks',
    'courtyard',
    'pedal',
    'panel',
    'seeds',
    'balcony',
    'yellow',
    'disc',
    'young man',
    'eyebrows',
    'crumbs',
    'spinach',
    'emblem',
    'object',
    'bar',
    'cardboard',
    'tissue',
    'light post',
    'ski jacket',
    'seasoning',
    'parasol',
    'terminal',
    'surfing',
    'streetlight',
    'alley',
    'cords',
    'image',
    'jug',
    'antenna',
    'puppy',
    'berries',
    'diamond',
    'pans',
    'fountain',
    'foreground',
    'syrup',
    'bride',
    'spray',
    'license',
    'peppers',
    'passengers',
    'cement',
    'flags',
    'shack',
    'trough',
    'objects',
    'arches',
    'streamer',
    'pots',
    'border',
    'baseboard',
    'beer bottle',
    'wrist watch',
    'tile floor',
    'page',
    'pin',
    'items',
    'baseline',
    'hanger',
    'tree branch',
    'tusks',
    'donkey',
    'containers',
    'condiments',
    'device',
    'envelope',
    'parachute',
    'mesh',
    'hut',
    'butterfly',
    'salt',
    'restroom',
    'twig',
    'pilot',
    'ivy',
    'furniture',
    'clay',
    'print',
    'sandwiches',
    'lion',
    'shingles',
    'pillars',
    'vehicles',
    'panes',
    'shoreline',
    'stream',
    'control',
    'lock',
    'microphone',
    'blades',
    'towel rack',
    'coaster',
    'star',
    'petals',
    'text',
    'feather',
    'spots',
    'buoy'
]

VG_ATTRS = [
    "landing",
    "cut",
    "protective",
    "reflective",
    "number",
    "electronic",
    "green",
    "flowered",
    "larger",
    "yellow",
    "square",
    "looking down",
    "license",
    "in air",
    "straw",
    "playing tennis",
    "cutting",
    "smaller",
    "teddy",
    "close",
    "tied",
    "evergreen",
    "wooden",
    "daytime",
    "stacked",
    "sharp",
    "outstretched",
    "short sleeved",
    "bright yellow",
    "gray",
    "lying",
    "multi colored",
    "present",
    "covered",
    "pointed",
    "wavy",
    "bare",
    "kitchen",
    "barren",
    "blond",
    "lined",
    "in the air",
    "on",
    "bunch",
    "gravel",
    "apple",
    "some",
    "out",
    "dusty",
    "cloth",
    "written",
    "staring",
    "frosted",
    "patchy",
    "airborne",
    "modern",
    "wrinkled",
    "hazy",
    "rolled",
    "clock",
    "zebra",
    "wet",
    "hairy",
    "up",
    "rippled",
    "many",
    "power",
    "delicious",
    "athletic",
    "opened",
    "laying",
    "dirt",
    "porcelain",
    "traffic",
    "snowy",
    "inside",
    "cell",
    "sleeveless",
    "human",
    "fuzzy",
    "pine",
    "swimming",
    "street",
    "whole",
    "baseball",
    "closed",
    "chocolate",
    "male",
    "light brown",
    "rubber",
    "stainless",
    "curly",
    "designed",
    "for sale",
    "chrome",
    "grass",
    "leaning",
    "together",
    "skinny",
    "pointy",
    "partial",
    "decorative",
    "chain",
    "vintage",
    "reflected",
    "iron",
    "colored",
    "slanted",
    "backwards",
    "person's",
    "fake",
    "asphalt",
    "bright green",
    "hooded",
    "reading",
    "clay",
    "clear",
    "bathroom",
    "flower",
    "ocean",
    "flat",
    "glowing",
    "rolled up",
    "swinging",
    "lying down",
    "cotton",
    "cracked",
    "floor",
    "short",
    "potted",
    "bronze",
    "in the distance",
    "running",
    "wrapped",
    "watching",
    "palm",
    "waving",
    "deep",
    "solid",
    "dark colored",
    "in the picture",
    "open",
    "fire",
    "floral",
    "giant",
    "pale",
    "posing",
    "set",
    "food",
    "paved",
    "top",
    "wall",
    "outdoor",
    "skateboarding",
    "patterned",
    "vertical",
    "dressed",
    "body",
    "black and white",
    "snowboarding",
    "broken",
    "lit",
    "pair",
    "under",
    "above",
    "stone",
    "off white",
    "arched",
    "hard",
    "brick",
    "shirtless",
    "toy",
    "color",
    "maroon",
    "trash",
    "muddy",
    "chopped",
    "chain link",
    "double",
    "sparse",
    "crashing",
    "bending",
    "white",
    "upside down",
    "black",
    "burgundy",
    "bright blue",
    "splashing",
    "cute",
    "round",
    "heavy",
    "stained",
    "young",
    "purple",
    "pink",
    "drinking",
    "multicolored",
    "knit",
    "gold",
    "bottom",
    "bent",
    "huge",
    "rolling",
    "fresh",
    "skating",
    "tail",
    "cooked",
    "in the background",
    "bricked",
    "beautiful",
    "choppy",
    "background",
    "tiled",
    "holding",
    "sitting",
    "female",
    "straight",
    "pictured",
    "clean",
    "group",
    "cheese",
    "snow covered",
    "messy",
    "three",
    "small",
    "sunny",
    "snow",
    "held",
    "parked",
    "crossed",
    "leather",
    "building",
    "reflection",
    "alone",
    "illuminated",
    "brown",
    "falling",
    "grouped",
    "double decker",
    "cloudless",
    "woven",
    "passenger",
    "furry",
    "city",
    "jumping",
    "cardboard",
    "teal",
    "docked",
    "rectangle",
    "neon",
    "glass",
    "woman's",
    "overcast",
    "narrow",
    "sleeping",
    "glazed",
    "distance",
    "full",
    "down",
    "stuffed",
    "brass",
    "existing",
    "trimmed",
    "breaking",
    "bald",
    "light gray",
    "horizontal",
    "shiny",
    "red",
    "nice",
    "long sleeved",
    "crossing",
    "water",
    "curled",
    "different",
    "tan",
    "blue",
    "dark red",
    "seated",
    "leafless",
    "soccer",
    "laying down",
    "sitting down",
    "sandy",
    "wine",
    "navy blue",
    "plastic",
    "old",
    "electrical",
    "standing",
    "middle",
    "lime green",
    "bus",
    "girl's",
    "dark blue",
    "large",
    "far",
    "looking",
    "worn",
    "cream colored",
    "metallic",
    "talking",
    "edge",
    "hanging",
    "thin",
    "piece",
    "high",
    "flying",
    "fried",
    "tree",
    "outdoors",
    "blurry",
    "steel",
    "blonde",
    "blue and white",
    "man's",
    "older",
    "ski",
    "is white",
    "several",
    "turned",
    "safety",
    "empty",
    "pretty",
    "woman",
    "puffy",
    "part",
    "melted",
    "smooth",
    "elephant",
    "hot",
    "little",
    "dirty",
    "moving",
    "low",
    "ivory",
    "triangular",
    "cooking",
    "framed",
    "showing",
    "overhead",
    "crouching",
    "roman",
    "bushy",
    "healthy",
    "bright",
    "multi-colored",
    "fancy",
    "orange",
    "dry",
    "sliced",
    "beige",
    "red and white",
    "rough",
    "half",
    "blurred",
    "dead",
    "light skinned",
    "side",
    "cream",
    "grazing",
    "ceramic",
    "mini",
    "parking",
    "ripe",
    "folded",
    "tiny",
    "floppy",
    "happy",
    "stainless steel",
    "window",
    "baby",
    "man",
    "long sleeve",
    "lush",
    "oval",
    "stop",
    "american",
    "asian",
    "wire",
    "extended",
    "playing",
    "golden",
    "old fashioned",
    "light grey",
    "mesh",
    "lighted",
    "silver",
    "cloudy",
    "concrete",
    "used",
    "printed",
    "electric",
    "grilled",
    "wild",
    "foamy",
    "short sleeve",
    "grey",
    "smiling",
    "eating",
    "kneeling",
    "wide",
    "carpeted",
    "granite",
    "glassy",
    "floating",
    "one",
    "laptop",
    "wispy",
    "fallen",
    "plush",
    "light blue",
    "leafy",
    "skiing",
    "dried",
    "dark grey",
    "distant",
    "rocky",
    "metal",
    "mounted",
    "walking",
    "striped",
    "busy",
    "tile",
    "sticking out",
    "driving",
    "dark gray",
    "displayed",
    "dark",
    "dark green",
    "shining",
    "back",
    "rock",
    "raised",
    "person",
    "plaid",
    "ready",
    "filled",
    "aluminum",
    "in picture",
    "in distance",
    "rear",
    "surfing",
    "turned on",
    "painted",
    "light colored",
    "wearing",
    "here",
    "pizza",
    "circle",
    "stopped",
    "squatting",
    "colorful",
    "slice",
    "tinted",
    "murky",
    "grassy",
    "coffee",
    "plain",
    "peach",
    "wood",
    "transparent",
    "row",
    "nike",
    "adult",
    "four",
    "growing",
    "marble",
    "toilet",
    "light",
    "balding",
    "computer",
    "antique",
    "cold",
    "bear",
    "calm",
    "on display",
    "denim",
    "shaded",
    "navy",
    "tall",
    "attached",
    "checkered",
    "waiting",
    "fat",
    "off",
    "digital",
    "rainbow",
    "rusted",
    "dark brown",
    "burnt",
    "table",
    "decorated",
    "light green",
    "piled",
    "lit up",
    "patch",
    "baked",
    "khaki",
    "thick",
    "is black",
    "ornate",
    "dog",
    "spotted",
    "long",
    "still",
    "reflecting",
    "resting",
    "head",
    "shallow",
    "crouched",
    "pile",
    "standing up",
    "barefoot",
    "hardwood",
    "shredded",
    "winter",
    "behind",
    "faded",
    "tennis",
    "riding",
    "rusty",
    "single",
    "snow-covered",
    "rounded",
    "soft",
    "paper",
    "circular",
    "rectangular",
    "cement",
    "fluffy",
    "in background",
    "train",
    "curved",
    "big",
    "wicker",
    "pointing",
    "turquoise",
    "upright",
    "flat screen",
    "working",
    "new",
    "toasted",
]


@DATASETS.register_module()
class VisualGenome(CustomDataset):

    CLASSES = tuple(VG_CLASSES)
    MAX_ATTR_PER_BOX = 5

    def pad_attr(self, boxes_attr):
        padded = []
        pad_const = len(VG_ATTRS)
        for attr in boxes_attr:
            p = attr[:self.MAX_ATTR_PER_BOX] + [pad_const] * \
                max(0, self.MAX_ATTR_PER_BOX - len(attr))
            padded.append(p)
        return padded

    def load_annotations(self, ann_file):
        # ann_list = mmcv.list_from_file(ann_file)
        with open(ann_file, mode='r') as f:
            ann_list = json.load(f)

        data_infos = []
        for i, ann_line in enumerate(ann_list):
            if len(ann_line['boxes']) == 0:
                continue

            width = ann_line['width']
            height = ann_line['height']

            bboxes = np.array(ann_line['boxes'])
            bboxes[:, 0::2] = np.clip(bboxes[:, 0::2], 1, width - 1)
            bboxes[:, 1::2] = np.clip(bboxes[:, 1::2], 1, height - 1)
            labels = ann_line['class_id']
            # attrs = [[3] * random.randint(1, 3)] * len(labels)
            attrs = self.pad_attr(ann_line['attribute_idx'])
            try:
                labels = np.array(labels).astype(np.int64)
                attrs = np.array(attrs).astype(np.int64)
                bboxes = bboxes.astype(np.float32)

            except:
                import pdb; pdb.set_trace()
            data_infos.append(
                dict(
                    filename=ann_line['image_name'],
                    width=width,
                    height=height,
                    ann=dict(
                        bboxes=bboxes,
                        labels=labels,
                        attrs=attrs)
                ))

        return data_infos

    def get_ann_info(self, idx):
        return self.data_infos[idx]['ann']
