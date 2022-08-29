def count_smileys(arr):
    """Find the number of smiley faces in a list"""

    # 1. List all possible smiley faces
    valid_faces = [':D', ':-D', ':~D', ';-D', ';D', ';~D',
                    ':)', ':-)', ';)', ';-)', ':~)', ';~)']
    num_smiley_faces = 0

    # 2. Loop through the list of possible smiley faces
    for face in valid_faces:
        # 3. Find of the a smiley face is located in the question array
        if face in arr:
            # 4. If found, update the count of smiley faces by 1
            num_smiley_faces += 1

    # 5. Return the total number of smiley faces found
    return num_smiley_faces

count_smileys([])
