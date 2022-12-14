import mnist_loader
import network
import pickle

training_data, validation_data , test_data = mnist_loader.load_data_wrapper()

training_data = list(training_data)
test_data = list(test_data)

net=network.Network([784,100,10])

net.SGD( training_data, 30, 10, 3.0, test_data=test_data)

archivo = open("red_prueba2.pkl",'wb')
pickle.dump(net,archivo)
archivo.close()
exit()
#leer el archivo

archivo_lectura = open("red_prueba2.pkl",'rb')
net = pickle.load(archivo_lectura)
archivo_lectura.close()

net.SGD( training_data, 30, 50, 5.0, test_data=test_data)

archivo = open("red_prueba2.pkl",'wb')
pickle.dump(net,archivo)
archivo.close()
exit()
