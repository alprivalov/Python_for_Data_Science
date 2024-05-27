class calculator:

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
    1.  Creation d'une array de comprehension en multipliant
        """
        print("Dot product is:", sum([cr * V2[i] for i, cr in enumerate(V1)]))

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
    1.  Creation d'une array de comprehension en additionnant
        """
        print("Add Vector is:", [cr + V2[i] for i, cr in enumerate(V1)])

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
    1.  Creation d'une array de comprehension en soustrayant
        """
        print("Sous Vector is:", [cr - V2[i] for i, cr in enumerate(V1)])
