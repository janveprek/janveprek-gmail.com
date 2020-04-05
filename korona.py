import csv
from datetime import date

from bs4 import BeautifulSoup
import urllib.request

if __name__ == "__main__":
  with urllib.request.urlopen('https://onemocneni-aktualne.mzcr.cz/covid-19') as url:
      content = url.read()
  soup = BeautifulSoup(content, 'html.parser')

  upper_text_tests = soup.find('p', {'class' : 'mb-5 text--center text--white'}).text
  number_of_tests = soup.find('p', {'id' : 'count-test'}).text
  lower_text_tests = soup.find('p', {'id' : 'last-modified-tests'}).text

  upper_text_sick = 'Celkový počet osob s prokázaným onemocněním COVID-19'
  number_of_sick = soup.find('p', {'id' : 'count-sick'}).text
  lower_text_sick = soup.find('p', {'id' : 'last-modified-datetime'}).text

  upper_text_recovered = soup.find('p', {'class' : 'mb-5 text--body-text-color text--center'}).text
  number_of_recovered = soup.find('p', {'id' : 'count-recover'}).text
  lower_text_recovered = soup.find('p', {'class' : 'h3 mt-10 text--center'}).text

  upper_text_dead = soup.findAll('p', {'class' : 'mb-5 text--body-text-color text--center'})[1].text
  number_of_dead = soup.find('p', {'id' : 'count-dead'}).text
  lower_text_dead = soup.findAll('p', {'class' : 'h3 mt-10 text--center'})[1].text

  json = {"phonetype": "N95", "cat": "WP"};

  with open('korona'+str(date.today())+'.txt', "w", encoding="utf-8") as text_file:
      print(upper_text_tests+' '+number_of_tests+' '+lower_text_tests, file=text_file)
      print(upper_text_sick+' '+number_of_sick+' '+lower_text_sick, file=text_file)
      print(upper_text_recovered+' '+number_of_recovered+' '+lower_text_recovered, file=text_file)
      print(upper_text_dead+' '+number_of_dead+' '+lower_text_dead, file=text_file)

  with open('korona'+str(date.today())+'.csv', mode='w', encoding="utf-8") as corona_file:
      corona_writer = csv.writer(corona_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      corona_writer.writerow([upper_text_tests,number_of_tests,lower_text_tests])
      corona_writer.writerow([upper_text_sick,number_of_sick,lower_text_sick])
      corona_writer.writerow([upper_text_recovered,number_of_recovered,lower_text_recovered])
      corona_writer.writerow([upper_text_dead,number_of_dead,lower_text_dead])
