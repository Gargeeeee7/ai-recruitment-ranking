def extract_experience(candidate):
    """
    Extract basic experience-related information from a candidate.
    """

    profile = candidate["profile"]
    career_history = candidate["career_history"]
    descriptions = []
    for job in career_history:
        descriptions.append(job["description"])
    experience = {
        "years_of_experience": profile["years_of_experience"],
        "current_title": profile["current_title"],
        "current_company": profile["current_company"],
        "current_industry": profile["current_industry"],
        "career_descriptions": descriptions,
    }

    return experience