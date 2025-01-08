

def calculate_area(length, width):
    """
        This function calculates the area of a rectangle.

        Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle

    Returns:
    float: The area of the rectangle
    """
    # Calculate area
    area = length * width
    return area

if __name__ == "__main__":
    # Define the length and width of the rectangle
    length = 5.0  # Length in meters
    width = 3.0   # Width in meters

    # Calculate the area using the calculate_area function
    area = calculate_area(length, width)

    print(f"The area of the rectangle is {area} square meters.")
