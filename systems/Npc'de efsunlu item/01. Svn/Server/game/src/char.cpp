// Arat :
// void CHARACTER::UpdatePacket()
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
DWORD CHARACTER::GetDragonCoin()
{
	std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT cash FROM account.account WHERE id = '%d';", GetDesc()->GetAccountTable().id));
	if (pMsg->Get()->uiNumRows == 0)
		return 0;
	
	MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
	DWORD dc = 0;
	str_to_number(dc, row[0]);
	return dc;
}

DWORD CHARACTER::GetDragonMark()
{
	std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT coins FROM account.account WHERE id = '%d';", GetDesc()->GetAccountTable().id));
	if (pMsg->Get()->uiNumRows == 0)
		return 0;
	
	MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
	DWORD mark = 0;
	str_to_number(mark, row[0]);
	return mark;
}

void CHARACTER::SetDragonCoin(DWORD amount)
{
	DBManager::instance().DirectQuery("UPDATE account.account SET cash = '%d' WHERE id = '%d';", amount, GetDesc()->GetAccountTable().id);
	RefreshDragonCoin();
}

void CHARACTER::SetDragonMark(DWORD amount)
{
	DBManager::instance().DirectQuery("UPDATE account.account SET coins = '%d' WHERE id = '%d';", amount, GetDesc()->GetAccountTable().id);
	RefreshDragonCoin();	
}

void CHARACTER::RefreshDragonCoin()
{	
	ChatPacket(CHAT_TYPE_COMMAND, "RefreshDragonCoin %d", GetDragonCoin());
	ChatPacket(CHAT_TYPE_COMMAND, "RefreshDragonMark %d", GetDragonMark());
}
#endif