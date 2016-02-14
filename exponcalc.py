import subprocess
	#An exponents calculator developed by Pixelshower89
music = subprocess.Popen(["afplay", "./soundtrack.wav"])
print('Hello, and welcome to the Exponents calculator!  X will be raised to the power of Y')
raw_x = raw_input("What will X be? ")
raw_y = raw_input('What will Y be? ')
if raw_y.isdigit()==True and raw_x.isdigit()==True:
	X=int(raw_x)
	Y=int(raw_y)
	result=X**Y
	print(result)
	print("Thank you for using Pixelshower89's Exponents calculator")
else:
	print("Using letters will crash the program.  Please us numbers in the future.")
	print("thank you for using Pixelshower89's Exponents calculator")

music.kill()
