import numpy as np



"""
NeuralNetwork class
"""
class NeuralNetwork:
    """
    constructor
        @param layers is our network layer information
        @param alpha is the learning rate for our network
    """
    def __init__(self, layers, activation_type='sigmoid', alpha=0.1):
        # alocating the network weights
        self.W = []
        # network layers size
        self.layers = layers
        # network activation function
        self.activation_type = activation_type
        # network learning rate
        self.alpha = alpha
        # calling our build method
        self.__build__()
    
    """
    build
        initializing network weights with random numbers.
    """
    def __build__(self):
        # start looping from the index of the first layer but
		# stop before we reach the last two layers
		for i in np.arange(0, len(layers) - 2):
			# randomly initialize a weight matrix connecting the
			# number of nodes in each respective layer together,
			# adding an extra node for the bias
			w = np.random.randn(layers[i] + 1, layers[i + 1] + 1)
			self.W.append(w / np.sqrt(layers[i]))
        # the last two layers are a special case where the input
		# connections need a bias term but the output does not
		w = np.random.randn(layers[-2] + 1, layers[-1])
		self.W.append(w / np.sqrt(layers[-2]))

    """
    repr
        get a single line information about our network.
    """
    def __repr__(self):
		# construct and return a string that represents the network
		# architecture
		return "NeuralNetwork: {}".format(
			"-".join(str(l) for l in self.layers))
    
    """
    activation functions
        @param x as input
        @returns output based on the activation type
            types: unit_step, sigmoid, relu, default
    """
    def __activation_function__(self, x):
        if self.activation_type == 'unit_step':
            return np.heaviside(x, 1)
        elif self.activation_type == 'sigmoid':
            return 1.0 / (1 + np.exp(-x))
        elif self.activation_type == 'relu':
            return x * (x > 0)
        else:
            return x
    
    """
    linear_activation_forward:
        using the activation function to perform a forwarding in
        feedforward steps.
        @param a_prev as previous answers
        @param w as the weights
        @param b as the baios
        @returns activation function result
    """
    def __linear_activation_forward__(self, a_prev, w, b):
        return self.__activation_function((w @ a_prev) + b)
    
    """
    fit
        responsible for actually training our model
        @param X training set
        @param y labels
        @param epochs the epochs number
        @param display update
    """
    def fit(self, X, y, epochs=1000, displayUpdate=100):
		# insert a column of 1's as the last entry in the feature
		# matrix -- this little trick allows us to treat the bias
		# as a trainable parameter within the weight matrix
		X = np.c_[X, np.ones((X.shape[0]))]
		# loop over the desired number of epochs
		for epoch in np.arange(0, epochs):
			# loop over each individual data point and train
			# our network on it
			for (x, target) in zip(X, y):
				self.fit_partial(x, target)
			# check to see if we should display a training update
			if epoch == 0 or (epoch + 1) % displayUpdate == 0:
				loss = self.calculate_loss(X, y)
				print("[INFO] epoch={}, loss={:.7f}".format(
					epoch + 1, loss))

    """
    feed_forward:
        receives input vector as a parameter and calculates the output vector based on weights and biases.
        @argument x is the input vector which is a numpy array.
        @returns output vector
    """
    def feed_forward(self):
        # layers results
        feed_forward_results = []
        # calculate the deepness
        deepness = len(self.parameters) // 2

        # doing feedforward for each layer
        for le in range(1, deepness):  # using our linear activation forward
            x = self.__linear_activation_forward(x, self.parameters['W' + str(le)], self.parameters['b' + str(le)])
            feed_forward_results.append(x)

        # last layer
        x = self.__linear_activation_forward(x, self.parameters['W' + str(deepness)], self.parameters['b' + str(deepness)])
        feed_forward_results.append(x)
        
        return feed_forward_results

    def back_propagetion(self, ff_results, y_train):
         pass
    
    """
    accuracy:
        calculating the output accuracy
        @argument y_pred predicted output
        @argument y_true the correct output
        @returns accuracy
    """
    def __accuracy(self, y_pred, y_true):
        return (y_pred.argmax(axis=1) == y_true.argmax(axis=1)).mean()

    """
    error:
        mean square error calculating
        @argument y_start the output
        @argument y_true the correct output
        @returns mean square error
    """
    def __error(self, y_star, y_true):
        return ((y_star - y_true) ** 2).sum() / (2 * y_star.size)
