while True:
    try:
        score = float(input("What score did you get on your exam? "))
        if not 0 <= score <= 100:
            print("Score must be between 0 and 100. Try again.")
            continue
        if score >= 90:
            grade = "Excellent 🎉"
        elif score >= 70:
            grade = "Good 🙂"
        elif score >= 50:
            grade = "Pass 😐"
        else:
            grade = "Fail 😢"
        print(grade)
        break
    except ValueError:
        print("Score must be a number. Try again.")
