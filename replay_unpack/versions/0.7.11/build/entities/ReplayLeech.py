#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class ReplayLeech(object):
    
    g_onCheckGamePing = EventHook()
    
    g_replayFromBeginning = EventHook()
    
    g_syncChunk = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None



        # MRO fix

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            
        ])
        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        self._methods.extend([
            (65, 'onCheckGamePing'),
            (10000000001, 'replayFromBeginning'),
            (10000000001, 'syncChunk'),
            
        ])
        # sort methods by size
        self._methods.sort(key=itemgetter(0))
        return

    @property
    def attributesMap(self):
        d = {}
        for i, (_, name) in enumerate(self._properties):
            d[i] = name
        return d

    @property
    def methodsMap(self):
        d = {}
        for i, (_, name) in enumerate(self._methods):
            d[i] = name
        return d

    ####################################
    #      METHODS
    ####################################

# method size: 65
    @unpack_func_args(['UINT64'])
    def onCheckGamePing(self, arg1):
        self.g_onCheckGamePing.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def replayFromBeginning(self, arg1):
        self.g_replayFromBeginning.fire(self, arg1)
# method size: 10000000001
    @unpack_func_args(['BLOB'])
    def syncChunk(self, arg1):
        self.g_syncChunk.fire(self, arg1)


    ####################################
    #       PROPERTIES
    ####################################



    def get_summary(self):
        print '~' * 60
        print 'Entity name: ', self.__class__.__name__
        print 'Total entity client properties: {:>5}'.format(len(self._properties))
        print 'Total entity client methods: {:>5}'.format(len(self._methods))

        print
        print 'Listing entity properties:'
        print '{:>4} {:>40}'.format('idx', 'property name')
        for i, p in self.attributesMap.items():
            print '{:>4} {:>40}'.format(i, p)

        print
        print 'Listing entity methods:'
        print '{:>4} {:>40}'.format('idx', 'method name')
        for i, p in self.methodsMap.items():
            print '{:>4} {:>40}'.format(i, p)
        print '~' * 60
        print
        print


    def __repr__(self):
        d = {}
        for _, p in self._properties:
            d[p] = getattr(self, p)
        return "<{}> {}".format(self.__class__.__name__, d)