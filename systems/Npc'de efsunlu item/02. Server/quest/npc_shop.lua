quest npc_shop begin
	state start begin
		-- Silahci
		when 9001.chat."Normal Market" begin
			setskin(NOWINDOW)
			npc.open_shop(1)
		end
		when 9001.chat."Nesne Market" begin
			setskin(NOWINDOW)
			npc.open_shop(2)
		end
		-- Zirhci
		when 9002.chat."Normal Market" begin
			setskin(NOWINDOW)
			npc.open_shop(11)
		end
		when 9002.chat."Nesne Market" begin
			setskin(NOWINDOW)
			npc.open_shop(12)
		end
		-- Satici
		when 9003.chat."Normal Market" begin
			setskin(NOWINDOW)
			npc.open_shop(21)
		end
		when 9003.chat."Nesne Market" begin
			setskin(NOWINDOW)
			npc.open_shop(22)
		end
		-- Depocu
		when 9005.chat."Normal Market" begin
			setskin(NOWINDOW)
			npc.open_shop(31)
		end
		-- Balikci
		when 9009.chat."Normal Market" begin
			setskin(NOWINDOW)
			npc.open_shop(41)
		end
		when 9009.chat."Nesne Market" begin
			setskin(NOWINDOW)
			npc.open_shop(42)
		end
		-- Simyaci
		when 20001.chat."Normal Market" begin
			setskin(NOWINDOW)
			npc.open_shop(51)
		end
		when 20001.chat."Nesne Market" begin
			setskin(NOWINDOW)
			npc.open_shop(52)
		end
		-- Biyolog
		when 20084.chat."Normal Market" begin
			setskin(NOWINDOW)
			npc.open_shop(61)
		end
		when 20084.chat."Nesne Market" begin
			setskin(NOWINDOW)
			npc.open_shop(62)
		end
		-- Hong-Hae
		when 20094.chat."Normal Market" begin
			setskin(NOWINDOW)
			npc.open_shop(71)
		end
		when 20094.chat."Nesne Market" begin
			setskin(NOWINDOW)
			npc.open_shop(72)
		end
		-- Yasli Kadin
		when 9006.chat."Normal Market" begin
			setskin(NOWINDOW)
			npc.open_shop(81)
		end
		-- Baokbae
		when 20015.chat."Normal Market" begin
			setskin(NOWINDOW)
			npc.open_shop(91)
		end
		when 20015.chat."Nesne Market" begin
			setskin(NOWINDOW)
			npc.open_shop(92)
		end
		-- Bedensel Savas Ogretmeni
		when 20300.chat."Normal Market" begin
			setskin(NOWINDOW)
			npc.open_shop(101)
		end
		when 20300.chat."Nesne Market" begin
			setskin(NOWINDOW)
			npc.open_shop(102)
		end
		-- Zihinsel Savas Ogretmeni
		when 20301.chat."Normal Market" begin
			setskin(NOWINDOW)
			npc.open_shop(103)
		end
		when 20301.chat."Nesne Market" begin
			setskin(NOWINDOW)
			npc.open_shop(104)
		end
		-- Yakin Dovus Ogretmeni
		when 20302.chat."Normal Market" begin
			setskin(NOWINDOW)
			npc.open_shop(105)
		end
		when 20302.chat."Nesne Market" begin
			setskin(NOWINDOW)
			npc.open_shop(106)
		end
		-- Uzak Dovus Ogretmeni
		when 20303.chat."Normal Market" begin
			setskin(NOWINDOW)
			npc.open_shop(107)
		end
		when 20303.chat."Nesne Market" begin
			setskin(NOWINDOW)
			npc.open_shop(108)
		end
		-- Buyulu Silah Ogretmeni
		when 20304.chat."Normal Market" begin
			setskin(NOWINDOW)
			npc.open_shop(109)
		end
		when 20304.chat."Nesne Market" begin
			setskin(NOWINDOW)
			npc.open_shop(110)
		end
		-- Karabuyu Ogretmeni
		when 20305.chat."Normal Market" begin
			setskin(NOWINDOW)
			npc.open_shop(111)
		end
		when 20305.chat."Nesne Market" begin
			setskin(NOWINDOW)
			npc.open_shop(112)
		end
		-- Ejderha Gucu Ogretmeni
		when 20306.chat."Normal Market" begin
			setskin(NOWINDOW)
			npc.open_shop(113)
		end
		when 20306.chat."Nesne Market" begin
			setskin(NOWINDOW)
			npc.open_shop(114)
		end
		-- Iyılestirme Ogretmeni
		when 20307.chat."Normal Market" begin
			setskin(NOWINDOW)
			npc.open_shop(115)
		end
		when 20307.chat."Nesne Market" begin
			setskin(NOWINDOW)
			npc.open_shop(116)
		end
	end
end