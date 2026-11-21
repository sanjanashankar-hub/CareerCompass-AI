def calculate_match(career, interest, skill, q1, q2, q3):
    match = 0

    if career == "Cybersecurity Analyst":
        if interest == "Cybersecurity":
            match += 40
        if skill == "Problem Solving":
            match += 20
        if q1 == "Solving technical problems":
            match += 15
        if q2 == "Computer Science":
            match += 15
        if q3 == "Working with computers":
            match += 10

    elif career == "Security Specialist":
        if interest == "Cybersecurity":
            match += 35
        if skill == "Problem Solving":
            match += 15
        if q1 == "Solving technical problems":
            match += 20
        if q2 == "Computer Science":
            match += 20
        if q3 == "Working with computers":
            match += 10

    elif career == "Cyber Forensics Analyst":
        if interest == "Cybersecurity":
            match += 30
        if skill == "Problem Solving":
            match += 15
        if q1 == "Solving technical problems":
            match += 20
        if q2 == "Computer Science":
            match += 15
        if q3 == "Working with computers":
            match += 20

    return match