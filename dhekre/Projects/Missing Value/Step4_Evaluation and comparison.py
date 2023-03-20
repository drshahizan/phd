## Step 4: Evaluation and Comparison

class ModelEvaluator:

    def __init__(self, X_train, X_test, y_train, y_test):
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test

    def evaluate_svm(self):
        svm = SVC(kernel='linear', probability=True)
        svm.fit(self.X_train, self.y_train)
        accuracy = accuracy_score(self.y_test, svm.predict(self.X_test))
        f1_score_val = f1_score(self.y_test, svm.predict(self.X_test), average='macro')
        recall = recall_score(self.y_test, svm.predict(self.X_test), average='macro')
        return accuracy, f1_score_val, recall

    def evaluate_naive_bayes(self):
        nb = GaussianNB()
        nb.fit(self.X_train, self.y_train)
        accuracy = accuracy_score(self.y_test, nb.predict(self.X_test))
        f1_score_val = f1_score(self.y_test, nb.predict(self.X_test), average='macro')
        recall = recall_score(self.y_test, nb.predict(self.X_test), average='macro')
        return accuracy, f1_score_val, recall

    def evaluate_linear_regression(self):
        lr = LogisticRegression(random_state=42)
        lr.fit(self.X_train, self.y_train)
        accuracy = accuracy_score(self.y_test, lr.predict(self.X_test))
        f1_score_val = f1_score(self.y_test, lr.predict(self.X_test), average='macro')
        recall = recall_score(self.y_test, lr.predict(self.X_test), average='macro')
        return accuracy, f1_score_val, recall

    def evaluate_lightgbm(self):
        lgbm = LGBMClassifier(random_state=42)
        lgbm.fit(self.X_train, self.y_train)
        accuracy = accuracy_score(self.y_test, lgbm.predict(self.X_test))
        f1_score_val = f1_score(self.y_test, lgbm.predict(self.X_test), average='macro')
        recall = recall_score(self.y_test, lgbm.predict(self.X_test), average='macro')
        return accuracy, f1_score_val, recall

    def evaluate_rnn(self):
        # Convert the data to numpy arrays
        X_train = np.array(self.X_train)
        y_train_cat = to_categorical(self.y_train, num_classes=2)
        X_test = np.array(self.X_test)
        y_test_cat = to_categorical(self.y_test, num_classes=2)

        # Reshape the data for RNN model
        X_train = X_train.reshape(X_train.shape[0], 1, X_train.shape[1])
        X_test = X_test.reshape(X_test.shape[0], 1, X_test.shape[1])

        # Create and compile the RNN model
        rnn = Sequential()
        rnn.add(LSTM(64, input_shape=(1, 26))) # This line is updated to match the correct input shape
        rnn.add(Dense(32, activation='relu'))
        rnn.add(Dense(2, activation='softmax'))  # Change the number of output units to 3
        rnn.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        # Train the RNN model
        rnn.fit(X_train, y_train_cat, epochs=50, batch_size=32, validation_split=0.2)

        # Evaluate the RNN model
        accuracy = accuracy_score(y_test_cat.argmax(axis=1), rnn.predict(X_test).argmax(axis=1))
        f1_score_val = f
