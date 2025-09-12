import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd

def get_population_data(countries):
    """Получает данные о населении стран с Worldometer"""
    # В реальном проекте нужно парсить сайт worldometers.info
    # Здесь создадим демонстрационные данные
    
    # Примерные данные для демонстрации
    years = [2000, 2010, 2020]
    population_data = {}
    
    # Примерные данные населения (в миллионах)
    demo_data = {
        'Китай': [1260, 1340, 1400],
        'Индия': [1050, 1230, 1380],
        'США': [282, 309, 331],
        'Россия': [146, 142, 144],
        'Бразилия': [174, 196, 213]
    }
    
    # Если запрошенные страны есть в демо-данных
    available_data = {}
    for country in countries:
        if country in demo_data:
            available_data[country] = demo_data[country]
    
    return years, available_data

def plot_population_charts(countries):
    """Строит столбчатые диаграммы населения стран"""
    years, population_data = get_population_data(countries)
    
    if not population_data:
        print("Данные для запрошенных стран не найдены")
        return
    
    # Создаем DataFrame для удобства
    df = pd.DataFrame(population_data, index=years)
    
    # Строим отдельные графики для каждого года
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    for i, year in enumerate(years):
        ax = axes[i]
        data = df.loc[year]
        
        bars = ax.bar(range(len(data)), data.values())
        ax.set_title(f'Население в {year} году')
        ax.set_xlabel('Страны')
        ax.set_ylabel('Население (млн)')
        ax.set_xticks(range(len(data)))
        ax.set_xticklabels(data.index, rotation=45)
        
        # Добавляем значения на столбцы
        for bar, value in zip(bars, data.values()):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
                   f'{value:.1f}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()
    
    # Также выводим таблицу с данными
    print("Данные о населении (млн человек):")
    print(df)

# Пример использования
selected_countries = ['Китай', 'Индия', 'США', 'Россия', 'Бразилия']
plot_population_charts(selected_countries)