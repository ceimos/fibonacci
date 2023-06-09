import sqlite3
from sample_data_stuff.testdata import *

input_string='''
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (11,3203,"2023-01-06","23:28:01","vel,","nascetur","mango"),
  (12,3214,"2020-10-17","14:21:44","dui.","arcu.","mango"),
  (13,1009,"2021-01-28","19:31:58","risus","cursus","banana"),
  (14,3103,"2021-08-24","10:21:18","tempor,","ac","apple"),
  (15,4747,"2023-09-24","2:50:57","tincidunt","purus,","apple"),
  (16,4564,"2020-12-01","11:20:48","placerat,","consectetuer","apple"),
  (17,3057,"2021-12-18","19:42:29","vitae,","ultricies","apple"),
  (18,2647,"2024-02-11","4:30:53","egestas","neque.","apple"),
  (19,2827,"2023-03-21","14:57:16","sociis","purus.","mango"),
  (20,2819,"2020-12-26","0:34:18","natoque","magna","banana");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (21,1485,"2024-03-31","16:15:12","In","malesuada","apple"),
  (22,139,"2020-10-22","0:49:29","ultrices","ipsum","apple"),
  (23,981,"2020-10-04","2:57:32","at","sed","apple"),
  (24,3282,"2023-05-10","5:53:32","sit","tincidunt","banana"),
  (25,4421,"2022-03-27","14:49:17","eu","luctus","banana"),
  (26,985,"2023-06-11","6:57:25","in","non","apple"),
  (27,1261,"2022-08-22","17:20:46","convallis","nascetur","apple"),
  (28,4527,"2022-12-07","14:56:09","in","Suspendisse","apple"),
  (29,3324,"2023-04-29","18:47:23","aliquam","lectus","apple"),
  (30,3174,"2023-12-05","11:14:22","nascetur","Fusce","banana");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (31,707,"2023-03-26","16:10:41","tellus","Fusce","apple"),
  (32,4880,"2021-09-18","17:26:57","magna","arcu.","mango"),
  (33,1474,"2021-05-24","13:07:04","Integer","Donec","apple"),
  (34,4219,"2020-12-28","18:40:28","ipsum","purus,","apple"),
  (35,1980,"2022-06-23","22:39:28","dignissim","elementum","banana"),
  (36,4406,"2023-05-14","7:33:59","sit","est","mango"),
  (37,532,"2023-07-03","0:20:20","dictum.","Duis","mango"),
  (38,493,"2021-04-20","20:52:49","ac","mattis.","mango"),
  (39,783,"2021-08-03","11:56:46","aliquam","nunc","apple"),
  (40,1612,"2020-11-22","14:12:02","molestie","amet,","banana");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (41,2984,"2021-09-13","20:03:41","eu","Nulla","apple"),
  (42,139,"2021-05-26","20:11:04","aliquet,","vestibulum.","mango"),
  (43,1274,"2023-07-18","19:15:09","diam","ipsum","mango"),
  (44,4426,"2022-03-01","11:48:55","Cum","libero.","mango"),
  (45,610,"2022-07-15","20:35:15","erat","erat,","banana"),
  (46,2901,"2023-10-11","4:08:40","vel","felis","apple"),
  (47,1665,"2023-09-25","23:30:54","Duis","Cras","mango"),
  (48,2267,"2024-01-13","5:51:34","aliquet","amet,","mango"),
  (49,3632,"2022-08-28","1:52:43","sodales","arcu","apple"),
  (50,234,"2021-06-01","11:11:22","volutpat.","aliquet","apple");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (51,4268,"2023-03-16","13:18:59","sociosqu","semper","apple"),
  (52,4867,"2021-07-22","17:22:34","ut","ligula","mango"),
  (53,2724,"2020-08-07","15:44:45","aliquet","ut","banana"),
  (54,4797,"2023-12-22","11:37:12","mollis","nonummy.","mango"),
  (55,3987,"2020-11-25","21:50:14","vitae,","vel,","banana"),
  (56,4153,"2023-08-31","17:36:42","nunc,","nonummy","mango"),
  (57,3143,"2021-08-02","6:15:47","vitae","dictum.","mango"),
  (58,4676,"2021-04-27","6:54:24","Duis","fringilla","mango"),
  (59,1666,"2021-05-01","10:51:50","lacus,","orci","banana"),
  (60,4495,"2023-06-02","20:42:46","amet,","lobortis","mango");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (61,323,"2022-04-12","8:35:51","dignissim.","sodales","banana"),
  (62,2936,"2023-02-21","8:46:44","amet","pede","apple"),
  (63,515,"2023-12-28","8:26:16","ultricies","Nunc","mango"),
  (64,4375,"2021-11-15","22:05:52","cubilia","vulputate,","apple"),
  (65,4799,"2021-02-15","9:08:45","nec","cursus","banana"),
  (66,4254,"2024-01-20","22:39:57","vel","vel","apple"),
  (67,1092,"2020-10-26","11:12:32","Aliquam","malesuada","banana"),
  (68,4411,"2024-03-31","12:24:46","amet","ipsum.","banana"),
  (69,546,"2022-12-24","7:28:01","lorem","a","banana"),
  (70,3995,"2021-03-25","5:15:12","vulputate","sit","banana");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (71,3410,"2021-06-11","21:15:57","lorem","quam.","banana"),
  (72,3884,"2024-03-16","10:14:19","a","justo","banana"),
  (73,3108,"2020-08-24","1:10:01","eu","tellus","mango"),
  (74,3780,"2021-10-13","16:21:58","Aenean","dolor","banana"),
  (75,4458,"2021-08-03","6:43:21","nulla","dictum","mango"),
  (76,4913,"2022-02-14","22:59:35","Etiam","Nunc","apple"),
  (77,95,"2024-01-21","18:13:15","magna.","Phasellus","apple"),
  (78,4276,"2020-08-18","6:12:06","Integer","in,","apple"),
  (79,4207,"2021-12-06","10:42:01","enim.","felis","apple"),
  (80,97,"2022-02-24","10:44:25","cursus.","a,","mango");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (81,3152,"2022-09-09","0:56:43","bibendum","Fusce","mango"),
  (82,798,"2020-12-05","3:00:08","sed,","tempor","apple"),
  (83,967,"2021-02-04","11:50:42","semper","massa.","apple"),
  (84,770,"2021-07-09","11:36:39","metus.","luctus","mango"),
  (85,1102,"2020-09-05","15:09:18","cursus","faucibus","banana"),
  (86,134,"2022-11-15","15:02:02","eu,","risus.","banana"),
  (87,2644,"2022-05-09","21:23:19","sed,","tellus","apple"),
  (88,1480,"2023-08-18","13:20:20","dolor","mauris.","mango"),
  (89,2205,"2022-05-29","6:47:19","pulvinar","Curae","banana"),
  (90,2898,"2023-06-02","15:17:07","dolor","erat.","mango");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (91,2497,"2020-09-13","11:39:14","augue.","erat","apple"),
  (92,2246,"2021-01-11","23:01:31","Cum","Mauris","banana"),
  (93,3515,"2023-12-26","7:17:21","at","adipiscing","banana"),
  (94,3006,"2022-03-22","5:36:52","gravida","dictum","apple"),
  (95,4198,"2021-11-22","18:48:52","egestas","ac","apple"),
  (96,3396,"2020-09-02","7:09:19","ornare","risus","mango"),
  (97,2111,"2023-09-12","23:20:01","erat","Vestibulum","apple"),
  (98,4828,"2021-04-11","9:59:03","eu","Cras","apple"),
  (99,2340,"2021-01-07","4:14:39","amet","fringilla.","mango"),
  (100,4394,"2021-11-30","14:26:18","lorem","nisi","banana");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (101,1611,"2021-02-18","20:22:28","elit.","Quisque","apple"),
  (102,4974,"2024-03-17","15:12:44","magnis","vitae","apple"),
  (103,2664,"2023-01-28","0:42:07","pharetra","non,","apple"),
  (104,1391,"2021-07-27","8:31:10","mollis","Etiam","apple"),
  (105,3712,"2022-08-03","2:22:23","magna","Etiam","mango"),
  (106,474,"2021-11-21","5:09:58","at,","ante,","banana"),
  (107,3351,"2024-03-28","5:41:52","ornare.","placerat","mango"),
  (108,1514,"2021-10-28","0:01:28","mi.","Aenean","mango"),
  (109,638,"2022-09-15","16:41:37","Quisque","diam","apple"),
  (110,2142,"2023-04-04","9:11:05","mus.","volutpat.","banana");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (111,3790,"2021-02-22","7:31:21","dignissim","Proin","apple"),
  (112,4056,"2021-06-25","20:37:21","Proin","tellus.","banana"),
  (113,3514,"2023-08-11","11:06:47","Nulla","feugiat","apple"),
  (114,2334,"2022-04-30","11:36:18","Aliquam","eu","apple"),
  (115,2668,"2024-01-03","22:46:43","euismod","cursus","apple"),
  (116,2857,"2021-04-26","15:32:29","Aenean","purus.","apple"),
  (117,449,"2022-06-10","12:55:19","scelerisque","dis","mango"),
  (118,1885,"2021-05-11","5:04:54","Suspendisse","Mauris","apple"),
  (119,1791,"2021-01-22","15:16:16","Donec","sagittis","banana"),
  (120,4427,"2021-09-13","1:50:03","nec,","bibendum","apple");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (121,735,"2022-11-16","3:09:36","interdum.","leo.","banana"),
  (122,1601,"2020-08-05","10:10:02","lobortis,","Nullam","apple"),
  (123,2390,"2020-11-26","1:56:04","lacinia","et","banana"),
  (124,1993,"2023-01-12","23:55:45","amet","dolor","apple"),
  (125,4322,"2023-03-29","19:00:19","interdum.","arcu.","banana"),
  (126,1973,"2022-10-18","16:28:58","Quisque","nec,","banana"),
  (127,2332,"2022-07-03","2:21:08","a","sit","banana"),
  (128,2589,"2022-06-30","22:26:19","Curabitur","aliquam","apple"),
  (129,3160,"2021-06-06","9:18:52","Fusce","elementum","apple"),
  (130,1364,"2023-05-26","6:49:29","Curabitur","urna","mango");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (131,3498,"2023-05-04","5:18:39","Aenean","neque.","apple"),
  (132,1196,"2021-05-03","15:51:24","posuere","et","apple"),
  (133,4511,"2022-09-12","20:23:06","sociis","felis.","mango"),
  (134,1978,"2023-10-25","2:17:38","tempor","cursus.","banana"),
  (135,2666,"2024-02-08","21:55:22","dolor,","sollicitudin","mango"),
  (136,2907,"2021-03-11","13:20:00","magna","augue","apple"),
  (137,2772,"2022-02-16","15:02:36","lacus.","natoque","banana"),
  (138,4971,"2022-11-10","20:31:19","nec","Etiam","banana"),
  (139,2472,"2022-03-01","12:56:00","Proin","fermentum","mango"),
  (140,3233,"2022-09-20","20:58:28","sit","suscipit,","banana");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (141,833,"2023-03-05","14:50:31","vulputate","eu","banana"),
  (142,1854,"2024-02-11","9:48:09","quam","egestas","banana"),
  (143,2264,"2021-12-30","0:34:03","diam.","a","mango"),
  (144,1988,"2021-06-23","11:40:22","auctor","mollis","mango"),
  (145,3838,"2022-05-29","8:04:51","cubilia","malesuada","banana"),
  (146,2996,"2020-09-17","13:19:53","ultricies","Donec","mango"),
  (147,1856,"2020-08-05","3:52:37","ullamcorper","ultrices","apple"),
  (148,3035,"2022-01-23","13:02:25","dis","aliquet,","apple"),
  (149,4726,"2022-04-23","6:19:37","velit","Quisque","mango"),
  (150,947,"2022-12-08","17:25:13","sapien","molestie","mango");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (151,3567,"2023-10-31","5:42:57","magna.","tellus.","mango"),
  (152,600,"2022-03-19","0:47:08","ultrices.","amet,","apple"),
  (153,2431,"2022-01-22","21:15:53","mollis","magna","banana"),
  (154,862,"2023-10-30","15:51:43","pede","nisi.","banana"),
  (155,1759,"2021-06-09","0:54:21","Donec","Fusce","mango"),
  (156,2457,"2023-12-24","14:49:04","Nulla","fringilla","banana"),
  (157,2239,"2021-09-23","18:23:37","felis","vel,","mango"),
  (158,2871,"2021-04-19","17:27:49","Ut","lectus","apple"),
  (159,828,"2022-02-18","22:30:37","ipsum","Lorem","mango"),
  (160,2024,"2023-09-08","15:28:13","lectus","varius","apple");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (161,2354,"2021-10-04","9:06:35","Nulla","ligula.","banana"),
  (162,3534,"2024-03-22","13:28:55","auctor","fringilla","banana"),
  (163,2695,"2024-02-22","5:33:20","sapien,","volutpat","apple"),
  (164,2287,"2024-01-30","2:41:10","ligula.","tortor,","mango"),
  (165,1884,"2021-05-20","20:02:57","nec","Donec","apple"),
  (166,940,"2021-01-26","5:07:34","morbi","convallis","apple"),
  (167,1510,"2023-05-28","10:34:10","egestas","non,","banana"),
  (168,489,"2021-07-15","3:53:56","sagittis","egestas,","mango"),
  (169,3205,"2021-08-07","16:20:33","adipiscing","sed,","apple"),
  (170,2532,"2020-10-23","10:25:03","et","Suspendisse","mango");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (171,1118,"2023-08-10","2:45:09","Morbi","fames","apple"),
  (172,2080,"2022-05-31","16:57:31","facilisis","tincidunt","apple"),
  (173,3120,"2023-08-15","23:00:15","ipsum.","Cras","mango"),
  (174,4737,"2023-11-27","12:31:44","quis","at","banana"),
  (175,3450,"2021-10-07","6:08:09","Aliquam","non","banana"),
  (176,3576,"2022-02-23","15:51:29","a,","magnis","mango"),
  (177,2484,"2021-12-21","5:48:25","molestie","sagittis","mango"),
  (178,4148,"2020-11-19","15:02:52","sem","bibendum","banana"),
  (179,4372,"2023-05-01","11:35:44","Donec","tempus,","apple"),
  (180,1152,"2022-06-20","17:04:45","ut","Donec","apple");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (181,856,"2024-02-20","6:49:32","lobortis","justo.","apple"),
  (182,207,"2022-07-04","21:15:47","quam.","ac","apple"),
  (183,2491,"2024-02-15","8:10:29","Duis","id","mango"),
  (184,644,"2024-02-10","23:55:41","a","Quisque","banana"),
  (185,266,"2023-01-18","12:21:22","fermentum","malesuada","apple"),
  (186,1236,"2024-01-14","21:34:07","libero.","congue","banana"),
  (187,190,"2024-02-28","17:47:15","lacinia","sit","apple"),
  (188,1551,"2023-12-30","13:04:22","justo.","nibh","banana"),
  (189,921,"2020-10-29","0:23:36","Maecenas","sem.","mango"),
  (190,3063,"2022-01-15","9:40:54","sed","egestas.","banana");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (191,4364,"2023-01-20","8:25:52","et","mi","banana"),
  (192,323,"2023-08-16","22:40:06","aliquam,","vitae","banana"),
  (193,4843,"2023-01-05","14:38:29","lectus","molestie","apple"),
  (194,4032,"2024-03-27","10:09:07","velit","molestie","banana"),
  (195,4981,"2023-10-08","12:29:19","pharetra","nibh.","mango"),
  (196,4632,"2021-08-24","10:45:54","eros","a","apple"),
  (197,4693,"2020-11-04","11:23:01","nec","at,","mango"),
  (198,3884,"2021-02-11","22:42:40","Donec","ac","banana"),
  (199,4042,"2020-09-01","20:36:47","felis","Nullam","banana"),
  (200,1874,"2023-06-13","23:26:34","at,","mauris","banana");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (201,1052,"2023-03-14","12:33:22","mauris,","auctor,","apple"),
  (202,2017,"2023-11-22","14:50:26","et","magna.","apple"),
  (203,72,"2021-07-27","11:56:54","congue","non,","mango"),
  (204,2199,"2020-10-09","9:58:59","amet","faucibus","banana"),
  (205,4286,"2022-10-04","5:28:04","feugiat","fringilla,","mango"),
  (206,487,"2022-02-03","1:49:51","auctor","lobortis.","banana"),
  (207,2254,"2021-11-16","20:16:29","vitae,","interdum.","mango"),
  (208,3236,"2022-07-24","1:34:49","dignissim","est","mango"),
  (209,1664,"2021-02-02","0:18:41","nulla","sem","apple"),
  (210,2705,"2023-03-15","8:32:47","Integer","ornare","mango");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (211,4073,"2022-01-27","20:38:35","velit.","ante","banana"),
  (212,2161,"2021-04-29","4:27:11","quis","enim.","apple"),
  (213,947,"2022-05-04","0:12:19","Morbi","Etiam","mango"),
  (214,3927,"2021-07-06","16:35:12","vel","luctus","mango"),
  (215,3717,"2023-10-01","11:39:57","risus.","vestibulum","mango"),
  (216,1833,"2023-07-30","10:01:26","Donec","Mauris","banana"),
  (217,770,"2023-03-15","14:42:37","erat,","tempus","apple"),
  (218,2150,"2021-08-16","20:50:21","turpis","id","banana"),
  (219,269,"2021-02-03","23:52:14","eget","eleifend","banana"),
  (220,943,"2021-12-19","22:45:29","cursus,","dolor","apple");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (221,3882,"2022-11-23","7:05:49","Quisque","auctor.","apple"),
  (222,3871,"2023-06-15","13:57:19","elit","risus.","banana"),
  (223,569,"2021-09-27","18:50:14","imperdiet","dis","banana"),
  (224,1764,"2023-08-07","11:21:01","ipsum.","et","banana"),
  (225,4610,"2022-06-20","17:27:04","a,","metus","banana"),
  (226,4593,"2023-05-01","11:25:15","nulla","lorem","banana"),
  (227,417,"2023-08-05","9:22:50","fringilla","sit","banana"),
  (228,4830,"2021-11-13","2:14:36","consectetuer","Maecenas","mango"),
  (229,3742,"2023-07-25","11:39:23","nec","eleifend","mango"),
  (230,1956,"2022-06-11","11:44:51","leo.","Fusce","apple");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (231,2238,"2021-02-01","10:25:59","Suspendisse","ut","banana"),
  (232,849,"2023-03-18","19:21:21","adipiscing","eget,","apple"),
  (233,3971,"2022-01-16","22:52:40","sagittis","metus","apple"),
  (234,233,"2023-06-07","3:35:46","libero.","et","apple"),
  (235,1000,"2023-12-20","8:32:17","Fusce","orci.","apple"),
  (236,2155,"2020-08-05","7:04:38","Quisque","sem,","banana"),
  (237,338,"2022-03-23","9:26:10","Aenean","orci,","apple"),
  (238,2036,"2021-05-07","13:04:44","leo.","Nullam","mango"),
  (239,2047,"2022-04-13","14:50:18","Nulla","fames","apple"),
  (240,1349,"2023-11-06","8:47:40","sem,","facilisis","apple");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (241,2726,"2022-10-18","7:00:57","vulputate,","orci","mango"),
  (242,3425,"2020-10-09","21:42:05","odio","ante,","banana"),
  (243,890,"2020-08-06","1:54:28","Vivamus","eros","mango"),
  (244,808,"2024-03-27","12:16:29","amet","molestie","apple"),
  (245,2075,"2022-01-16","1:20:41","elit,","justo","apple"),
  (246,1981,"2022-06-09","3:54:51","leo,","sapien.","apple"),
  (247,2999,"2020-11-10","20:57:42","est,","habitant","banana"),
  (248,3853,"2020-10-08","22:51:16","ante,","orci","banana"),
  (249,661,"2023-03-21","22:52:37","Fusce","accumsan","banana"),
  (250,1704,"2021-08-17","6:43:19","dui","vel,","mango");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (251,4781,"2023-07-25","19:37:57","ullamcorper,","nonummy","mango"),
  (252,1217,"2022-09-11","3:28:13","mattis.","quam.","banana"),
  (253,154,"2023-11-07","0:05:42","orci.","ut,","banana"),
  (254,4900,"2022-05-24","22:20:30","Proin","penatibus","mango"),
  (255,3582,"2023-12-17","10:35:47","Morbi","placerat,","apple"),
  (256,593,"2024-01-25","14:30:31","at","leo,","banana"),
  (257,2521,"2023-08-23","22:06:56","mollis","ut","apple"),
  (258,1746,"2022-05-19","2:36:12","elit.","risus,","apple"),
  (259,4392,"2020-11-04","4:54:29","Mauris","Duis","apple"),
  (260,2863,"2020-09-05","17:48:46","eget","enim.","apple");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (261,4705,"2024-02-07","6:44:07","magna.","senectus","mango"),
  (262,75,"2021-12-25","2:18:53","scelerisque","scelerisque","banana"),
  (263,2181,"2021-06-09","2:44:32","ipsum.","sociis","apple"),
  (264,2425,"2022-04-22","14:10:46","et","mauris","apple"),
  (265,922,"2022-11-16","12:15:09","blandit.","amet","banana"),
  (266,2679,"2022-03-27","16:52:20","hendrerit","vitae","banana"),
  (267,2615,"2020-12-17","19:32:29","convallis","consectetuer","banana"),
  (268,1381,"2023-11-17","0:01:32","tempor","sapien.","banana"),
  (269,377,"2024-01-17","11:21:27","Nullam","sollicitudin","mango"),
  (270,3408,"2021-04-23","7:41:25","quis,","lacus","apple");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (271,3278,"2021-11-21","13:16:07","massa.","augue","apple"),
  (272,3711,"2021-09-12","19:36:07","egestas","Aenean","mango"),
  (273,500,"2022-11-02","18:14:56","tincidunt","et,","mango"),
  (274,3604,"2023-02-13","14:49:41","Mauris","Integer","apple"),
  (275,3,"2023-08-04","7:41:27","augue.","lorem","mango"),
  (276,1265,"2024-01-15","15:37:18","Nunc","volutpat","mango"),
  (277,2657,"2022-09-04","14:30:04","placerat.","nibh","mango"),
  (278,572,"2020-09-11","19:40:50","magna.","tellus","banana"),
  (279,4842,"2023-03-24","17:48:07","Vivamus","neque","apple"),
  (280,1792,"2024-03-26","15:42:10","metus.","vitae,","mango");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (281,1895,"2023-09-09","20:42:55","et","magna","mango"),
  (282,4267,"2024-02-04","2:09:04","Curabitur","Vivamus","apple"),
  (283,4830,"2022-03-04","11:27:42","dapibus","lorem,","mango"),
  (284,3825,"2023-03-16","11:47:55","ultrices.","et,","banana"),
  (285,768,"2023-03-10","2:27:13","dapibus","sit","mango"),
  (286,240,"2023-03-22","19:23:27","justo.","pede,","apple"),
  (287,783,"2020-08-30","15:53:09","et","pede.","banana"),
  (288,1958,"2022-01-06","9:50:31","Nulla","ac","banana"),
  (289,3114,"2023-09-13","21:01:50","eu","vel","apple"),
  (290,4757,"2023-06-18","10:09:30","quam.","facilisis","apple");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (291,2061,"2021-08-08","22:35:13","nisi","Nulla","apple"),
  (292,1789,"2023-07-23","12:58:38","purus","elementum","banana"),
  (293,2774,"2023-06-12","9:16:56","rutrum","neque.","mango"),
  (294,4636,"2022-04-04","21:23:26","molestie","eleifend.","apple"),
  (295,1830,"2021-05-08","11:26:36","lobortis","ut","apple"),
  (296,4986,"2021-04-28","17:41:36","semper","Quisque","apple"),
  (297,3328,"2022-07-16","1:28:58","et","sed","mango"),
  (298,1804,"2020-09-26","8:53:26","ut","sed","apple"),
  (299,3860,"2021-10-21","19:43:34","Curae","Aliquam","mango"),
  (300,1904,"2023-08-12","18:01:38","est.","tempus","mango");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (301,873,"2023-08-08","23:07:30","ultricies","nec,","mango"),
  (302,1768,"2020-10-01","17:28:51","ligula.","vulputate,","apple"),
  (303,3768,"2023-01-08","9:40:22","convallis","convallis,","apple"),
  (304,1329,"2021-04-20","14:42:56","venenatis","Sed","mango"),
  (305,2650,"2023-05-26","23:44:54","Ut","est,","apple"),
  (306,410,"2021-07-27","1:00:26","Ut","lorem","banana"),
  (307,480,"2021-10-18","11:25:44","dapibus","luctus","mango"),
  (308,1651,"2021-06-18","6:36:37","tincidunt","dolor.","mango"),
  (309,3407,"2021-06-30","8:47:57","non","facilisis,","banana"),
  (310,252,"2023-01-31","23:38:46","massa","ac","mango");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (311,2195,"2023-12-29","2:25:48","dui.","ante.","mango"),
  (312,3845,"2022-05-30","12:49:15","Phasellus","sit","mango"),
  (313,1720,"2022-06-10","1:12:24","interdum","laoreet","banana"),
  (314,305,"2022-03-13","14:21:05","eget","accumsan","banana"),
  (315,4358,"2022-07-30","3:10:15","quis,","arcu.","banana"),
  (316,715,"2023-10-18","17:23:01","vitae","blandit","banana"),
  (317,394,"2023-02-21","6:18:09","turpis","nascetur","banana"),
  (318,3838,"2022-09-30","18:25:03","sit","pretium","banana"),
  (319,948,"2023-12-16","22:17:23","sit","lectus","mango"),
  (320,2992,"2022-02-22","7:40:53","id","nunc","mango");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (321,979,"2022-01-20","10:09:19","tellus","euismod","mango"),
  (322,1678,"2021-02-11","11:57:29","tellus.","semper","banana"),
  (323,1133,"2023-09-21","12:41:40","Mauris","sit","banana"),
  (324,3670,"2021-08-30","19:25:02","pede.","odio,","mango"),
  (325,3200,"2023-11-09","19:06:07","at","fringilla","mango"),
  (326,540,"2023-09-09","9:01:13","sed,","Suspendisse","banana"),
  (327,4225,"2022-11-27","1:39:08","blandit","Donec","banana"),
  (328,3107,"2020-12-18","4:02:34","mauris","mus.","apple"),
  (329,2085,"2023-09-29","2:15:58","Pellentesque","blandit.","mango"),
  (330,2349,"2021-02-21","23:14:12","nisl.","est.","banana");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (331,3166,"2023-02-10","1:15:26","Lorem","sagittis.","apple"),
  (332,450,"2022-08-10","2:25:47","tincidunt","Proin","mango"),
  (333,4592,"2023-09-09","15:14:10","laoreet,","dapibus","banana"),
  (334,4862,"2024-01-02","10:39:30","lacus.","risus","mango"),
  (335,435,"2021-04-20","17:05:11","augue.","varius","mango"),
  (336,2627,"2021-09-26","13:09:53","congue,","urna.","banana"),
  (337,1209,"2021-07-18","5:33:32","enim","Suspendisse","mango"),
  (338,2531,"2020-08-25","20:07:49","Sed","rutrum","mango"),
  (339,2965,"2020-11-26","7:54:16","in","sociis","banana"),
  (340,2400,"2023-03-24","11:36:26","et,","sociosqu","banana");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (341,2412,"2021-06-05","0:39:50","vel,","mauris","apple"),
  (342,4640,"2020-09-19","7:45:15","nibh","semper","apple"),
  (343,1272,"2022-01-10","7:54:45","amet,","at","apple"),
  (344,427,"2020-08-13","0:49:34","tincidunt,","condimentum","apple"),
  (345,4772,"2022-05-17","18:02:18","dolor.","Sed","apple"),
  (346,2465,"2024-03-29","14:18:48","Maecenas","non","mango"),
  (347,1110,"2023-03-17","18:33:47","elit","Integer","mango"),
  (348,1689,"2023-02-28","11:44:56","Aenean","lacinia","mango"),
  (349,4818,"2020-11-02","0:38:46","diam","Lorem","mango"),
  (350,2054,"2022-04-08","2:35:15","lobortis","tincidunt","banana");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (351,3674,"2021-07-05","17:59:47","nisl.","sollicitudin","banana"),
  (352,244,"2022-07-26","9:40:10","tristique","orci.","apple"),
  (353,4664,"2022-11-22","16:35:34","purus","magna","mango"),
  (354,3004,"2022-09-17","12:47:11","nunc","diam","banana"),
  (355,1291,"2020-09-17","22:56:03","nibh.","amet,","apple"),
  (356,4228,"2022-08-28","8:57:05","amet,","nisi","apple"),
  (357,4997,"2022-03-15","3:56:20","vestibulum.","adipiscing","banana"),
  (358,854,"2024-02-29","8:54:50","nec","mauris","banana"),
  (359,4101,"2022-09-15","15:52:58","aliquet","eros.","mango"),
  (360,1249,"2022-11-07","20:08:01","aliquet","elit.","mango");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (361,4004,"2020-12-09","19:34:04","et","augue","apple"),
  (362,2007,"2021-07-25","13:19:28","eget","In","apple"),
  (363,248,"2022-11-20","21:25:32","In","non","apple"),
  (364,32,"2021-03-26","6:07:49","Curae","mauris","apple"),
  (365,3364,"2020-10-26","2:12:59","enim","ipsum","mango"),
  (366,3281,"2023-04-20","6:14:45","nibh","Aliquam","mango"),
  (367,2479,"2021-01-22","5:14:37","amet","Etiam","banana"),
  (368,2850,"2022-11-13","10:21:31","natoque","dolor.","apple"),
  (369,3841,"2021-03-26","3:57:53","volutpat","auctor.","banana"),
  (370,2338,"2023-03-23","7:12:10","odio.","est.","apple");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (371,2856,"2023-12-03","14:44:41","in,","auctor","apple"),
  (372,3097,"2021-07-22","4:38:40","semper,","in","mango"),
  (373,1716,"2021-09-14","7:40:52","interdum.","porttitor","apple"),
  (374,449,"2020-11-19","10:40:47","neque","posuere,","mango"),
  (375,1489,"2022-03-12","1:54:58","turpis.","Donec","mango"),
  (376,4857,"2022-09-10","7:38:43","ipsum.","nec","banana"),
  (377,2785,"2020-12-29","3:32:34","nonummy","Nulla","mango"),
  (378,4892,"2021-08-26","16:54:50","dictum","ligula","mango"),
  (379,3060,"2023-05-24","4:06:44","sed","felis","banana"),
  (380,193,"2023-06-21","0:59:12","odio","Fusce","mango");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (381,2876,"2021-05-24","8:32:50","amet","tellus.","apple"),
  (382,2680,"2022-06-15","6:19:27","eu","ligula.","mango"),
  (383,3665,"2021-05-12","15:33:28","Donec","pellentesque","mango"),
  (384,3228,"2023-02-26","13:18:22","enim","amet,","apple"),
  (385,2705,"2022-12-24","23:13:00","nec","Donec","banana"),
  (386,1372,"2023-07-24","9:33:56","ipsum.","lacinia","mango"),
  (387,2212,"2021-03-20","2:09:59","in,","arcu","apple"),
  (388,4598,"2024-01-18","23:17:56","eget","pede.","apple"),
  (389,4263,"2022-05-08","6:52:29","dignissim","Donec","mango"),
  (390,1609,"2022-10-19","0:32:17","metus","cubilia","banana");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (391,601,"2023-07-10","2:32:18","pede,","Maecenas","apple"),
  (392,1589,"2021-06-18","20:10:07","blandit","enim,","mango"),
  (393,3869,"2020-10-23","19:46:48","consequat","id","banana"),
  (394,3510,"2021-11-29","13:47:38","metus","Praesent","apple"),
  (395,1936,"2021-12-09","4:25:16","sit","luctus","banana"),
  (396,4928,"2021-09-04","11:19:40","elit,","hymenaeos.","apple"),
  (397,4063,"2021-07-18","18:47:12","Vivamus","elit","apple"),
  (398,178,"2021-02-23","7:14:08","nec,","ornare","mango"),
  (399,728,"2020-12-04","4:35:38","netus","malesuada","banana"),
  (400,3400,"2021-08-20","19:23:55","scelerisque","velit.","apple");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (401,594,"2020-10-19","14:25:41","iaculis","in,","mango"),
  (402,3944,"2022-08-07","3:02:20","Nunc","ultrices","mango"),
  (403,4311,"2021-04-27","15:19:03","pellentesque","magna.","banana"),
  (404,4085,"2022-09-23","9:00:23","consequat","Etiam","banana"),
  (405,2531,"2022-01-17","20:42:27","cursus,","diam.","apple"),
  (406,1239,"2022-09-22","5:09:03","consectetuer","mattis","mango"),
  (407,3403,"2023-11-03","6:46:57","tempus,","aliquet","mango"),
  (408,4223,"2023-07-18","1:32:14","sit","et","mango"),
  (409,3037,"2023-05-31","16:06:42","turpis","venenatis","banana"),
  (410,692,"2023-03-21","0:37:02","vitae","Cras","apple");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (411,4616,"2021-08-24","1:24:17","nulla","dolor.","mango"),
  (412,4037,"2021-04-26","7:14:21","eu","Proin","mango"),
  (413,1098,"2023-10-09","20:50:19","leo.","amet,","apple"),
  (414,1861,"2024-03-16","0:32:59","non","diam","banana"),
  (415,1676,"2022-02-18","17:53:12","Sed","Nam","banana"),
  (416,3866,"2024-01-05","12:06:33","montes,","dolor","apple"),
  (417,3512,"2022-06-03","9:01:56","mus.","in","mango"),
  (418,619,"2022-05-07","16:20:39","ac","vulputate","mango"),
  (419,3171,"2022-08-11","3:54:36","arcu","Sed","mango"),
  (420,3420,"2023-08-02","21:24:08","a","habitant","mango");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (421,2590,"2021-12-07","4:02:54","nisi.","Duis","banana"),
  (422,2183,"2024-02-22","14:26:34","feugiat.","sem.","apple"),
  (423,3580,"2023-12-25","8:59:50","dui.","tempus","banana"),
  (424,4825,"2022-02-14","21:47:44","at,","ultricies","apple"),
  (425,2928,"2023-03-19","17:39:23","Ut","habitant","banana"),
  (426,4875,"2023-02-02","20:17:35","Nam","Vivamus","banana"),
  (427,3436,"2022-06-06","15:44:27","nunc,","Morbi","mango"),
  (428,387,"2022-03-07","16:30:49","Integer","auctor,","apple"),
  (429,843,"2023-10-11","16:34:20","placerat.","dictum","apple"),
  (430,893,"2020-12-15","9:35:26","magna","vulputate,","mango");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (431,1008,"2021-10-10","7:10:06","Ut","Mauris","banana"),
  (432,4097,"2022-03-25","14:22:40","orci.","imperdiet","banana"),
  (433,4812,"2021-08-24","11:30:02","quis","magna.","banana"),
  (434,1195,"2022-10-29","20:07:05","aliquet","Proin","banana"),
  (435,2176,"2022-05-04","13:25:16","ac,","Proin","banana"),
  (436,587,"2022-04-22","19:39:32","aliquet,","Aliquam","banana"),
  (437,4636,"2023-02-28","12:08:21","nec","nunc","banana"),
  (438,2961,"2023-08-02","15:56:19","Ut","risus.","apple"),
  (439,781,"2021-01-11","5:15:44","convallis","urna.","apple"),
  (440,4950,"2022-12-08","12:37:57","nec,","porttitor","mango");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (441,2768,"2021-12-28","12:14:40","vel","amet","apple"),
  (442,3077,"2021-04-03","8:27:57","odio","mauris","mango"),
  (443,2159,"2023-04-16","0:25:42","ut","malesuada","mango"),
  (444,2961,"2023-02-12","11:40:38","sem","lectus","apple"),
  (445,3522,"2021-03-06","12:30:49","Morbi","ipsum.","banana"),
  (446,3818,"2022-07-27","7:15:39","Nulla","fringilla","banana"),
  (447,4857,"2024-01-10","3:13:38","vulputate","lacus,","apple"),
  (448,3019,"2023-01-26","15:24:22","magnis","diam.","apple"),
  (449,4957,"2020-10-11","5:00:52","ante.","hymenaeos.","mango"),
  (450,4554,"2023-05-13","19:52:40","turpis.","lorem","mango");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (451,510,"2022-09-29","3:08:41","ornare","lectus","apple"),
  (452,3018,"2021-11-28","19:34:58","vitae","id","banana"),
  (453,3438,"2023-02-16","22:04:06","sodales","Nulla","mango"),
  (454,860,"2020-12-14","11:18:12","ipsum","Nunc","banana"),
  (455,4773,"2022-10-27","4:13:31","adipiscing","ut","mango"),
  (456,1490,"2023-07-16","6:33:46","quis,","Maecenas","banana"),
  (457,2501,"2020-10-04","4:20:49","metus.","semper","apple"),
  (458,1764,"2021-07-09","3:01:22","purus,","nisl","banana"),
  (459,215,"2023-05-26","8:00:27","semper","tincidunt.","apple"),
  (460,2560,"2022-08-18","14:40:59","Sed","dapibus","apple");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (461,3440,"2020-10-26","15:19:48","Etiam","lorem","banana"),
  (462,173,"2023-03-30","1:50:47","dui.","libero.","banana"),
  (463,1940,"2021-05-04","5:43:45","sollicitudin","felis.","mango"),
  (464,1079,"2024-01-20","20:04:43","in,","Mauris","mango"),
  (465,1945,"2022-02-07","22:46:54","id","mauris","apple"),
  (466,2423,"2023-06-01","16:43:56","sem.","eget","mango"),
  (467,1758,"2023-03-30","16:07:03","est","lorem,","mango"),
  (468,4481,"2020-10-12","9:38:32","mollis.","nisl.","banana"),
  (469,2074,"2023-04-28","10:52:31","arcu.","magna.","banana"),
  (470,3783,"2022-11-18","4:40:49","nec,","tempor,","banana");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (471,3779,"2021-07-31","8:19:53","imperdiet","Donec","banana"),
  (472,217,"2020-08-05","5:26:56","vitae,","neque","mango"),
  (473,1875,"2021-09-16","12:07:12","varius","vehicula.","mango"),
  (474,4820,"2021-03-01","10:55:45","in","nulla.","banana"),
  (475,4640,"2021-12-11","12:58:04","quis","eget,","banana"),
  (476,234,"2022-05-31","15:24:12","orci","rutrum.","apple"),
  (477,1521,"2020-08-17","11:36:57","risus.","sit","mango"),
  (478,718,"2020-12-01","17:19:08","Phasellus","amet,","banana"),
  (479,365,"2021-10-24","1:34:33","penatibus","consectetuer","mango"),
  (480,3761,"2023-05-14","6:46:09","eu","fames","banana");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (481,4684,"2021-06-29","13:08:52","a,","tristique","banana"),
  (482,1347,"2023-10-21","3:37:02","malesuada","interdum.","banana"),
  (483,2186,"2023-02-16","4:22:46","amet,","Morbi","banana"),
  (484,3907,"2024-01-12","2:39:11","est,","sagittis","banana"),
  (485,2283,"2021-03-09","11:58:41","commodo","ut","apple"),
  (486,3181,"2022-03-16","15:40:48","nunc","feugiat","mango"),
  (487,2325,"2023-08-07","23:29:49","dolor","posuere","apple"),
  (488,2719,"2023-03-29","14:53:05","pharetra","magna.","mango"),
  (489,2285,"2021-05-01","17:01:38","mauris,","lectus","apple"),
  (490,1045,"2023-09-21","14:47:06","nascetur","turpis","apple");
INSERT INTO main (`sno`,`amount`,`date`,`time`,`mode`,`remark`,`category`)
VALUES
  (491,919,"2021-05-20","15:14:30","interdum.","amet","banana"),
  (492,3692,"2023-04-13","22:24:00","ipsum","Ut","apple"),
  (493,3043,"2022-10-24","8:37:35","aliquet,","urna.","banana"),
  (494,324,"2022-01-25","7:37:33","lobortis","odio.","apple"),
  (495,4441,"2021-04-18","23:34:08","ullamcorper","sollicitudin","banana"),
  (496,2492,"2022-02-12","0:33:02","commodo","tempus","apple"),
  (497,1016,"2021-03-19","19:51:22","et,","nisl","apple"),
  (498,52,"2021-02-21","5:03:39","nisl","in","mango"),
  (499,2820,"2023-09-19","15:16:02","libero","ornare,","mango"),
  (500,1439,"2022-09-07","8:12:24","sit","cursus","mango");
'''

database_name="sample_data.db"

con=sqlite3.connect(database_name)
cur=con.cursor()
cur.executescript(input_string)
con.commit()
con.close()