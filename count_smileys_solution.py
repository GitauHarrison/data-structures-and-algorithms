def count_smileys(arr):
    valid_faces = [':D', ':-D', ':~D', ';-D', ';D', ';~D',
                    ':)', ':-)', ';)', ';-)', ':~)', ';~)']
    num_smiley_faces = 0
    for face in valid_faces:
        if face in arr:
            num_smiley_faces += 1
    print( num_smiley_faces)

count_smileys([])
