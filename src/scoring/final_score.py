from src.jd_parser.parse_jd import JD_REQUIREMENTS


def score_experience(experience):
    """
    Score candidate experience (0-35)
    """

    score = 0

    years = experience["years_of_experience"]

    if 5 <= years <= 9:
        score += 15
    elif years >= 3:
        score += 10
    else:
        score += 5

    title = experience["current_title"].lower()

    preferred_titles = [
        t.lower()
        for t in JD_REQUIREMENTS["preferred_titles"]
    ]

    if any(t in title for t in preferred_titles):
        score += 10

    descriptions = " ".join(
        experience["career_descriptions"]
    ).lower()

    important_words = [
        "recommendation",
        "retrieval",
        "ranking",
        "embedding",
        "vector",
        "search",
        "production",
        "llm",
        "machine learning",
        "ml"
    ]

    matches = 0

    for word in important_words:
        if word in descriptions:
            matches += 1

    score += min(matches, 10)

    return score


def score_skills(skill_data):
    """
    Score skills (0-30)
    """

    score = 0

    required = [
        s.lower()
        for s in JD_REQUIREMENTS["required_skills"]
    ]

    preferred = [
        s.lower()
        for s in JD_REQUIREMENTS["preferred_skills"]
    ]

    for skill in skill_data["skills"]:

        name = skill["name"].lower()

        if any(req.lower() in name for req in required):
            score += 3

        if any(pref.lower() in name for pref in preferred):
            score += 2

        if skill["proficiency"] == "advanced":
            score += 1

    return min(score, 30)


def score_behavior(signals):
    """
    Score behavioral signals (0-20)
    """

    score = 0

    if signals["open_to_work_flag"]:
        score += 5

    if signals["notice_period_days"] <= 30:
        score += 5

    if signals["github_activity_score"] > 50:
        score += 3

    if signals["recruiter_response_rate"] > 0.5:
        score += 3

    if signals["interview_completion_rate"] > 0.8:
        score += 2

    if signals["willing_to_relocate"]:
        score += 2

    return score


def score_education(education):

    score = 0

    for edu in education["education"]:

        field = edu["field_of_study"].lower()

        if "computer" in field:
            score += 3

        if edu["tier"] == "tier_1":
            score += 2

    return min(score, 5)


def calculate_final_score(
    experience,
    skills,
    signals,
    education,
):

    experience_score = score_experience(experience)
    skill_score = score_skills(skills)
    behavior_score = score_behavior(signals)
    education_score = score_education(education)

    total = (
        experience_score
        + skill_score
        + behavior_score
        + education_score
    )

    return {
        "experience_score": experience_score,
        "skill_score": skill_score,
        "behavior_score": behavior_score,
        "education_score": education_score,
        "total_score": total,
    }