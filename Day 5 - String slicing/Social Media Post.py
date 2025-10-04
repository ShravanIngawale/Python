# Sample news article
article = "The Indian Space Research Organisation (ISRO) successfully launched the Gaganyaan test vehicle from Sriharikota on Saturday morning. This marks a significant step toward India's ambitious human spaceflight mission led by top scientists."

# 1. Summary (first 51 chars)
summary = article[:51]

# 2. Organization name (ISRO)
organization = article[40:44]

# 3. Mission name
mission = article[72:81]

# 4. Location (slice "Shriharikota")
location = article[99:111]

# 5. Day (slice "Saturday")
day = article[115:123]

# 6. Last sentence as impact statement
impact = article[-66:-16]

# 7. Create short headline
headline = "🚀 " + organization + " Launches " + mission + " on " + day + " at" + location 

# 8. Slice keyword tags
tag1 = "#" + mission
tag2 = "#" + organization
tag3 = "#SpaceMission"

# 9. Reporter's note (slice and reuse intro)
report_note = "Report: " + article[:38] + "..."

# 10. Final post (combine all)
final_post = headline + "\n\n" + summary + "...\n" + impact[:50] + "...\n\n" + tag1 + " " + tag2 + " " + tag3 + "\n" + report_note

print("Headline:", headline + "\n")
print("Summary:", summary + "..." + "\n")
print("Impact:", impact + "..." + "\n")
print("Tags:", tag1, tag2, tag3)
print("Note:", report_note)
print("\nFinal Social Media Post:\n")
print(final_post)