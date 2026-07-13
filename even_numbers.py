number = list(map(int,input("Enter a list of integers separated by spaces :").split()))
even_numbers = list(filter(lambda x: x%2 ==0 , number))
squared_even_numbers = list(map(lambda x: x**2, even_numbers))
print("squared even numbers:", squared_even_numbers)
