#### **1. Ülevaade**  
Arvehaldussüsteem on veebipõhine lahendus, mis on loodud **Django ja Bootstrap 4** abil, et pakkuda **kasutajasõbralikku, efektiivset ja automatiseeritud arveldamise lahendust**. See võimaldab **arvete loomist, haldamist, saatmist ja maksmist**, kasutades **Stripe'i makselahendust**. Süsteem toetab **PDF-arvete genereerimist, e-posti teel saatmist ja staatuse jälgimist**. Lisaks pakub see kasutajatele turvalist **autentimist ja autoriseerimist** Django **User Authentication System** abil.

https://github.com/arvutionu2015m/arvehaldussusteem/blob/main/Kuvat%C3%B5mmis%202025-03-20%20071815.png

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://myoctocat.com/assets/images/base-octocat.svg)

#### **2. Peamised Funktsioonid**  
✅ **Kasutaja autentimine** – sisse- ja väljalogimine, registreerimine.  
✅ **Arvete loomine** – kliendi andmete, maksesumma, maksude ja arve staatuse lisamine.  
✅ **PDF-arvete genereerimine** – kasutades **ReportLab**, et luua professionaalseid PDF-formaadis arveid.  
✅ **E-posti arve saatmine** – võimaldab arveid klientidele saata **automaatse e-kirjaga**.  
✅ **Maksmise integreerimine Stripe'iga** – kasutajad saavad maksta **QR-koodi ja Stripe'i Checkouti kaudu**.  
✅ **Staatused ja filtreerimine** – arved on jaotatud **Makstud, Ootel, Ületähtaegne**.  
✅ **Bootstrap 4 responsiivne disain** – sobib **mobiili-, tahvli- ja töölauavaatele**.  
✅ **Jaluse (sticky footer) ja kasutajaliidese täiustused** – parem navigeerimine, aktiivsete lehtede esiletõstmine.

---

#### **3. Tehnoloogiad ja Struktuur**  
- **Backend:** Django (Python), SQLite/PostgreSQL, Django Authentication.  
- **Frontend:** Bootstrap 4, HTML, CSS, JavaScript.  
- **Arvete PDF genereerimine:** ReportLab.  
- **Makselahendused:** Stripe API.  
- **Hosting ja Deployment:** **Docker, Nginx, Gunicorn (tootmises)**.  

**Projekt kasutab MVC arhitektuurimustrit (Model-View-Controller), kus:**  
📌 **Models (`models.py`)** – andmebaasi struktuur, sh. Invoice, User.  
📌 **Views (`views.py`)** – äritsükkel ja loogika (arve loomine, maksehaldus).  
📌 **Templates (`home.html`, `create_invoice.html`, `invoice_detail.html`)** – dünaamilised HTML-lehed Bootstrapiga.  

---

#### **4. Turvalisus ja Andmekaitse**  
🔒 **CSRF Token** – Django CSRF-kaitse igas vormis.  
🔒 **Paroolihashimine** – Django autentimine hoiab kasutaja paroole turvaliselt.  
🔒 **Stripe PCI-DSS vastavus** – maksete töötlemine on turvaline.  
🔒 **SQL Injection ja XSS kaitse** – Django ORM välistab SQL-injection rünnakud.  

---

#### **5. Kasutajate Eelised ja Kasutajaliides**  
💼 **Ettevõtetele ja freelanceritele mõeldud lahendus** – lihtne ja kiire arveldamine.  
📩 **Automaatne arve saatmine e-postiga** – kliendid saavad e-kirjaga PDF-arve.  
📊 **Statistika ja filtreerimine** – kiire ülevaade tasumata ja makstud arvete kohta.  
📱 **Mobiilisõbralik ja kiire disain** – sobib igas seadmes kasutamiseks.  

---

#### **6. Edasised Täiustused ja Arendustegevused**  
🚀 **Tulevikus plaanitavad uuendused:**  
✅ **Tume režiim (Dark Mode)** – valikuline disain mugavaks kasutamiseks.  
✅ **Mitme valuuta ja keele tugi** – laiem haare rahvusvaheliste klientide jaoks.  
✅ **Automaatne kordusarvete saatmine** – tellimusel põhinevate teenuste jaoks.  
✅ **CSV ja Excel ekspordi võimalus** – arveandmete eksport Exceli tabelitena.  

---

### **📌 Kokkuvõte**
**Arvehaldussüsteem** on **efektiivne, skaleeritav ja kasutajasõbralik veebipõhine lahendus**, mis **automatiseerib arveldamise protsessi**. Kasutades **Django** ja **Bootstrap 4**, pakub see **mugavat navigeerimist, professionaalseid PDF-arveid, turvalist maksete töötlemist Stripe'iga** ning võimalust **hallata arveid dünaamiliselt ja turvaliselt**.

**Kas soovite lisada rohkem personaliseerimist, nt ettevõtte logo ja brändingu?** 😊
