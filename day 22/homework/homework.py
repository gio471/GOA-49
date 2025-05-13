def function(age):
    if age < 18:
        return "You got discount"
    else:
        return "You didn't get discount"
    
manual_reverse = "Hello"
print(manual_reverse[::-1])

test_string = "Hello World"

print(test_string.upper())
print(test_string.lower())
print(test_string.capitalize())
print(test_string.swapcase())
print(test_string.find("H"))
print(test_string.find("World"))
print(test_string.find("X"))


# მეთოდები ობიექტის წევრები არიან და კონკრეტულად იმ ობიექტის მონაცემებზე მუშაობენ.
# მაგალითად, "Hello".upper()-ში .upper() მეთოდი მუშაობს "Hello" სტრიქონზე.მეთოდები ობიექტზე დამოკიდებულია,
# და ისინი უკეთესად აღწერენ ობიექტზე მოქმედებებს. ეს ხდის მათ სახელის უფრო ლოგიკურს.
# Dot notation იყენებს წერტილს (.) ობიექტის სახელისა და მისი თვისების ან მეთოდის გამოძახებისთვის.
