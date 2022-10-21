def make_generators_generator(g):
    """Generates all the "sub"-generators of the generator returned by
    the generator function g.

    >>> def every_m_ints_to(n, m):
    ...     i = 0
    ...     while (i <= n):
    ...         yield i
    ...         i += m
    ...
    >>> def every_3_ints_to_10():
    ...     for item in every_m_ints_to(10, 3):
    ...         yield item
    ...
    >>> for gen in make_generators_generator(every_3_ints_to_10):
    ...     print("Next Generator:")
    ...     for item in gen:
    ...         print(item)
    ...
    Next Generator:
    0
    Next Generator:
    0
    3
    Next Generator:
    0
    3
    6
    Next Generator:
    0
    3
    6
    9
    """
    "*** YOUR CODE HERE ***"
    """
    ##########Version1-begin
    length = len(list(g()))

    def generators_generator(i):
        iters = g()
        for _ in range(i): 
            yield next(iters)
    
    for i in range(length):
        yield generators_generator(i+1)
    #########Version1-end
    """
    """version2-begin""" 
    def make_pre_gene(g):
        def pre_gene():
            yield from iter(list(g())[:-1])
        return pre_gene
    if len(list(g())) == 1:
        yield g()
    else:
        yield from make_generators_generator(make_pre_gene(g))
        yield g() 
    """version2-end""" 