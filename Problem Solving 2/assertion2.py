def check_name(name):
  assert isinstance(name, str), "The submitted input is not a string"
  
  return name.upper()

print(check_name("alif"))

print(check_name(123))