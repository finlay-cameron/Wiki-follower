#Imports
from json import dump, load
from selenium import webdriver
from selenium.webdriver.common.by import By

#Config
ses = webdriver.Chrome() #Can be set to different browser (not tested)
fileName = "data.json" #Where to dump the data to
loops = 500

#Mainloop
indexes = 0 #In case of while loop
try:
    for i in range(loops): #Change to "while True:" to go until you interupt.
        urls = []
        ses.get("https://en.wikipedia.org/wiki/Special:Random") #Set to a custom page if you want
        while True:
            name=ses.find_element(By.ID, "firstHeading").text
            if (ses.current_url, name) in urls:
                urls.append((ses.current_url, name))
                print(f"Page {len(urls)}: {name}")
                message = "Loop found."
                break
            urls.append((ses.current_url, name))
            print(f"Page {len(urls)}: {name}")
            Links = ses.find_element(By.ID, "mw-content-text").find_elements(By.TAG_NAME, "a")
            Lindex = 0
            try:
                while Links[Lindex].get_property("href").startswith(ses.current_url) or "disambiguation" in Links[Lindex].get_property("href") or ":" in Links[Lindex].get_property("href").split(".org/wiki/")[-1] or not Links[Lindex].get_property("href").startswith("https://en.wikipedia.org/wiki/") or Links[Lindex].get_property("class") == "mw-disambig":
                    Lindex+=1
            except IndexError:
                message = "No valid url found."
                break
            ses.get(Links[Lindex].get_property("href"))

        print(f"Loop {indexes} stopped, reason: {message}\nThere were {len(urls)} pages.\nData dumped to {fileName}.\n")

        with open(fileName, "r") as f:
            dat = load(f)
        dat.append(urls)
        with open(fileName, "w") as f:
            dump(dat, f)
        indexes+=1
except KeyboardInterrupt:
    print(f"stopped at {indexes} loops")

ses.close()