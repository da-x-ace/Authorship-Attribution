java -Xmx4g -classpath "C:\Program Files (x86)\Weka-3-6\weka.jar" weka.classifiers.bayes.NaiveBayes -t train.arff -d naivebayes.model -x 5 > results_train

java -Xmx4g -classpath "C:\Program Files (x86)\Weka-3-6\weka.jar" weka.classifiers.bayes.NaiveBayes -i -l naivebayes.model -T test.arff -x 5 > results_test