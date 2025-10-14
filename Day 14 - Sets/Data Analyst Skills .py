skills_required = {"Python", "SQL", "Excel", "Statistics", "Data Visualization"}
skills_i_have = {"Python", "Excel"}
print("Required Skills:", skills_required)

common_skills = skills_required.intersection(skills_i_have)
print("\nSkills i already have:", common_skills)

skills_i_have.add("SQL")
print("Update my skills:", skills_i_have)

missing_skills = skills_required.difference(skills_i_have)
print("\nSkills you still need to learn:", missing_skills)

has_all_skills = skills_i_have.issuperset(skills_required)
print("Do you have all required skills?", has_all_skills)

backup_skills = skills_i_have.copy()
print("\nBackup of your skills:", backup_skills)