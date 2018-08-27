# Bài Toán Spam-Filtering 

## 1.Giới thiệu bài toán 

Tin nhắn rác (spam) thực sự là một vấn đề khó chịu đối với người sử dụng điện thoại di động. Bài viết này chúng ta sẽ áp dụng một thuật toán phân loại đơn giản có tên là Naive Bayes classifier dựa trên công thức xác suất Bayes có ở tất cả các giáo trình thống kê cơ bản để xây dựng một cỗ máy phân loại tin nhắn rác.

## 2.Xác định bài toán

* Input: Tập văn bản mail tiếng việt và có gán nhãn spam or ham (File DataTrain 80 văn bản)
* Output: Với mỗi văn bản phải xác định loại của văn bản đó là ham or spam (File DataTest 20 văn bản) 

## 3. Khám phá dữ liệu

* Đây là văn bản tiếng việt nên cần phải tách từ tiếng việt.
* Số lượng file spam và hàm trong file train đã cân bằng.

## 4.Giải quyết bài toán 

### 4.1. Tiền xử lý dữ liệu

* Sử dụng tool pyvi để tách từ tiếng việt 
* Chúng ta phải loại bỏ hết dấu câu để quá trình lọc spam-ham được chính xác. Nhận thấy, trong tiếng việt, chỉ đánh dấu vào các chứ cái a,d,e,i,o,u,y nên ta sẽ cần loại bỏ dấu trong các chữ này (ở chữ d là trong trường hợp đ). 
<img src="https://sv1.uphinhnhanh.com/images/2018/08/27/Capture99a3b.png">
* Tách Data và Nhãn ra riêng biệt để phục vụ cho quá trình training
<img src="https://i.imgur.com/tqSQ21U.png">

### 4.2. Bắt đầu training 
* Ở đây có một vấn đề, các giải thuật Machine Learning chỉ làm việc được với số, nên mình sẽ convert "ham", "spam" và cả các sms về định dạng số. Bắt đầu với "ham" (tương ứng với số 0) và "spam" (tương ứng với số 1). 
* Tiếp theo, ta sẽ transform sms messages thành dạng số ( dùng module mà scikit learn cung cấp ). Module mà scikit learn cung cấp cho phép chuyển đổi định dạng text thành vector, mình sẽ import CountVectorizer và transform text thành vector. Cách transform thế này: mình có một mảng các string, mình sẽ transform mảng này sao mỗi string sẽ chuyển đổi thành 1 vector có độ dài d (số từ xuất hiện ít nhất 1 lần), giá trị của thành phần thứ i trong vector chính là số lần từ đó xuất hiện trong string. 
* Sau đó, Ta sẽ import Naive Bayes, fit rồi predict là xong. 
<img src="https://i.imgur.com/BxwzfZm.png">
* Kết quả: 
<img src="https://i.imgur.com/LrsHzjQ.png">

## 5.Các cách để nâng cao accurancy bài toán. 
Ta có thể thấy accurancy chỉ đạt 85% có thể do nhiều lý do và có 1 số cách để raise nó lên như sau: 

1. Do data train quá ít nên kết quả chưa ra đc accurancy cao. Chúng ta nên tăng thêm data train cho nó

2.Apply grid search với MultinomialNB để tăng accurancy. Param mà mình apply Grid Search ở đây là alpha, người ta thêm nó vào cải thiện độ chính xác.
 <img src="https://i.imgur.com/I0HuPMU.png">
 
Nhưng kết quả cho ra k tăng lên (ta in ra best_param và kết quả của nó) :
<img src="https://i.imgur.com/XnEHoYl.png">

3.Ta nhận thấy, có vẻ như thuật toán NaiveBayes cho ta kết quả không được cao và một số tài liệu trên mạng có suggest thuật toán SVM cho bài toán lọc thư rác với một kết quả tốt hơn nên chúng ta sẽ test với thuật toán này với dữ liệu ham và spam riêng. 

<img src="https://sv1.uphinhnhanh.com/images/2018/08/27/Capturef7024.png">

Kết quả có raise lên nhưng có vẻ chưa đc như ý mình muốn:  <img src="https://sv1.uphinhnhanh.com/images/2018/08/27/Capture4cc2b.png">

Có vẻ như chúng ta lại phải tinh chỉnh mô hình thêm để tăng thêm accurancy rồi.Có lẽ các param1 và 2 trong GridSearch chưa khớp nhau rùi. Ta thử tham số C thành  "C": [0.50,0.51,0.52,0.53,0.54,0.55] xem sao. 
Thật đáng ngạc nhiên, Accurancy lên cao lên tương đối: 
<img src="https://sv1.uphinhnhanh.com/images/2018/08/27/Capturea72a4.png">


## 6.Cơ sở lý thuyết
Thuật toán mình dùng trong bài này là Naive Bayes.

Lý thuyết Bayes thì có lẽ không còn quá xa lạ với chúng ta nữa rồi. Nó chính là sự liên hệ giữa các xác suất có điều kiện. Điều đó gợi ý cho chúng ta rằng chúng ta có thể tính toán một xác suất chưa biết dựa vào các xác suất có điều kiện khác. Thuật toán Naive Bayes cũng dựa trên việc tính toán các xác suất có điều kiện đó. Nghe tên thuật toán là đã thấy gì đó ngây ngô rồi. Tại sao lại là Naive nhỉ. Không phải ngẫu nhiên mà người ta đặt tên thuật toán này như thế. Tên gọi này dựa trên một giả thuyết rằng các chiều của dữ liệu X=(x_1, x_2, ...., x_n)X=(x 
1
​	
 ,x 
2
​	
 ,....,x 
n
​	
 ) là độc lập về mặt xác suất với nhau. 
 <img src="https://viblo.asia/uploads/a468626e-0831-4efb-b4be-537f5329f050.png"> Chúng ta có thể thấy rằng giả thuyết này có vẻ khá ngây thơ vì trên thực tế điều này có thể nói là không thể xảy ra tức là chúng ta rất ít khi tìm được một tập dữ liệu mà các thành phần của nó không liên quan gì đến nhau. Tuy nhiên, giả thiết ngây ngô này lại mang lại những kết quả tốt bất ngờ. Giả thiết về sự độc lập của các chiều dữ liệu này được gọi là Naive Bayes (xin phép không dịch). Cách xác định class của dữ liệu dựa trên giả thiết này có tên là Naive Bayes Classifier (NBC). Tuy nhiên dựa vào giả thuyết này mà bước training và testing trở nên vô cùng nhanh chóng và đơn giản. Chúng ta có thể sử dụng nó cho các bài toán large-scale. Trên thực tế, NBC hoạt động khá hiệu quả trong nhiều bài toán thực tế, đặc biệt là trong các bài toán phân loại văn bản, ví dụ như lọc tin nhắn rác hay lọc email spam. 
 
 
 Vài nét về thuật toán SVM
 
 Áp dụng SVM trong phân loại thư rác
Đối với bài toán phân loại rác, giống như phần phân
loại Bayes (mục 2.1.3), thuật toán SVM xem mỗi vector i
xi
là
một vector đặc trưng biểu diễn cho nội dung thư và yi là nhãn
phân loại đối với dữ liệu huấn luyện. Tương tự như phần phân
loại Bayes, giá trị xi có thể là 0 hoặc 1. 

 <img src="https://sv1.uphinhnhanh.com/images/2018/08/27/Capture6ffdb.png"> 
