def compress(string):
  if len(string) == 0:
    return string
  parts = []
  current_letter = string[0]
  current_count = 1
  for letter in string[1:]:
    if current_letter == letter:
      current_count += 1
    else:
      parts.append(current_letter + str(current_count))
      current_letter = letter
      current_count = 1
  print(parts)
  parts.append(current_letter + str(current_count))
  print(parts)
  compressed = "".join(parts)
  return compressed
  #if len(compressed) < len(string):
  #  print (compressed)
  #else:
  #  print(string)

print(compress("aasseederr"))