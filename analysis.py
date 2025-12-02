import pandas as pd
from flask import Flask, render_template
import matplotlib.pyplot as plt

app = Flask(__name__)

df = pd.read_excel("filmler.xlsx")


#En yüksek puanlı
top_film=df.nlargest(1,"IMDB Puanı").iloc[0]

#En düşük puanlı
lower_film=df.nsmallest(1,"IMDB Puanı").iloc[0]

#En uzun süreli film
max_time=df.nlargest(1,"Süre").iloc[0]

#En kısa süreli film
min_time=df.nsmallest(1,"Süre").iloc[0]


#Tür başına film sayısı
tur_count=df.groupby("Tür")["Film Adı"].count()



#Grafikler

#Yıllara göre film sayısı
film_per_year=df.groupby("Yıl")["Film Adı"].count()
plt.figure(figsize=(10,5))
plt.plot(film_per_year.index,film_per_year.values,"b")
plt.title("Yıllara Göre Film Sayısı")
plt.xlabel("Yıl")
plt.ylabel("Film Sayısı")
plt.savefig("static/film_per_year.png")
plt.close()


#Türlere göre ortalama IMDB puanı
film_per_score=df.groupby("Tür")["IMDB Puanı"].mean()
plt.figure(figsize=(10,5))
plt.plot(film_per_score.index,film_per_score.values,"b")
plt.title("Türlere Göre Ortalama IMDB Puanı")
plt.ylabel("Puan")
plt.savefig("static/film_per_score.png")
plt.close()


#Türlere göre film sayısı
film_type=df.groupby("Tür")["Film Adı"].count()
plt.figure(figsize=(10,5))
plt.plot(film_type.index,film_type.values,"b")
plt.title("Türlere Göre Film Sayısı")
plt.ylabel("Sayı")
plt.savefig("static/film_type.png")
plt.close()




@app.route("/")
def index():
    return render_template(
        "index.html",
        top_film=top_film,
        lower_film=lower_film,
        max_time=max_time,
        min_time=min_time
    )

app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True)