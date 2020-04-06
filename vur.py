import requests
for x in range(100):
    r = requests.post("http://cats.iku.edu.tr/portal/relogin", data={"eid":"test123","pw":"asd123","submit":"Giriş"})
    print(x + ".istek / dönen =>" +r.status_code)
