The followings are the syntax of each csv files
################################################

title_link2.csv : separator is "; "
[course title]; [link for course details]

title_provider2.csv : separator is ";% "       (could consider redo later with separate rows?)
[course title]; [provider]; ... [provider]

course_competencies2.csv : separator is ";% "
[course title];% [competency title];% [link for competency performance statement]
*** Sorting is done by exhausting all the competencies in a single [course_title], then move on to the next [course_title]
*** Note that it may have duplicate [course title] since 1 course may have multiple [competency title]
*** And same [competency title] may reappear at different [course_title]


competencies_link.csv : separator is ";% "			(because ";" is used in some descriptions)
[competency title];% [competency code];% [description];% [link for competency performance statement];% [pdf link]
*** course_competencies2 and competencies_link.csv could NOT be merged together directly

jobroles_link_only.csv : separator is ","
[job_role],[link for job role details]

job_group.csv : separator is ";"
[job_role];[functional group];[job_family];[also known as]

job_competency.csv : separator is ";"
[job_role];[competency]

job_nocompetency.csv : separator is ";"   (this is the list of job roles with no competency details available)
[job_role];[link for job role details]

Total 525 [competency_title]
	  458 [course_title]
	  1389 combinations (course & competency)
	  
	  273 [job_role]
	  59 out of 273 job roles have no competency info available (empty zip)
	  2502 combinations (job_role & competency)

##############################
###Python files

## Actual Web Scrap (loop to open webpages on browser)

# Loop multiple web pages
NICF_loop.py -> title_link2.csv (open single nicf_training_courses.html)
			 -> title_provider2.csv (same as above, but commentted out)

job_loop.py -> job_competency.csv  (open jobroles_link_only.csv) #-> onejob_html.py as prototype
			-> job_group.csv

read_csv_url.py -> course_competencies2.csv (open title_link2.csv)  #a list of links for course details ->individual_course_html.py as prototype



# Single-page Web Scrap
Job_Roles.py -> jobroles_link.csv (open single Job_Roles.html)


#############################################
## Debug with one page (local saved)
Competencies.py -> competencies_link.csv  (open single Competencies.html)




