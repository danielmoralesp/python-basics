import numpy as np

class Perceptron(object):
    """Perceptron classifier

    Parameters
    ----------

    eta : float
        Tasa de aprendizaje (entre 0.0 y 1.0)
    n_iter : int
        Pasa el conjunto de datos de entrenamiento
    random_state : int
        Semilla de generador de numeros aleatorios para inicializacion de peso aleatorio.

    Atributes
    ---------

    w_ : 1d-array
        Peso despues de la instalacion
    errors_ : list
        Numero de clasificaciones erroneas (actualizaciones) en cada epoca.
    """

    def __init__(self, eta=0.01, n_inter=50, random_state=1):
        self.eta = eta
        self.n_inter = n_inter
        self.random_state = random_state


    def fit(self, X, y):
        """Ajustar los datos de entrenamiento.

        Parameters
        ----------

        X : {array-like}, shape = [ n_samples, n_features ]
            Vectores de entrenamiento, donde n_samples es el numero de muestras y n_features es el numero de caracteristicas.

        y : array-like, shape = [n_samples]
            Valores target

        Returns
        -------

        self : object

        """

        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])

        self.errors_ = []

        for _ in range(self.n_inter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """ Calculatar input neto"""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        """ Clase de retorno lavel despues del paso de la unidad"""
        return np.where(self.net_input(X) >= 0.0, 1, -1)
