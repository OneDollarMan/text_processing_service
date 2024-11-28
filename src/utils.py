from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from schemas import ProcessedTextSchema, SearchResultsSchema, SearchResultSchema
import spacy
from nltk.corpus import stopwords

nlp = spacy.load("ru_core_news_sm")
stop_words = set(stopwords.words('russian'))
database = []
with open('db.txt', 'r') as file:
    for line in file:
        database.append(line)

# Создание TF-IDF индекса
vectorizer = TfidfVectorizer()


def process_text(text: str):
    """
    Функция обработки текста.
    :param text: Входная строка
    :return: Список токенов
    """
    # Приведение к нижнему регистрку
    text = text.lower()

    # Токенизация
    doc = nlp(text)

    # Лемматизация и очистка от стоп-слов
    tokens = [
        token.lemma_ for token in doc
        if token.lemma_ not in stop_words and token.is_alpha
    ]
    return ProcessedTextSchema(tokens=tokens)


tfidf_matrix = vectorizer.fit_transform([' '.join(process_text(text).tokens) for text in database])


def search(query: str, top_n: int = 3):
    """
    Функция для поиска релевантных текстов в базе данных.
    :param query: Строка запроса
    :param top_n: Количество топ-результатов
    :return: Список релевантных текстов
    """
    # Преобразуем запрос в TF-IDF вектор
    query = ' '.join(process_text(query).tokens)
    query_vector = vectorizer.transform([query])

    # Вычисляем косинусное сходство
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix).flatten()

    # Находим индексы топ-N результатов
    top_indices = similarity_scores.argsort()[-top_n:][::-1]

    # Возвращаем соответствующие тексты из базы данных
    results = [SearchResultSchema(text=database[i], score=similarity_scores[i]) for i in top_indices]
    return SearchResultsSchema(results=results)