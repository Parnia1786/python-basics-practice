# Multi Score Calculator - Calculate average exam score and final grade

total_scores = []

suffixes = ["st", "nd", "rd"]
while True:
    try:
        exam_num = len(total_scores) + 1
        if exam_num > 3:
            suffix = "th"
        else:
            suffix = suffixes[exam_num-1]
        score = input(f"What score did you get on your {exam_num}{suffix} exam (q to quit)? ").strip()
        if score.lower() in ["q", "quit"]:
            break
        score = float(score)
        if not 0 <= score <= 100:
            print("Invalid score. Score must be 0 to 100.")
            continue
        total_scores.append(score)
    except ValueError:
        print("Invalid score. Score must be a number.")

if total_scores:
    total = sum(total_scores)
    mean = total / len(total_scores)
    print("\nTotal exams:", len(total_scores))
    print("Scores:", total_scores)
    print(f"Average score: {mean:.2f}")
    if 90<=mean:
        grade = "Excellent 🎉\n"
    elif 70<=mean:
        grade = "Good 🙂\n"
    elif 50<=mean:
        grade = "Pass 😐\n"
    elif mean<50:
        grade = "Fail 😢\n"
    print(grade)
else:
    print("\nNo scores were entered.\n")
