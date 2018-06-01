##可以在调用model.compile()之前初始化优化器对象，然后传入
##所有的优化器都可以使用的参数
clipnorm:
  所有的参数梯度都将被剪辑为一个最大值
clipvalue
  所有的参数梯度被剪辑到一个范围-clipvalue~+clipvalue
  SGD
  keras.optimizers.SGD(lr=0.01, momentum=0.0, decay=0.0, nesterov=False)
  
  sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
  model.compile(loss='mean_squared_error', optimizer=sgd)
  
  RMSprop
  
    keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-06)
    
    Adagrad
    
    keras.optimizers.Adagrad(lr=0.01, epsilon=1e-06)
    
    Adadelta
    
    keras.optimizers.Adadelta(lr=1.0, rho=0.95, epsilon=1e-06)
    
    Adam
    
    keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08)
    
    Adamax
    
    keras.optimizers.Adamax(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=1e-08)
    
    Nadam
    
    keras.optimizers.Nadam(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=1e-08, schedule_decay=0.004)
