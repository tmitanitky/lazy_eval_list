class lazy_eval_list(list):
    # when used with bisect method, func must be monotonically increasing function
    def __init__(self, func, a, memorize=True):
        super().__init__(a)
        self._func = func
        self._eval = {}
        
    def __getitem__(self, key):
        if type(key) is int:
            return self.__evaluate__(super().__getitem__(key))
        elif type(key) is slice:
            return [self.__evaluate__(item) for item in super().__getitem__(key)]
        
    def __evaluate__(self, item):
        if item not in self._eval:
            self._eval[item] = self._func(item)
        return self._eval[item]
    
    def __repr__(self):
        return 'lazy_eval_list({}, {})'.format(self._func, super().__repr__())
