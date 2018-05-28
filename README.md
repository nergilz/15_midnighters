## Night Owls Detector

---

The script find out who sent the tasks for verification after 24:00 before 5:00

### Discription

+ The script requests to API [devman.org](htttps//:devman.org)
+ Get midnight coders form 24:00 to 5:00 o'clock
+ You need a [devman API](https://devman.org/api/challenges/solution_attempts/?page=1)
+ You need a library [requests](http://docs.python-requests.org/en/master/user/quickstart/)
+ and library [pytz](http://pytz.sourceforge.net/)
+ It is recommended to use [virtualenv](https://docs.python.org/3/library/venv.html) 


### How to install requests and pytz
```bash
pip install -r requirements.txt
```

### Start script example

```bash
python3 seek_dev_nighters.py
```

### Example result
```bash
id215639888
id45197784
id311542249
dreamfall3r
nick__korolev
id185085967
 Time script: 8.784622794000825
```

### Requirements

```bash
Python ver 3.5 (or higher)
```

---

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
