Bài Toán Spam-Filtering

1.Giới thiệu bài toán

Tin nhắn rác (spam) thực sự là một vấn đề khó chịu đối với người sử dụng điện thoại di động. Bài viết này chúng ta sẽ áp dụng một thuật toán phân loại đơn giản có tên là Naive Bayes classifier dựa trên công thức xác suất Bayes có ở tất cả các giáo trình thống kê cơ bản để xây dựng một cỗ máy phân loại tin nhắn rác.

2.Xác định bài toán

• Input: Tập văn bản mail tiếng việt và có gán nhãn spam or ham (File DataTrain 80 văn bản)
• Output: Với mỗi văn bản phải xác định loại của văn bản đó là ham or spam (File DataTest 20 văn bản) 

3. Khám phá dữ liệu

• Đây là văn bản tiếng việt nên cần phải tách từ tiếng việt.
• Số lương file spam và ham trong file train đã cân bằng.

4.Giải quyết bài toán 

4.1. Tiền xử lý dữ liệu

      4.1.1.Tách từ tiếng việt
      Sử dụng tool pyvi để tách từ tiếng việt 
