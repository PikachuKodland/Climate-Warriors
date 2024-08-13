--main.py
# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)


if __name__ == "__main__":
    app.run(debug=True)


--index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0"
    />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link rel="stylesheet" href="../static/css/style.css" />
    <title>İklim Savaşçıları</title>
</head>
<body>
    <header class="header">
      <nav class="header__nav main-nav">
        <ul class="main-nav__list main-list">
          <li class="main-list__item list-item">
            <a class="list-item__link" href="#about">Fabrikalar</a>
          </li>
          <li class="main-list__item list-item">
            <a class="list-item__link" href="#skills">Ormansızlaşma</a>
          </li>
          <li class="main-list__item list-item">
            <a class="list-item__link" href="#feedback">Güneş Panelleri</a>
          </li>
        </ul>
      </nav>
    </header>
    <main class="main">
      <!-- Home Section -->
      <section class="main__home home" id="home">
        <video class="home__video" autoplay loop muted playsinline>
          <source src="../static/videos/fabrika.mp4" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
        <h1 class="home__title">İKLİM SAVAŞÇILARI</h1>
        <p class="home__subtitle">BİR ŞEYLER ÖĞRENMENİN VAKTİ GELDİ!</p>
      </section>
      
      <!-- Factories and Their Effects Section -->
      <section class="main__about about" id="about">
        <h2 class="about__title">Fabrikalar ve Zararları</h2>
        <div class="info-block">
          <img
            class="info-block__img"
            src="../static/img/İklim Savaşçıları.png"
            alt="Fabrikalar"
            width="450"
            height="450"
          />
          <video class="info-block__video" autoplay loop muted playsinline>
            <source src="../static/videos/Ormansızlaşma.mp4" type="video/mp4" />
            Your browser does not support the video tag.
          </video>
          <p class="info-block__text">
            Fabrikalar, modern yaşamın bel kemiğidir ve ekonomik kalkınmanın önemli bir parçasıdır. Ancak, bu büyük endüstriyel yapılar çevre üzerinde çeşitli olumsuz etkiler bırakmaktadır. İşte fabrikaların çevreye verdiği başlıca zararlar:
            <br /><br />
            <strong>Hava Kirliliği:</strong> Fabrikalar, üretim süreçlerinde çeşitli gazlar ve partiküller yayarak hava kalitesini düşürür. Bu kirleticiler, solunum yolları hastalıklarına ve genel sağlık sorunlarına yol açabilir.
            <br /><br />
            <strong>Su Kirliliği:</strong> Endüstriyel atıklar genellikle su kaynaklarına karışarak nehirleri, gölleri ve yer altı su kaynaklarını kirletir. Bu kirlilik, su ekosistemlerine zarar verir ve insan sağlığı için risk oluşturur.
            <br /><br />
            <strong>Toprak Kirliliği:</strong> Fabrikalar, kimyasal sızıntılar ve atıklar yoluyla toprağın kirlenmesine neden olabilir. Kirlenmiş toprak, tarımsal ürünlerin kalitesini düşürebilir ve gıda güvenliğini tehdit edebilir.
            <br /><br />
            <strong>Doğal Kaynakların Tükenmesi:</strong> Fabrikalar, büyük miktarda doğal kaynak tüketir ve bu da kaynakların tükenmesine neden olabilir. Özellikle su ve enerji kaynakları, endüstriyel üretim için yoğun şekilde kullanılır.
            <br /><br />
            <strong>İklim Değişikliği:</strong> Fabrikalar, sera gazı emisyonları yoluyla iklim değişikliğine katkıda bulunur. Karbon dioksit ve diğer sera gazları, küresel ısınmayı hızlandırarak iklim dengesini bozabilir.
            <br /><br />
            Bu olumsuz etkileri azaltmak için fabrikaların daha sürdürülebilir üretim yöntemlerine geçmesi, atık yönetimini iyileştirmesi ve çevre dostu teknolojilere yatırım yapması gerekmektedir. Çevremizi korumak için hem bireylerin hem de endüstrilerin üzerlerine düşen sorumlulukları yerine getirmesi büyük önem taşımaktadır.
          </p>
        </div>
      </section>

      <!-- Deforestation Section -->
      <section class="main__skills skills" id="skills">
        <h2 class="skills__title">Ormansızlaşma ve Zararları</h2>
        <ul class="skills__list skills-list">
          <li class="skills-list__skill skill">
            <p class="skill__text">
              Ormansızlaşma, doğal ormanların kesilmesi veya yok edilmesi sonucu meydana gelen bir çevre sorunudur. Bu durum, ekosistemlerin dengesini bozarak çevresel ve iklimsel etkiler yaratır. Ormanların azalması, birçok olumsuz sonuca yol açar:
              <br /><br />
              <strong>Biyolojik Çeşitliliğin Kaybı:</strong> Ormanlar, çeşitli bitki ve hayvan türlerine ev sahipliği yapar. Ormansızlaşma, bu türlerin yaşam alanlarını kaybetmelerine neden olur, bu da türlerin yok olma riskini artırır.
              <br /><br />
              <strong>İklim Değişikliği:</strong> Ormanlar, karbondioksiti emerek atmosferdeki sera gazlarını azaltır. Ağaçların kesilmesi, bu karbonun tekrar atmosfere salınmasına neden olur ve iklim değişikliğine katkıda bulunur.
              <br /><br />
              <strong>Toprak Erozyonu:</strong> Ağaç kökleri toprağı sabitlemeye yardımcı olur. Ormanların yok olması, toprağın yerinden oynayarak erozyona neden olur ve bu da tarım arazilerini ve su kaynaklarını olumsuz etkiler.
              <br /><br />
              <strong>Su Döngüsünün Bozulması:</strong> Ormanlar, yağışları toplayarak yeraltı su seviyelerini düzenler. Ormansızlaşma, su döngüsünün bozulmasına ve kuraklık gibi su sıkıntısı sorunlarına yol açar.
              <br /><br />
              <strong>Yerel İklim Değişiklikleri:</strong> Ormanlar, yerel iklimi düzenlemekte önemli bir rol oynar. Ormansızlaşma, sıcaklıkların artmasına ve hava koşullarının değişmesine neden olabilir.
              <br /><br />
              <strong>Yerel Toplumların Yaşamları:</strong> Birçok yerel topluluk, ormanlardan doğrudan geçimlerini sağlar. Ormansızlaşma, bu toplulukların yaşamlarını ve geçim kaynaklarını tehdit eder.
              <br /><br />
              Ormansızlaşmayı önlemek ve ormanları korumak, bu olumsuz etkilerin önüne geçmek için kritik öneme sahiptir. Sürdürülebilir orman yönetimi ve koruma çabaları, gelecekteki nesiller için çevresel dengenin korunmasına yardımcı olabilir.
            </p>
          </li>
        </ul>
      </section>

      <!-- Solar Panels Section -->
      <section class="main__feedback feedback" id="feedback">
        <h2 class="feedback__title">Güneş Paneli ve Kullanmamanın  Zararları</h2>
        <video class="panel__video" autoplay loop muted playsinline>
          <source src="../static/videos/Güneş Paneli.mp4" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
        <p class="feedback__text">
          Güneş panelleri, yenilenebilir enerji kaynakları arasında en popüler olanlardan biridir ve çevre dostu enerji üretiminin önemli bir parçasıdır. Ancak, her teknolojide olduğu gibi, güneş panellerinin de bazı çevresel etkileri ve potansiyel zararları bulunmaktadır:
          <br /><br />
          <strong>Üretim Süreci:</strong> Güneş panellerinin üretim süreci, çeşitli kimyasal maddelerin kullanıldığı ve enerji tüketiminin yüksek olduğu bir süreçtir. Bu üretim sürecinde kullanılan malzemeler ve enerji kaynakları, çevreye bazı etkilerde bulunabilir.
          <br /><br />
          <strong>Malzeme Kullanımı:</strong> Güneş panelleri, nadir bulunan metaller ve diğer malzemeler içerir. Bu malzemelerin çıkarılması ve işlenmesi, çevresel etkiler yaratabilir ve bu süreçte oluşan atıklar çevreye zarar verebilir.
          <br /><br />
          <strong>Toprak ve Arazi Kullanımı:</strong> Geniş güneş paneli tarlaları, büyük miktarda arazi kullanımını gerektirebilir. Bu da doğal yaşam alanlarının tahrip olmasına ve toprak erozyonuna yol açabilir.
          <br /><br />
          <strong>Atık Yönetimi:</strong> Güneş panellerinin ömrü sona erdiğinde, geri dönüşüm veya atık yönetimi gereklidir. Panellerin geri dönüşümü sırasında bazı zararlı maddeler çevreye salınabilir.
          <br /><br />
          <strong>Su Kullanımı:</strong> Güneş paneli üretimi ve temizliği sırasında su kullanılmaktadır. Su tüketimi, su kaynakları üzerinde baskı oluşturabilir.
          <br /><br />
          Güneş panellerinin çevresel etkilerini en aza indirmek için sürdürülebilir üretim ve geri dönüşüm yöntemlerinin geliştirilmesi önemlidir. Yenilenebilir enerji kaynaklarına geçiş, fosil yakıtların çevresel etkilerini azaltmada önemli bir adımdır, ancak bu süreçte çevresel sürdürülebilirlik dikkate alınmalıdır.
        </p>
      </section>
    </main>
</body>
</html>


 --css
 
/* Global Styles */
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: rgb(70, 64, 122);
  color: #333;
  line-height: 1.6;
}

img,
video {
  max-width: 100%;
  height: auto;
}

/* Header Styles */
.header {
  background-color: rgb(68, 64, 102);
  color: #fff;
  padding: 1rem 0;
}

.header__nav {
  display: flex;
  justify-content: center;
  align-items: center;
}

.main-nav__list {
  list-style: none;
  display: flex;
  gap: 1rem;
  padding: 0;
}

.list-item__link {
  color: #fd6702;
  text-decoration:none;
  font-weight: bold;
  transition: color 0.3s ease-in-out;
}


.list-item__link:hover {
  color: #f4f4f9;
}

/* Main Styles */
.main {
  padding: 2rem;
}

/* Home Section */
.home {
  position: relative;
  text-align: center;
  color: white;
}

.home__video {
  width: 100%;
  height: auto;
  display: block;
}

.home__title {
  position: absolute;
  top: 20%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 5rem;
  margin: 0;
  background-color: rgb(54, 52, 70);
  padding: 15px; /* Yazının etrafına boşluk eklemek için */
  border-radius: 10px; /* Köşeleri yuvarlamak için */
  display: inline-block; /* Yalnızca yazı alanını kaplayacak şekilde */
  color:#fd6702
}

.home__subtitle {
  position: absolute;
  top: 30%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 1.9rem;
  margin: 0;
  background-color: rgb(68, 64, 102);
  padding: 10px; /* Yazının etrafına boşluk eklemek için */
  border-radius: 5px; /* Köşeleri yuvarlamak için */
  display: inline-block; /* Yalnızca yazı alanını kaplayacak şekilde */
  color:#ffc400
}

/* About Section */
.about {
  padding: 2rem;
  background-color: #f4f4f9;
}

.about__title {
  font-size: 2.5rem;
  text-align: center;
}

.info-block {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
  align-items: center;
}

.info-block__img,
.info-block__video {
  flex: 1 1 300px;
}

.info-block__text {
  flex: 1 1 300px;
  font-size: 1rem;
}

/* Skills Section */
.skills {
  padding: 2rem;
  background-color: #e9ecef;
}

.skills__title {
  font-size: 2.5rem;
  text-align: center;
}

.skills__list {
  list-style: none;
  padding: 0;
}

.skill__text {
  font-size: 1rem;
  line-height: 1.8;
  margin: 1rem 0;
}

/* Feedback Section */
.feedback {
  padding: 2rem;
  background-color: #f4f4f9;
}

.feedback__title {
  font-size: 2.5rem;
  text-align: center;
}

.feedback__text {
  font-size: 1rem;
  line-height: 1.8;
  margin: 1rem 0;
}

.panel__video {
  width: 100%;
  height: auto;
  display: block;
}
