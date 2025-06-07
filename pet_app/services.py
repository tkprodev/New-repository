"""Services for the pet application."""


def calculate_adoption_fee(pet: dict) -> int:
    """Return a simple adoption fee based on pet age."""
    base_fee = 50
    if pet.get("age", 0) < 2:
        return base_fee + 20
    return base_fee
