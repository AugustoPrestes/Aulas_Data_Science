# Machine Learnini: Classificação

### Regressão Logística

* Fórmula:

  * $ y = \frac{1}{1 + e^{(\beta_{0} + \beta_{1x1})}}$
* Trabalha melhor com variaveis binarias
* Metricas:

  * Log Loss: $ L_{log}(y, p) = - (ylog(p) + (1 - y)log(1 - p)))$

  ---

### Árvore de Decisão

* Metricas:
  * Coeficiente de Gini: $G = \frac{\sum^{n}_{i=1} \sum^{n}_{j=1}||x_{i} - x_{j}||}{2n^{2}\bar{x}}$
  * Entropia: $H = - [p \	log_{2}(p) + (1 - p)log_{2}(1 - p)]$
  *
