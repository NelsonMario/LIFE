import requests
import tensorflow as tf
symptoms = []

symptoms.append("9")
symptoms.append("10")
symptoms.append("11")

def listToString():
    symptomString = ""
    symptomsLen = len(symptoms)
    for index, x in enumerate(symptoms):
        symptomString = symptomString + x
        if index < symptomsLen - 1:
            symptomString = symptomString + ","

    return symptomString

symptomString = listToString()

r = requests.get("https://sandbox-healthservice.priaid.ch/diagnosis?symptoms=["+symptomString+"]&gender=male&year_of_birth=2000&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im5lbHNvbi5sYXRmQGdtYWlsLmNvbSIsInJvbGUiOiJVc2VyIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvc2lkIjoiNjYzMyIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IjIwMCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGltaXQiOiI5OTk5OTk5OTkiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXAiOiJQcmVtaXVtIiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9sYW5ndWFnZSI6ImVuLWdiIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiMjA5OS0xMi0zMSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbWVtYmVyc2hpcHN0YXJ0IjoiMjAyMC0wMy0xNSIsImlzcyI6Imh0dHBzOi8vc2FuZGJveC1hdXRoc2VydmljZS5wcmlhaWQuY2giLCJhdWQiOiJodHRwczovL2hlYWx0aHNlcnZpY2UucHJpYWlkLmNoIiwiZXhwIjoxNTg0MzI5NzY4LCJuYmYiOjE1ODQzMjI1Njh9.jdgbaCuPyy0-EV4Y3nf0txSPhJANld7dWlypqJGLf7k&format=json&language=en-gb")

print(r.text)
