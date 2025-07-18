# ------------------- Simulando contents de data/countries.py -------------------
countries = [
  'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
  'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
  'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin',
  'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei',
  'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada',
  'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi',
  'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire",
  'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti',
  'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador',
  'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia',
  'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany',
  'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana',
  'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq',
  'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan',
  'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan',
  'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein',
  'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia',
  'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius',
  'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco',
  'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
  'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan',
  'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
  'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda',
  'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino',
  'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro',
  'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
  'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan',
  'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan',
  'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago',
  'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine',
  'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay',
  'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen',
  'Zambia', 'Zimbabwe',
]

# ---------------- Simulando contents de data/countries_data.py ----------------
countries_data = [
    {'name': 'China', 'population': 1411778724, 'languages': ['Chinese']},
    {'name': 'India', 'population': 1380004385, 'languages': ['Hindi', 'English']},
    {'name': 'United States', 'population': 331893745, 'languages': ['English']},
    {'name': 'Indonesia', 'population': 273523621, 'languages': ['Indonesian']},
    {'name': 'Pakistan', 'population': 220892331, 'languages': ['Urdu', 'English']},
    {'name': 'Brazil', 'population': 212821986, 'languages': ['Portuguese']},
    {'name': 'Nigeria', 'population': 206139587, 'languages': ['English']},
    {'name': 'Bangladesh', 'population': 164689383, 'languages': ['Bengali']},
    {'name': 'Russia', 'population': 145912025, 'languages': ['Russian']},
    {'name': 'Mexico', 'population': 128932753, 'languages': ['Spanish']},
]

# --------------------- Código que usa esas variables --------------------------
from collections import Counter

def nivel_3():
    # Países que contienen 'land'
    paises_con_land = [pais for pais in countries if 'land' in pais]
    print("Países que contienen 'land':")
    print(paises_con_land)

    # Invertir lista de frutas usando un bucle
    frutas = ['banana', 'orange', 'mango', 'lemon']
    frutas_invertidas = []
    for i in range(len(frutas) - 1, -1, -1):
        frutas_invertidas.append(frutas[i])
    print("\nFrutas en orden inverso:")
    print(frutas_invertidas)

    # Número total de idiomas únicos
    idiomas_unicos = set()
    for pais in countries_data:
        for idioma in pais['languages']:
            idiomas_unicos.add(idioma)
    print(f"\nNúmero total de idiomas únicos: {len(idiomas_unicos)}")

    # Top 10 idiomas más hablados
    contador_idiomas = Counter()
    for pais in countries_data:
        for idioma in pais['languages']:
            contador_idiomas[idioma] += 1
    print("\nTop 10 idiomas más hablados:")
    for idioma, cantidad in contador_idiomas.most_common(10):
        print(f"{idioma}: hablado en {cantidad} países")

    # Top 10 países más poblados
    paises_poblacion = [(pais['name'], pais['population']) for pais in countries_data]
    paises_poblacion.sort(key=lambda x: x[1], reverse=True)
    print("\nTop 10 países más poblados:")
    for nombre, poblacion in paises_poblacion[:10]:
        print(f"{nombre}: {poblacion:,} habitantes")

if __name__ == "__main__":
    nivel_3()
