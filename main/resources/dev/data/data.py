from random import random, sample

from main.src.model.api_model import FullMatch


matches = [FullMatch(0, 1030, 1026, 1, 6), FullMatch(1, 1028, 1038, 6, 4), FullMatch(2, 1034, 1038, 3, 9),
           FullMatch(3, 1029, 1037, 1, 4), FullMatch(4, 1034, 1027, 2, 9), FullMatch(5, 1027, 1028, 1, 7),
           FullMatch(6, 1031, 1036, 5, 9), FullMatch(7, 1028, 1037, 3, 7), FullMatch(8, 1037, 1029, 9, 3),
           FullMatch(9, 1026, 1030, 0, 7), FullMatch(10, 1028, 1038, 8, 2), FullMatch(11, 1034, 1035, 3, 3),
           FullMatch(12, 1033, 1027, 7, 9), FullMatch(13, 1026, 1037, 7, 6), FullMatch(14, 1028, 1026, 3, 7),
           FullMatch(15, 1033, 1035, 4, 9), FullMatch(16, 1027, 1036, 5, 0), FullMatch(17, 1035, 1026, 0, 1),
           FullMatch(18, 1037, 1028, 7, 0), FullMatch(19, 1038, 1035, 4, 2), FullMatch(20, 1032, 1028, 5, 2),
           FullMatch(21, 1027, 1034, 3, 0), FullMatch(22, 1036, 1032, 5, 0), FullMatch(23, 1037, 1027, 0, 4),
           FullMatch(24, 1031, 1036, 5, 7), FullMatch(25, 1032, 1033, 4, 8), FullMatch(26, 1030, 1031, 8, 2),
           FullMatch(27, 1037, 1032, 2, 7), FullMatch(28, 1029, 1033, 1, 6), FullMatch(29, 1026, 1031, 7, 7),
           FullMatch(30, 1029, 1030, 0, 4), FullMatch(31, 1036, 1029, 0, 2), FullMatch(32, 1036, 1029, 4, 4),
           FullMatch(33, 1027, 1032, 9, 1), FullMatch(34, 1038, 1028, 6, 3), FullMatch(35, 1026, 1032, 2, 3),
           FullMatch(36, 1035, 1028, 0, 9), FullMatch(37, 1032, 1036, 7, 4), FullMatch(38, 1026, 1033, 1, 8),
           FullMatch(39, 1034, 1025, 4, 3), FullMatch(40, 1032, 1025, 2, 0), FullMatch(41, 1031, 1033, 5, 1),
           FullMatch(42, 1025, 1031, 6, 9), FullMatch(43, 1036, 1026, 5, 1), FullMatch(44, 1033, 1032, 2, 5),
           FullMatch(45, 1035, 1034, 5, 3), FullMatch(46, 1033, 1029, 3, 8), FullMatch(47, 1037, 1025, 1, 9),
           FullMatch(48, 1027, 1029, 0, 0), FullMatch(49, 1030, 1037, 1, 7), FullMatch(50, 1037, 1029, 3, 2),
           FullMatch(51, 1030, 1026, 8, 9), FullMatch(52, 1031, 1032, 2, 3), FullMatch(53, 1030, 1036, 9, 3),
           FullMatch(54, 1025, 1034, 7, 8), FullMatch(55, 1035, 1037, 2, 2), FullMatch(56, 1029, 1025, 2, 2),
           FullMatch(57, 1034, 1026, 0, 8), FullMatch(58, 1033, 1027, 9, 4), FullMatch(59, 1037, 1031, 2, 5),
           FullMatch(60, 1036, 1030, 9, 5), FullMatch(61, 1032, 1029, 9, 9), FullMatch(62, 1026, 1029, 6, 8),
           FullMatch(63, 1026, 1027, 5, 2), FullMatch(64, 1038, 1037, 4, 7), FullMatch(65, 1034, 1035, 7, 6),
           FullMatch(66, 1037, 1034, 1, 9), FullMatch(67, 1028, 1033, 8, 2), FullMatch(68, 1025, 1035, 0, 6),
           FullMatch(69, 1034, 1026, 9, 6), FullMatch(70, 1028, 1036, 0, 2), FullMatch(71, 1029, 1034, 7, 1),
           FullMatch(72, 1031, 1034, 1, 0), FullMatch(73, 1037, 1025, 2, 7), FullMatch(74, 1029, 1025, 4, 8),
           FullMatch(75, 1030, 1036, 6, 0), FullMatch(76, 1037, 1029, 8, 0), FullMatch(77, 1035, 1037, 8, 8),
           FullMatch(78, 1037, 1029, 4, 8), FullMatch(79, 1037, 1026, 2, 4), FullMatch(80, 1028, 1038, 0, 3),
           FullMatch(81, 1033, 1035, 6, 8), FullMatch(82, 1031, 1034, 8, 3), FullMatch(83, 1033, 1025, 0, 8),
           FullMatch(84, 1032, 1031, 4, 4), FullMatch(85, 1033, 1029, 3, 3), FullMatch(86, 1030, 1035, 7, 4),
           FullMatch(87, 1033, 1037, 6, 6), FullMatch(88, 1025, 1032, 8, 8), FullMatch(89, 1038, 1029, 4, 3),
           FullMatch(90, 1036, 1037, 2, 7), FullMatch(91, 1025, 1034, 4, 7), FullMatch(92, 1028, 1027, 8, 6),
           FullMatch(93, 1034, 1037, 0, 9), FullMatch(94, 1029, 1028, 2, 4), FullMatch(95, 1027, 1029, 1, 0),
           FullMatch(96, 1025, 1027, 3, 2), FullMatch(97, 1030, 1027, 6, 6), FullMatch(98, 1038, 1027, 0, 5),
           FullMatch(99, 1033, 1025, 4, 7), FullMatch(100, 1036, 1038, 4, 1), FullMatch(101, 1027, 1033, 0, 6),
           FullMatch(102, 1038, 1028, 4, 9), FullMatch(103, 1028, 1032, 4, 4), FullMatch(104, 1038, 1032, 6, 5),
           FullMatch(105, 1031, 1029, 7, 6), FullMatch(106, 1037, 1026, 9, 9), FullMatch(107, 1028, 1035, 5, 4),
           FullMatch(108, 1030, 1025, 7, 2), FullMatch(109, 1033, 1029, 7, 1), FullMatch(110, 1027, 1034, 5, 0),
           FullMatch(111, 1037, 1033, 7, 9), FullMatch(112, 1037, 1038, 4, 4), FullMatch(113, 1031, 1035, 1, 7),
           FullMatch(114, 1037, 1033, 2, 1), FullMatch(115, 1027, 1036, 8, 8), FullMatch(116, 1032, 1025, 8, 8),
           FullMatch(117, 1031, 1034, 1, 1), FullMatch(118, 1038, 1026, 9, 9), FullMatch(119, 1034, 1036, 8, 8),
           FullMatch(120, 1026, 1033, 7, 9), FullMatch(121, 1036, 1029, 9, 0), FullMatch(122, 1032, 1037, 8, 1),
           FullMatch(123, 1033, 1029, 2, 5), FullMatch(124, 1036, 1029, 7, 4), FullMatch(125, 1037, 1034, 6, 0),
           FullMatch(126, 1031, 1032, 9, 6), FullMatch(127, 1032, 1026, 1, 2), FullMatch(128, 1037, 1036, 4, 5),
           FullMatch(129, 1025, 1026, 7, 2), FullMatch(130, 1038, 1032, 5, 3), FullMatch(131, 1031, 1033, 3, 5),
           FullMatch(132, 1027, 1035, 4, 7), FullMatch(133, 1030, 1028, 5, 3), FullMatch(134, 1029, 1033, 3, 3),
           FullMatch(135, 1034, 1032, 9, 8), FullMatch(136, 1029, 1032, 0, 7), FullMatch(137, 1037, 1028, 9, 8),
           FullMatch(138, 1031, 1037, 2, 5), FullMatch(139, 1033, 1032, 8, 9), FullMatch(140, 1026, 1033, 6, 4),
           FullMatch(141, 1031, 1030, 1, 1), FullMatch(142, 1028, 1034, 4, 6), FullMatch(143, 1027, 1029, 5, 8),
           FullMatch(144, 1035, 1037, 9, 9), FullMatch(145, 1036, 1025, 7, 2), FullMatch(146, 1025, 1033, 1, 6),
           FullMatch(147, 1033, 1027, 5, 2), FullMatch(148, 1030, 1033, 6, 4), FullMatch(149, 1038, 1029, 6, 4),
           FullMatch(150, 1036, 1037, 2, 5), FullMatch(151, 1033, 1027, 3, 4), FullMatch(152, 1035, 1029, 0, 8),
           FullMatch(153, 1025, 1029, 3, 8), FullMatch(154, 1027, 1026, 6, 3), FullMatch(155, 1037, 1030, 6, 2),
           FullMatch(156, 1038, 1033, 5, 5), FullMatch(157, 1037, 1033, 5, 6), FullMatch(158, 1035, 1026, 4, 5),
           FullMatch(159, 1029, 1026, 0, 8), FullMatch(160, 1025, 1034, 0, 1), FullMatch(161, 1028, 1031, 7, 5),
           FullMatch(162, 1037, 1038, 5, 7), FullMatch(163, 1033, 1035, 2, 9), FullMatch(164, 1029, 1035, 8, 0),
           FullMatch(165, 1035, 1038, 0, 5), FullMatch(166, 1030, 1035, 2, 2), FullMatch(167, 1034, 1028, 4, 5),
           FullMatch(168, 1029, 1037, 6, 4), FullMatch(169, 1032, 1028, 7, 5), FullMatch(170, 1035, 1028, 6, 6),
           FullMatch(171, 1026, 1028, 9, 1), FullMatch(172, 1027, 1034, 4, 5), FullMatch(173, 1036, 1025, 6, 6),
           FullMatch(174, 1027, 1038, 4, 4), FullMatch(175, 1032, 1035, 2, 9), FullMatch(176, 1027, 1025, 5, 3),
           FullMatch(177, 1029, 1038, 7, 1), FullMatch(178, 1026, 1038, 3, 7), FullMatch(179, 1031, 1026, 7, 4),
           FullMatch(180, 1033, 1029, 6, 0), FullMatch(181, 1027, 1034, 4, 4), FullMatch(182, 1029, 1034, 6, 0),
           FullMatch(183, 1028, 1030, 8, 2), FullMatch(184, 1031, 1025, 7, 4), FullMatch(185, 1027, 1037, 3, 1),
           FullMatch(186, 1028, 1031, 1, 1), FullMatch(187, 1028, 1025, 9, 1), FullMatch(188, 1037, 1028, 6, 3),
           FullMatch(189, 1027, 1025, 2, 1), FullMatch(190, 1031, 1036, 5, 8), FullMatch(191, 1030, 1027, 2, 8),
           FullMatch(192, 1031, 1030, 3, 2), FullMatch(193, 1034, 1037, 6, 9), FullMatch(194, 1032, 1028, 8, 8),
           FullMatch(195, 1032, 1033, 7, 9), FullMatch(196, 1036, 1027, 4, 0), FullMatch(197, 1032, 1028, 2, 2),
           FullMatch(198, 1026, 1036, 5, 2), FullMatch(199, 1037, 1036, 5, 1), FullMatch(199, 1037, 1036, 5, 5)]

matches_test = [FullMatch(0, 1037, 1031, 2, 6), FullMatch(1, 1035, 1036, 6, 5), FullMatch(2, 1033, 1025, 5, 5),
                FullMatch(3, 1034, 1028, 0, 2), FullMatch(4, 1037, 1032, 7, 8), FullMatch(5, 1028, 1029, 9, 0),
                FullMatch(6, 1036, 1033, 2, 4), FullMatch(7, 1028, 1034, 5, 5), FullMatch(8, 1025, 1026, 7, 7),
                FullMatch(9, 1027, 1033, 8, 6), FullMatch(10, 1035, 1028, 2, 4), FullMatch(11, 1027, 1037, 3, 3),
                FullMatch(12, 1035, 1030, 7, 5), FullMatch(13, 1029, 1025, 3, 3), FullMatch(14, 1029, 1029, 9, 9),
                FullMatch(15, 1028, 1032, 0, 7), FullMatch(16, 1035, 1028, 2, 2), FullMatch(17, 1026, 1036, 3, 3),
                FullMatch(18, 1036, 1027, 2, 8), FullMatch(19, 1028, 1029, 3, 7), FullMatch(20, 1034, 1036, 8, 9),
                FullMatch(21, 1028, 1031, 5, 0), FullMatch(22, 1032, 1033, 4, 4), FullMatch(23, 1029, 1027, 0, 4),
                FullMatch(24, 1036, 1029, 4, 1), FullMatch(25, 1025, 1028, 9, 9), FullMatch(26, 1029, 1030, 6, 7),
                FullMatch(27, 1026, 1032, 5, 6), FullMatch(28, 1030, 1037, 2, 9), FullMatch(29, 1034, 1032, 0, 3),
                FullMatch(30, 1034, 1027, 2, 5), FullMatch(31, 1031, 1037, 0, 0), FullMatch(32, 1029, 1035, 5, 6),
                FullMatch(33, 1030, 1037, 4, 5), FullMatch(34, 1037, 1028, 1, 1), FullMatch(35, 1037, 1032, 6, 2),
                FullMatch(36, 1027, 1026, 5, 3), FullMatch(37, 1029, 1027, 1, 1), FullMatch(38, 1036, 1028, 7, 5),
                FullMatch(39, 1038, 1028, 4, 5), FullMatch(40, 1038, 1031, 4, 0), FullMatch(41, 1033, 1037, 0, 5),
                FullMatch(42, 1037, 1034, 6, 6), FullMatch(43, 1036, 1038, 2, 3), FullMatch(44, 1037, 1036, 6, 0),
                FullMatch(45, 1033, 1031, 9, 9), FullMatch(46, 1028, 1025, 4, 1), FullMatch(47, 1036, 1027, 5, 8),
                FullMatch(48, 1029, 1038, 3, 6), FullMatch(49, 1037, 1032, 0, 0), FullMatch(50, 1034, 1025, 1, 2),
                FullMatch(51, 1037, 1034, 7, 4), FullMatch(52, 1032, 1036, 2, 9), FullMatch(53, 1032, 1026, 7, 7),
                FullMatch(54, 1025, 1033, 5, 7), FullMatch(55, 1034, 1025, 1, 8), FullMatch(56, 1030, 1027, 6, 6),
                FullMatch(57, 1029, 1027, 9, 9), FullMatch(58, 1033, 1036, 3, 3), FullMatch(59, 1029, 1030, 3, 5),
                FullMatch(60, 1037, 1026, 9, 2), FullMatch(61, 1035, 1034, 0, 2), FullMatch(62, 1031, 1032, 5, 7),
                FullMatch(63, 1025, 1037, 3, 1), FullMatch(64, 1027, 1036, 8, 2), FullMatch(65, 1029, 1031, 3, 0),
                FullMatch(66, 1031, 1030, 4, 9), FullMatch(67, 1036, 1027, 5, 3), FullMatch(68, 1032, 1032, 5, 1),
                FullMatch(69, 1028, 1035, 3, 5), FullMatch(70, 1038, 1034, 4, 3), FullMatch(71, 1035, 1034, 9, 8),
                FullMatch(72, 1038, 1032, 3, 7), FullMatch(73, 1032, 1033, 8, 6), FullMatch(74, 1029, 1033, 9, 2),
                FullMatch(75, 1031, 1035, 2, 2), FullMatch(76, 1038, 1034, 9, 3), FullMatch(77, 1028, 1026, 4, 9),
                FullMatch(78, 1026, 1025, 3, 1), FullMatch(79, 1036, 1027, 1, 1)]

matches_to_predict = [FullMatch(0, 1026, 1034, 0, 4), FullMatch(1, 1035, 1033, 0, 6), FullMatch(2, 1033, 1032, 4, 4),
                      FullMatch(3, 1027, 1038, 5, 7), FullMatch(4, 1035, 1030, 1, 4), FullMatch(5, 1032, 1036, 1, 6),
                      FullMatch(6, 1030, 1034, 1, 4), FullMatch(7, 1033, 1031, 1, 8), FullMatch(8, 1025, 1028, 0, 6),
                      FullMatch(9, 1032, 1035, 6, 3), FullMatch(10, 1036, 1038, 1, 2), FullMatch(11, 1031, 1032, 1, 4),
                      FullMatch(12, 1032, 1028, 2, 6), FullMatch(13, 1033, 1034, 9, 9), FullMatch(14, 1033, 1031, 4, 1),
                      FullMatch(15, 1026, 1033, 6, 9), FullMatch(16, 1038, 1032, 1, 1), FullMatch(17, 1030, 1032, 8, 0),
                      FullMatch(18, 1037, 1026, 9, 3), FullMatch(19, 1032, 1031, 3, 9), FullMatch(20, 1036, 1029, 7, 0),
                      FullMatch(21, 1036, 1032, 0, 4), FullMatch(22, 1028, 1030, 8, 2), FullMatch(23, 1038, 1026, 3, 2),
                      FullMatch(24, 1031, 1033, 9, 0), FullMatch(25, 1026, 1025, 9, 5), FullMatch(26, 1035, 1034, 5, 1),
                      FullMatch(27, 1035, 1029, 8, 5), FullMatch(28, 1030, 1032, 3, 0), FullMatch(29, 1036, 1035, 7, 6),
                      FullMatch(30, 1025, 1036, 9, 6), FullMatch(31, 1034, 1035, 1, 6), FullMatch(32, 1031, 1033, 3, 5),
                      FullMatch(33, 1029, 1030, 5, 4), FullMatch(34, 1029, 1038, 8, 0), FullMatch(35, 1035, 1029, 8, 8),
                      FullMatch(36, 1028, 1034, 5, 7), FullMatch(37, 1038, 1034, 6, 0), FullMatch(38, 1034, 1037, 3, 1),
                      FullMatch(39, 1028, 1025, 6, 8)]

teams = [1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038]
# if __name__ == '__main__':
#     # for i in range(0, 200):
#     #     team1, team2 = sample(teams, 2)
#     #     team1score = int(random() * 10)
#     #     team2score = int(random() * 10)
#     #     print(f'matches.append(FullMatch({i}, {team1}, {team2}, {team1score}, {team2score}))')
#
#
#     for i in matches:
#         print(i.team_away_id)
#         teams.append(i.team_away_id)
#         teams.append(i.team_home_id)
#
#     for i in range(0, 80):
#         team1, team2 = sample(teams, 2)
#         team1score = int(random() * 10)
#         team2score = int(random() * 10)
#         print(f'matches_test.append(FullMatch({i}, {team1}, {team2}, {team1score}, {team2score}))')

    # for i in range(0, 40):
    #     team1, team2 = sample(teams, 2)
    #     team1score = int(random() * 10)
    #     team2score = int(random() * 10)
    #     print(f'matches_to_predict.append(FullMatch({i}, {team1}, {team2}, {team1score}, {team2score}))')
