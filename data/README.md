<div dir="rtl">

# נתונים, מקורות ורישיונות

הורדו ב־24.10.2026. כל קובץ קטן מ־5MB ונשמר במאגר; הרצת מחברות ובדיקות אינה דורשת רשת. אלו נתונים לימודיים היסטוריים, ללא רשומות חדשות ממוסד רפואי. גודל המדגם והבחירה בו מגבילים הכללה. אין לפרש מודל כחיזוי רפואי מאושר.

| קובץ | שורות | מקור וייחוס | רישיון/תנאי המקור |
|---|---:|---|---|
| `pima.csv` | 768 | [מראה Plotly](https://github.com/plotly/datasets/blob/master/diabetes.csv), Pima Indians Diabetes, NIDDK; Smith et al. (1988) | מראת Plotly מופצת תחת MIT, ראו `licenses/plotly-MIT.txt`; נתוני Pima המקוריים מיוחסים ל־NIDDK |
| `heart.csv` | 303 | [מראה Heart UCI](https://github.com/sharmaroshan/Heart-UCI-Dataset/blob/master/heart.csv); [UCI Heart Disease](https://doi.org/10.24432/C52P4X), Janosi, Steinbrunn, Pfisterer, Detrano (1988) | נתוני UCI: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); הייחוס כאן, העתק עם כותרות ויעד בינארי |
| `breast_cancer.csv` | 569 | `sklearn.datasets.load_breast_cancer`; [UCI Wisconsin Diagnostic Breast Cancer](https://doi.org/10.24432/C5DW2B), Wolberg, Street, Mangasarian, Street (1995) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); היעד הומר ל־1=ממאיר |
| `titanic.csv` | 156 | [מראה Plotly](https://github.com/plotly/datasets/blob/master/titanic.csv), נתוני Titanic/Kaggle; שמות העמודות הומרו לאותיות קטנות | רישיון מראת Plotly: MIT, העתק הרישיון ב־`licenses/plotly-MIT.txt`; רישיון המראה אינו קביעה חדשה לגבי זכויות בנתוני המקור ההיסטוריים |
| `california.csv` | 5,000 | [Hands-On ML, Aurélien Géron](https://github.com/ageron/handson-ml2/blob/master/datasets/housing/housing.csv); נתוני מפקד קליפורניה 1990, Pace & Barry (1997), StatLib | מראת הספר: Apache 2.0, ראו `licenses/housing-Apache-2.0.txt`; דגימת `sample(5000, random_state=42)` מתוך 20,640 שורות, ללא `ocean_proximity` |
| `messy_health.csv` | 210 | נגזרת לימודית של 200 שורות Pima הראשונות; נוספו מזהים מלאכותיים, 10 שורות כפולות ושיבושים מתועדים להלן | אותם תנאי MIT של מראת Pima, עם השינויים המתועדים כאן; אינו מקור קליני נוסף |

רישיונות של מאגרי מראה מתועדים כרישיונות המראה בלבד; אין לייחס אוטומטית רישיון תוכנה לכל נתוני צד שלישי. הקישורים למקורות המקוריים נשמרים לצורך בדיקה וייחוס. טקסט [CC BY 4.0 המלא](https://creativecommons.org/licenses/by/4.0/legalcode) ותנאי הייחוס חלים על נתוני UCI. נתוני הספר וה־CSV אינם קוד חדש של המעבדה.

## מילון קצר והחלטות חשובות

- **Pima:** נשים בנות 21 ומעלה ממורשת Pima; אינו מדגם כללי. `target`: אבחנת סוכרת בינארית; `pregnancies`: מספר הריונות; `glucose`: ריכוז גלוקוז במבחן העמסה; `blood_pressure`: לחץ דם דיאסטולי (mmHg); `skin_thickness`: עובי קפל עור (mm); `insulin`: אינסולין לאחר שעתיים; `bmi`: ק״ג/מ״ר; `pedigree`: ציון היסטוריה משפחתית; `age`: שנים. אפסים בחמשת המדדים הפיזיולוגיים הם קודי חסר, אך אפס הריונות הוא תקין.
- **Heart:** משתני `age`, `sex` (0/1 בקידוד המקור), `cp` (סוג כאב), `trestbps` (לחץ דם), `chol` (כולסטרול), `fbs`, `restecg`, `thalach`, `exang`, `oldpeak`, `slope`, `ca`, `thal`, `target`. עמודות קטגוריות נשמרו כקודים מספריים; מתאם מספרי בהן דורש זהירות. זהו עותק Kaggle נפוץ של נתוני UCI; אין להשתמש בפרשנות הקלינית של כיוון `target` בלי אימות הגדרת המראה. התרגיל משתמש בו רק כקבוצת תצוגה.
- **Breast cancer:** יחידת התצפית היא דגימת FNA של גוש בשד; 30 מאפייני גרעין תא, לפי mean/error/worst. **אצלנו `target=1` ממאיר ו־0 שפיר**, הפוך מהקידוד המקורי של sklearn. השכיחות אינה שכיחות סרטן באוכלוסייה.
- **Titanic:** `survived` (1 שרד), `pclass` (1/2/3), `sex`, `age` (שנים), `sibsp`, `parch`, `fare` (מחיר הכרטיס), `embarked` (נמל), `passengerid`, `name`, `ticket`, `cabin`. חסרים נשמרו; שורה היא נוסע בתת־מדגם בן 156 הרשומות שבמראה Plotly (לא כל 891 נוסעי מדגם האימון). אין להשתמש במזהה או בשם כתחליף להסבר כללי.
- **California:** שורה היא קבוצת בלוקים במפקד, לא בית יחיד. `longitude`, `latitude`, `housing_median_age`, `total_rooms`, `total_bedrooms`, `population`, `households`, `median_income` (עשרות אלפי דולר), `median_house_value` (דולר, יעד). היעד חסום מלמעלה; פיצול אקראי אינו מבחן הכללה לאזור חדש או לשנה אחרת. חסרים טבעיים ב־`total_bedrooms` נשמרו.
- **Messy health:** `patient_id` הוא מזהה לימודי, לא מאפיין למודל; `outcome` הוא יעד Pima. `sex` נוצר כ־female בהתאם לאוכלוסיית המקור ונפגע ברווחים, אותיות ו־null; בדיקת פונקציית הניקוי כוללת גם קטגוריית male לבדיקת הכללה בלבד. `age` מכיל `unknown` ו־999; `bmi` מכיל חסרים ו־500; עשר הרשומות הראשונות כפולות. החריגים המכוונים אינם תצפיות אמיתיות. השלמת חציונים בתרגיל 2 היא ניקוי תיאורי; במודל לומדים חציון רק בתוך train/CV.

הקובץ `manifest.json` מכיל SHA-256 וגודל לכל CSV לזיהוי שינויים בגרסת התרגול.

</div>
