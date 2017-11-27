import attr


@attr.s(slots=True)
class InterbaseInterval:
    start = attr.ib(validator=attr.validators.instance_of(int))
    end = attr.ib(validator=attr.validators.instance_of(int))

    def __str__(self):
        return "<{},{}>".format(self.start, self.end)


    def abuts(a, b):
        """Return True if a and b "touch" the same interbase coordinate without overlapping (symmetric)"""
        return a.start == b.end or a.end == b.start


    def coincides_with(a, b):
        """Return True if a == b or a `intersects` b (symmetric)"""
        return a == b or a.intersects(b)


    def encloses(a, b):
        """Returns True if `a` is within `b`, including when `a==b`.

        """

        return a.start <= b.start <= a.end and a.start <= b.end <= a.end


    def intersects(a, b):
        """Return True if `b.start` or `b.end` is in (`a.start`, `a.end`)
        -or- the symmetric comparison is True. (symmetric)

        A zero-width Interval may intersect a non-zero-width Interval.

        """
        def intersect_1way(x, y):
            return x.start < y.start < x.end or x.start < y.end < x.end
        return intersect_1way(a, b) or intersect_1way(b, a)


    def overlap(a, b):

        """Returns overlap of a and b (symmetric)

        Cases:
        * overlap  < 0 when a and b do not overlap
        * overlap == 0 when a and b abut or at least one is zero width
        * overlap  > 0 when a and b overlap

        """

        return min(a.end, b.end) - max(a.start, b.start)


    def overlaps(a, b):
        """Returns True if a and b overlap by at least one nucleotide position (symmetric)

        """
        return a.overlap(b) > 0
