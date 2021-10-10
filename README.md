# VTU-Results-Crawler-Selenium

The web crawler script ([vtuselenium.py](https://github.com/anantmoudgalya/VTU-Results-Crawler-Selenium/blob/master/vtuselenium.py)) can be used to scrape results from the VTU Results website.

This script automates the process of checking results of a student on the VTU Results website, which is very slow if done manually.

There were a couple of challenges faced while writing this script to achieve the goal of automating result collection.

1. The captcha in the form had to be bypassed. Which was done by taking a screenshot of the captcha image in the form, and then an OCR package (pytesseract) was used to detect captcha text in the same.
2. The script had to handle for the results being randomized in a table, i.e, first row might be the Computer Networks score for one student, but not for another, which was solved by using regular expressions based on the course code (15CS51 is the Computer Networks course code for everyone), to ensure correctness.

Then the final GPA was calculated based on these scores and all the results were saved in a neat CSV file. 
All of this can be accomplished in under 5 minutes with this script.

### NOTE: This script worked for the 2018 and 2019 versions of the VTU Results page, please make changes as necessary for the later versions.
