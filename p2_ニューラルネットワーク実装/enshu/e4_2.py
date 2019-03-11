# インポート
from mnist import load_mnist
from e4_1 import NeuralNetwork
import numpy as np

# 読み込み（初回時のみダウンロードも行います）
# mnist = load_mnist()

# データセットへのアクセス
# mnist["train_img"]    # 訓練データ画像   [60000, 784]
# mnist["train_label"]  # 訓練データラベル [60000, 10]
# mnist["test_img"]     # テストデータ画像 [10000, 784]
# mnist["test_label"]   # テストラベル     [10000, 10]


def main():
    mnist = load_mnist()
    model = NeuralNetwork()

    batch_size = 100
    train_images = 60000
    train_epochs = 100
    train_iters = train_epochs * (train_images // batch_size)

    for i in range(train_iters):
        # 60,000の数字の中からランダムに100個の数字を選ぶ
        indices = np.random.choice(train_images, batch_size)
        # ミニバッチの獲得
        mini_batch_image = mnist["train_img"][indices]
        mini_batch_label = mnist["train_label"][indices]
        model.sgd(mini_batch_image, mini_batch_label, 0.0001)
        # 100ループごとに損失関数を表示
        if i % 100 == 0:
            print("Loss {0}: {1}".format(
                i, model.loss(mini_batch_image, mini_batch_label)))
            # 正解率を表示
            accuracy = np.average(
                (np.argmax(mini_batch_label, axis=1) == np.argmax(model.forward(mini_batch_image), axis=1)).astype(int))
            print("Acc: {0} %".format(accuracy * 100))

        # テストデータに対する損失を表示
    print("Test Loss: {0}".format(model.loss(
        mnist["test_img"], mnist["test_label"])))
    test_acc = np.average(
        (np.argmax(mnist["test_label"], axis=1) == np.argmax(model.forward(mnist["test_img"]), axis=1)).astype(int))
    print("Test Acc: {0} %".format(test_acc * 100))


if __name__ == "__main__":
    main()
