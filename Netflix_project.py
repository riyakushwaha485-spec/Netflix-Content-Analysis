# ==========================================
# NETFLIX CONTENT ANALYSIS
# ==========================================
import pandas as pd
import matplotlib.pyplot as plt
# ==========================================
# 1. LOAD DATASET
# ==========================================
df = pd.read_csv("netflix_titles_practice.csv")
# ==========================================
# 2. DATA UNDERSTANDING
# ==========================================

print(df.head())
print(df.shape)
print(df.columns)
df.info()
# ==========================================
# 3. DATA CLEANING
# ==========================================
print(df.duplicated().sum())
print(df.isna().sum())
# ==========================================
# 4. BASIC ANALYSIS
# ==========================================
#Q1. How many total titles are available on Netflix?
print(len(df))
#Q2. How many Movies and TV Shows are available?
print(df["type"].value_counts())
#Q3. What is the oldest release year in the dataset?
print(df["release_year"].min())
#Q4. What is the most recent release year?
print(df["release_year"].max())
#Q5. Which rating is the most common on Netflix?
print(df["rating"].value_counts().idxmax())
# ==========================================
# 5. MOVIES VS TV SHOWS
# ==========================================
#🟣 Q6. What percentage of Netflix content consists of Movies and TV Shows?
movie_percentage = (df["type"] == "Movie").sum() / len(df) * 100
tv_show_percentage = (df["type"] == "TV Show").sum() / len(df) * 100
print(f"Movies: {movie_percentage:.2f}%")
print(f"TV Shows: {tv_show_percentage:.2f}%")   
#🎬 Q7. What is the average duration of Movies?
movies = df[df["type"] == "Movie"]
movie_durations = movies["duration"].str.extract(r"(\d+)")[0].astype(float)
print(movie_durations.mean())
#🎬 Q8. How many TV Shows have only one season?
    
tv_shows = df[df["type"] == "TV Show"]


one_season = tv_shows[tv_shows["duration"] == "1 Season"]

print("TV Shows with only 1 season:", len(one_season))

#🎬 Q9. Which TV Show has the highest number of seasons?
tv_shows = df[df["type"] == "TV Show"]
season_counts = tv_shows["duration"].str.extract(r"(\d+)")[0].astype(int)
max_seasons = season_counts.max()
print("TV Show with the highest number of seasons:", tv_shows.loc[season_counts == max_seasons, "title"].iloc[0])

# ==========================================
# 6. COUNTRY ANALYSIS🌍🌍
# ==========================================
#Q10. Which country has the highest number of titles on Netflix?
country_counts = df["country"].value_counts()
print(country_counts)
print("Country with the highest number of titles:", country_counts.idxmax())
#Q11. What are the top 5 countries with the highest number of Netflix titles?
top_five_highest_country= df["country"].value_counts().head(5)
print(top_five_highest_country)
#Q12. How many Netflix titles are from India?
India_titles= df[df["country"]=="India"]
print(len(India_titles))
# Q13. What is the distribution of Movies and TV Shows in India?
india_titles = df[df["country"] == "India"]

print(india_titles["type"].value_counts())
# Q14. What are the most common genres in Indian Netflix titles?
india_titles = df[df["country"] == "India"]

genres = india_titles["listed_in"].str.split(", ").explode()

print(genres.value_counts())
# ==========================================
# 7. TIME ANALYSIS
# ==========================================
#🕐 Q17. How many Netflix titles were released in each year?
netflix_title = df["release_year"].value_counts().sort_index()
print(netflix_title)
#🕐 Q18. Which year had the highest number of Netflix titles?
highest_year = df["release_year"].value_counts().idxmax()
print("Year with the highest number of Netflix titles:", highest_year)
#🕐 Q19. How has the number of Netflix titles changed after 2015?
titles_after_2015 = df[df["release_year"] > 2015]
yearly_titles = titles_after_2015["release_year"].value_counts().sort_index()
print(yearly_titles)
#🕐 Q20. How does the number of Movies and TV Shows vary by release year?
year_type_count = df.groupby(["release_year", "type"]).size().unstack(fill_value=0)
print(year_type_count)
#Q21. What is the average release year of Netflix titles?
average_release_year = df["release_year"].mean()
print("Average release year of Netflix titles:", round(average_release_year, 2))
title_before_2015 = df[df["release_year"] < 2015]
print("Number of titles released before 2015:", len(title_before_2015))
#🕐 Q23. What is the oldest release year in the dataset?
oldest_release_year=df["release_year"].min()
print(oldest_release_year)
#Q24. What is the most recent release year in the dataset?
recent_release_year=df["release_year"].max()
print(recent_release_year)
#Q25.
release_2024=df[df["release_year"]==2024]
print("Titles released in 2024:", len(release_2024))
#🕐 Q26. Which release year had the fewest Netflix titles?
fewset_release_year=df["release_year"].value_counts().idxmin()
print(fewset_release_year)
# ==========================================
# 8. RATINGS ANALYSIS
# ==========================================
#Q27. What is the distribution of ratings on Netflix?
rating_distribution=df["rating"].value_counts()
print(rating_distribution)
# Q28. What is the most common rating for Movies?
movies = df[df["type"] == "Movie"]
movie_rating = movies["rating"].value_counts()
print("Most common rating for Movies:", movie_rating.idxmax())
# Q29. Most common rating for TV Shows
tv_shows = df[df["type"] == "TV Show"]
tv_rating = tv_shows["rating"].value_counts()
print("Most common rating for TV Shows:", tv_rating.idxmax())
## ==========================================
# 9. VISUALIZATIONS☠️💀☠️
# ==========================================
#Q30. Create a bar chart showing the number of Movies and TV Shows on Netflix.
import matplotlib.pyplot as plt
type_count = df["type"].value_counts()
type_count.plot(kind="bar")
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Number of Titles")
plt.show()
#Q31. Create a bar chart showing the Top 5 Countries by number of Netflix titles.
top_countries = df["country"].value_counts().head(5)
top_countries.plot(kind="bar")
plt.title("Top 5 Countries by Netflix Titles")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.show()
# Q32. Create a bar chart showing the Top 5 Genres on Netflix.
# Q33. Create a line chart showing the number of Netflix titles released each year.
yearly_titles = df["release_year"].value_counts().sort_index()
yearly_titles.plot(kind="line")
plt.title("Netflix Titles Released by Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.show()
#Q34. Create a bar chart showing ratings distribution.
rating_count = df["rating"].value_counts()
rating_count.plot(kind="bar")
plt.title("Netflix Ratings Distribution")
plt.xlabel("Rating")

plt.ylabel("Number of Titles")
plt.show()
#Q35. Which type of content is more common on Netflix — Movies or TV Shows?
common_content=df["type"].value_counts()
print(common_content)
# PART 9 — FINAL INSIGHTS

# 1. Content Type
type_count = df["type"].value_counts()
print("Content Type:")
print(type_count)

# 2. Top Country
country_count = df["country"].value_counts()
print("\nTop Country:")
print(country_count.head(5))

# 3. Release Year
year_count = df["release_year"].value_counts().sort_index()
print("\nTitles by Year:")
print(year_count)

# 4. Ratings
rating_count = df["rating"].value_counts()
print("\nRatings:")
print(rating_count)

# 5. India Analysis
india = df[df["country"] == "India"]
print("\nIndia Titles:", len(india))
print("India Content Type:")
print(india["type"].value_counts())

# 6. Recent Content
recent = df[df["release_year"] >= 2020]
print("\nTitles released from 2020 onwards:", len(recent))
# ==========================================
# 10. KEY INSIGHTS
# ==========================================
# 1. Movies account for 64% of the titles, while TV Shows account for 36%.
# 2. India has the highest number of titles in the dataset.
# 3. 2021 and 2024 have the highest number of titles released.
# 4. 13+ and 16+ are the most common ratings.
# 5. India contributes 36% of the total titles.
# 6. 68% of titles were released from 2020 onwards.
