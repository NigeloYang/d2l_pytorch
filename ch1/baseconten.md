##机器学习中的关键组件
- 数据 data
- 模型 model
- 目标函数 objective function，用来量化模型的有效性
- 算法 algorithm，调整模型参数以优化目标函数

###数据
数据集由一个个样本（example, sample）组成，大多时候，它们遵循独立同分布(independently and identically distributed, i.i.d.)。 
样本有时也叫做数据点（data point）或者数据实例（data instance），通常每个样本由一组称为特征（features，或协变量（covariates））的属性组成。
机器学习模型会根据这些属性进行预测。 在监督学习问题中，模型要预测的是一个特殊的属性，它被称为标签（label，或目标（target））。

