import requests

def main():
	baseLink = input("Inserte link base del anime (https://www5.jkanime.video/NOMBRE_ANIME/)")
	totalChapters = int(input("Total de capitulos?"))
	
	for i in range(totalChapters):
		url = baseLink + f'{i + 1}/'
		print('-------------------------------------')
		print('baseLink:', url)
		response = requests.get(url)
		print("Links del capitulo:", i + 1)
		links = []
		linkFrom = 0 
		linkTo = -1
		

		while (linkFrom >= 0):
			linkFrom = response.text.find('data-video', linkFrom + 10)
			if(linkFrom != -1):
				linkTo = response.text.find(' title', linkFrom + 10)

			if(linkFrom != -1 and linkTo != -1 and linkTo > linkFrom):
				obj = response.text[linkTo + 8: response.text.find('"', linkTo + 10)] + ': ' + response.text[linkFrom + 12: linkTo - 2]
				links.append(obj)

		for i in links:
			print(i)


if __name__ == "__main__":
	main()