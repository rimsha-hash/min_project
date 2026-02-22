data=[1,2,3,4,5,6,7,8,9,10]
it=iter(data)
while True:
    try:
      print(next(it))
    except Exception as e:
        break
      