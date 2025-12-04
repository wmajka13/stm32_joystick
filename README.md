
Mini-projekt składa się z joysticka podłączonego do stm32-nucleo-f411RE oraz kodu w pythonie.

Ruchy joystickiem zczytywane są przy pomocy ADC (które wyzwalane jest zdarzeniem timera TIM3). Następnie przy pomocy DMA zczytane wartości przesyłane są do pamięci. Dalej timerem wyzwalana jest komunikacja UART i dane przesyłane są do PC, gdzie odczytuje się je przy pomocy biblioteki pyseries. 

Następnie wykrozystanie opencv umożliwia stworzenie animacji, na której kółko porusza się zgodnie z ruchami joysticka. Jego wciśnięcie powoduje losową zmianę koloru.