java -Xmx4g -classpath "C:\Program Files (x86)\Weka-3-6\weka.jar" weka.classifiers.functions.SMO -t train.arff -d smo.model -x 5 -C 0.1 > results_train

java -Xmx4g -classpath "C:\Program Files (x86)\Weka-3-6\weka.jar" weka.classifiers.functions.SMO -i -l smo.model -T test.arff -x 5 > results_test