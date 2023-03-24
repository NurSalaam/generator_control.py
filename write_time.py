import requests
import datetime
import time


def write_start_time():
  url = 'https://api.sheety.co/226fefa2280cad2f32bd32f74162c63b/generatorControl/time'
  current_date = datetime.date.today()
  formatted_date = current_date.strftime('%Y-%m-%d')
  current_time = datetime.datetime.now().time()
  formatted_time = current_time.strftime('%H:%M:%S')

  headers = {
    # "Authorization": "Bearer antonius_379",
    "Content-Type": "application/json",
  }

  payload = {
    "#": '',
    "startDate": f"{formatted_date}",
    "endDate": '',
    "startTime": f"{formatted_time}",
    "endTime": ''
  }
  response = requests.post(url, headers=headers, json={"time": payload})
  print(response.text)


def write_stop_time():
  id = _get_last_id()
  url = f'https://api.sheety.co/226fefa2280cad2f32bd32f74162c63b/generatorControl/time/{id}'
  current_date = datetime.date.today()
  formatted_date = current_date.strftime('%Y-%m-%d')
  current_time = datetime.datetime.now().time()
  formatted_time = current_time.strftime('%H:%M:%S')

  headers = {
    # "Authorization": "Bearer antonius_379",
    "Content-Type": "application/json",
  }

  payload = {
    "#": '',
    "endDate": f"{formatted_date}",
    "endTime": f"{formatted_time}"
  }
  response = requests.put(url, headers=headers, json={"time": payload})
  print(response.text)


def _get_last_id():
  url = 'https://api.sheety.co/226fefa2280cad2f32bd32f74162c63b/generatorControl/time'

  response = requests.get(url)
  data = response.json()
  last_entry = data['time'][-1]
  id = last_entry['id']
  print(id)

  return id


write_start_time()
time.sleep(3)
write_stop_time()