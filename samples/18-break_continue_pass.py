x = range(1, 11)
for number in x:
    if number == 8:  # will print all without the 8
        # continue # continue the loop from the beginning without printing.
        # break  # will break the loop it self on 8
        pass  # will pass the condition to the loop and print the 8
        # you can use it if you still update your if condition and wanna to pass the value till finished.
    print(number)