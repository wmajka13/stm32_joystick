# STM32 Joystick Controller with Python Visualization

Projekt realizujący system sterowania i wizualizacji w czasie rzeczywistym. Wykorzystuje mikrokontroler **STM32 Nucleo-F411RE** do akwizycji danych z analogowego joysticka oraz skrypt w języku **Python (OpenCV)** do wizualizacji ruchów i interakcji.

Celem projektu była implementacja wydajnej akwizycji danych z wykorzystaniem **DMA** i timerów sprzętowych, co pozwala na minimalizację obciążenia CPU.

## Kluczowe funkcjonalności

### Firmware (STM32)
* **Hardware-Triggered ADC:** Próbkowanie ADC wyzwalane jest sprzętowo przez **Timer (TIM3)**, co zapewnia idealnie stałą częstotliwość próbkowania niezależną od kodu.
* **DMA Transfer:** Dane z przetwornika ADC są przesyłane bezpośrednio do pamięci RAM przez kontroler DMA, bez udziału procesora.
* **Non-blocking Debouncing:** Obsługa przycisku joysticka realizowana przez przerwanie zewnętrzne (**EXTI**). Eliminacja drgań styków (debouncing) oparta jest na liczniku systemowym **SysTick**, co nie blokuje głównej pętli programu (`HAL_Delay` nie jest używane).
* **Cykliczna komunikacja UART:** Wysyłanie danych do PC jest synchronizowane osobnym timerem.

### Software (Python PC)
* **Odbiór danych:** Wykorzystanie biblioteki `pyserial` do asynchronicznego odbierania ramek danych.
* **Wizualizacja:** Graficzna reprezentacja danych przy użyciu **OpenCV**. Pozycja obiektu na ekranie odpowiada wychyleniu joysticka.
* **Interakcja:** Zmiana koloru obiektu w reakcji na przerwanie sprzętowe (wciśnięcie przycisku).
---
Autor: Wiktor Majka
