# LuckyNumber
with special cal ,get some numbers


1、MongoDB数据库备份
    1、语法：
        mongodump -h dbhost -d dbname -o dbdirectory
        参数说明：
            -h： MongDB所在服务器地址，例如：127.0.0.1，当然也可以指定端口号：127.0.0.1:27017
            -d： 需要备份的数据库实例，例如：test
            -o： 备份的数据存放位置，例如：/home/mongodump/，当然该目录需要提前建立，这个目录里面存放该数据库实例的备份数据。
    2、实例：
        sudo rm -rf /home/momgodump/
        sudo mkdir -p /home/momgodump
        sudo mongodump -h 192.168.17.129:27017 -d itcast -o /home/mongodump/
        -
2、MongoDB数据库恢复
    1、语法：
        mongorestore -h dbhost -d dbname --dir dbdirectory
 
        参数或名：
            -h： MongoDB所在服务器地址
            -d： 需要恢复的数据库实例，例如：test，当然这个名称也可以和备份时候的不一样，比如test2
            --dir： 备份数据所在位置，例如：/home/mongodump/itcast/
            --drop： 恢复的时候，先删除当前数据，然后恢复备份的数据。就是说，恢复后，备份后添加修改的数据都会被删除，慎用！
    2、实例：
    mongorestore -h 192.168.17.129:27017 -d itcast_restore --dir /home/mongodump/itcast/
