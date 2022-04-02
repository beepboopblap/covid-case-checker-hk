from bs4 import BeautifulSoup
import requests

url = 'https://alea.care/resources/hong-kong-guide-to-coronavirus-covid19'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find('li')
results = str(results)
updated = soup.find_all('div', class_="lastUpdate teal lora-Bold")
updated = str(updated)
vaccine_num = soup.find_all('li')
cases_today = results.split()
updated_data = updated.split()
final = cases_today[0]
final = final.replace("<li>", "")
update_list = [updated_data[6], " ",updated_data[7]," ", updated_data[8]]
final_update = ''.join(update_list)
final_update = final_update.replace("</div>", "")
final_update = final_update.replace("'","")
final_update = final_update.replace("]", "")
print("\n")
print("Covid Cases Today in Hong Kong")
print("Last updated:", final_update ,"\n")
print("Cases:",final)
print("\n")


