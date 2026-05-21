"""A program to plan a tea party."""

__author__: str = "730700758"


def main_planner(guests: int) -> None:
    """Plan the tea party."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(
                tea_count=tea_bags(people=guests),
                treat_count=treats(people=guests),
            )
        )
    )


def tea_bags(people: int) -> int:
    """Calculate tea bags needed."""
    return people * 2


def treats(people: int) -> int:
    """Calculate treats needed."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate total cost."""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
