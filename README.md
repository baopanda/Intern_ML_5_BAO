Cơ Sở Lý Thuyết
Thuật toán mình dùng trong bài này là Naive Bayes. 
Các bạn có thể đọc thêm về cơ sở lý thuyết tại đây: machinelearningcoban.com 
Mình sẽ chỉ giải thích một cách đơn giản nhất, đủ để bạn hiểu những gì mình đã làm ở trên. 
Bài toán đặt ra ở đây là xác định xác suất để một điểm dữ liệu x bất kì rơi vào các class 1, 2, 3, ... C. 
Hay chính xác là đi tính p(y = c|x) p(y=c∣x) Nói riêng về ứng dụng và bài toán mình đề cập ở trên. 
Mục tiêu ở đây, ví dụ với một string là "Tối nay có ăn tối không em". 
Chúng ta sẽ tách string này thành từng từ riêng biệt: "Tối", "nay", "có", ăn", "tối", "không", "em". 
Làm trương tự vậy với tất cả string. Và ta sẽ tính xác xuất trên tất cả các string với mỗi từ. 
Cứ hiểu đơn giản ở đây, là từ nào xuất hiện càng nhiều trong các tin nhắn được gán nhãn "ham" thì khi một tin nhắn chưa được gán nhãn chứa từ đấy.
Xác suất nó là tin nhắn "ham" càng cao. 
Tương tự vậy với các từ trong sms "spam".
