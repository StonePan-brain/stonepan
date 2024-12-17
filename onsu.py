import random

# Danh sách câu hỏi và đáp án
questions = [
    {
        "question": "Nguyên nhân nào đã thúc đẩy chủ nghĩa tư bản phát triển mạnh mẽ vào cuối thế kỷ XIX đầu thế kỷ XX?",
        "options": ["Thành tựu của cuộc cách mạng khoa học kỹ thuật.",
                    "Đã lập ra các tổ chức liên kết kinh tế, chính trị.",
                    "Chủ nghĩa tư bản chuyển sang giai đoạn độc quyền.",
                    "Các nước tư bản đã biết liên kết chặt chẽ với nhau."],
        "correct_answer": "A"
    },
    {
        "question": "Đâu là nguyên nhân quan trọng nhất dẫn tới sự xuất hiện các tổ chức độc quyền ở các nước tư bản từ thế kỷ XIX?",
        "options": ["Quá trình tập trung sản xuất và tập trung tư bản.",
                    "Do sự xâm lược và mở rộng hệ thống thuộc địa.",
                    "Ra đời chủ nghĩa đế quốc và chiến tranh thế giới.",
                    "Chủ nghĩa tư bản hiện đại ra đời và tự thích nghi."],
        "correct_answer": "A"
    },
    {
        "question": "Đâu là nguyên nhân quan trọng dẫn đến phong trào “chiếm lấy phố Wall” ở Mỹ?",
        "options": ["Sự bất bình của quần chúng nhân dân.",
                    "Được sự kích động, giúp đỡ từ bên ngoài.",
                    "Chống chế độ phân biệt chủng tộc ở Mỹ.",
                    "Cuộc khủng bố mới nhằm vào nước Mỹ."],
        "correct_answer": "A"
    },
    {
        "question": "Theo Lê –nin chủ nghĩa tư bản độc quyền vào những năm đầu thế kỉ XX có bao nhiêu đặc điểm lớn?",
        "options": ["2.",
                    "3.",
                    "4.",
                    "5."],
        "correct_answer": "D"
    },
    {
        "question": "Một trong những đóng góp tích cực của chủ nghĩa tư bản hiện đại đối với nền văn minh nhân loại là",
        "options": ["chế tạo thành công bom nguyên tử.",
                    "tạo ra lượng của cải vật chất khổng lồ.",
                    "gây ra hiện tượng hiệu ứng nhà kính.",
                    "khắc phục tình trạng nước biển dâng."],
        "correct_answer": "B"
    },
    {
        "question": "Một trong những đặc điểm của chủ nghĩa tư bản hiện đại là",
        "options": ["xuất hiện các tổ chức độc quyền.",
                    "Là chủ nghĩa tư bản độc quyền nhà nước.",
                    "tiến hành cách mạng công nghiệp.",
                    "sản xuất hàng hoá theo dây chuyền."],
        "correct_answer": "B"
    },
    {
        "question": "Nửa sau thế kỷ XIX, chủ nghĩa tư bản được xác lập ở quốc gia nào sau đây?",
        "options": ["Anh.",
                    "Pháp.",
                    "Italia.",
                    "Mỹ."],
        "correct_answer": "C"
    },
    {
        "question": "Chủ nghĩa tư bản mở rộng phạm vi ra ngoài châu Âu từ",
        "options": ["cuối thế kỷ XVIII.",
                    "cuối thế kỷ XVII.",
                    "đầu thế kỷ XIX.",
                    "đầu thế kỷ XVIII."],
        "correct_answer": "A"
    },
    {
        "question": "Đâu là tác động của các cuộc cách mạng công nghiệp thời cận đại đối với chủ nghĩa tư bản?",
        "options": ["Giải quyết được các mâu thuẫn, tranh chấp trong xã hội.",
                    "Thay đổi bộ mặt chủ nghĩa tư bản theo hướng tích cực.",
                    "Thu hẹp khoảng cách phân biệt giàu nghèo trong xã hội.",
                    "Xoá bỏ được tình trạng phân biệt chủng tộc ở các nước."],
        "correct_answer": "B"
    },
    {
        "question": "Từ sự phát triển kinh tế của các nước tư bản Âu - Mĩ cuối thế kỉ XIX đầu thế kỉ XX, hiện nay để tăng năng suất lao động, Việt Nam cần phải",
        "options": ["nghiên cứu, cải tiến, áp dụng khoa học - kĩ thuật vào sản xuất.",
                    "tăng cường thành lập các tổ chức độc quyền để tăng cạnh tranh.",
                    "Tham gia các liên minh kinh tế với các nước tư bản hùng mạnh.",
                    "nhà nước tăng cường mua các phát minh khoa học trên thế giới."],
        "correct_answer": "A"
    },
    {
        "question": "Chủ nghĩa xã hội phát triển như thế nào sau Chiến tranh thế giới thứ nhất? ",
        "options": ["Mở rộng ảnh hưởng tại Châu Á, châu Âu.",
                    "Giảm thiểu ảnh hưởng của Liên Xô trong khu vực. ",
                    "Tham gia các liên minh kinh tế với các nước tư bản hùng mạnh.",
                    "Hoàn toàn bị lãng quên và không còn tồn tại."],
        "correct_answer": "A"
    },
    {
        "question": "Một trong những nước cộng hoà đầu tiên gia nhập Liên bang Cộng hoà xã hội chủ nghĩa Xô viết vào năm 1922 là",
        "options": ["U-crai-na.",
                    "Trung Quốc. ",
                    "Ai Cập.",
                    "Ấn Độ."],
        "correct_answer": "A"
    },
    {
        "question": "Hình ảnh nào sau đây xuất hiện trên Quốc huy đầu tiên của Liên Xô (1923)?",
        "options": ["Lúa mì.",
                    "Mặt trăng. ",
                    "Lúa nước.",
                    "Cành ô liu."],
        "correct_answer": "A"
    },
    {
        "question": "Năm 1924, Hiến pháp đầu tiên của Liên Xô đã",
        "options": ["hoàn thành quá trình thành lập nhà nước.",
                    "kết thúc cuộc đấu tranh bảo vệ tổ quốc. ",
                    "thực hiện quyền bình đẳng, tự quyết của các dân tộc.",
                    "giải quyết vấn đề hòa bình cho nhân dân ruộng đất cho nông dân."],
        "correct_answer": "A"
    },
    {
        "question": "Sự ra đời của Liên bang cộng hòa xã hội chủ nghĩa Xô Viết đã",
        "options": ["giải phóng các dân tộc trên toàn thế giới.",
                    "lãnh đạo phong trào công nhân ở các nươc tư bản. ",
                    "tạo nên sức mạnh tổng hợp để xây dựng CNXH và bảo vệ đất nước.",
                    "đập tan âm mưu xâm lược của các nước đế quốc."],
        "correct_answer": "C"
    },
    {
        "question": "Đại hội lần thứ nhất các Xô viết toàn Liên bang diễn ra cuối tháng 12 năm 1922 đã tuyên bố thành lập",
        "options": ["Liên bang Cộng hòa xã hội chủ nghĩa Xô viết (gọi tắt là Liên Xô).",
                    "Cộng hòa Xô viết đầu tiên là Nga, Ucraina, Bêlarút và Captazơ. ",
                    "Cộng đồng các quốc gia độc lập (SNG).",
                    "nước Nga Xô viết Xã hội chủ nghĩa."],
        "correct_answer": "A"
    },
    {
        "question": "Liên Xô là tên gọi tắt của ",
        "options": ["Liên bang Cộng hòa xã hội chủ nghĩa Xô viết.",
                    "Liên minh các đảng ở nước Nga. ",
                    "Liên hiệp các nước xã hội chủ nghĩa Xô viết.",
                    "Phong trào liên kết toàn Xô viết."],
        "correct_answer": "A"
    },
    {
        "question": "Lãnh đạo Cách mạng tháng Mười Nga năm 1917 là  ",
        "options": ["Mác.",
                    "Ănghen. ",
                    "Xtalin.",
                    "Lênin."],
        "correct_answer": "D"
    },
    {
        "question": "Ngày 25/10/1917 (theo lịch Nga) ở nước Nga diễn ra sự kiện nào? ",
        "options": ["Cách mạng Tháng Mười Nga thắng lợi.",
                    "Nga chính thức tham gia vào cuộc chiến tranh thế giới thứ nhất.  ",
                    "Luận cương Tháng Tư được thông qua.",
                    "Nga rút khỏi chiến tranh thế giới thứ nhất."],
        "correct_answer": "A"
    },
    {
        "question": "Sau khi giành thắng lợi, chính quyền Xô viết ban hành ",
        "options": ["“Sắc lệnh Hòa bình” và “Sắc lệnh Ruộng đất”.",
                    "“Sắc lệnh Ruộng đất” và “Sắc lệnh kinh tế - xã hội”. ",
                    "“Sắc lệnh Tổng tuyển cử” và “Sắc lệnh Hòa bình”.",
                    "“Sắc lệnh kinh tế - xã hội”."],
        "correct_answer": "A"
    },
    {
        "question": "Liên bang Cộng hoà xã hội chủ nghĩa Xô viết được thành lập trong bối cảnh nào? ",
        "options": ["Các nước cộng hòa Xô viết phát triển không đồng đều về kinh tế.",
                    "Mâu thuẫn giữa các dân tộc Nga với chế độ Nga Hoàng gay gắt. ",
                    "Các nước cộng hòa Xô Viết có sự thống nhất về chính sách phát triển. ",
                    "Mâu thuẫn giữa nước Nga với các nước cộng hòa Xô viết gay gắt."],
        "correct_answer": "A"
    },
    {
        "question": "Quốc gia nào sau đây là nhà nước chuyên chính vô sản đầu tiên trên thế giới?",
        "options": ["Anh.",
                    "Pháp.",
                    "Liên Xô. ",
                    "Mĩ."],
        "correct_answer": "C"
    },
    {
        "question": "Khi mới thành lập, Liên Xô gồm 4 nước Cộng hoà Xô viết đầu tiên là:",
        "options": ["Nga, U-crai-na, ngoại Cáp-ca-dơ và Lat-vi-a.",
                    "Nga, Bê-lô-rút-xi-a, ngoại Cáp-ca-dơ và Lat-vi-a.",
                    "Nga, Bê-lô-rút-xi-a, U-crai-na và ngoại Cáp-ca-dơ. ",
                    "Nga, Bê-lô-rút-xi-a, U-crai-na, Ka-dắc-xtăn."],
        "correct_answer": "C"
    },
    {
        "question": "Tháng 12-1922, Đại hội lần thứ nhất của Xô viết toàn Liên bang quyết định ",
        "options": ["thành lập Liên bang cộng hòa xã hội chủ nghĩa Xô viết.",
                    "nước Nga Xô viết rút khỏi chiến tranh thế giới.",
                    "lật đổ hoàn toàn chế độ Nga Hoàng Nicolai II. ",
                    "thành lập chế độ quân chủ chuyên chế ở Nga."],
        "correct_answer": "A"
    },
    {
        "question": "Việc thành lập Liên bang cộng hòa xã hội chủ nghĩa Xô Viết có ý nghĩa như thế nào đối với nước Nga?",
        "options": ["Thúc đẩy phong trào cách mạng tại châu Âu. ",
                    "Kiềm chế sự phát triển của chủ nghĩa tư bản. ",
                    "Xây dựng được liên minh quân sự chống Đức Quốc xã. ",
                    "Xác lập chế độ xã hội chủ nghĩa trên toàn lãnh thổ Liên Xô."],
        "correct_answer": "D"
    },
    {
        "question": "Nội dung nào sau đây là nguyên nhân khách quan dẫn đến sự sụp đổ của chủ nghĩa xã hội\n ở Liên Xô và Đông Âu trong đầu thập niên 90 (thế kỉ XX)? ",
        "options": ["Khi cải tổ lại mắc phải nhiều thiếu sót và sai lầm. ",
                    "Sự chống phá của các thế lực thù địch trong và ngoài nước.  ",
                    "Đường lối lãnh đạo mang tính chủ quan, duy ý chí.  ",
                    "Không bắt kịp bước phát triển của khoa học kĩ thuật."],
        "correct_answer": "B"
    },
    {
        "question": "Chính quyền Xô viết được thành lập ở nước Nga sau Cách mạng tháng Mười (1917) không đại diện cho giai cấp nào sau đây?",
        "options": ["Công nhân. ",
                    "Nông dân.  ",
                    "Binh lính.  ",
                    "Tư sản."],
        "correct_answer": "D"
    },
    {
        "question": "Hình thức đấu tranh chủ yếu trong Cách mạng tháng Mười năm 1917 ở Nga là",
        "options": ["chiến tranh cách mạng. ",
                    "bạo động cách mạng.  ",
                    "khởi nghĩa vũ trang.  ",
                    "khởi nghĩa từng phần."],
        "correct_answer": "C"
    },
    {
        "question": "Theo Hiến pháp Liên Xô biện pháp giải quyết vấn đề dân tộc là dựa trên nguyên tắc",
        "options": ["bình đẳng và tình hữu nghị giữa các dân tộc. ",
                    "cạnh tranh và hợp tác kinh tế giữa các dân tộc. ",
                    "tôn trọng chủ quyền lãnh thổ giữa các dân tộc.",
                    "không can thiệp vào công việc nội bộ của nhau."],
        "correct_answer": "A"
    },
    {
        "question": "Cách mạng tháng Mười Nga đã thay đổi cục diện chính trị thế giới vì đã",
        "options": ["xác lập chế độ xã hội chủ nghĩa, làm cho hệ thống tư bản chủ nghĩa không còn là duy nhất. ",
                    "tạo tiền đề cho sự ra đời của các tổ chức vô sản quốc tế. ",
                    "đưa nhân dân lao động Nga lần đầu tiên được làm chủ đất nước, làm chủ vận mệnh của mình.",
                    "cổ vũ và để lại nhiều bài học kinh nghiệm quý báu cho phong trào đấu tranh giải phóng dân tộc."],
        "correct_answer": "A"
    },
    {
        "question": "Đảng và Nhà nước Trung Quốc xác định trọng tâm của đường lối cải cách - mở cửa từ năm 1978 là gì?",
        "options": ["Lấy cải cách kinh tế làm trung tâm. ",
                    "Lấy đổi mới chính trị làm trung tâm.",
                    "Đổi mới chính trị là nền tảng để đẩy mạnh đổi mới kinh tế.",
                    "Đổi mới kinh tế và đổi mới chính trị được tiến hành đồng thời."],
        "correct_answer": "A"
    },
    {
        "question": "Trong 30 năm (1978 - 2008) thực hiện đường lối cải cách, Trung Quốc đã đạt được thành tựu về kinh tế nào dưới đây",
        "options": ["Năm 1998, phóng tàu vũ trụ có người lái.",
                    "Là con rồng kinh tế ở châu Á.",
                    "Trở thành trung tâm kinh tế tài chính thế giới.",
                    "Cường quốc có tốc độ phát triển nhanh nhất thế giới."],
        "correct_answer": "D"
    },
    {
        "question": "Sự ra đời của quốc gia nào sau đây đã mở rộng không gian địa lý của chủ nghĩa xã hội sang khu vực Mĩ latinh?",
        "options": ["Thái Lan.",
                    "Cuba.",
                    "Ấn Độ.",
                    "Iran."],
        "correct_answer": "B"
    },
    {
        "question": "Sự ra đời của quốc gia nào sau đây đã mở rộng không gian địa lý của chủ nghĩa xã hội sang khu vực châu Á?",
        "options": ["Mêhicô.",
                    "Trung Quốc.",
                    "Ấn Độ.",
                    "Brazil."],
        "correct_answer": "B"
    },
    {
        "question": "Nội dung trọng tâm trong đường lối cải cách mở của ở Trung Quốc năm 1978 là",
        "options": ["chính trị.",
                    "kinh tế.",
                    "văn hóa.",
                    "giáo dục."],
        "correct_answer": "B"
    },
    {
        "question": "Trong công cuộc cải cách mở cửa (1978), Trung Quốc đạt được thành tựu nào về khoa học - công nghệ?",
        "options": ["Kinh tế đứng thứ hai thế giới.",
                    "Xóa đói giảm nghèo.",
                    "Đã cải cách giáo dục toàn diện.",
                    "Phóng thành công tàu vũ trụ. "],
        "correct_answer": "D"
    },
    {
        "question": "Hiện nay, quốc gia nào kiên trì theo con đường xã hội chủ nghĩa ở khu vực Mĩ Latinh?",
        "options": ["Iran.",
                    "Irắc.",
                    "Thổ Nhĩ Kì.",
                    "Cuba."],
        "correct_answer": "D"
    },
    {
        "question": "Từ năm 1991 đến nay, nhân dân một số nước ở khu vực nào sau đây tiến hành cải cách, đổi mới, kiên định con đường xã hội chủ nghĩa?",
        "options": ["Châu Á.",
                    "Bắc Phi.",
                    "Tây Âu.",
                    "Nam Phi."],
        "correct_answer": "A"
    },
    {
        "question": "Tháng 12-1978, quốc gia nào sau đây thực hiện công cuộc cải cách và mở cửa, đạt được thành tựu to lớn về kinh tế xã hội?",
        "options": ["Liên Xô.",
                    "Cu-ba.",
                    "Ấn Độ.",
                    "Trung Quốc."],
        "correct_answer": "D"
    },
    {
        "question": "Từ năm 1978, để đưa đất nước vượt qua những khó khăn, thách thức, Trung Quốc thực hiện chủ trương nào sau đây?",
        "options": ["Tiến hành công cuộc đổi mới đất nước.",
                    "Tiến hành công cuộc cải cách mở cửa.",
                    "Tiến hành công cuộc cải tổ đất nước.",
                    "Tiến hành cách mạng dân tộc, dân chủ."],
        "correct_answer": "B"
    },
    {
        "question": "Quốc gia nào sau đây không phát triển đất nước theo con đường XHCN?",
        "options": ["Việt Nam.",
                    "Lào.",
                    "Cam-pu-chia.",
                    "Triều Tiên."],
        "correct_answer": "C"
    },
    {
        "question": "Hiện nay, những quốc gia nào vẫn đi theo đường lối xã hội chủ nghĩa?",
        "options": ["Thái Lan, Mianma, Malaixia, Singapo, Ấn Độ.",
                    "Triều Tiên, Mông Cổ, Hàn Quốc, Ấn Độ, Nhật Bản.",
                    "Angiêri, Tuynidi, Marốc, Ai Cập, Xu đăng.",
                    "Trung Quốc, Cuba, Việt Nam, Lào."],
        "correct_answer": "D"
    },
    {
        "question": "Đâu không phải là thành tựu về khoa học - kĩ thuật của Trung Quốc từ sau công cuộc cải cách - mở cửa (1978)?",
        "options": ["Phóng thành công các con tàu “Thần Châu” vào không gian vũ trụ.",
                    "Là nước đầu tiên phóng thành công vệ tinh nhân tạo của trái đất.",
                    "Thực hiện chương trình thám hiểm không gian từ năm 1992",
                    "Là quốc gia thứ ba (sau Nga, Mĩ) có tàu cùng với con người bay vào vũ trụ."],
        "correct_answer": "B"
    },
    {
        "question": "Sự kiện nào sau đây đã đánh dấu chủ nghĩa xã hội mở rộng sang khu vực Mĩ La-tinh?",
        "options": ["Thắng lợi của cách mạng Việt Nam (1945).",
                    "Nước Cộng hòa Ấn Độ thành lập (1950).",
                    "Hiệp định Giơ-ne-vơ về Đông Dương (1954).",
                    "Thắng lợi của cách mạng Cu-ba (1959)."],
        "correct_answer": "D"
    },
    {
        "question": "Từ năm 1976 đến nay, nhân dân Việt Nam thực hiện nhiệm vụ chiến lược nào?",
        "options": ["Xây dựng chủ nghĩa xã hội.",
                    "Kháng chiến chống Pháp.",
                    "Kháng chiến chống Mĩ.",
                    "Giải phóng dân tộc."],
        "correct_answer": "A"
    },
    {
        "question": "Một trong những nguyên nhân chung dẫn đến thắng lợi của công cuộc cải cách mở cửa của Trung Quốc và công cuộc đổi mới ở Việt Nam là",
        "options": ["sự lãnh đạo đúng đắn của Đảng cộng sản.",
                    "tận dụng các yêu tố bên ngoài để phát triển.",
                    "sự giúp đỡ của Liên Xô và các nước Đông Âu.",
                    "lãnh thổ rộng lớn, tài nguyên phong phú, nhân lực dồi dào."],
        "correct_answer": "A"
    },
    {
        "question": "Trung Quốc duy trì được tốc độ tăng trưởng kinh tế cao trong nhiều năm nhờ nhân tố khách quan nào sau đây?",
        "options": ["Quyết tâm cải cách thể chế kinh tế của Đảng, Chính phủ, nhân dân Trung Quốc.",
                    "Đường lối cải cách, mở cửa đúng đắn của Đảng Cộng sản Trung Quốc.",
                    "Tận dụng cơ hội từ xu thế toàn cầu hóa kinh tế mang lại.",
                    "Nguồn nhân lực dồi dào, lãnh thổ rộng lớn, tài nguyên phong phú."],
        "correct_answer": "C"
    },
    {
        "question": "Điểm chung của Việt Nam và Trung Quốc từ năm 1991 đến nay là",
        "options": ["từng bước tiến hành cải cách, mở cửa, đổi mới.",
                    "trở thành các quốc gia có tốc độ tăng trưởng cao.",
                    "tham gia vào tổ chức ASEAN.",
                    "thực hiện nền kinh tế kế hoạch hóa tập trung."],
        "correct_answer": "A"
    },
    {
        "question": "Nội dung nào sau đây là một trong những ý nghĩa của công cuộc cải cách mở cửa của Trung Quốc?",
        "options": ["Giúp Trung Quốc trở thành cường quốc tư bản chủ nghĩa.",
                    "Tạo điều kiện cho sự hội nhập quốc tế trên các lĩnh vực.",
                    "Đưa Trung Quốc trở thành một trong các con rồng châu Á.",
                    "Đưa cơ chế tập trung, quan liêu bao cấp thành xu thế chủ đạo."],
        "correct_answer": "B"
    },
    {
        "question": "Điểm giống nhau trong công cuộc cải tổ ở Liên Xô và cuộc cải cách mở cửa ở Trung Quốc là",
        "options": ["thực hiện đa nguyên đa đảng để cùng lãnh đạo đất nước.",
                    "duy trì cơ chế quản lí tập trung.",
                    "chú trọng đổi mới chính trị và xã hội.",
                    "tiến hành khi đất nước khủng hoảng."],
        "correct_answer": "D"
    },
]


# Hàm để kiểm tra và chấm điểm
def ask_questions(questions):
    score = 0
    wrong_answers = []  # Danh sách lưu các câu sai
    question_counter = 0  # Biến đếm số câu hỏi đã trả lời
    total_questions = len(questions)  # Tổng số câu hỏi

    random.shuffle(questions)  # Trộn ngẫu nhiên danh sách câu hỏi

    for q in questions:
        question_counter += 1  # Tăng biến đếm câu hỏi lên

        # Hiển thị số câu hỏi còn lại và câu hỏi hiện tại
        print(f"\nCâu hỏi {question_counter}/{total_questions}:")
        print(f"Số câu hỏi còn lại: {total_questions - question_counter}")

        # Lưu đáp án đúng (A, B, C, D)
        correct_answer = q["correct_answer"]
        options = q["options"]

        # Xáo trộn các đáp án
        shuffled_options = options[:]
        random.shuffle(shuffled_options)

        # Tìm vị trí của đáp án đúng trong danh sách xáo trộn
        correct_answer_shuffled = shuffled_options.index(q["options"][ord(correct_answer) - ord('A')])

        # Tạo lại chữ cái (A, B, C, D) tương ứng với các lựa chọn sau khi xáo trộn
        option_labels = ['A', 'B', 'C', 'D']
        answer_mapping = dict(zip(option_labels, shuffled_options))

        print("\n" + q["question"])

        # Hiển thị các đáp án theo thứ tự A, B, C, D sau khi xáo trộn
        for label in option_labels:
            print(f"{label}. {answer_mapping[label]}")

        # Đảm bảo người dùng nhập đáp án hợp lệ
        while True:
            answer = input("Chọn đáp án (A, B, C, D): ").upper()
            if answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Vui lòng nhập A, B, C hoặc D.")

        # Kiểm tra đáp án người chơi
        if answer == option_labels[correct_answer_shuffled]:
            print("\033[32mĐúng rồi!\033[0m")  # In màu xanh cho đáp án đúng
            score += 1
        else:
            print(f"\033[31mSai rồi.\033[0m")  # In màu đỏ cho câu sai
            # In đáp án đúng với màu xanh và xuống dòng riêng biệt
            print(f"\033[34mĐáp án đúng là {option_labels[correct_answer_shuffled]}: {answer_mapping[option_labels[correct_answer_shuffled]]}\033[0m")
            wrong_answers.append(q)  # Thêm câu hỏi vào danh sách các câu sai

        # Dòng gạch dưới giúp phân biệt giữa các câu hỏi
        print("-" * 40)

    print(f"\nKết quả: Bạn đã trả lời đúng \033[34m{score}/{len(questions)}\033[0m câu.")  # In kết quả màu xanh

    # Nếu có câu sai, hỏi người chơi có muốn trả lời lại không
    if wrong_answers:
        print("\nBạn có muốn trả lời lại những câu sai không? (Có/Không)")
        retry = input().strip().lower()
        if retry == "có":
            ask_questions(wrong_answers)  # Đặt lại các câu sai để người chơi trả lời lại
            return
        else:
            print("\nCảm ơn bạn đã tham gia!")

    # Hỏi người chơi có muốn chơi lại từ đầu không
    print("\nBạn có muốn chơi lại từ đầu không? (A: Có/B: Không)")
    play_again = input().strip().lower()
    if play_again == "a":
        ask_questions(questions)  # Gọi lại hàm ask_questions để chơi lại từ đầu
    else:
        print("\nCảm ơn bạn đã tham gia!")

# Chạy chương trình
ask_questions(questions)
