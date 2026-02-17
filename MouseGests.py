from pynput import mouse
from moosegesture import Recognizer
import matplotlib.pyplot as plt

# Inicjalizacja rozpoznawacza gestów
recognizer = Recognizer()

# Lista punktów (x, y)
points = []
drawing = False  # Czy użytkownik trzyma przycisk myszy?

def on_move(x, y):
    global points, drawing
    if drawing:
        points.append((x, y))

def on_click(x, y, button, pressed):
    global points, drawing

    # Używamy prawego przycisku do rysowania gestów
    if button == mouse.Button.right:
        if pressed:
            drawing = True
            points = [(x, y)]
        else:
            drawing = False
            if len(points) > 5:
                gesture = recognizer.recognize(points)
                print(f"Rozpoznany gest: {gesture}")
                
                # Wizualizacja trajektorii
                xs, ys = zip(*points)
                plt.plot(xs, ys, '-o', color='blue')
                plt.title(f"Trajektoria gestu: {gesture}")
                plt.show()

                # Przykład akcji na podstawie gestu
                if gesture == "circle":
                    print("🟢 Okrąg! Uruchamiam akcję — np. zmiana koloru.")
                elif gesture == "v":
                    print("✅ Gest V – potwierdzenie akcji.")
                elif gesture == "l":
                    print("⬅️ Gest L – cofnięcie operacji.")
                else:
                    print("❓ Nieznany gest.")
            else:
                print("Za mało punktów do rozpoznania gestu.")

# Nasłuchiwanie myszy
with mouse.Listener(on_move=on_move, on_click=on_click) as listener:
    print("Rysuj gest prawym przyciskiem myszy...")
    listener.join()
