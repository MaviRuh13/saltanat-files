#../game/src/charbattle.cpp // open - search

int dam

# Change everything:

long long dam
#########################################
#../game/src/char.h // open - search

int dam

# Change everything:

long long dam

#../InstanceBaseEffect.cpp sini açıp 

# ARAYIN

void CInstanceBase::AddDamageEffect(DWORD damage,BYTE flag,BOOL bSelf,BOOL bTarget)

# DEĞİŞTİRİN

void CInstanceBase::AddDamageEffect(long long damage,BYTE flag,BOOL bSelf,BOOL bTarget)


# AYNI CPP DE ARAYIN

DWORD damage = sDamage.damage;

# DEĞİŞTİRİN

long long damage = sDamage.damage;



# AYNI CPP DE ARAYIN

if(index > 7)
DEĞİŞTİRİN
if(index > 10)

# AYNI CPP DE ARAYIN

	DWORD index = 0;
	DWORD num = 0;

# DEĞİŞTİRİN

	long long index = 0;
	long long num = 0;

--------------------------------------------------------

#../InstanceBase.h dosyasını açıp

# ARAYIN

DWORD damage;

# DEĞİŞTİRİN

long long damage;


#../AYNI H DE ARAYIN

void AddDamageEffect(DWORD damage,BYTE flag,BOOL bSelf,BOOL bTarget);

# DEĞİŞTİRİN

void AddDamageEffect(long long damage,BYTE flag,BOOL bSelf,BOOL bTarget);