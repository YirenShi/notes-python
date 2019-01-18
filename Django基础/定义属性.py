"""
字段类型


使用时需要引入django.db.models包，字段类型如下：

AutoField：自动增长的IntegerField，通常不用指定，不指定时Django会自动创建属性名为id的自动增长属性。

BooleanField：布尔字段，值为True或False

NullBooleanField：支持Null、True、False三种值。

CharField(max_length=字符长度)：字符串，参数max_length表示最大字符个数。

TextField：大文本字段，一般超过4000个字符时使用

IntegerField：整数



DecimalField(max_digits=None, decimal_places=None)：十进制浮点数

参数max_digits表示总位数
参数decimal_places表示小数位数

FloatField：浮点数
DateField[auto_now=False, auto_now_add=False])：日期

参数auto_now表示每次保存对象时，自动设置该字段为当前时间，用于”最后一次修改”的时间戳，它总是使用当前日期，默认为false
参数auto_now_add表示当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前日期，默认为false
参数auto_now_add和auto_now是相互排斥的，组合将会发生错误 TimeField：时间，参数同DateField
DateTimeField：日期时间，参数同DateFie

FileField：上传文件字段

ImageField：继承于FileField，对上传的内容进行校验，确保是有效的图片


选项

通过选项实现对字段的约束，选项如下：

null：如果为True，表示允许为空，默认值是False

blank：如果为True，则该字段允许为空白，默认值是False

对比：null是数据库范畴的概念，blank是表单验证证范畴的

db_column：字段的名称，如果未指定，则使用属性的名称

db_index：若值为True, 则在表中会为此字段创建索引，默认值是False

default：默认值

primary_key：若为True，则该字段会成为模型的主键字段，默认值是False，一般作为AutoField的选项使用

unique：如果为True, 这个字段在表中必须有唯一值，默认值是False




关系字段类型

关系型数据库的关系包括三种类型：
ForeignKey：一对多，将字段定义在多的一端中

ManyToManyField：多对多，将字段定义在两端中

OneToOneField：一对一，将字段定义在任意一端中
关系

选项	解释	访问	示例
OneToOneField	一对一， 将字段定义在任意一端中	对象.模型类	Grade.student
ForeignKey	一对多， 将字段定义在多端中	对象.模型类_set	Grade.student_set
ManyToManyField	多对多， 将字段定义在两端中
参数1：对象名 参数2：on_delete=models.CASCADE

"""