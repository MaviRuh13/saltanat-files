// -----------------------------------------------Arat----------------------------------------------- //

		BYTE level = (BYTE)strtoul(row[4], (char**) NULL, 10);

// --------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
		int level = (int)strtoul(row[4], (char**) NULL, 10);
#else
		BYTE level = (BYTE)strtoul(row[4], (char**) NULL, 10);
#endif

// -----------------------------------------------Arat----------------------------------------------- //

	sys_log(0, "GUILD: AddMember PID %u, grade %u, job %u, level %u, offer %u, name %s ptr %p",

// --------------------------------------------Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
	sys_log(0, "GUILD: AddMember PID %u, grade %u, job %u, level %d, offer %u, name %s ptr %p",
#else
	sys_log(0, "GUILD: AddMember PID %u, grade %u, job %u, level %u, offer %u, name %s ptr %p",
#endif

// -----------------------------------------------Arat----------------------------------------------- //

void CGuild::ChangeMemberData(DWORD pid, DWORD offer, BYTE level, BYTE grade)

// -------------------------------------- ---Komple Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
void CGuild::ChangeMemberData(DWORD pid, DWORD offer, int level, BYTE grade)
#else
void CGuild::ChangeMemberData(DWORD pid, DWORD offer, BYTE level, BYTE grade)
#endif
{
	TGuildMemberContainer::iterator cit = m_member.find(pid);

	if (cit == m_member.end())
		return;

	cit->second.offer_exp = offer;
	cit->second.level = level;
	cit->second.grade = grade;
	cit->second._dummy = 0;

	TPacketGCGuild pack;
#ifdef __MAX_LEVEL_300__
	TGuildMemberPacketData mbData;
#else
	memset(&pack, 0, sizeof(pack));
#endif
	pack.header = HEADER_GC_GUILD;
#ifdef __MAX_LEVEL_300__
	pack.subheader = GUILD_SUBHEADER_GC_LIST;
	pack.size = sizeof(TPacketGCGuild);
	pack.size += sizeof(TGuildMemberPacketData);
#endif

	for (TGuildMemberOnlineContainer::iterator it = m_memberOnline.begin(); it != m_memberOnline.end(); ++it)
	{
		LPDESC d = (*it)->GetDesc();
		if (d)
		{
#ifdef __MAX_LEVEL_300__
			TEMP_BUFFER buf;

			buf.write(&pack, sizeof(pack));

			mbData.byNameFlag = 0;
			mbData.byGrade = cit->second.grade;
			mbData.byIsGeneral = cit->second.is_general;
			mbData.byJob = cit->second.job;
			mbData.byLevel = cit->second.level;
			mbData.dwOffer = cit->second.offer_exp;
			mbData.pid = cit->second.pid;
			buf.write(&mbData, sizeof(TGuildMemberPacketData));

			d->Packet(buf.read_peek(), buf.size());
#else
			pack.subheader = GUILD_SUBHEADER_GC_LIST;
			pack.size = sizeof(pack) + 13;
			d->BufferedPacket(&pack, sizeof(pack));
			d->Packet(&(cit->second), sizeof(DWORD) * 3 + 1);
#endif
		}
	}
}

// -----------------------------------------------Arat----------------------------------------------- //

void CGuild::LevelChange(DWORD pid, BYTE level)

// -------------------------------------- ---Komple Degistir----------------------------------------------- //

#ifdef __MAX_LEVEL_300__
void CGuild::LevelChange(DWORD pid, int level)
#else
void CGuild::LevelChange(DWORD pid, BYTE level)
#endif
{
	TGuildMemberContainer::iterator cit = m_member.find(pid);

	if (cit == m_member.end())
		return;

	cit->second.level = level;

	TPacketGuildChangeMemberData gd_guild;

	gd_guild.guild_id = GetID();
	gd_guild.pid = pid;
	gd_guild.offer = cit->second.offer_exp;
	gd_guild.grade = cit->second.grade;
	gd_guild.level = level;

	db_clientdesc->DBPacket(HEADER_GD_GUILD_CHANGE_MEMBER_DATA, 0, &gd_guild, sizeof(gd_guild));

	TPacketGCGuild pack;
#ifdef __MAX_LEVEL_300__
	TGuildMemberPacketData mbData;
#endif
	pack.header = HEADER_GC_GUILD;
#ifdef __MAX_LEVEL_300__
	pack.subheader = GUILD_SUBHEADER_GC_LIST;
	pack.size = sizeof(TPacketGCGuild);
	pack.size += sizeof(TGuildMemberPacketData);
#endif
	cit->second._dummy = 0;

	for (TGuildMemberOnlineContainer::iterator it = m_memberOnline.begin(); it != m_memberOnline.end(); ++it)
	{
		LPDESC d = (*it)->GetDesc();

		if (d)
		{
#ifdef __MAX_LEVEL_300__
			TEMP_BUFFER buf;

			buf.write(&pack, sizeof(pack));

			mbData.byNameFlag = 0;
			mbData.byGrade = cit->second.grade;
			mbData.byIsGeneral = cit->second.is_general;
			mbData.byJob = cit->second.job;
			mbData.byLevel = cit->second.level;
			mbData.dwOffer = cit->second.offer_exp;
			mbData.pid = cit->second.pid;
			buf.write(&mbData, sizeof(TGuildMemberPacketData));

			d->Packet(buf.read_peek(), buf.size());
#else
			pack.subheader = GUILD_SUBHEADER_GC_LIST;
			pack.size = sizeof(pack) + 13;
			d->BufferedPacket(&pack, sizeof(pack));
			d->Packet(&(cit->second), sizeof(DWORD) * 3 + 1);
#endif
		}
	}
}

// -----------------------------------------------Arat----------------------------------------------- //

bool CGuild::OfferExp(LPCHARACTER ch, int amount)

// -------------------------------------- ---Komple Degistir----------------------------------------------- //

bool CGuild::OfferExp(LPCHARACTER ch, int amount)
{
	TGuildMemberContainer::iterator cit = m_member.find(ch->GetPlayerID());

	if (cit == m_member.end())
		return false;

	if (m_data.exp+amount < m_data.exp)
		return false;

	if (amount < 0)
		return false;

	if (ch->GetExp() < (DWORD) amount)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("<길드> 제공하고자 하는 경험치가 남은 경험치보다 많습니다."));
		return false;
	}

	if (ch->GetExp() - (DWORD) amount > ch->GetExp())
	{
		sys_err("Wrong guild offer amount %d by %s[%u]", amount, ch->GetName(), ch->GetPlayerID());
		return false;
	}

	ch->PointChange(POINT_EXP, -amount);

	TPacketGuildExpUpdate guild_exp;
	guild_exp.guild_id = GetID();
	guild_exp.amount = amount / 100;
	db_clientdesc->DBPacket(HEADER_GD_GUILD_EXP_UPDATE, 0, &guild_exp, sizeof(guild_exp));
	GuildPointChange(POINT_EXP, amount / 100, true);

	cit->second.offer_exp += amount / 100;
	cit->second._dummy = 0;

	TPacketGCGuild pack;
#ifdef __MAX_LEVEL_300__
	TGuildMemberPacketData mbData;
#endif
	pack.header = HEADER_GC_GUILD;
#ifdef __MAX_LEVEL_300__
	pack.subheader = GUILD_SUBHEADER_GC_LIST;
	pack.size = sizeof(TPacketGCGuild);
	pack.size += sizeof(TGuildMemberPacketData);
#endif

	for (TGuildMemberOnlineContainer::iterator it = m_memberOnline.begin(); it != m_memberOnline.end(); ++it)
	{
		LPDESC d = (*it)->GetDesc();
		if (d)
		{
#ifdef __MAX_LEVEL_300__
			TEMP_BUFFER buf;

			buf.write(&pack, sizeof(pack));

			mbData.byNameFlag = 0;
			mbData.byGrade = cit->second.grade;
			mbData.byIsGeneral = cit->second.is_general;
			mbData.byJob = cit->second.job;
			mbData.byLevel = cit->second.level;
			mbData.dwOffer = cit->second.offer_exp;
			mbData.pid = cit->second.pid;
			buf.write(&mbData, sizeof(TGuildMemberPacketData));

			d->Packet(buf.read_peek(), buf.size());
#else
			pack.subheader = GUILD_SUBHEADER_GC_LIST;
			pack.size = sizeof(pack) + 13;
			d->BufferedPacket(&pack, sizeof(pack));
			d->Packet(&(cit->second), sizeof(DWORD) * 3 + 1);
#endif
		}
	}

	SaveMember(ch->GetPlayerID());

	TPacketGuildChangeMemberData gd_guild;

	gd_guild.guild_id = GetID();
	gd_guild.pid = ch->GetPlayerID();
	gd_guild.offer = cit->second.offer_exp;
	gd_guild.level = ch->GetLevel();
	gd_guild.grade = cit->second.grade;

	db_clientdesc->DBPacket(HEADER_GD_GUILD_CHANGE_MEMBER_DATA, 0, &gd_guild, sizeof(gd_guild));
	return true;
}

// -----------------------------------------------Arat----------------------------------------------- //

void CGuild::SendListPacket(LPCHARACTER ch)

// -------------------------------------- ---Komple Degistir----------------------------------------------- //

void CGuild::SendListPacket(LPCHARACTER ch)
{
	/*
	   List Packet

	   Header
	   Count (byte)
	   [
	   ...
	   name_flag 1 - 이름을 보내느냐 안보내느냐
	   name CHARACTER_NAME_MAX_LEN+1
	   ] * Count

	 */
	LPDESC d;
	if (!(d=ch->GetDesc()))
		return;

	TPacketGCGuild pack;
	pack.header = HEADER_GC_GUILD;
	pack.size = sizeof(TPacketGCGuild);
	pack.subheader = GUILD_SUBHEADER_GC_LIST;

	pack.size += sizeof(TGuildMemberPacketData) * m_member.size();
#ifdef __MAX_LEVEL_300__
	pack.size += (CHARACTER_NAME_MAX_LEN + 1) * m_member.size();
#endif
	TEMP_BUFFER buf;
#ifdef __MAX_LEVEL_300__
	TGuildMemberPacketData mbData;
#endif
	buf.write(&pack,sizeof(pack));

	char c[CHARACTER_NAME_MAX_LEN+1];

	for (TGuildMemberContainer::iterator it = m_member.begin(); it != m_member.end(); ++it)
	{
		it->second._dummy = 1;
#ifdef __MAX_LEVEL_300__
		mbData.byNameFlag = 1;
		mbData.byGrade = it->second.grade;
		mbData.byIsGeneral = it->second.is_general;
		mbData.byJob = it->second.job;
		mbData.byLevel = it->second.level;
		mbData.dwOffer = it->second.offer_exp;
		mbData.pid = it->second.pid;

		buf.write(&mbData, sizeof(TGuildMemberPacketData));
#else
		buf.write(&(it->second), sizeof(DWORD)*3+1);
#endif
		strlcpy(c, it->second.name.c_str(), MIN(sizeof(c), it->second.name.length() + 1));

		buf.write(c, CHARACTER_NAME_MAX_LEN+1 );

		if ( test_server )
			sys_log(0 ,"name %s job %d  ", it->second.name.c_str(), it->second.job );
	}

	d->Packet(buf.read_peek(), buf.size());

	for (TGuildMemberOnlineContainer::iterator it = m_memberOnline.begin(); it != m_memberOnline.end(); ++it)
	{
		SendLoginPacket(ch, *it);
	}

	for (TGuildMemberP2POnlineContainer::iterator it = m_memberP2POnline.begin(); it != m_memberP2POnline.end(); ++it)
	{
		SendLoginPacket(ch, *it);
	}

}

// -----------------------------------------------Arat----------------------------------------------- //

void CGuild::SendListOneToAll(DWORD pid)

// -------------------------------------- ---Komple Degistir----------------------------------------------- //

void CGuild::SendListOneToAll(DWORD pid)
{

	TPacketGCGuild pack;
	pack.header = HEADER_GC_GUILD;
	pack.size = sizeof(TPacketGCGuild);
	pack.subheader = GUILD_SUBHEADER_GC_LIST;

	pack.size += sizeof(TGuildMemberPacketData);
#ifdef __MAX_LEVEL_300__
	TGuildMemberPacketData mbData;
#endif
	char c[CHARACTER_NAME_MAX_LEN+1];
	memset(c, 0, sizeof(c));

	TGuildMemberContainer::iterator cit = m_member.find(pid);
	if (cit == m_member.end())
		return;

	for (TGuildMemberOnlineContainer::iterator it = m_memberOnline.begin(); it!= m_memberOnline.end(); ++it)
	{
		LPDESC d = (*it)->GetDesc();
		if (!d) 
			continue;

		TEMP_BUFFER buf;

		buf.write(&pack, sizeof(pack));

		cit->second._dummy = 1;
#ifdef __MAX_LEVEL_300__
		mbData.byNameFlag = 1;
		mbData.byGrade = cit->second.grade;
		mbData.byIsGeneral = cit->second.is_general;
		mbData.byJob = cit->second.job;
		mbData.byLevel = cit->second.level;
		mbData.dwOffer = cit->second.offer_exp;
		mbData.pid = cit->second.pid;
		//buf.write(&(cit->second), sizeof(DWORD) * 3 +1);
		buf.write(&mbData, sizeof(TGuildMemberPacketData));
#else
		buf.write(&(cit->second), sizeof(DWORD) * 3 +1);
#endif
		buf.write(cit->second.name.c_str(), cit->second.name.length());
		buf.write(c, CHARACTER_NAME_MAX_LEN + 1 - cit->second.name.length());
		d->Packet(buf.read_peek(), buf.size());
	}
}

// -----------------------------------------------Arat----------------------------------------------- //

	SGuildMember::SGuildMember(DWORD pid, BYTE grade, BYTE is_general, BYTE job, BYTE level, DWORD offer_exp, char* name)

// -------------------------------------- ------Degistir----------------------------------------------- //
#ifdef __MAX_LEVEL_300__
	SGuildMember::SGuildMember(DWORD pid, BYTE grade, BYTE is_general, BYTE job, int level, DWORD offer_exp, char* name)
#else
	SGuildMember::SGuildMember(DWORD pid, BYTE grade, BYTE is_general, BYTE job, BYTE level, DWORD offer_exp, char* name)
#endif