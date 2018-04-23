# git基本操作

1. 克隆代码
    ```
    git clone https://github.com/Huang0321/test.git
    git clone git@github.com:Huang0321/test.git
    ctr + insert 复制
    shift + insert 粘贴
    ``` 
2.  删除分支
    ```
    git branch -D branch_name 
    ```
3. 查看分支
```
    git branch
``` 
4. 创建分支
```
    git branch branch_name
```
5. 切换分支
```
    git chekout branch_name
    git chekout -b branch_name (创建并切换分支)
```
6. 查看状态
```
    git status
```
7. 添加修改的数据到缓存区
```
    git add .
    git add file_name
```
7.  提交修改到本地分支
```
    git commit -m '注解'
```
9.  提交本地分支到远程分支上
```
    git push origin
```
10. 设置全局变量
```    
    git config --global user.name 'usename'
    git config --global user.email 'email'
```
11. 合并add和commit操作
```
    git commit -am '注解'
```
12. 创建秘钥
```
    ssh-keygen -t rsa -C 账号
```
13. 比较分支之间的不同
```
    git diff branch_pne branch_two
```
14. 合并
```
    git merge branch
```
15. 打tag标签
```
    git tag -a version_number -m '注解'
```
16. 推送版本
```
    git push origin version_number
```
17. 删除远程分支
```
    git push origin --delete branch_name
```
18. 查看版本号
```
    git tag
```
19. 删除版本号
```
    git tag -d version_number
```
20. 删除远程版本号
```
    push origin --delete tag version_number
```
21. 缓存修改的代码
```
    git stash
```
22. 查看缓存
``` 
    git stash list
```
23. 还原缓存
```
    git stash apply stash@{x}
```
