def calculate_score(q1, q2, q3):
    score = 0

    if q1 == "Solving technical problems":
        score += 2

    if q2 == "Computer Science":
        score += 2

    if q3 == "Working with computers":
        score += 2

    if q1 == "Helping and communicating with people":
        score += 2

    if q1 == "Creating designs and visuals":
        score += 2

    if q1 == "Managing and organizing things":
        score += 2

    if q2 == "Business":
        score += 2

    if q2 == "Arts and Design":
        score += 2

    if q2 == "Teaching and Education":
        score += 2

    if q3 == "Working with people":
        score += 2

    if q3 == "Creating new ideas":
        score += 2

    if q3 == "Planning and managing":
        score += 2

    return score