from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras

housing = fetch_california_housing()
X_train_full, X_test, y_train_full, y_test = train_test_split(
    housing.data, housing.target
)
X_train, X_valid, y_train, y_valid = train_test_split(
    X_train_full, y_train_full
)

print(X_train[0])
print(y_train[0])
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_valid = scaler.transform(X_valid)
X_test = scaler.transform(X_test)

# keras 函数式API
input_ = keras.layers.Input(shape=X_train.shape[1:])
hidden1 = keras.layers.Dense(30, activation="relu")(input_)
hidden2 = keras.layers.Dense(30, activation="relu")(hidden1)
concat = keras.layers.Concatenate()([input_, hidden2])
output = keras.layers.Dense(1)(hidden1)
model = keras.Model(inputs=[input_], outputs=[output])

# model = keras.models.Sequential([
#     keras.layers.Dense(30, activation="relu",
#                        input_shape=X_train.shape[1:]),
#     keras.layers.Dense(1)
# ])

model.compile(loss="mean_squared_error",
              optimizer="sgd",
             )

# 个人理解为钩子函数 当然这并不准确 哈哈
checkpoint_cb = keras.callbacks.ModelCheckpoint("my_model.h5", save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True)
history = model.fit(X_train, y_train, epochs=20,
                    validation_data=(X_valid, y_valid),
                    callbacks=[checkpoint_cb, early_stopping_cb]
                    )
mse_test = model.evaluate(X_test, y_test)
y_pre = model.predict(X_test[:10])
print(y_pre)
print(y_test[:10])

