def main():
  with open('books/frankenstein.txt') as f:
    file_contents = f.read()
  
  count = count_words(file_contents)
  chars = dict(sorted(count_char(file_contents).items(), key=lambda item: item[1], reverse=True))

  print('--- Begin report of books/frankenstein.txt ---')
  print(f'{count} words found in the document')
  print()
  
  for key in chars:
    print(f"The '{key}' character was found {chars[key]} times")
  
  print('--- End report ---')


def count_words(string):
  words = string.split()

  return len(words)

def count_char(string):
  char_dict = {}
  for char in string:
    if char.isalpha():
      if char.lower() in char_dict:
        char_dict[char.lower()] += 1
      else:
        char_dict[char.lower()] = 1
  
  return char_dict

main()
