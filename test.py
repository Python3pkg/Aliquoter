from aliquoter import aliquot, Quad, Point

print(aliquot(
            Quad(
                nw=Point(lat=4, int=0),
                sw=Point(lat=0, int=0),
                ne=Point(lat=4, int=4),
                se=Point(lat=0, int=4),
            ),
            ['SW', 'SW', 'E']
        ))

