import attr


@attr.s(slots=True)
class InterbaseInterval:
    start = attr.ib(validator=attr.validators.instance_of(int))
    end = attr.ib(validator=attr.validators.instance_of(int))

    def __str__(self):
        return "<{},{}>".format(self.start, self.end)


    def encloses(a, b):
        """Returns True if `a` fully encloses `b`, including when `a==b`.

        """

        return a.start <= b.start <= a.end and a.start <= b.end <= a.end


    def overlap(a, b):
        """Returns overlap of a and b.

        Cases:
        * overlap  < 0 when a and b do not overlap
        * overlap == 0 when a and b abut or at least one is zero width
        * overlap  > 0 when a and b overlap

        """

        return min(a.end, b.end) - max(a.start, b.start)


    def overlaps(a, b):
        """Returns True if a and b overlap (including by zero-width
        coordinate)

        """
        return a.overlap(b) >= 0


    def within(a, b):

        """Returns True if b `encloses` a

        """  

        return b.start <= a.start <= b.end and b.start <= a.end <= b.end

