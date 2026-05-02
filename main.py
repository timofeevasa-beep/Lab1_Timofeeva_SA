from triangle import TriangleAnalyzer

def main():
    print("Программа для определения типа треугольника")
    print("Введите длины трех сторон (выход: 'exit'):")
    
    analyzer = TriangleAnalyzer(100)
    
    while True:
        print("\n" + "-"*40)
        a = input("Сторона A: ")
        if a.lower() == 'exit':
            break
            
        b = input("Сторона B: ")
        if b.lower() == 'exit':
            break
            
        c = input("Сторона C: ")
        if c.lower() == 'exit':
            break
        
        result_type, coordinates = analyzer.process_request(a, b, c)
        
        if result_type:
            print(f"\nРезультат: {result_type}")
            print(f"Координаты вершин:")
            print(f"  Вершина A: {coordinates[0]}")
            print(f"  Вершина B: {coordinates[1]}")
            print(f"  Вершина C: {coordinates[2]}")
        else:
            print("\nОшибка: невалидные входные данные")
        print()

if __name__ == "__main__":
    main()
