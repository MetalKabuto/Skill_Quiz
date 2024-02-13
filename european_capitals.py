# Det här skriptet innehåller en uppsättning frågor och tillhörande svar för en kunskapstävling om Europas huvudstäder.

# Skapar en samling benämnd 'european_capitals'.
# Varje post i denna samling är ett par (en sorts datastruktur för att lagra två relaterade data) bestående av två textsträngar:
# den första textsträngen ställer en fråga om vilken stad som är huvudstad i ett specifikt europeiskt nation,
# medan den andra textsträngen ger det korrekta namnet på denna huvudstad.

european_capitals = [
    ("Vad är huvudstaden i Albanien?", "Tirana"),
    ("Vad är huvudstaden i Andorra?", "Andorra la Vella"),
    ("Vad är huvudstaden i Armenien?", "Jerevan"),
    ("Vad är huvudstaden i Österrike?", "Wien"),
    ("Vad är huvudstaden i Azerbajdzjan?", "Baku"),
    ("Vad är huvudstaden i Vitryssland?", "Minsk"),
    ("Vad är huvudstaden i Belgien?", "Bryssel"),
    ("Vad är huvudstaden i Bosnien och Hercegovina?", "Sarajevo"),
    ("Vad är huvudstaden i Bulgarien?", "Sofia"),
    ("Vad är huvudstaden i Kroatien?", "Zagreb"),
    ("Vad är huvudstaden i Cypern?", "Nicosia"),
    ("Vad är huvudstaden i Tjeckien?", "Prag"),
    ("Vad är huvudstaden i Danmark?", "Köpenhamn"),
    ("Vad är huvudstaden i Estland?", "Tallinn"),
    ("Vad är huvudstaden i Finland?", "Helsingfors"),
    ("Vad är huvudstaden i Frankrike?", "Paris"),
    ("Vad är huvudstaden i Georgien?", "Tbilisi"),
    ("Vad är huvudstaden i Tyskland?", "Berlin"),
    ("Vad är huvudstaden i Grekland?", "Aten"),
    ("Vad är huvudstaden i Ungern?", "Budapest"),
    ("Vad är huvudstaden i Island?", "Reykjavik"),
    ("Vad är huvudstaden i Irland?", "Dublin"),
    ("Vad är huvudstaden i Italien?", "Rom"),
    ("Vad är huvudstaden i Kosovo?", "Pristina"),
    ("Vad är huvudstaden i Lettland?", "Riga"),
    ("Vad är huvudstaden i Liechtenstein?", "Vaduz"),
    ("Vad är huvudstaden i Litauen?", "Vilnius"),
    ("Vad är huvudstaden i Luxemburg?", "Luxemburg"),
    ("Vad är huvudstaden i Malta?", "Valletta"),
    ("Vad är huvudstaden i Moldavien?", "Chisinau"),
    ("Vad är huvudstaden i Monaco?", "Monaco"),
    ("Vad är huvudstaden i Montenegro?", "Podgorica"),
    ("Vad är huvudstaden i Nederländerna?", "Amsterdam"),
    ("Vad är huvudstaden i Nordmakedonien?", "Skopje"),
    ("Vad är huvudstaden i Norge?", "Oslo"),
    ("Vad är huvudstaden i Polen?", "Warszawa"),
    ("Vad är huvudstaden i Portugal?", "Lissabon"),
    ("Vad är huvudstaden i Rumänien?", "Bukarest"),
    ("Vad är huvudstaden i Ryssland?", "Moskva"),
    ("Vad är huvudstaden i San Marino?", "San Marino"),
    ("Vad är huvudstaden i Serbien?", "Belgrad"),
    ("Vad är huvudstaden i Slovakien?", "Bratislava"),
    ("Vad är huvudstaden i Slovenien?", "Ljubljana"),
    ("Vad är huvudstaden i Spanien?", "Madrid"),
    ("Vad är huvudstaden i Sverige?", "Stockholm"),
    ("Vad är huvudstaden i Schweiz?", "Bern"),
    ("Vad är huvudstaden i Turkiet?", "Ankara"),
    ("Vad är huvudstaden i Ukraina?", "Kiev"),
    ("Vad är huvudstaden i Storbritannien?", "London"),
    ("Vad är huvudstaden i Vatikanstaten?", "Vatikanstaten"),
]

# Denna samling är tänkt att användas inom ramen för en geografisk tävling där programvaran slumpvis väljer en frågeställning från listan,
# visar den för spelaren, och spelaren måste ange vad hen tror är den rätta huvudstaden.
# Efteråt kan programmet jämföra spelarens angivna svar mot det andra elementet i det utvalda paret
# för att bestämma om svaret var korrekt eller ej.
