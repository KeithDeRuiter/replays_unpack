#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables

from interfaces.EntityLookuper import EntityLookuper
from interfaces.TransactionAPI import TransactionAPI



class Login(EntityLookuper, TransactionAPI):
    
    g_onKickedFromServer = EventHook()
    
    g_receiveLoginQueueNumber = EventHook()
    
    def __init__(self):
        self.id = None
        self.position = None


        self._accountDBID_s = None


        # MRO fix

        EntityLookuper.__init__(self)

        TransactionAPI.__init__(self)

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            (10000000000, 'accountDBID_s'),
            
        ])
        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        self._methods.extend([
            (10000000001, 'onKickedFromServer'),
            (73, 'receiveLoginQueueNumber'),
            
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

# method size: 10000000001
    @unpack_func_args(['UINT32', 'UINT8', 'STRING'])
    def onKickedFromServer(self, arg1, arg2, arg3):
        self.g_onKickedFromServer.fire(self, arg1, arg2, arg3)
# method size: 73
    @unpack_func_args(['UINT8', 'UINT64'])
    def receiveLoginQueueNumber(self, arg1, arg2):
        self.g_receiveLoginQueueNumber.fire(self, arg1, arg2)


    ####################################
    #       PROPERTIES
    ####################################

# property size: 10000000000
    @property
    def accountDBID_s(self):
        return self._accountDBID_s

    @accountDBID_s.setter
    def accountDBID_s(self, value):
        self._accountDBID_s, = unpack_variables(value, ['STRING'])


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