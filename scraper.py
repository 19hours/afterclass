import json
import csv

# column_name = ["CourseCode", "Description"]

# req = '''{
# 	"nodes": [
# 		{
# 			"interesting": true,
# 			"practical": true,
# 			"fairGradingCourse": false,
# 			"gainedNewSkills": false,
# 			"manageableWorkloadCourse": false,
# 			"isAnonymous": true,
# 			"experience": "The mod is a good balance between social sci and IS. You learn how to use skills in both departments to come up with your reports/group projects. You learn skills like how to do analysis on google trends, twitter, instagram and many more. In terms of bidding, don't bid so high since the majority of the students will be from SMT and it's compulsory for them to take the mod. The workload is quite intense, I find myself doing work every week. The practical lessons are not conducted very smoothly so be prepared for a lot of self learning too. But the mod is useful overall.",
# 			"improvement": "The grading for the module is not very clear. In fact I find it quite biased (based on first impressions on a too short presentation time). Additionally, she has higher expectations in terms of what kind of analysis you do but she does not teach you how to do it. Again, a lot of self learning. ",
# 			"score": 4,
# 			"createdAt": "2021-06-26T14:00:17+08:00",
# 			"upvotes": 0,
# 			"userId": "5bea7606-4d9c-455d-bfda-19715c12b53f",
# 			"userFirstName": "Anonymous",
# 			"userLastName": null,
# 			"smumodsReview": false,
# 			"id": "77f32f5a-b886-4d20-9a57-d3ab0d98ea54",
# 			"userVote": 0,
# 			"course": {
# 				"courseCode": "SMT203",
# 				"description": "Globally, there is an increasing trend towards the transitioning from ‘cities’ to ‘smart cities’. It is often envisioned that by leveraging ICT (information and communications technology), smart cities can enable its dwellers to improve their overall quality of lives across different domains – such as health, work and play. In this course, you will learn how to design, develop and manage these smart city systems. In addition, you will learn about the issues, considerations and principles, in the management of smart city solutions.",
# 				"__typename": "Course"
# 			},
# 			"__typename": "Review"
# 		},
# 		{
# 			"interesting": true,
# 			"practical": true,
# 			"fairGradingCourse": true,
# 			"gainedNewSkills": true,
# 			"manageableWorkloadCourse": true,
# 			"isAnonymous": true,
# 			"experience": "This mod builds upon your knowledge in IS/SMT111 (intro to programming (python)) AND IS112 (data management), so it was really an eye-opener in terms of how those mods can help you build something bigger. In my case, it was an app. If you want to know how to use APIs, create your own application (be it on the web or telebot), this is the mod for you. We were in groups of 6 (can form your team) so if your team can evenly split up the work it will be manageable. There were 2 paired assignments as well, can choose your pair. One of the most useful mods I've taken in SMU.",
# 			"improvement": null,
# 			"score": 4,
# 			"createdAt": "2020-06-24T21:20:31+08:00",
# 			"upvotes": 1,
# 			"userId": "bffe4ced-8b85-4640-9794-f42863e94c66",
# 			"userFirstName": "Anonymous",
# 			"userLastName": null,
# 			"smumodsReview": true,
# 			"id": "742c906f-ebb8-4704-a727-5a8d132fd76f",
# 			"userVote": 0,
# 			"course": {
# 				"courseCode": "SMT203",
# 				"description": "Globally, there is an increasing trend towards the transitioning from ‘cities’ to ‘smart cities’. It is often envisioned that by leveraging ICT (information and communications technology), smart cities can enable its dwellers to improve their overall quality of lives across different domains – such as health, work and play. In this course, you will learn how to design, develop and manage these smart city systems. In addition, you will learn about the issues, considerations and principles, in the management of smart city solutions.",
# 				"__typename": "Course"
# 			},
# 			"__typename": "Review"
# 		}
# 	]
# }'''

data = json.loads(req, strict=False)

with open("reviews.csv", "a") as f:
  for review in data["nodes"]:
    writer = csv.writer(f)
    # CourseCode,Experience,Improvement,Interesting,Practical,FairGradingCourse,GainedNewSkills,ManageableWorkloadCourse,FirstName,LastName,CourseDescription,CreatedAt
    courseCode = review["course"]["courseCode"]
    courseDescription = review["course"]["description"]
    if courseDescription:
      courseDescription = courseDescription.replace("\n", " ").strip()
    experience = review["experience"]
    if experience:
      experience = experience.replace("\n", " ").strip()
    improvement = review["improvement"]
    if improvement:
      improvement = improvement.replace("\n", " ").strip()
    interesting = review["interesting"]
    practical = review["practical"]
    fairGradingCourse = review["fairGradingCourse"]
    gainedNewSkills = review["gainedNewSkills"]
    manageableWorkloadCourse = review["manageableWorkloadCourse"]
    firstName = review["userFirstName"]
    if firstName:
      firstName = firstName.strip()
    lastName = review["userLastName"]
    if lastName:
      lastName = lastName.strip()
    createdAt = review["createdAt"]
    writer.writerow([
      courseCode, 
      experience, 
      improvement, 
      interesting, 
      practical, 
      fairGradingCourse, 
      gainedNewSkills, 
      manageableWorkloadCourse, 
      firstName,
      lastName,
      courseDescription,
      createdAt
    ])
