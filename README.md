# Twittor
>* 本專案為利用Python Flask、Bootstrap 、MySQL、Nginx、Docker架設並部署在 AWS 的類Twitter網站。
>* 實作使用者註冊、驗證及登入交互功能；並提供發布貼文及上傳相片功能。

## Demo Website
* 網址：https://bizara.link/
* 測試帳號及密碼
  * Account：admin
  * PassWord：admin
* 開放註冊惟尚無法驗證(認證信件會寄至本人信箱)

## network architecture
![未命名绘图(1)](https://github.com/z50205/Twittor/assets/19884343/d46252ca-8d42-4064-8827-40e9cebf92d4)

## Site Introduction
### SignIn
> 登入頁面，可依資料庫帳戶資訊登入，並連結註冊及忘記密碼頁面
![SignIn](https://github.com/z50205/Twittor/assets/19884343/25303eb4-b919-46a8-b91f-f90f6ab24807)
### Explore 
> 可觀看所有推文，進行貼文分頁載入(pagination)，並依照推文時間排序
![Explore](https://github.com/z50205/Twittor/assets/19884343/58c5eb57-0df0-40ff-a001-dab48e80b570)
### Index
> 可發布推文，另提供上傳圖片的功能紀錄於/static資料夾內
![index](https://github.com/z50205/Twittor/assets/19884343/b2d229a7-d1de-4091-907f-d5ba53639f74)
### Username
> 可進行Follow功能，並有認證標籤提供辨識及自我介紹顯示
![username](https://github.com/z50205/Twittor/assets/19884343/e27c90c3-84be-468f-aa0c-2b7fe5430d2f)

## Reference
* 依照[repo](https://github.com/xiaopeng163/twittor)架構進行Flask學習並進行修改及新功能開發。

