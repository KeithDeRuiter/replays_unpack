#      DO NOT CHANGE THIS FILE     #
# FILE WAS GENERATED AUTOMATICALLY #

from def_generator.events import EventHook
from operator import itemgetter

from def_generator.decorators import unpack_func_args, unpack_variables




class AvatarObserver(object):
    
    def __init__(self):
        self.id = None
        self.position = None


        self._remoteCamera = None

        self._isObserverFPV = None

        self._observerFPVControlMode = None

        self._numOfObservers = None


        # MRO fix

        self._properties = getattr(self, '_properties', [])
        self._properties.extend([
            (168, 'remoteCamera'),
            (8, 'isObserverFPV'),
            (8, 'observerFPVControlMode'),
            (8, 'numOfObservers'),
            
        ])
        # sort properties by size
        self._properties.sort(key=itemgetter(0))

        self._methods = getattr(self, '_methods', [])
        self._methods.extend([
            
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



    ####################################
    #       PROPERTIES
    ####################################

# property size: 168
    @property
    def remoteCamera(self):
        return self._remoteCamera

    @remoteCamera.setter
    def remoteCamera(self, value):
        self._remoteCamera, = unpack_variables(value, ['REMOTE_CAMERA_DATA'])
# property size: 8
    @property
    def isObserverFPV(self):
        return self._isObserverFPV

    @isObserverFPV.setter
    def isObserverFPV(self, value):
        self._isObserverFPV, = unpack_variables(value, ['BOOL'])
# property size: 8
    @property
    def observerFPVControlMode(self):
        return self._observerFPVControlMode

    @observerFPVControlMode.setter
    def observerFPVControlMode(self, value):
        self._observerFPVControlMode, = unpack_variables(value, ['UINT8'])
# property size: 8
    @property
    def numOfObservers(self):
        return self._numOfObservers

    @numOfObservers.setter
    def numOfObservers(self, value):
        self._numOfObservers, = unpack_variables(value, ['UINT8'])


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