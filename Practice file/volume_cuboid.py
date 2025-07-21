def cuboid_volume(side):
    """
    Calculates the volume of a cube (a special type of cuboid where all sides are equal).
    It expects a numeric input (int or float).
    """
    # Ensure 'side' is treated as a number.
    # If this function were to take string input, it would need a try-except float(side) conversion.
    # For now, we assume the caller passes a number, as tests do.
    return side * side * side

# --- Code below this line will ONLY run when volume_cuboid.py is executed directly ---
# --- It will NOT run when this file is imported by test_volume_cuboid.py ---
if __name__ == "__main__":
    print("--- Running volume_cuboid.py directly for demonstration ---")

    # Example usage with numbers
    print("The volume of cuboid (side 2):", cuboid_volume(2))
    print("The volume of cuboid (side 1.1):", cuboid_volume(1.1))
    print("The volume of cuboid (side -2.5):", cuboid_volume(-2.5))