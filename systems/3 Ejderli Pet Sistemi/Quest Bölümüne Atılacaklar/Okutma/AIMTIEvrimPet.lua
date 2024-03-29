QuestFolder = get_locale_base_path().."/quest/"
PetSystem = {['Folder'] = QuestFolder.."/pet/", ['ItemExp'] = 400000, ['UpdateFrequency'] = 30, ['Flag'] = "active_pet", ['ExpFlag'] = "exp_blocked"}

PetSystem[1] = 
			{['Name'] = "Catalik", ['Level'] = 22, ['Item'] = 53001, ['pet'] = 1, ['MaxLevel'] = 250, ['WindowSize'] = 395,
			 ['Skill']= {
						{['type']=apply.MAX_HP,['name']="Max.HP ",['max_points']=50,['min_level']=1,['desc']="60.000 Max.HP",['mult']=60000,['tag']=" Max.HP"},
						{['type']=apply.MAX_SP,['name']="Max.SP ",['max_points']=100,['min_level']=50,['desc']="5000 Max.SP",['mult']=5000,['tag']=" Max.SP"},
						{['type']=apply.CAST_SPEED,['name']="Büyü Hýzý ",['max_points']=20,['min_level']=250,['desc']="+1 Büyü Hýzý ",['mult']=1,['tag']="% Büyü Hýzý "},
						{['type']=apply.ATTBONUS_UNDEAD,['name']="Ölümsüz ",['max_points']=40,['min_level']=150,['desc']="+5 Ölümsüzlere karþý güçlü ",['mult']=5,['tag']="% Ölümsüzlere karþý güçlü "},
						{['type']=apply.ATTBONUS_MONSTER,['name']="Canavar ",['max_points']=40,['min_level']=75,['desc']="+5 Canavarlara karþý güçlü ",['mult']=5,['tag']="% Canavarlara karþý güçlü "}
						},
			 ['ExpTable'] = {5000000,5000000,5000000,5000000,5000000,5000000,5000000,5000000,5000000,6000000,               ----- Seviye 1.10
							 6000000,6000000,6000000,6000000,6000000,6000000,6000000,6000000,6000000,7000000,               ----- Seviye 11.20
							 7000000,7000000,7000000,7000000,7000000,7000000,7000000,7000000,7000000,8000000,               ----- Seviye 21.30
							 8000000,8000000,8000000,8000000,8000000,8000000,8000000,8000000,8000000,8500000,               ----- Seviye 31.40
							 8500000,8500000,8500000,8500000,8500000,8500000,8500000,8500000,8500000,9000000,               ----- Seviye 41.50
							 9000000,9000000,9000000,9000000,9000000,9000000,9000000,9000000,9000000,9500000,               ----- Seviye 51.60
							 9500000,9500000,9500000,9500000,9500000,9500000,9500000,9500000,9500000,10000000,               ----- Seviye 61.70
							 10000000,10000000,10000000,10000000,10000000,10000000,10000000,10000000,10000000,10500000,               ----- Seviye 71.80
							 10500000,10500000,10500000,10500000,10500000,10500000,10500000,10500000,10500000,11000000,               ----- Seviye 81.90
							 11000000,11000000,11000000,11000000,11000000,11000000,11000000,11000000,11000000,12250000,               ----- Seviye 91.100
							 12250000,12250000,12250000,12250000,12250000,12250000,12250000,12250000,12250000,13250000,               ----- Seviye 101.110
							 13250000,13250000,13250000,13250000,13250000,13250000,13250000,13250000,13250000,14250000,               ----- Seviye 111.120
							 14250000,14250000,14250000,14250000,14250000,14250000,14250000,14250000,14250000,15250000,               ----- Seviye 121.130
							 15250000,15250000,15250000,15250000,15250000,15250000,15250000,15250000,15250000,16250000,               ----- Seviye 131.140
							 16250000,16250000,16250000,16250000,16250000,16250000,16250000,16250000,16250000,17250000,               ----- Seviye 141.150
							 17250000,17250000,17250000,17250000,17250000,17250000,17250000,17250000,17250000,18250000,               ----- Seviye 151.160
							 18250000,18250000,18250000,18250000,18250000,18250000,18250000,18250000,18250000,19250000,               ----- Seviye 161.170
							 19250000,19250000,19250000,19250000,19250000,19250000,19250000,19250000,19250000,21250000,               ----- Seviye 171.180
							 21250000,21250000,21250000,21250000,21250000,21250000,21250000,21250000,21250000,22250000,               ----- Seviye 181.190
							 22250000,22250000,22250000,22250000,22250000,22250000,22250000,22250000,22250000,25250000,               ----- Seviye 191.200
							 25250000,25250000,25250000,25250000,25250000,25250000,25250000,25250000,25250000,26250000,               ----- Seviye 201.210
							 26250000,26250000,26250000,26250000,26250000,26250000,26250000,26250000,26250000,27250000,               ----- Seviye 211.220
							 27250000,27250000,27250000,27250000,27250000,27250000,27250000,27250000,27250000,29250000,               ----- Seviye 221.230
							 29250000,29250000,29250000,29250000,29250000,29250000,29250000,29250000,29250000,30000000,               ----- Seviye 231.240
							 30000000,30000000,30000000,30000000,30000000,30000000,30000000,30000000,30000000,1               ----- Seviye 241.250 END
							}
			}

PetSystem[2] = 
			{['Name'] = "Wslik", ['Level'] = 23, ['Item'] = 53002, ['pet'] = 1, ['MaxLevel'] = 310, ['WindowSize'] = 395,
			 ['Skill']= {
						{['type']=apply.MAX_HP,['name']="Max HP",['max_points']=60,['min_level']=1,['desc']="100.000 Max.HP",['mult']=100000,['tag']=" Max.HP"},
						{['type']=apply.MAX_SP,['name']="Max.SP ",['max_points']=100,['min_level']=50,['desc']="5000 Max.SP",['mult']=5000,['tag']=" Max.SP"},
						{['type']=apply.CRITICAL_PCT,['name']="Kritik vurus",['max_points']=15,['min_level']=60,['desc']="+1% Kritik vurus",['mult']=1,['tag']="% Kritik"},
						{['type']=apply.RESIST_WARRIOR,['name']="Savasci Savunma",['max_points']=10,['min_level']=60,['desc']="+1% Kritik vurus",['mult']=1,['tag']="% Savasci Savunma"},
						{['type']=apply.RESIST_ASSASSIN,['name']="Ninja Savunma",['max_points']=10,['min_level']=60,['desc']="+1% Kritik vurus",['mult']=1,['tag']="% Ninja Savunma"},
						{['type']=apply.RESIST_SURA,['name']="Sura Savunma",['max_points']=10,['min_level']=60,['desc']="+1% Kritik vurus",['mult']=1,['tag']="% Sura Savunma"},
						{['type']=apply.RESIST_SHAMAN,['name']="Þaman Savunma",['max_points']=10,['min_level']=310,['desc']="+1% Kritik vurus",['mult']=1,['tag']="% Þaman Savunma"},
						{['type']=apply.RESIST_WOLFMAN,['name']="Lycan Savunma",['max_points']=10,['min_level']=310,['desc']="+1% Kritik vurus",['mult']=1,['tag']="% Lycan Savunma"}
						},
			 ['ExpTable'] = {5000000,5000000,5000000,5000000,5000000,5000000,5000000,5000000,5000000,6000000,               ----- Seviye 1.10
							 6000000,6000000,6000000,6000000,6000000,6000000,6000000,6000000,6000000,7000000,               ----- Seviye 11.20
							 7000000,7000000,7000000,7000000,7000000,7000000,7000000,7000000,7000000,8000000,               ----- Seviye 21.30
							 8000000,8000000,8000000,8000000,8000000,8000000,8000000,8000000,8000000,8500000,               ----- Seviye 31.40
							 8500000,8500000,8500000,8500000,8500000,8500000,8500000,8500000,8500000,9000000,               ----- Seviye 41.50
							 9000000,9000000,9000000,9000000,9000000,9000000,9000000,9000000,9000000,9500000,               ----- Seviye 51.60
							 9500000,9500000,9500000,9500000,9500000,9500000,9500000,9500000,9500000,10000000,               ----- Seviye 61.70
							 10000000,10000000,10000000,10000000,10000000,10000000,10000000,10000000,10000000,10500000,               ----- Seviye 71.80
							 10500000,10500000,10500000,10500000,10500000,10500000,10500000,10500000,10500000,11000000,               ----- Seviye 81.90
							 11000000,11000000,11000000,11000000,11000000,11000000,11000000,11000000,11000000,12250000,               ----- Seviye 91.100
							 12250000,12250000,12250000,12250000,12250000,12250000,12250000,12250000,12250000,13250000,               ----- Seviye 101.110
							 13250000,13250000,13250000,13250000,13250000,13250000,13250000,13250000,13250000,14250000,               ----- Seviye 111.120
							 14250000,14250000,14250000,14250000,14250000,14250000,14250000,14250000,14250000,15250000,               ----- Seviye 121.130
							 15250000,15250000,15250000,15250000,15250000,15250000,15250000,15250000,15250000,16250000,               ----- Seviye 131.140
							 16250000,16250000,16250000,16250000,16250000,16250000,16250000,16250000,16250000,17250000,               ----- Seviye 141.150
							 17250000,17250000,17250000,17250000,17250000,17250000,17250000,17250000,17250000,18250000,               ----- Seviye 151.160
							 18250000,18250000,18250000,18250000,18250000,18250000,18250000,18250000,18250000,19250000,               ----- Seviye 161.170
							 19250000,19250000,19250000,19250000,19250000,19250000,19250000,19250000,19250000,21250000,               ----- Seviye 171.180
							 21250000,21250000,21250000,21250000,21250000,21250000,21250000,21250000,21250000,22250000,               ----- Seviye 181.190
							 22250000,22250000,22250000,22250000,22250000,22250000,22250000,22250000,22250000,25250000,               ----- Seviye 191.200
							 25250000,25250000,25250000,25250000,25250000,25250000,25250000,25250000,25250000,26250000,               ----- Seviye 201.210
							 26250000,26250000,26250000,26250000,26250000,26250000,26250000,26250000,26250000,27250000,               ----- Seviye 211.220
							 27250000,27250000,27250000,27250000,27250000,27250000,27250000,27250000,27250000,29250000,               ----- Seviye 221.230
							 29250000,29250000,29250000,29250000,29250000,29250000,29250000,29250000,29250000,30000000,               ----- Seviye 231.240
							 30000000,30000000,30000000,30000000,30000000,30000000,30000000,30000000,30000000,32000000,               ----- Seviye 241.250
							 32000000,32000000,32000000,32000000,32000000,32000000,32000000,32000000,32000000,32000000,               ----- Seviye 251.260 
							 32000000,32000000,32000000,32000000,32000000,32000000,32000000,32000000,32000000,32000000,               ----- Seviye 261.270 
							 32000000,32000000,32000000,32000000,32000000,32000000,32000000,32000000,32000000,32000000,               ----- Seviye 271.280 
							 32000000,32000000,32000000,32000000,32000000,32000000,32000000,32000000,32000000,32000000,               ----- Seviye 281.290 
							 32000000,32000000,32000000,32000000,32000000,32000000,32000000,32000000,32000000,32000000,               ----- Seviye 291.300 END
							 32000000,32000000,32000000,32000000,32000000,32000000,32000000,32000000,32000000,1               ----- Seviye 301.310 END


							}
			}

function PetSystem.ShowMenu(PetIndex)
		local pet_menu
		if pc.getqf("exp_blocked") == 0 then
			pet_menu = {"Bilgi","Beceri Daðýtýmý ","EXP Blokla","Evcil Hayvan Durumu","Evcil Hayvaný Gönder ","Pencereyi kapat"}
		else
			pet_menu = {"Bilgi","Beceri Daðýtýmý ","EXP Bloklamayý kaldýr ","Evcil Hayvan Durumu ","Evcil Hayvaný Gönder ","Pencereyi kapat "}
		end
		say_reward("") 
		local skill_points, liv, ex = PetSystem.ReadStatus(PetIndex)
		say("Seviye: "..liv.." / "..PetSystem[PetIndex].MaxLevel.."  -  Beceri Puaný: "..skill_points.." ")
		if not PetSystem.IsExpBlocked() then
			say("Exp kazanma: "..ex.." / "..PetSystem[PetIndex].ExpTable[liv].." (Açýk) ")
		else
			say("Exp kazanma: "..ex.." / "..PetSystem[PetIndex].ExpTable[liv].." (Kapalý) ")
		end
		say("")
		say_title("Ne yapmak istiyorsun?")
		say_size(350, 340)
		local s = select_table(pet_menu)		
		if s == 1 then
			say_title("")
			say("Evcil Hayvanlar sizinle birlikte peþinizde ")
			say("dolaþýrlar. Bu Evcil Hayvanlar geliþtirilebilir. ")
			say("Seviyeleri yükseltilebilir. Seviyeleri yükseldikçe ")
			say("verdiði bonus puanlarýda artar. ")
			say("Bu bonus puanlarý siz belirleyebilirsiniz. ")
			say("Bonuslar her Evcil Hayvanda farklýdýr. ")
			say("Evcil Hayvanlara EXP Þiþesi isimli eþya ile ")
			say("seviye kazandýrabilirsiniz. ")		
		elseif s == 2 then
			say_title("")
			say("Merhaba "..pc.get_name()..". ")
			say("Seviye: "..liv.." / "..PetSystem[PetIndex].MaxLevel.."  -  Mevcut Beceri Puaný: "..skill_points.." ")
			say("")
			say_title("Lütfen bir iþlem seçin. ")
			local a = select("Beceri Arttýr (+)","Beceri Azalt (-)","Pencereyi kapat")
			if a == 3 then 
				return
			elseif a == 1 then
				if skill_points == 0 then
					syschat("Beceri arttýrmak için Beceri puaný yok.")
					return
				end
				local skill_value = {}
				local menu_abi = {}
				skill_value = PetSystem.LoadSkill(PetIndex)
				for i = 1, table.getn(PetSystem[PetIndex].Skill) do
					if liv >= PetSystem[PetIndex].Skill[i].min_level then
						table.insert(menu_abi, PetSystem[PetIndex].Skill[i].name..": "..skill_value[i].." puan")
					end
				end				
				table.insert(menu_abi, "Pencereyi kapat")
				if table.getn(menu_abi) == 1 then
					syschat("Evcil hayvanýn daha yüksek seviyeye ulaþmalý. ")
					return
				end
				say_title("")
				say("Arttýrmak için lütfen bir beceri seçin. ")
				say_size(350, PetSystem[PetIndex].WindowSize)			
				local s = select_table(menu_abi)
				if s == table.getn(menu_abi) then
					return			
				end
				say_title("Mevcut Beceri Puaný: "..skill_value[s].." ")
				if skill_value[s] == PetSystem[PetIndex].Skill[s].max_points then
					say("Özellik son seviyeye ulaþtý! ")
					say("Daha fazla Beceri puaný veremezsin.")
					return
				end
				say("Bir Beceri puaný ")
				say(""..PetSystem[PetIndex].Skill[s].desc.." vermektedir.")
				say("")
				say_reward("Bu özelliðe Max. "..PetSystem[PetIndex].Skill[s].max_points.." puan verebilirsin. ")
				say("")
				local a = select("Beceriyi Arttýr (+) ", "Pencereyi kapat ")
				if a == 2 then
					return
				end
				say_title("")
				say("Özelliðe verebileceðiniz maksimum puaný göz")
				say("önünde bulundurarak bir rakam giriniz.")
				say("Bu özelliði kaç puan yükseltmek istersiniz?")
				say("")
				local points = tonumber(input())
				if points == nil or points < 1 then
					syschat("Geçersiz bir deðer girdin.")
					return
				elseif points > skill_points then
					syschat("Yeterli Beceri puaný yok.")
					return
				elseif (skill_value[s]+points) > PetSystem[PetIndex].Skill[s].max_points then
					say_title("")
					say("Seçilen özellik için girdiðiniz "..points.." puan geçersiz. ")
					say("Beceriye verilebilecek maksimum puana göz atýn. ")
					say("Daha küçük deðerler kullanýn. ")
					return
				end
				PetSystem.RemoveBonus(PetIndex)
				syschat("Beceri arttýrma iþlemi baþarýyla tamamlandý. ")
				skill_value[s] = skill_value[s]+points
				PetSystem.ChangeSkillPoints(PetIndex, -points)
				PetSystem.SaveSkill(PetIndex, skill_value)
				PetSystem.AddBonus(PetIndex)
				PetSystem.pokaz_gui(2)
			elseif a == 2 then
				say_title("Beceri Azalt:")
				local skill_value = {}
				local menu_abi = {}
				skill_value = PetSystem.LoadSkill(PetIndex)
				for i = 1, table.getn(PetSystem[PetIndex].Skill) do
					if liv >= PetSystem[PetIndex].Skill[i].min_level then
						table.insert(menu_abi, PetSystem[PetIndex].Skill[i].name..": "..skill_value[i].." puan")
					end
				end
				table.insert(menu_abi, "Pencereyi kapat")
				if table.getn(menu_abi) == 1 then
					syschat("Bu becerinin azalmasý mümkün deðildir.")
					return
				end				
				say("Lütfen puanýný azaltmak istediðin beceriyi seç. ")
				say_size(350, PetSystem[PetIndex].WindowSize)				
				local s = select_table(menu_abi)
				if s == table.getn(menu_abi) then
					return			
				end
				if skill_value[s] == 0 then
					syschat("Bu özelliðin Beceri puanýný daha fazla azaltamazsýn.")
					return
				end
				say_title("")
				say("Bu yeteneðin beceri puanýný buradan")
				say("sýfýrlayabilirsin.")
				say("")
				local b = select("Tüm puanlarý sýfýrla","Pencereyi kapat")
				if b == 3 then
					return
				elseif b == 1 then
					say_title("")
					say("Bu özelliðin beceri puanlarýný sýfýrlamak")
					say("istediðinden emin misin?")
					say("")
					local c = select("Evet","Hayýr")
					if c == 2 then
						return
					end
					PetSystem.RemoveBonus(PetIndex)
					PetSystem.ChangeSkillPoints(PetIndex, skill_value[s])
					skill_value[s] = 0
					PetSystem.SaveSkill(PetIndex, skill_value)
					PetSystem.AddBonus(PetIndex)
					PetSystem.pokaz_gui(2)
					syschat("Seçtiðin özelliðin beceri puaný baþarýyla sýfýrlandý. ")
				end
			end
		elseif s == 3 then
			if not PetSystem.IsExpBlocked() then
				say_title("")
				say("Evcil Hayvanýn EXP kazanmasýný engellemek")
				say("istiyor musun?")
				say("")
				local a = select("Evet","Hayýr")
				if a == 2 then
					return
				end
				syschat("Evcil Hayvan artýk EXP kazanamayacak.")
				PetSystem.BlockExp()
				PetSystem.pokaz_gui(2)
			else
				say_title("")
				say("EXP kazanmayý aktifleþtirmek istiyor musun?")
				say("")
				local a = select("Evet","Hayýr")
				if a == 2 then
					return
				end
				syschat("Evcil Hayvanýn artýk EXP kazanabilir.")
				PetSystem.UnblockExp()
				PetSystem.pokaz_gui(2)
			end
		elseif s == 4 then
			say_size(350, 340)
			say_title("Evcil Hayvanýn puanlarý ve becerileri:")
			local skill_value = {}
			skill_value = PetSystem.LoadSkill(PetIndex)
			say("")
			for i = 1, table.getn(PetSystem[PetIndex].Skill) do
				if liv >= PetSystem[PetIndex].Skill[i].min_level then
					local total = skill_value[i]*PetSystem[PetIndex].Skill[i].mult
					say_reward(PetSystem[PetIndex].Skill[i].name..": "..skill_value[i].." puan.")
					say("Bonus: "..total..PetSystem[PetIndex].Skill[i].tag)
				end
			end
			say("")			
		elseif s == 5 then
			PetSystem.pokaz_gui(5)		
		elseif s == 6 then
			return
		end
end

function PetSystem.PetBack()
	pet.unsummon(20123)	
	PetSystem.RemoveBonus()
	PetSystem.SetInactive()
	pc.setqf("petindex", 0)
	cmdchat("PetZamnkij")	
	chat("Evcil Hayvan Gönderildi. ")
end

function PetSystem.Pette(at)
	deneme = PetSystem . GetLevel ( petIndex )
	if at == 1 then 
		pet.summon(20123,deneme)	
	end
end

function PetSystem.LoadSkill(PetIndex)
	local FileName = PetSystem.Folder..pc.get_name().."_"..PetSystem[PetIndex].Name.."_skills"
	local PetSkill = {}
	if io.open(FileName, "r") == nil then
		io.output(FileName)
		for i = 1,table.getn(PetSystem[PetIndex].Skill) do
			io.write("0\n")
			table.insert(PetSkill, 0)
		end
		io.flush()
		io.close()
		return PetSkill
	end
	for line in io.lines(FileName) do
		table.insert(PetSkill, tonumber(line))
	end
	return PetSkill
end

function PetSystem.SaveSkill(PetIndex, SkillList)
	local FileName = PetSystem.Folder..pc.get_name().."_"..PetSystem[PetIndex].Name.."_skills"
	io.output(FileName)
	for i,v in ipairs(SkillList) do
		io.write(tostring(v).."\n")
	end
	io.flush()
	io.close()
end

function PetSystem.ReadStatus(petIndex)
	local FileName = PetSystem.Folder..pc.get_name().."_"..PetSystem[petIndex].Name.."_stats"
	local skill, liv, ex, ev, ev1 , ev2, ev3
	if io.open(FileName, "r") != nil then
		io.input(FileName)
		skill = tonumber(io.read())
		liv = tonumber(io.read())
		ex = tonumber(io.read())
		ev = tonumber(io.read())
		ev1 = tonumber(io.read())
		ev2 = tonumber(io.read())
		ev3 = tonumber(io.read())
		io.input():close()
	else
		io.output(FileName)
		io.write("1\n1\n0\n34006\n1\n34002\n5\n")
		io.flush()
		io.close()	
		skill = 1
		liv = 1
		ex = 0
		ev = 34006
		ev1 = 1
		ev2 = 34002
		ev3 = 5
	end
	return skill, liv, ex, ev, ev1, ev2, ev3
end

function PetSystem.GetLevel(petIndex)
	local FileName = PetSystem.Folder..pc.get_name().."_"..PetSystem[petIndex].Name.."_stats"
	local liv
	if io.open(FileName, "r") != nil then
		io.input(FileName)
		io.read()
		liv = tonumber(io.read())
		io.input():close()
	else
		liv = 1
	end
	return liv
end

function PetSystem.GetPoly(petIndex)
	local FileName = PetSystem.Folder..pc.get_name().."_"..PetSystem[petIndex].Name.."_www"
	local poly1
	if io.open(FileName, "r") != nil then
		io.input(FileName)
		poly1 = tonumber(io.read())

		io.input():close()
	else
		io.output(FileName)
		io.write("1\n")
		io.flush()
		io.close()	
		poly1 = 1
	end
	return poly1
end

function PetSystem.ChangeSkillPoints(PetIndex, amount)
	local FileName = PetSystem.Folder..pc.get_name().."_"..PetSystem[PetIndex].Name.."_stats"
	local skill, liv, ex, ev, ev1, ev2, ev3
	if io.open(FileName, "r") != nil then
		io.input(FileName)
		skill = tonumber(io.read())
		liv = tonumber(io.read())
		ex = tonumber(io.read())
		ev = tonumber(io.read())
		ev1 = tonumber(io.read())
		ev2 = tonumber(io.read())
		ev3 = tonumber(io.read())
		skill = skill+amount
		io.input():close()
	else
		skill = amount
	end
	io.output(FileName)
	io.write(tostring(skill).."\n")
	io.write(tostring(liv).."\n")
	io.write(tostring(ex).."\n")
	io.write(tostring(ev).."\n")
	io.write(tostring(ev1).."\n")
	io.write(tostring(ev2).."\n")
	io.write(tostring(ev3).."\n")
	io.flush()
	io.close()
end

function PetSystem.GiveExp(petIndex, amount)
	local FileName = PetSystem.Folder..pc.get_name().."_"..PetSystem[petIndex].Name.."_stats"
	local skill, liv, ex, ev, ev1, ev2, ev3
	if io.open(FileName, "r") != nil then
		io.input(FileName)
		skill = tonumber(io.read())
		liv = tonumber(io.read())
		ex = tonumber(io.read())
		ev = tonumber(io.read())
		ev1 = tonumber(io.read())
		ev2 = tonumber(io.read())
		ev3 = tonumber(io.read())
		ex = ex+amount
		io.input():close()
	else
		skill = 0
		liv = 1
		ev = 1
		ev1 = 1
		ev2 = 1
		ev3 = 1
		ex = amount
	end
	if liv == PetSystem[petIndex].MaxLevel then
		return false
	end
	if ex >= PetSystem[petIndex].ExpTable[liv] then
		ex = ex-PetSystem[petIndex].ExpTable[liv]
		liv = liv+1
		skill = skill+1
		local petIndex = pc.getqf("petindex")
		if petIndex == 1 then
		if liv >= 80 and liv <= 80 then
			pet.unsummon(ev, ev1)
			ev = ev+1
			ev1 = ev1+1
		elseif liv >= 180 and liv <= 180 then
			pet.unsummon(ev, ev1)
			ev = ev+1
			ev1 = ev1+1
		elseif liv >= 250 and liv <= 250 then
			pet.unsummon(ev, ev1)
			ev = ev+1
			ev1 = ev1+1
		end
		end
		if petIndex == 2 then
		if liv >= 180 and liv <= 180 then
			pet.unsummon(ev2, ev3)
			ev2 = 34016
			ev3 = 6
		elseif liv >= 250 and liv <= 250 then
			pet.unsummon(ev2, ev3)
			ev2 = 34003
			ev3 = 7
		elseif liv >= 260 and liv <= 260 then
			pet.unsummon(ev2, ev3)
			ev2 = 34030
			ev3 = 10
		elseif liv >= 280 and liv <= 280 then
			pet.unsummon(ev2, ev3)
			ev2 = 34031
			ev3 = 11
		elseif liv >= 310 and liv <= 310 then
			pet.unsummon(ev2, ev3)
			ev2 = 34032
			ev3 = 12
		end
		end
		if liv == PetSystem[petIndex].MaxLevel then
			ex = 0
			syschat("Evcil Hayvan son seviyeye ulaþtý.")
		else
			---syschat("Evcil Hayvan Seviyesi: "..liv.."")
		end
		if petIndex == 1 then
		local deneme = " Lv."..liv.." "..pc.get_name()
		pet.unsummon(ev, deneme)
		pet.summon(ev, deneme)
		elseif petIndex == 2 then
		local deneme = " Lv."..liv.." "..pc.get_name()
		pet.unsummon(ev2, deneme)
		pet.summon(ev2, deneme)
		end
	end
	io.output(FileName)
	io.write(tostring(skill).."\n")
	io.write(tostring(liv).."\n")
	io.write(tostring(ex).."\n")
	io.write(tostring(ev).."\n")
	io.write(tostring(ev1).."\n")
	io.write(tostring(ev2).."\n")
	io.write(tostring(ev3).."\n")
	io.flush()
	io.close()	
	return true
end

function PetSystem.AddBonus(PetIndex)
	local SkillList = {}
	SkillList = PetSystem.LoadSkill(PetIndex)
	for i = 1,table.getn(SkillList) do
		affect.add_collect(PetSystem[PetIndex].Skill[i].type, SkillList[i]*PetSystem[PetIndex].Skill[i].mult, 60*60*24*365)
	end
end

function PetSystem.RemoveBonus(PetIndex)
	local SkillList = {}
	SkillList = PetSystem.LoadSkill(PetIndex)
	for i = 1,table.getn(SkillList) do
		affect.remove_collect(PetSystem[PetIndex].Skill[i].type, SkillList[i]*PetSystem[PetIndex].Skill[i].mult, 60*60*24*365)
	end
end

function PetSystem.SetHorseData(level, name)
	horse.set_name(name)
	horse.set_level(level)
end

function PetSystem.IsPetLevel(level)
	for i = 1,PetSystem.GetPetNumber() do
		if level == PetSystem[i].Level then
			return true
		end
	end
	return false
end

function PetSystem.NewSkillLearnt(PetIndex, PetLevel)
	for i = 1,table.getn(PetSystem[PetIndex].Skill) do
		if PetLevel == PetSystem[PetIndex].Skill[i].min_level then
			return true
		end
	end
	return false
end

function PetSystem.GetPetNumber()
	return table.getn(PetSystem)
end

function PetSystem.SetActivePet(petIndex)
	pc.setqf(PetSystem.Flag, petIndex)
end

function PetSystem.IsActive()
	return (pc.getqf(PetSystem.Flag) > 0)
end

function PetSystem.SetInactive()
	pc.setqf(PetSystem.Flag, 0)
end

function PetSystem.GetActivePet()
	return pc.getqf(PetSystem.Flag)
end

function PetSystem.BlockExp()
	pc.setqf(PetSystem.ExpFlag, 1)
end

function PetSystem.UnblockExp()
	pc.setqf(PetSystem.ExpFlag, 0)
end

function PetSystem.IsExpBlocked()
	return (pc.getqf(PetSystem.ExpFlag) == 1)
end
function PetSystem.pokaz_gui(arg , petIndex)
	local petIndex = pc.getqf("petindex")
	local skill_points, liv, ex, ev, ev1,ev2, ev3 = PetSystem.ReadStatus(petIndex)
	local level1 = " Lv."..liv.." "..pc.get_name()
	if PetSystem.IsExpBlocked() then
		blokada = 1
	else
		blokada = 0
	end
	if arg == 1 then
		if petIndex == 1 then
		pet.summon(ev,level1)	
		cmdchat("PetPokaz "..ev1.." "..liv.." "..ex.." "..PetSystem[petIndex].ExpTable[liv].." "..blokada.." "..skill_points.."")
		chat ( "Evcil Hayvan Çaðrýldý. " ) 
		elseif petIndex == 2 then
		pet.summon(ev2,level1)	
		cmdchat("PetPokaz "..ev3.." "..liv.." "..ex.." "..PetSystem[petIndex].ExpTable[liv].." "..blokada.." "..skill_points.."")
		chat ( "Evcil Hayvan Çaðrýldý. " ) 
		end
	end
	if arg == 2 then
		if petIndex == 1 then
		cmdchat("PetPokaz "..ev1.." "..liv.." "..ex.." "..PetSystem[petIndex].ExpTable[liv].." "..blokada.." "..skill_points.."")
		elseif petIndex == 2 then
		cmdchat("PetPokaz "..ev3.." "..liv.." "..ex.." "..PetSystem[petIndex].ExpTable[liv].." "..blokada.." "..skill_points.."")
		end
	end
	if arg == 5 then
		pet.unsummon(ev,level1)	
		pet.unsummon(ev2,level1)	
		cmdchat("PetZamnkij")	
		chat("Evcil Hayvan Gönderildi. ")
		PetSystem.RemoveBonus(petIndex)
		PetSystem.SetInactive() 
		pc.setqf("petindex",0)
	end
	if arg == 6 then	
		PetSystem.RemoveBonus(petIndex)
		PetSystem.SetInactive() 
		cmdchat("PetZamnkij")	
		pc.setqf("petindex",0)
	end
end


